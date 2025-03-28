from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple, Dict, Callable, Optional, Any, Union

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, param)


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor, Utils):
    
    def __init__(self, ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.function_current: Optional[FuncDecl] = None
        
        self.builtin_funcs = self._initialize_builtins()
        self.list_function: List[FuncDecl] = list(self.builtin_funcs.values())
    
    def _initialize_builtins(self) -> Dict[str, FuncDecl]:
        return {
            "getInt": FuncDecl("getInt", [], IntType(), Block([])),
            "putInt": FuncDecl("putInt", [ParamDecl("i", IntType())], VoidType(), Block([])),
            "putIntLn": FuncDecl("putIntLn", [ParamDecl("i", IntType())], VoidType(), Block([])),
            "getFloat": FuncDecl("getFloat", [], FloatType(), Block([])),
            "putFloat": FuncDecl("putFloat", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            "putFloatLn": FuncDecl("putFloatLn", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            "getBool": FuncDecl("getBool", [], BoolType(), Block([])),
            "putBool": FuncDecl("putBool", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            "putBoolLn": FuncDecl("putBoolLn", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            "getString": FuncDecl("getString", [], StringType(), Block([])),
            "putString": FuncDecl("putString", [ParamDecl("s", StringType())], VoidType(), Block([])),
            "putStringLn": FuncDecl("putStringLn", [ParamDecl("s", StringType())], VoidType(), Block([])),
            "putLn": FuncDecl("putLn", [], VoidType(), Block([]))
        }
    
    def _get_builtin_symbols(self) -> List[Symbol]:
        return [Symbol(name, FuntionType(), func) for name, func in self.builtin_funcs.items()]

    def check(self):
        self.visit(self.ast, None)

    def check_redeclared(self, current_scope, name, kind, get_name=lambda x: x.name):
        if self.lookup(name, current_scope, get_name) is not None:
            raise Redeclared(kind, name)
            
    def visitProgram(self, ast: Program, c: None):
        self.list_type = []
        for decl in ast.decl:
            if isinstance(decl, Type):
                self.list_type.append(self.visit(decl, self.list_type))

        user_functions = [decl for decl in ast.decl if isinstance(decl, FuncDecl)]
        self.list_function.extend(user_functions)
        
        method_decls = [decl for decl in ast.decl if isinstance(decl, MethodDecl)]
        for method_decl in method_decls:
            struct_type = self.lookup(method_decl.recType.name, self.list_type, lambda x: x.name)
            if struct_type is None:
                raise Undeclared(StaticErrorType(), method_decl.recType.name)
            
            self.check_redeclared(struct_type.methods, method_decl.fun.name, Method(), lambda x: x.fun.name)
            struct_type.methods.append(method_decl)

        env = [self._get_builtin_symbols()]
        
        for decl in (d for d in ast.decl if isinstance(d, Decl)):
            result = self.visit(decl, [env[0]])
            if isinstance(result, Symbol):
                env[0].insert(0, result)

    def visitStructType(self, ast: StructType, c: List[Union[StructType, InterfaceType]]) -> StructType:
        self.check_redeclared(c, ast.name, StaticErrorType())
        
        processed_elements = []
        for field_name, field_type in ast.elements:
            for processed_name, _ in processed_elements:
                if processed_name == field_name:
                    raise Redeclared(Field(), field_name)
            processed_elements.append((field_name, field_type))
        
        ast.elements = processed_elements
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        self.check_redeclared(c, ast.name, Prototype())
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]) -> InterfaceType:
        self.check_redeclared(c, ast.name, StaticErrorType())
        
        processed_methods = []
        for method in ast.methods:
            self.check_redeclared(processed_methods, method.name, Prototype())
            processed_methods.append(self.visit(method, processed_methods))
        
        ast.methods = processed_methods
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        self.check_redeclared(c[0], ast.name, Function())
        
        self.function_current = ast
        
        param_symbols = []
        for param in ast.params:
            param_symbol = self.visit(param, param_symbols)
            param_symbols.append(param_symbol)
            
        self.visit(ast.body, [param_symbols] + c)
        
        self.function_current = None
        return Symbol(ast.name, FuntionType(), ast)

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        self.check_redeclared(c, ast.parName, Parameter())
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        struct_type = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
        if struct_type is None:
            raise Undeclared(StaticErrorType(), ast.recType.name)
            
        self.function_current = ast.fun
        
        env = [Symbol(ast.receiver, struct_type)]
        
        for param in ast.fun.params:
            if param.parName == ast.receiver:
                raise Redeclared(Parameter(), param.parName)
                
            param_symbol = self.visit(param, env)
            env.append(param_symbol)
        
        self.visit(ast.fun.body, [env] + c)
        self.function_current = None

    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        self.check_redeclared(c[0], ast.varName, Variable())
        
        if ast.varInit:
            init_type = self.visit(ast.varInit, c)
            if ast.varType and not self.typeMatch(init_type, ast.varType):
                raise TypeMismatch(ast)
        
            if isinstance(init_type, StructType) and isinstance(ast.varType, StructType):
                if init_type.name != ast.varType.name:
                    raise TypeMismatch(ast)
        
        var_type = ast.varType if ast.varType else self.visit(ast.varInit, c)
        return Symbol(ast.varName, var_type, None)

    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        self.check_redeclared(c[0], ast.conName, Constant())
        
        if ast.iniExpr is None:
            raise TypeMismatch(ast)
            
        init_type = self.visit(ast.iniExpr, c)
        if ast.conType and not self.typeMatch(init_type, ast.conType):
            raise TypeMismatch(ast)
        
        inferred_type = ast.conType if ast.conType else init_type
        return Symbol(ast.conName, inferred_type, None)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        local_env = []
        for member in ast.member:
            result = self.visit(member, [local_env] + c)
            if isinstance(result, Symbol):
                local_env.insert(0, result)

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None: 
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None: 
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None: 
        self.visit(Block([VarDecl(ast.idx.name, None, None), VarDecl(ast.value.name, None, None)] + ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next(filter(None, (self.lookup(ast.name, scope, lambda x: x.name) for scope in c)), None)
        if res and not isinstance(res.mtype, FuntionType):
            if isinstance(res.mtype, Id):
                type_name = res.mtype.name
                type_res = self.lookup(type_name, self.list_type, lambda x: x.name)
                if type_res:
                    return type_res
                raise Undeclared(StaticErrorType(), type_name)
            return res.mtype
        
        type_res = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if type_res:
            return type_res
        
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if res:
            if len(ast.args) != len(res.params):
                raise TypeMismatch(ast)
            for i, arg in enumerate(ast.args):
                arg_type = self.visit(arg, c)
                param_type = res.params[i].parType
                if not self.typeMatch(arg_type, param_type):
                    raise TypeMismatch(ast)
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        if not isinstance(type_receiver, StructType):
            raise TypeMismatch(ast)
        
        found_field = False
        for field_name, field_type in type_receiver.elements:
            if field_name == ast.field:
                found_field = True
                return field_type
        
        if not found_field:
            raise Undeclared(Field(), ast.field)

    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        res = None
        if isinstance(type_receiver, StructType):
            res = self.lookup(ast.metName, type_receiver.methods, lambda x: x.fun.name)
        elif isinstance(type_receiver, InterfaceType):
            res = self.lookup(ast.metName, type_receiver.methods, lambda x: x.name)
            
        if res is None:
            raise Undeclared(Method(), ast.metName)
        
        return res.retType if isinstance(res, FuncDecl) else res.fun.retType if isinstance(res, MethodDecl) else res.retType

    def visitIntType(self, ast, param): return None
    def visitFloatType(self, ast, param): return None
    def visitBoolType(self, ast, param): return None
    def visitStringType(self, ast, param): return None
    def visitVoidType(self, ast, param): return None
    def visitArrayType(self, ast, param): return None
    def visitAssign(self, ast, param): return None
    def visitIf(self, ast, param): return None
    def visitContinue(self, ast, c):
        if not self.function_current:
            raise TypeMismatch(ast)
        return None

    def visitBreak(self, ast, c):
        if not self.function_current:
            raise TypeMismatch(ast)
        return None

    def visitReturn(self, ast, c):
        if not self.function_current:
            raise TypeMismatch(ast)
        if isinstance(self.function_current.retType, VoidType):
            if ast.expr:
                raise TypeMismatch(ast)
        else:
            if not ast.expr:
                raise TypeMismatch(ast)
            expr_type = self.visit(ast.expr, c)
            if not self.typeMatch(expr_type, self.function_current.retType):
                raise TypeMismatch(ast)
        return None

    def visitBinaryOp(self, ast, c):
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        
        if ast.op in ['+', '-', '*', '/']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            elif isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                if isinstance(left_type, IntType) or isinstance(right_type, IntType) or \
                   isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                    return FloatType()
            elif ast.op == '+' and isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            raise TypeMismatch(ast)
        
        elif ast.op == '%':
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            raise TypeMismatch(ast)
        
        elif ast.op in ['==', '!=', '<', '<=', '>', '>=']:
            if type(left_type) == type(right_type) and (isinstance(left_type, IntType) or 
                                                       isinstance(left_type, FloatType) or 
                                                       isinstance(left_type, StringType)):
                return BoolType()
            raise TypeMismatch(ast)
        
        elif ast.op in ['&&', '||']:
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
            raise TypeMismatch(ast)
        
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast, c):
        expr_type = self.visit(ast.operand, c)
        
        if ast.op == '!':
            if isinstance(expr_type, BoolType):
                return BoolType()
        elif ast.op == '-':
            if isinstance(expr_type, IntType):
                return IntType()
            elif isinstance(expr_type, FloatType):
                return FloatType()
        
        raise TypeMismatch(ast)

    def visitArrayCell(self, ast, c):
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)
        
        for idx in ast.idx:
            idx_type = self.visit(idx, c)
            if not isinstance(idx_type, IntType):
                raise TypeMismatch(ast)
        
        return arr_type.eleType

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        if not ast.explist:
            return ArrayType(0, NilType())
        
        elem_types = [self.visit(expr, c) for expr in ast.explist]
        first_type = elem_types[0]
        for elem_type in elem_types[1:]:
            if not self.typeMatch(elem_type, first_type):
                raise TypeMismatch(ast)
        
        return ArrayType(len(ast.explist), first_type)

    def visitStructLiteral(self, ast, c):
        struct_type = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if struct_type is None or not isinstance(struct_type, StructType):
            raise Undeclared(StaticErrorType(), ast.name)
        
        if len(ast.fields) != len(struct_type.elements):
            raise TypeMismatch(ast)
        
        for i, field in enumerate(ast.fields):
            field_type = self.visit(field, c)
            struct_field_type = struct_type.elements[i][1]
            if not self.typeMatch(field_type, struct_field_type):
                raise TypeMismatch(ast)
        
        return struct_type

    def visitNilLiteral(self, ast, c):
        return NilType()

    def typeMatch(self, type1, type2):
        if type1 is None or type2 is None:
            return True
        if isinstance(type1, IntType) and isinstance(type2, FloatType):
            return True
        if isinstance(type1, Type) and isinstance(type2, Type):
            if isinstance(type1, StructType) and isinstance(type2, StructType):
                return type1.name == type2.name
            return type(type1) == type(type2)
        if isinstance(type1, ArrayType) and isinstance(type2, ArrayType):
            return type1.size == type2.size and self.typeMatch(type1.eleType, type2.eleType)
        if isinstance(type1, StructType) and isinstance(type2, InterfaceType):
            for method in type2.methods:
                struct_method = self.lookup(method.name, type1.methods, lambda x: x.name)
                if struct_method is None:
                    return False
            return True
        return False
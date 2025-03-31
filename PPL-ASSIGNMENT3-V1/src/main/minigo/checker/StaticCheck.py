"""
 * Authors: Ho Gia Thang - 2213187
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Union

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    
    def __init__(self,ast):
        self.helper = HelperClass()
        self.ast = ast
        self.global_envi    = self.helper.initializeGlobalEnvironment()
        self.list_type      = []
        self.list_function  = self.helper.buildInbuiltFunction()
        self.current_func   = None

    def check(self):
        return self.visit(self.ast,self.global_envi)
    
    def __debug(self, c: List[List[Symbol]]):
        for ele in c:
            print('-----------------')
            for sym in ele:
                print(sym.__str__())
        return None

    def __functionVisit(self, cur_envi, cur_list):
        for ele in cur_list:
            sym = self.visit(ele, cur_envi)
            if isinstance(sym, Symbol):
                cur_envi[0] = [sym] + cur_envi[0]
        return cur_envi
    
    def __update_method(self, method, list_type):
        type_name = method.recType.name
        type_declared = self.helper.getType(list_type, method.recType)
        if type_declared is None:
            raise Undeclared(Type(), type_name)

        if isinstance(type_declared, StructType):
            if self.helper.checkRedeclared(method.fun.name, type_declared.methods):
                raise Redeclared(Method(), method.fun.name)
            type_declared.methods += [Symbol(method.fun.name, MType(method.fun.params, method.fun.retType))]

        return type_declared
    
    def __checkArrayMembersType(self, ast, c, eleType):
        if type(ast) is list:
            for ele in ast:
                if self.__checkArrayMembersType(ele, c, eleType):
                    return True
        else:
            arrType = self.visit(ast, c)
            if arrType is None:
                raise Undeclared(Identifier(), ast.name)
            if self.helper.checkTypeMismatch(eleType, eleType, True):
                return True
            return False
        return False

    def __evaluateDimensionExpr(self, expr, c, memo=None):
        if memo is None:
            memo = {}
        
        expr_key = str(expr)
        if expr_key in memo:
            return memo[expr_key]
        
        result = None
        if isinstance(expr, IntLiteral):
            result = expr.value
        elif isinstance(expr, Id):
            for scope in c:
                sym = self.lookup(expr.name, scope, lambda x: x.name)
                if sym is not None and sym.value is not None:
                    if isinstance(sym.value, IntLiteral):
                        result = sym.value.value
                        break
                    else:
                        result = self.__evaluateDimensionExpr(sym.value, c, memo)
                        break
        elif isinstance(expr, BinaryOp):
            left = self.__evaluateDimensionExpr(expr.left, c, memo)
            right = self.__evaluateDimensionExpr(expr.right, c, memo)
            
            if left is not None and right is not None:
                if expr.op == '+':
                    result = left + right
                elif expr.op == '-':
                    result = left - right
                elif expr.op == '*':
                    result = left * right
                elif expr.op == '/':
                    if right != 0:  
                        result = left // right
        
        memo[expr_key] = result
        return result
    
    def __checkArrayTypeMismatch(self, lhs, rhs, c, assign=False):
        if len(lhs.dimens) != len(rhs.dimens):
            return True
            
        memo = {}
        
        for i in range(len(lhs.dimens)):
            lhs_val = self.__evaluateDimensionExpr(lhs.dimens[i], c, memo)
            rhs_val = self.__evaluateDimensionExpr(rhs.dimens[i], c, memo)
            
            if lhs_val is not None and rhs_val is not None:
                if lhs_val != rhs_val:
                    return True
            elif lhs.dimens[i] != rhs.dimens[i]:
                return True
        
        return self.helper.checkTypeMismatch(lhs.eleType, rhs.eleType, assign)
    
    def visitProgram(self, ast: Program, c: List[Symbol]):
        self.list_type = reduce(
            lambda acc, ele: acc + [ele] if (isinstance(ele, StructType) or isinstance(ele, InterfaceType)) else acc,
            ast.decl,
            []
        )

        self.list_function = reduce(
            lambda acc, ele:
                acc + [ele] if isinstance(ele, FuncDecl) else acc,
            ast.decl,
            self.list_function
        )

        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                self.__update_method(decl, self.list_type)

        return reduce(
            lambda acc, ele: [[self.visit(ele, acc)] + acc[0]] + acc[1:] if isinstance(self.visit(ele, acc), Symbol) else acc,
            ast.decl,
            [c]
        )

    def visitVarDecl(self, ast, c):
        if self.helper.checkRedeclared(ast.varName, c[0]):
            raise Redeclared(Variable(), ast.varName)
        if ast.varInit:
            exprType = self.visit(ast.varInit, c)
            if exprType is None:
                raise Undeclared(Identifier(), ast.varInit.name)
           
            if isinstance(exprType, Id):
                exprType = self.helper.getType(self.list_type, exprType)

            if ast.varType:
                declType = ast.varType
                if isinstance(declType, Id):
                    declType = self.helper.getType(self.list_type, ast.varType)
                
                if isinstance(declType, ArrayType) and isinstance(exprType, ArrayType):
                    if self.__checkArrayTypeMismatch(declType, exprType, c, True):
                        raise TypeMismatch(ast)
                elif self.helper.checkTypeMismatch(declType, exprType, True):
                    raise TypeMismatch(ast)
                    
                return Symbol(ast.varName, declType, ast.varInit)
            return Symbol(ast.varName, exprType, ast.varInit)

        if ast.varType:
            return Symbol(ast.varName, ast.varType)
        return Symbol(ast.varName, None)

    def visitConstDecl(self, ast, c):
        if self.helper.checkRedeclared(ast.conName, c[0]):
            raise Redeclared(Constant(), ast.conName)

        if ast.iniExpr:
            exprType = self.visit(ast.iniExpr, c)
            if exprType is None:
                raise Undeclared(Identifier(), ast.iniExpr.name)
            if isinstance(exprType, Id):
                exprType = self.helper.getType(self.list_type, exprType)

            if ast.conType:
                declType = ast.conType
                if isinstance(declType, Id):
                    declType = self.helper.getType(self.list_type, ast.conType)
                
                if isinstance(declType, ArrayType) and isinstance(exprType, ArrayType):
                    if self.__checkArrayTypeMismatch(declType, exprType, c, True):
                        raise TypeMismatch(ast)

                if self.helper.checkTypeMismatch(declType, exprType, True):
                    raise TypeMismatch(ast)
                elif self.helper.checkTypeMismatch(exprType, declType, True):
                    raise TypeMismatch(ast)
                
                return Symbol(ast.conName, declType , ast.iniExpr)
            return Symbol(ast.conName, exprType, ast.iniExpr)

        
        return Symbol(ast.conName, ast.conType, ast.iniExpr)

    def visitFuncDecl(self, ast, c):
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Function(), ast.name)

        self.current_func = ast
        listParam = self.__functionVisit([[]] + c, ast.params)
        local_envi = self.__functionVisit([[]] + listParam, ast.body.member)

        self.current_func = None
        return Symbol(ast.name, MType(listParam, ast.retType))

    def visitParamDecl(self, ast, c):
        if self.helper.checkRedeclared(ast.parName, c[0]):
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType)

    def visitMethodDecl(self, ast, c):
        recType = self.helper.getType(self.list_type, ast.recType) 
        if recType is None:
            raise Undeclared(Type(), ast.recType.name)

        self.current_func = ast.fun
        
        listParam = self.__functionVisit([[Symbol(ast.receiver, ast.recType)]] + c, ast.fun.params)
        self.__functionVisit([[]] + listParam, ast.fun.body.member)

        self.current_func = None
        return None

    def visitStructType(self, ast, c):
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Type(), ast.name)

        list_field : List[Symbol] = []
        # list_return_elements: List[Tuple[str,Type]] = []
        for ele in ast.elements:
            if self.helper.checkRedeclared(ele[0], list_field):
                raise Redeclared(Field(), ele[0])

            eleType = ele[1]
            if isinstance(ele[1], StructType) or isinstance(ele[1], InterfaceType) or isinstance(ele[1], Id):
                eleType = self.helper.getType(self.list_type, ele[1])
                if eleType is None:
                    raise Undeclared(Type(), ele[1].name)
            
            list_field += [Symbol(ele[0], eleType)]
            # list_return_elements += [(ele[0], eleType)]

        return Symbol(ast.name, StructType(ast.name, ast.elements, ast.methods))
        

    def visitInterfaceType(self, ast, c):
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Type(), ast.name)
        
        list_prototype = reduce(
            lambda acc, ele: [[self.visit(ele, acc)] + acc[0]] + acc[1:] if self.visit(ele, acc) else acc,
            ast.methods,
            [[]] + c
        )[0]
        return Symbol(ast.name, InterfaceType(ast.name, list_prototype))
        
    def visitPrototype(self, ast, c):
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Prototype(), ast.name)
        return Symbol(ast.name, MType(ast.params, ast.retType))

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()



    def visitArrayLiteral(self, ast, c):
        if self.__checkArrayMembersType(ast.value, c, ast.eleType):
            raise TypeMismatch(ast)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast, c):
        struct = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if struct is None:
            raise Undeclared(Type(), ast.name)
        for ele in ast.elements:
            field = self.lookup(ele[0], struct.elements, lambda x: x[0])
            if field is None:
                raise Undeclared(Field(), ele[0])
            
            eleType = self.visit(ele[1], c)
            if eleType is None:
                raise Undeclared(Identifier(), ele[1].name)
            
            fieldType = field[1]
            if isinstance(field[1], Id):
                fieldType = self.helper.getType(self.list_type, field[1])
            
            if self.helper.checkTypeMismatch(fieldType, eleType):
                raise TypeMismatch(ast)

        return StructType(struct.name, struct.elements, struct.methods)

    def visitNilLiteral(self, ast, c):
        return VoidType()

    def visitReturn(self, ast, c):
        retType = self.current_func.retType
        if ast.expr:
            exprType = self.visit(ast.expr, c)
            if isinstance(retType, Id):
                retType = self.helper.getType(self.list_type, retType)

            if self.helper.checkTypeMismatch(retType, exprType):
                raise TypeMismatch(ast)
        else:
            if not isinstance(retType, VoidType):
                raise TypeMismatch(ast)
        return None
    
    def visitBinaryOp(self, ast, c):
        leftType = self.visit(ast.left, c)
        rightType = self.visit(ast.right, c)
        if leftType is None or rightType is None:
            raise Undeclared(Identifier(), ast.left.name if leftType is None else ast.right.name)

        if isinstance(leftType, StringType) and isinstance(rightType, StringType) and ast.op == '+':
            return StringType()
        
        if ast.op in ['+', '-', '*', '/']:
            # Handle Float + Float = Float
            if isinstance(leftType, FloatType) and isinstance(rightType, FloatType):
                return FloatType()
            # Handle Int + Int = Int
            if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                return IntType()
            # Handle Float + Int = Float or Int + Float = Float
            if (isinstance(leftType, FloatType) and isinstance(rightType, IntType)) or \
               (isinstance(leftType, IntType) and isinstance(rightType, FloatType)):
                return FloatType()
            raise TypeMismatch(ast)
        if ast.op in ['%']:
            if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                return IntType()
            raise TypeMismatch(ast)
        if ast.op in ['==', '!=', '<', '<=', '>', '>=']:
            if self.helper.checkTypeMismatch(leftType, rightType):
                raise TypeMismatch(ast)
            return BoolType()
        
        if ast.op in ['&&', '||']:
            if isinstance(leftType, BoolType) and isinstance(rightType, BoolType):
                return BoolType()
            raise TypeMismatch(ast)

    def visitId(self, ast, c):
        for ele in c:
            symbol = self.lookup(ast.name, ele, lambda x: x.name)
            if symbol is not None:
                if isinstance(symbol.mtype, MType):
                    return symbol.mtype.rettype
                if isinstance(symbol.mtype, Id):
                    return self.visit(symbol.mtype, c)
                if isinstance(symbol.mtype, ArrayType):
                    return ArrayType(symbol.mtype.dimens, symbol.mtype.eleType)
                return symbol.mtype

        return self.helper.getType(self.list_type, ast)

    def __getArrayType(self, ast, arrType, c) -> Type:
        #ArrayType:
            # dimens: List[Expr]
            # eleType: Type

        # arr
        # idx: List[Expr]
        
        # var a [2][3][3] int;
        # var b = a[1][2]; -> ArrayType([3], IntType())
        # var c = a[1][2][3]; -> IntType()
        # var d = a[1] -> ArrayType([3][3], IntType())
        idx_len = len(ast.idx)
        arr_len = len(arrType.dimens)

        if idx_len > arr_len:
            raise TypeMismatch(ast)
        if idx_len == arr_len:
            return arrType.eleType

        return ArrayType(
            arrType.dimens[(arr_len - idx_len):],
            arrType.eleType
        )

    def visitArrayCell(self, ast, c):
        arrayType = self.visit(ast.arr, c)
        
        if not isinstance(arrayType, ArrayType):
            raise TypeMismatch(ast)

        list_index = list(filter(
            lambda x: not isinstance(self.visit(x, c), IntType),
            ast.idx
        ))
        if len(list_index) > 0:
            raise TypeMismatch(ast)
        
        return self.__getArrayType(ast, arrayType, c)
        


    def visitFieldAccess(self, ast, c):
        recv = self.visit(ast.receiver, c)
        
        if not isinstance(recv, Id) and not isinstance(recv, StructType):
            raise TypeMismatch(ast)
        
        struct = self.lookup(recv.name, self.list_type, lambda x: x.name)
        if not isinstance(struct, StructType):
            raise TypeMismatch(ast)
        field = self.lookup(ast.field, struct.elements, lambda x: x[0])
        if field is None:
            raise Undeclared(Field(), ast.field)
        return field[1]

    def visitUnaryOp(self, ast, c):
        bodyType = self.visit(ast.body, c)
        if bodyType is None:
            raise Undeclared(Identifier(), ast.body.name)
        
        if ast.op in ['!']:
            if isinstance(bodyType, BoolType):
                return BoolType()
            raise TypeMismatch(ast)
        
        if ast.op in ['-']:
            if isinstance(bodyType, IntType):
                return IntType()
            if isinstance(bodyType, FloatType):
                return FloatType()
        raise TypeMismatch(ast)

    def visitFuncCall(self, ast, c):
        function = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if function is None:
            raise Undeclared(Function(), ast.funName)
        if len(ast.args) != len(function.params):
            raise TypeMismatch(ast)
        
        list_mismatch_param = list(
            filter(
                lambda x: self.helper.checkTypeMismatch(self.visit(x[0], c), x[1].parType),
                zip(ast.args, function.params)
            )
        )
        if len(list_mismatch_param) > 0:
            raise TypeMismatch(ast)   

        return function.retType

    def visitMethCall(self, ast, c):
        type = self.visit(ast.receiver, c)
        if not isinstance(type, StructType) and not isinstance(type, InterfaceType):
            raise TypeMismatch(ast)
        method = self.lookup(ast.metName, type.methods, lambda x: x.name)
        if method is None:
            raise Undeclared(Method(), ast.metName)
        if len(ast.args) != len(method.mtype.partype):
            raise TypeMismatch(ast)
        
        list_mismatch_param = list(
            filter(
                lambda x: self.helper.checkTypeMismatch(self.visit(x[0], c), x[1].parType),
                zip(ast.args, method.mtype.partype)
            )
        )
        if len(list_mismatch_param) > 0:
            raise TypeMismatch(ast)    
        return method.mtype.rettype

    def visitAssign(self, ast, c):
        lhsType = self.visit(ast.lhs, c)
        rhsType = self.visit(ast.rhs, c)

        if lhsType is None and not isinstance(rhsType, VoidType):
            return Symbol(ast.lhs.name, rhsType, ast.rhs)
            
        if isinstance(lhsType, ArrayType) and isinstance(rhsType, ArrayType):
            if self.__checkArrayTypeMismatch(lhsType, rhsType, c, True):
                raise TypeMismatch(ast)
        elif self.helper.checkTypeMismatch(lhsType, rhsType, True):
            raise TypeMismatch(ast)
            
        return None
    
    def visitIf(self, ast, c):
        condType = self.visit(ast.expr, c)
        if not isinstance(condType, BoolType):
            raise TypeMismatch(ast)
        self.__functionVisit([[]] + c, ast.thenStmt.member)
        if ast.elseStmt:
            self.__functionVisit([[]] + c, ast.elseStmt.member)
        return None

    def visitBreak(self, ast, c):
        return None
    
    def visitContinue(self, ast, c):
        return None
    
    def visitForBasic(self, ast, c):
        typeExpr = self.visit(ast.cond, c)
        if not isinstance(typeExpr, BoolType):
            raise TypeMismatch(ast)
        self.__functionVisit([[]] + c, ast.loop.member)
        return None

    def visitForStep(self, ast, c):
        cur_envi = [[]] + c
        cur_envi = [[self.visit(ast.init, cur_envi)] + cur_envi[0]] + cur_envi[1:] if not None else cur_envi
        condType  = self.visit(ast.cond, cur_envi)        
        if not isinstance(condType, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.upda, cur_envi)
        self.__functionVisit(cur_envi, ast.loop.member)
        return None

    def visitForEach(self, ast, c):
        arrayType = self.visit(ast.arr, [[]] + c)
        if not isinstance(arrayType, ArrayType):
            raise TypeMismatch(ast)
        
        if ast.idx.name != '_':
            env = [[Symbol(ast.idx.name, IntType()), Symbol(ast.value.name, arrayType)]] + c
        else:
            env = [[Symbol(ast.value.name, arrayType)]] + c
        self.__functionVisit(env, ast.loop.member)
        return None

class HelperClass(StaticChecker):
    def __init__(self):
        pass

    def initializeGlobalEnvironment(self) -> List[Symbol]:
        return [
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
            Symbol("putFloat", MType([FloatType()], VoidType())),
            Symbol("putFloatLn", MType([FloatType()], VoidType())),
            Symbol("getBool", MType([], BoolType())),
            Symbol("putBool", MType([BoolType()], VoidType())),
            Symbol("putBoolLn", MType([BoolType()], VoidType())),
            Symbol("getString", MType([], StringType())),
            Symbol("putString", MType([StringType()], VoidType())),
            Symbol("putStringLn", MType([StringType()], VoidType())),
            Symbol("putLn", MType([], VoidType()))
        ]

    def buildInbuiltFunction(self) -> List[Symbol]:
        return [
            FuncDecl("getInt", [], IntType(), Block([Return(None)])),
            FuncDecl("putInt", [ParamDecl("x", IntType())], VoidType(), Block([Return(None)])),
            FuncDecl("putIntLn", [ParamDecl("x", IntType())], VoidType(), Block([Return(None)])),
            FuncDecl("getFloat", [], FloatType(), Block([Return(None)])),
            FuncDecl("putFloat", [ParamDecl("x", FloatType())], VoidType(), Block([Return(None)])),
            FuncDecl("putFloatLn", [ParamDecl("x", FloatType())], VoidType(), Block([Return(None)])),
            FuncDecl("getBool", [], BoolType(), Block([Return(None)])),
            FuncDecl("putBool", [ParamDecl("x", BoolType())], VoidType(), Block([Return(None)])),
            FuncDecl("putBoolLn", [ParamDecl("x", BoolType())], VoidType(), Block([Return(None)])),
            FuncDecl("getString", [], StringType(), Block([Return(None)])),
            FuncDecl("putString", [ParamDecl("x", StringType())], VoidType(), Block([Return(None)])),
            FuncDecl("putStringLn", [ParamDecl("x", StringType())], VoidType(), Block([Return(None)])),
            FuncDecl("putLn", [], VoidType(), Block([Return(None)])),
        ]

    def checkRedeclared(self, name: str, List: List[Symbol]) -> bool:
        filtered_list = list(filter(None, List))
        return self.lookup(name, filtered_list, lambda x: x.name) is not None

    def checkTypeMismatch(self, lhs: Type, rhs: Type, assign = False) -> bool:
        if isinstance(rhs, VoidType) and assign:
            return True
        if isinstance(lhs, FloatType) and isinstance(rhs, IntType) and assign:
            return False
        if isinstance(lhs, Id) and isinstance(rhs, Id):
            return lhs.name != rhs.name
        if isinstance(lhs, StructType) and isinstance(rhs, StructType):
            return lhs.name != rhs.name
        if isinstance(lhs, InterfaceType) and isinstance(rhs, InterfaceType):
            return lhs.name != rhs.name
        if isinstance(lhs, InterfaceType) and isinstance(rhs, StructType):
            list_undeclared_prototype = list(
                filter(
                    lambda x: self.checkMethod(x, rhs.methods),
                    lhs.methods
                )
            )
            if len(list_undeclared_prototype) > 0:
                return True
            return False

        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            return type(lhs.eleType) != type(rhs.eleType)
        
        return type(lhs) != type(rhs)

    def getType(self, listType: List[Union[StructType, InterfaceType]], recType: Type) -> Union[StructType, InterfaceType]:
        recType =  list(filter(lambda x: x.name == recType.name, listType))
        return recType[0] if len(recType) > 0 else None

    def isDeclared(self, value: (str, Type), list_declare) -> bool:
        return value in list_declare

    def checkMethod(self, prototype: Prototype, list_method: List[Symbol]) -> bool:
        method: Method = self.lookup(prototype.name, list_method, lambda x: x.name)
        if method is None or len(prototype.params) != len(method.mtype.partype):
            return True

        list_mismatch_param = list(
            filter(
                lambda x: self.checkTypeMismatch(x[0], x[1].parType),
                zip(prototype.params, method.mtype.partype)
            )
        )
        if len(list_mismatch_param) > 0:
            return True

        return self.checkTypeMismatch(prototype.retType, method.mtype.rettype)
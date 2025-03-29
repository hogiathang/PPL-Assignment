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
    def __debug(self, c: List[List[Symbol]]):
        for ele in c:
            print('-----------------')
            for sym in ele:
                print(sym.__str__())
            print('-----------------')
        return None

    def __functionVisit(self, cur_envi, cur_list):
        return list(reduce(
            lambda acc, ele:
                [[self.visit(ele, acc)] + acc[0]] + acc[1:] if not None else acc,
            cur_list,
            cur_envi
        ))    
    
    def __init__(self,ast):
        self.helper = HelperClass()
        self.ast = ast
        self.global_envi    = self.helper.initializeGlobalEnvironment()
        self.list_type      = []
        self.list_function  = self.helper.buildInbuiltFunction()
        self.list_interface_declared = []
        self.current_func   = None

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast: Program, c: List[Symbol]):
        # Add all struct and interface type to list_type
        self.list_type = reduce(
            lambda acc, ele: acc + [ele] if (isinstance(ele, StructType) or isinstance(ele, InterfaceType)) else acc,
            ast.decl,
            []
        )

        # Add all function to list_function
        self.list_function = reduce(
            lambda acc, ele:
                acc + [ele] if isinstance(ele, FuncDecl) else acc,
            ast.decl,
            self.list_function
        )

        # Visit declaration
        return reduce(
            lambda acc, ele: [[self.visit(ele, acc)] + acc[0]] + acc[1:] if not None else acc,
            ast.decl,
            [c]
        )

    def visitVarDecl(self, ast, c):
        # Check name of variable declared
        if self.helper.checkRedeclared(ast.varName, c[0]):
            raise Redeclared(Variable(), ast.varName)

    
        if ast.varInit:
            exprType = self.visit(ast.varInit, c)
            if isinstance(exprType, Id):
                exprType = self.helper.getType(self.list_type, exprType)

            if ast.varType:
                declType = self.helper.getType(self.list_type, ast.varType)
            
                if self.helper.checkTypeMismatch(exprType, declType):
                    raise TypeMismatch(ast)
                
                return Symbol(ast.varName, exprType, ast.varInit)
            return Symbol(ast.varName, exprType, ast.varInit)

        if ast.varType:
            return Symbol(ast.varName, ast.varType)
        return Symbol(ast.varName, None)

    def visitConstDecl(self, ast, c):
        # Check name of constant declared
        if self.helper.checkRedeclared(ast.conName, c[0]):
            raise Redeclared(Constant(), ast.conName)
        
        if ast.iniExpr:
            exprType = self.visit(ast.iniExpr, c)
            if isinstance(exprType, Id):
                exprType = self.helper.getType(self.list_type, exprType)

            if ast.conType:
                declType = self.helper.getType(self.list_type, ast.conType)
            
                if self.helper.checkTypeMismatch(exprType, declType):
                    raise TypeMismatch(ast)
                
                return Symbol(ast.conName, declType , ast.iniExpr)
            return Symbol(ast.conName, exprType, ast.iniExpr)

        
        return Symbol(ast.conName, ast.conType, ast.iniExpr)

    def visitFuncDecl(self, ast, c):
        # Check name of function declared
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Function(), ast.name)

        self.current_func = ast
        # Add parameter to current environment
        listParam = self.__functionVisit([[]] + c, ast.params)
        local_envi = self.__functionVisit(listParam, ast.body.member)

        self.current_func = None
        return Symbol(ast.name, MType(listParam, ast.retType))

    def visitParamDecl(self, ast, c):
        # Check name of parameter declared
        if self.helper.checkRedeclared(ast.parName, c[0]):
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType)

    def visitMethodDecl(self, ast, c):
        # Check name of method declared
        recType = self.helper.getType(self.list_type, ast.recType) 
        if recType is None:
            raise Undeclared(Type(), ast.recType.name)

        self.current_func = ast.fun

        if isinstance(recType, StructType):
            if self.helper.checkRedeclared(ast.fun.name, recType.methods):
                raise Redeclared(Method(), ast.fun.name)
            listParam = self.__functionVisit([[Symbol(ast.receiver, ast.recType)]] + c, ast.fun.params)
            local_envi = self.__functionVisit(listParam, ast.fun.body.member)

            recType.methods += [Symbol(ast.fun.name, MType(listParam, ast.fun.retType))]
        else:
            if self.helper.isDeclared((ast.fun.name, recType), self.list_interface_declared):
                raise Redeclared(Method(), ast.fun.name)
            
            listParam = self.__functionVisit([[Symbol(ast.receiver, ast.recType)]] + c, ast.fun.params)
            local_envi = self.__functionVisit(listParam, ast.fun.body.member)

            self.list_interface_declared += [(ast.fun.name, recType)]
        self.current_func = None
        return None

    def visitStructType(self, ast, c):
        # Check name of struct declared
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Type(), ast.name)

        # Check name of field declared
        list_field = []
        for ele in ast.elements:
            # Check redeclared field
            if self.helper.checkRedeclared(ele[0], list_field):
                raise Redeclared(Field(), ele[0])

            # Check undeclared type
            if isinstance(ele[1], StructType) or isinstance(ele[1], InterfaceType):
                if self.helper.getType(self.list_type, ele[1]) is None:
                    raise Undeclared(Type(), ele[1].name)
            
            list_field += [Symbol(ele[0], ele[1])]
        return Symbol(ast.name, StructType(ast.name, list_field, []))

    def visitInterfaceType(self, ast, c):
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Type(), ast.name)

        list_prototype = reduce(
                lambda acc, ele:
                    [[self.visit(ele, acc)] + acc[0]] + acc[1:] if not None else acc,
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
        return ArrayType(self.visit(ast.value[0], c))

    def visitNilLiteral(self, ast, c):
        return VoidType()

    def visitReturn(self, ast, c):
        retType = self.current_func.retType
        if ast.expr:
            exprType = self.visit(ast.expr, c)
            if self.helper.checkTypeMismatch(retType, exprType):
                raise TypeMismatch(ast)
        else:
            if not isinstance(retType, VoidType):
                raise TypeMismatch(ast)
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

    def visitAssign(self, ast, c):
        lhsType = self.visit(ast.lhs, c)
        rhsType = self.visit(ast.rhs, c)
        if lhsType is None:
            return Symbol(ast.lhs.name, rhsType, ast.rhs)
        if self.helper.checkTypeMismatch(lhsType, rhsType):
            raise TypeMismatchInStatement(ast)
        return None


    def visitForEach(self, ast, c):
        arrayType = self.visit(ast.arr, [[]] + c)
        if not isinstance(arrayType, ArrayType):
            raise TypeMismatchInExpression(ast.arr)


        if ast.idx.name != '_':
            env = [[Symbol(ast.idx.name, IntType()), Symbol(ast.value.name, arrayType)]] + c
        else:
            env = [[Symbol(ast.value.name, arrayType)]] + c

        self.__functionVisit(env, ast.loop.member)
        return None


    def visitBinaryOp(self, ast, c):
        print("visitBinaryOp")
        leftType = self.visit(ast.left, c)
        rightType = self.visit(ast.right, c)    

        if isinstance(leftType, StringType) and isinstance(rightType, StringType) and ast.op == '+':
            return StringType()
        
        if ast.op in ['+', '-', '*', '/']:
            if isinstance(leftType, FloatType) or isinstance(rightType, FloatType):
                if isinstance(leftType, IntType) or isinstance(rightType, IntType):
                    return FloatType()
                if isinstance(leftType, FloatType) and isinstance(rightType, FloatType):
                    return FloatType()
            if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                return IntType()
            raise TypeMismatch(ast)
        if ast.op in ['%']:
            if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                return IntType()
            raise TypeMismatch(ast)
        if ast.op in ['==', '!=', '<', '<=', '>', '>=']:
            print("leftType", leftType)
            print("rightType", rightType)
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
                return symbol.mtype
        return None

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitExpr(self, ast, c):
        if self.helper.isBasicType(ast, c) is not None:
            return self.helper.isBasicType(ast, c)

        if self.helper.isLiteral(ast, c) is not None:
            return self.helper.isLiteral(ast, c)

        if self.helper.isOtherType(ast, c) is not None:
            return self.helper.isOtherType(ast, c)
        
        return None

    def isBasicType(self, ast: PrimLit, c: List[List[Symbol]]) -> Type:
        if isinstance(ast, IntLiteral):
            return IntType()
        if isinstance(ast, FloatLiteral):
            return FloatType()
        if isinstance(ast, StringLiteral):
            return StringType()
        if isinstance(ast, BooleanLiteral):
            return BoolType()
        return None

    def isLiteral(self, ast: Literal, c: List[List[Symbol]]) -> Type:
        if isinstance(ast, NilLiteral):
            return VoidType()

        if isinstance(ast, ArrayLiteral):
            listDimensType = filter(
                lambda x: not isinstance(self.visit(x, c), IntType),
                ast.dimens
            )
            if len(listDimensType) > 0:
                raise TypeMismatch(ast)
            
            return ArrayType(ast.dimens, ast.eleType)
       
        if isinstance(ast, StructLiteral):
            struct = self.lookup(ast.name, self.list_type, lambda x: x.name)
            if struct is None:
                raise Undeclared(Type(), ast.name)
            
            if isinstance(struct, InterfaceType):
                    raise TypeMismatch(ast)

            check_undeclare = list(filter(
                lambda x: self.lookup(x[0], struct.elements, lambda y: y[0]) is None,
                ast.elements
            ))

            if len(check_undeclare) > 0:
                raise Undeclared(Field(), check_undeclare[0][0])

            check_type_mismatch = list(filter(
                lambda x: self.checkTypeMismatch(
                    self.lookup(x[0], struct.elements, lambda y: y[0])[1],
                    self.visit(x[1], c)
                )
            ))

            if len(check_type_mismatch) > 0:
                raise TypeMismatch(ast)

            return StructType(struct.name, struct.elements, struct.methods)
        return None

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

    def visitFieldAccess(self, ast, c):
        recv = self.visit(ast.receiver, c)
        struct = self.lookup(recv.name, self.list_type, lambda x: x.name)
        if not isinstance(struct, StructType):
            raise TypeMismatch(ast)

        field = self.lookup(ast.field, struct.elements, lambda x: x[0])
        if field is None:
            raise Undeclared(Field(), ast.field)
        
        return field[1]

    def visitUnaryOp(self, ast, c):
        if ast.op in ['!']:
            if isinstance(self.visit(ast.body, c), BoolType):
                return BoolType()
            raise TypeMismatch(ast)
        
        if ast.op in ['-']:
            if isinstance(self.visit(ast.body, c), IntType):
                return IntType()
            if isinstance(self.visit(ast.body, c), FloatType):
                return FloatType()
        raise TypeMismatch(ast)

    def visitFuncCall(self, ast, c):
        function = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if function is None:
            raise Undeclared(Function(), ast.funName)
        return function.retType

    def visitMethodCall(self, ast, c):
        pass
        

   
class HelperClass(Utils):
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
        return self.lookup(name, List, lambda x: x.name) is not None

    def checkTypeMismatch(self, type1, type2) -> bool:
        if isinstance(type1, StructType) and isinstance(type2, StructType):
            return type1.name != type2.name
        return type(type1) != type(type2)

    def getType(self, listType: List[Union[StructType, InterfaceType]], recType: Type) -> Union[StructType, InterfaceType]:
        recType =  list(filter(lambda x: x.name == recType.name, listType))
        return recType[0] if len(recType) > 0 else None

    def isDeclared(self, value: (str, Type), list_declare) -> bool:
        return value in list_declare


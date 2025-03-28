"""
 * Authors: Ho Gia Thang - 2213187
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

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


class HelperClass(Utils):
    def __init__(self):
        pass

    def initializeGlobalEnvironment(self) -> List[List[Symbol]]:
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

    def checkRedeclared(self, name: str, List: List[Symbol]) -> bool:
        return self.lookup(name, List, lambda x: x.name) is not None

    def checkTypeMismatch(self, type1, type2) -> bool:
        return type(type1) != type(type2)

    def getType(self, listType: List[Union[StructType, InterfaceType]], recType: Type) -> Union[StructType, InterfaceType]:
        recType =  list(filter(lambda x: x.name == recType.name, listType))
        return recType[0] if len(recType) > 0 else None

    def isDeclared(self, value: (str, Type), list_declare) -> bool:
        return value in list_declare

    
class StaticChecker(BaseVisitor,Utils):

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
        self.list_function  = []
        self.list_interface_declared = []
        self.current_func   = None

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast: Program, c: List[Symbol]):
        # Add all struct and interface type to list_type
        self.list_type = reduce(
            lambda acc, ele: acc + [ele] if (isinstance(ele, StructType) or isinstance(ele, InterfaceType)) else acc,
            ast.decl,
            []
        )

        # Add all function to list_function
        self.list_function = reduce(
            lambda acc, ele: acc + [ele] if isinstance(ele, FuncDecl) else acc,
            ast.decl,
            []
        )

        # Visit declaration
        return List(reduce(
            lambda acc, ele: [[self.visit(ele, acc)] + acc[0]] + acc[1:] if not None else acc,
            ast.decl,
            [c]
        ))

    def visitVarDecl(self, ast, c):
        # Check name of variable declared
        if self.helper.checkRedeclared(ast.varName, c[0]):
            raise Redeclared(Variable(), ast.varName)

        if ast.varInit:
            Type = self.visit(ast.varInit, c)
            if ast.varType:
                if self.helper.checkTypeMismatch(ast.varType, ast.varInit):
                    raise TypeMismatch(ast)
                return Symbol(ast.varName, ast.varType, ast.varInit)
            return Symbol(ast.varName, Type, ast.varInit)
        if ast.varType:
            return Symbol(ast.varName, ast.varType)
        return Symbol(ast.varName, None)

    def visitConstDecl(self, ast, c):
        # Check name of constant declared
        if self.helper.checkRedeclared(ast.conName, c[0]):
            raise Redeclared(Constant(), ast.conName)

        Type = self.visit(ast.iniExpr, c)
        if ast.conType:
            if self.helper.checkTypeMismatch(ast.conType, ast.iniExpr):
                raise TypeMismatch(ast)
            return Symbol(ast.conName, ast.conType, ast.iniExpr)
        return Symbol(ast.conName, Type, ast.iniExpr)

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
        # Check name of interface declared
        if self.helper.checkRedeclared(ast.name, c[0]):
            raise Redeclared(Type(), ast.name)

        # Check name of field declared
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
        initValue = self.visit(ast.init, c)
        condType  = self.visit(ast.cond, initValue)
        
        if not isinstance(condType, BoolType):
            raise TypeMismatch(ast)

        upDat     = self.visit(ast.up, initValue)
        self.__functionVisit(upDat, ast.loop.member)
        return None

    def visitForEach(self, ast, c):
        if ast.idx.name != '_':
            env = [[Symbol(ast.idx.name, IntType()), Symbol(ast.value.name, )]] + c
        else:
            env = [[Symbol(ast.value.name, )]] + c

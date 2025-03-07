# STUDENT ID: 2213187
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])

    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))
    	
    def visitVarDecl(self,ctx:MiniGoParser.VarDeclContext):
        (varType, varInit) = self.visit(ctx.varDetail())
        return VarDecl(ctx.IDENTIFIER().getText(), varType, varInit)

    def visitVarDetail(self, ctx:MiniGoParser.VarDetailContext):
        if ctx.getChildCount() == 2:
            return (self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
        elif ctx.varDeclType():
            return (self.visit(ctx.varDeclType()), None)
        else:
            return (None, self.visit(ctx.varDeclExpr()))
    
    # #-------------------Const------------------
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        conName = ctx.IDENTIFIER().getText()
        conType = None
        conInit = self.visit(ctx.varDeclExpr())
        return ConstDecl(conName,conType,conInit)

    # #-------------------Type-------------------
    def visitVarDeclType(self, ctx:MiniGoParser.VarDeclTypeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return ArrayType(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
    
    def visitBaseType(self, ctx:MiniGoParser.BaseTypeContext):
        if ctx.getChild(0).getText() == "int":
            return IntType()
        if ctx.getChild(0).getText() == "float":
            return FloatType()
        if ctx.getChild(0).getText() == "boolean":
            return BoolType()
        if ctx.getChild(0).getText() == "string":
            return StringType()
        return Id(ctx.getChild(0).getText())

    # #-------------------VarExpression-------------------
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return [self.visit(i) for i in ctx.intLitOrConstant()]

    def visitIntLitOrConstant(self, ctx:MiniGoParser.IntLitOrConstantContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        return Id(ctx.IDENTIFIER().getText())

    def visitVarDeclExpr(self, ctx:MiniGoParser.VarDeclExprContext):
        return self.visit(ctx.expr())


    # #-------------------Expression-------------------
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visit(ctx.getChild(0))

    def visitLogicOrExpr(self, ctx:MiniGoParser.LogicOrExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicAndExpr())
        return BinaryOp("||", self.visit(ctx.logicOrExpr()), self.visit(ctx.logicAndExpr()))

    def visitLogicAndExpr(self, ctx:MiniGoParser.LogicAndExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equalityExpr())
        return BinaryOp("&&", self.visit(ctx.logicAndExpr()), self.visit(ctx.equalityExpr()))

    def visitEqualityExpr(self, ctx:MiniGoParser.EqualityExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additiveExpr())
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.equalityExpr()), self.visit(ctx.additiveExpr()))

    def visitAdditiveExpr(self, ctx:MiniGoParser.AdditiveExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicativeExpr())
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.additiveExpr()), self.visit(ctx.multiplicativeExpr()))

    def visitMultiplicativeExpr(self, ctx:MiniGoParser.MultiplicativeExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpr())
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.multiplicativeExpr()), self.visit(ctx.unaryExpr()))

    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primaryExpr())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.unaryExpr()))

    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        expr = self.visit(ctx.getChild(0))
        if ctx.callSuffix():
            argList = self.visit(ctx.callSuffix())
            expr = FuncCall(expr, argList)
        elif type(expr) == str:
            expr = Id(expr)

        for suffix in ctx.primarySuffix():
            if suffix.DOT():
                if suffix.getChildCount() == 4:
                    argList = self.visit(suffix.callSuffix())
                    expr = MethCall(expr, suffix.IDENTIFIER().getText(), argList)
                    expr = ArrayCell(expr, self.visit(suffix.arraySuffix()))

                elif suffix.getChildCount() == 3 and suffix.callSuffix():
                    argList = self.visit(suffix.callSuffix())
                    expr = MethCall(expr, suffix.IDENTIFIER().getText(), argList)

                elif suffix.getChildCount() == 3 and suffix.arraySuffix():
                    expr = FieldAccess(expr, suffix.IDENTIFIER().getText())
                    expr = ArrayCell(expr, self.visit(suffix.arraySuffix()))
                else:
                    expr = FieldAccess(expr, suffix.IDENTIFIER().getText())
            else:
                if suffix.arraySuffix():
                    expr = ArrayCell(expr, self.visit(suffix.arraySuffix()))
        return expr

    def visitTerm(self, ctx:MiniGoParser.TermContext):
        # ( expr )
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        if ctx.INT_LIT():
            # text    = ctx.INT_LIT().getText()

            # if text.startswith("0x") or text.startswith("0X"):
            #     value =  int(text[2:], 16)

            # elif text.startswith("0o") or text.startswith("0O"):
            #     value =  int(text[2:], 8)
            
            # elif text.startswith("0b") or text.startswith("0B"):
            #     value =  int(text[2:], 2)

            # else:
            #     value =  int(text)

            return IntLiteral(ctx.INT_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(True)
        if ctx.FALSE():
            return BooleanLiteral(False)
        if ctx.NIL():
            return NilLiteral()
        if ctx.structLit():
            return self.visit(ctx.structLit())
        if ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        

    def visitCallSuffix(self, ctx:MiniGoParser.CallSuffixContext):
        return self.visit(ctx.argList()) if ctx.argList() else []

    def visitArgList(self, ctx:MiniGoParser.ArgListContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitArraySuffix(self, ctx:MiniGoParser.ArraySuffixContext):
        return [self.visit(expr) for expr in ctx.expr()]

    # #-------------------Function-------------------
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        funcName = ctx.IDENTIFIER().getText()
        funcParam = self.visit(ctx.funcParam()) if ctx.funcParam() else []
        funcType = self.visit(ctx.funcType())
        block = Block([self.visit(i) for i in ctx.statement()])

        return FuncDecl(funcName,funcParam,funcType,block)

    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):

        if ctx.getChildCount() == 2:
            listID = self.visitFuncListIdentifiers(ctx.getChild(0))
            typeOfId = self.visit(ctx.getChild(1))
            return [ParamDecl(i, typeOfId) for i in listID]

        if ctx.getChildCount() == 4:
            listID = self.visitFuncListIdentifiers(ctx.getChild(0))
            typeOfId = self.visit(ctx.getChild(1))
            nextParam = self.visit(ctx.getChild(3))
            return [ParamDecl(i, typeOfId) for i in listID] + nextParam

    def visitFuncListIdentifiers(self, ctx:MiniGoParser.FuncListIdentifiersContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        
        nextParam = self.visit(ctx.getChild(2))
        return [ctx.IDENTIFIER().getText()] + nextParam

    def visitFuncType(self, ctx:MiniGoParser.FuncTypeContext):
        if ctx.getChildCount() == 0:
            return VoidType()
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return ArrayType(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))

    # #-------------------Method-------------------

    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        receiver = ctx.IDENTIFIER(0).getText()
        recType  = Id(ctx.IDENTIFIER(1).getText())
        methodName = ctx.IDENTIFIER(2).getText()
        methodParam = self.visit(ctx.funcParam()) if ctx.funcParam() else []
        methodType = self.visit(ctx.funcType())
        block = Block([self.visitStatement(i) for i in ctx.statement()])
        return MethodDecl(receiver, recType, FuncDecl(methodName, methodParam, methodType, block))

    # #-------------------Type Decl-------------------
    def visitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        if ctx.STRUCT():
            name = ctx.IDENTIFIER().getText()
            fields = self.visit(ctx.structDeclBlock())
            elements = []
            methods = []
            for field in fields:
                if type(field) == tuple:
                    elements.append(field)
                else:
                    methods.append(field)
            return StructType(name, elements, methods)

        if ctx.INTERFACE():
            name = ctx.IDENTIFIER().getText()
            methods = self.visit(ctx.interfaceDeclBlock())
            return InterfaceType(name, methods)

    # #-------------------Struct Decl-------------------
    def visitStructDeclBlock(self, ctx:MiniGoParser.StructDeclBlockContext):
        return [self.visit(i) for i in ctx.structDeclField()]

    def visitStructDeclField(self, ctx:MiniGoParser.StructDeclFieldContext):
        return (ctx.IDENTIFIER().getText(), self.visit(ctx.getChild(1)))

    # $ #-------------------Interface Decl-------------------
    def visitInterfaceDeclBlock(self, ctx:MiniGoParser.InterfaceDeclBlockContext):
        return [self.visit(i) for i in ctx.interfaceDeclField()]

    def visitInterfaceDeclField(self, ctx:MiniGoParser.InterfaceDeclFieldContext):
        funcParam = self.visit(ctx.prototypeParam()) if ctx.prototypeParam() else []
        funcType = self.visit(ctx.funcType())
        return Prototype(ctx.IDENTIFIER().getText(), funcParam, funcType)

    def visitPrototypeParam(self, ctx:MiniGoParser.PrototypeParamContext):
        if ctx.getChildCount() == 2:
            listID = self.visitFuncListIdentifiers(ctx.getChild(0))
            typeOfId = self.visit(ctx.getChild(1))
            return [typeOfId for i in listID]
                

        if ctx.getChildCount() == 4:
            listID = self.visitFuncListIdentifiers(ctx.getChild(0))
            typeOfId = self.visit(ctx.getChild(1))
            nextParam = self.visit(ctx.getChild(3))
            return [typeOfId for i in listID] + nextParam

    # #-------------------Statement-------------------
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitDeclarationStatement(self, ctx:MiniGoParser.DeclarationStatementContext):
        return self.visit(ctx.getChild(0))

    def visitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        lhs = self.visit(ctx.getChild(0))
        if ctx.getChild(1).getText() == "+=":
            rhs = BinaryOp("+",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "-=":
            rhs = BinaryOp("-",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "*=":
            rhs = BinaryOp("*",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "/=":
            rhs = BinaryOp("/",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "%=":
            rhs = BinaryOp("%",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == ":=":
            rhs = self.visit(ctx.getChild(2))
        return Assign(lhs, rhs)

    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        expr = self.visit(ctx.expr())
        thenStmt = Block([self.visit(i) for i in ctx.statement()])
        elseStmt = None
        listElseIfStmt = []
        for elseIfStmt in ctx.elseIfStatement():
            elseExpr, elseThenStmt = self.visit(elseIfStmt)
            listElseIfStmt.append((elseExpr, elseThenStmt))

        if ctx.elseStatement():
            elseStmt = Block(self.visit(ctx.elseStatement()))
        
        for element in listElseIfStmt[::-1]:
            elseStmt = If(element[0], element[1], elseStmt)
        

        return If(expr, thenStmt, elseStmt)

    # $-------------------If Stmt-------------------
    def visitElseIfStatement(self, ctx:MiniGoParser.ElseIfStatementContext):
        expr = self.visit(ctx.expr())
        thenStmt = Block([self.visit(i) for i in ctx.statement()])
        return expr, thenStmt

    def visitElseStatement(self, ctx:MiniGoParser.ElseStatementContext):
        return [self.visit(i) for i in ctx.statement()]

    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visit(ctx.getChild(0))

    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return Break()

    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return Continue()

    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visit(ctx.getChild(0))

    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)

    

    # $-------------------Assign Statement-------------------
    def visitAssignStateLHS(self, ctx:MiniGoParser.AssignStateLHSContext):
        name = ctx.IDENTIFIER().getText()
        listArray = []
        expr = None
        for i in ctx.expr():
            listArray.append(self.visit(i))
        expr = ArrayCell(Id(name), listArray) if listArray != [] else Id(name)

        if ctx.assignTail():
            name, listArray, nextAssign = self.visit(ctx.assignTail())
            expr = FieldAccess(expr, name)
            expr = ArrayCell(expr, listArray) if listArray != [] else expr
            while nextAssign != None:
                name, listArray, nextAssign = self.visit(nextAssign)
                expr = FieldAccess(expr, name)
                expr = ArrayCell(expr, listArray) if listArray != [] else expr
        return expr

    def visitAssignTail(self, ctx:MiniGoParser.AssignTailContext):
        nextAssign = ctx.assignTail() if ctx.assignTail() else None
        listArray = []
        for i in ctx.expr():
            listArray.append(self.visit(i))
        return ctx.IDENTIFIER().getText(), listArray, nextAssign
 

    # $-------------------Call Statement-------------------
    def visitMethodCallStatement(self, ctx:MiniGoParser.MethodCallStatementContext):
        name = ctx.IDENTIFIER().getText()
        argList = self.visit(ctx.callStatementParam()) if ctx.callStatementParam() else []
        listMethod = self.visit(ctx.methodCallHead(0))
        receiver = None
        if listMethod[0] == "Field":
            receiver = Id(listMethod[1])
        elif listMethod[0] == "ArrayCell":
            receiver = ArrayCell(Id(listMethod[1]), listMethod[2])
        else:
            receiver = FuncCall(listMethod[1], listMethod[2])

        for method in ctx.methodCallHead()[1:]:
            listMethod = self.visit(method)
            if listMethod[0] == "Field":
                receiver = FieldAccess(receiver, listMethod[1])
            elif listMethod[0] == "ArrayCell":
                receiver = FieldAccess(receiver, listMethod[1])
                receiver = ArrayCell(receiver, listMethod[2])
            else:
                receiver = MethCall(receiver, listMethod[1], listMethod[2])
        return MethCall(receiver, name, argList)

    def visitMethodCallHead(self, ctx:MiniGoParser.MethodCallHeadContext):
        name = ctx.IDENTIFIER().getText()
        if ctx.LPAREN():
            argList = self.visit(ctx.callStatementParam()) if ctx.callStatementParam() else []
            return "Meth", name, argList
        elif ctx.callStatementArrayTail():
            arrayList = self.visit(ctx.callStatementArrayTail())
            return "ArrayCell", name, arrayList

        return "Field", name, None

                 
    def visitFuncCallStatement(self, ctx:MiniGoParser.FuncCallStatementContext):
        name = ctx.IDENTIFIER().getText()
        argList = self.visit(ctx.callStatementParam()) if ctx.callStatementParam() else []
        return FuncCall(name, argList)

    def visitCallStatementParam(self, ctx:MiniGoParser.CallStatementParamContext):
        return [self.visit(i) for i in ctx.expr()]
                
    def visitCallStatementArrayTail(self, ctx:MiniGoParser.CallStatementArrayTailContext):
        return [self.visit(i) for i in ctx.expr()] 

    
    # $-------------------For Statement-------------------
    def visitBasicForStatement(self, ctx:MiniGoParser.BasicForStatementContext):
        if ctx.forInitilization():
            init = self.visit(ctx.forInitilization())
            cond = self.visit(ctx.forCondition())
            upda = self.visit(ctx.forUpdate())
            block = Block([self.visit(i) for i in ctx.statement()])
            return ForStep(init, cond, upda, block)
        else:
            cond = self.visit(ctx.forCondition())
            block = Block([self.visit(i) for i in ctx.statement()])
            return ForBasic(cond, block)

    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visit(ctx.expr())

    def visitForInitilization(self, ctx:MiniGoParser.ForInitilizationContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        if ctx.getChildCount() == 3:
            name = ctx.IDENTIFIER().getText()
            expr = self.visit(ctx.varDeclExpr())
            varDecl = VarDecl(name, None, expr)
            return varDecl

        if ctx.getChildCount() == 4:
            name = ctx.IDENTIFIER().getText()
            expr = self.visit(ctx.varDeclExpr())
            varType = self.visit(ctx.varDeclType())
            varDecl = VarDecl(name, varType, expr)
            return varDecl

    def visitForUpdate(self, ctx:MiniGoParser.ForUpdateContext):
        lhs = Id(ctx.IDENTIFIER().getText())
        op = ctx.getChild(1).getText()
        if ctx.getChild(1).getText() == "+=":
            rhs = BinaryOp("+",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "-=":
            rhs = BinaryOp("-",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "*=":
            rhs = BinaryOp("*",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "/=":
            rhs = BinaryOp("/",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == "%=":
            rhs = BinaryOp("%",lhs, self.visit(ctx.getChild(2)))
        elif ctx.getChild(1).getText() == ":=":
            rhs = self.visit(ctx.getChild(2))
        return Assign(lhs, rhs)

    def visitForRangeStatement(self, ctx:MiniGoParser.ForRangeStatementContext):
        idx = Id(self.visit(ctx.index()))
        value = Id(self.visit(ctx.value()))
        arr = self.visit(ctx.forArray())
        block = Block([self.visit(i) for i in ctx.statement()])
        return ForEach(idx, value, arr, block)

    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return ctx.getChild(0).getText()

    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return ctx.getChild(0).getText()

    def visitForArray(self, ctx:MiniGoParser.ForArrayContext):
        return self.visit(ctx.getChild(0))

    


    # $-------------------Array Literal-------------------
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        dimens = self.visit(ctx.arrayType())
        eleType = self.visit(ctx.baseType())
        value = self.visit(ctx.arrayBlock())
        return ArrayLiteral(dimens, eleType, value)

    def visitArrayBlock(self, ctx:MiniGoParser.ArrayBlockContext):
        return [self.visit(i) for i in ctx.arrayLitContent()]

    def visitArrayLitContent(self, ctx:MiniGoParser.ArrayLitContentContext):
        return self.visit(ctx.getChild(0))

    def visitNoArrayLit(self, ctx:MiniGoParser.NoArrayLitContext):
        if ctx.INT_LIT():
            # text    = ctx.INT_LIT().getText()
            # if text.startswith("0x") or text.startswith("0X"):
            #     value =  int(text[2:], 16)
            # elif text.startswith("0o") or text.startswith("0O"):
            #     value =  int(text[2:], 8)
            # elif text.startswith("0b") or text.startswith("0B"):
            #     value =  int(text[2:], 2)
            # else:
            #     value =  int(text)
            return IntLiteral(ctx.INT_LIT().getText())  
            
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(True)
        if ctx.FALSE():
            return BooleanLiteral(False)
        if ctx.NIL():
            return NilLiteral()
        if ctx.structLit():
            return self.visit(ctx.structLit())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())

    # $-------------------Struct Literal-------------------
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        name = ctx.IDENTIFIER().getText()
        fields = self.visit(ctx.optionalStructFields())
        return StructLiteral(name, fields)

    def visitOptionalStructFields(self, ctx:MiniGoParser.OptionalStructFieldsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.structFieldList())

    def visitStructFieldList(self, ctx:MiniGoParser.StructFieldListContext):
        return [self.visit(i) for i in ctx.structFieldAssign()]

    def visitStructFieldAssign(self, ctx:MiniGoParser.StructFieldAssignContext):
        return (ctx.IDENTIFIER().getText(), self.visit(ctx.expr()))
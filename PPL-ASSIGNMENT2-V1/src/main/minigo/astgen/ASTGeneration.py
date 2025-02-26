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
        conName = self.IDENTIFIER().getText()
        conType = self.visit(ctx.varDeclType()) if ctx.varDeclType() else None
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
        return ctx.getChild(0).getText()

    def visitVarDeclExpr(self, ctx:MiniGoParser.VarDeclExprContext):
        return self.visit(ctx.expr())


    # #-------------------Expression-------------------
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.getChild(0) == ctx.logicOrExpr():
            return self.visit(ctx.logicOrExpr())
        elif ctx.getChild(0) == ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.getChild(0) == crx.structLit():
            return self.visit(ctx.structLit())
        else:
            raise Exception("Invalid expression")

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
                else:
                    argList = self.visit(suffix.callSuffix())
                    expr = FuncCall(expr, argList)
        return expr

    def visitTerm(self, ctx:MiniGoParser.TermContext):
        # ( expr )
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.INT_LIT():
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
            return "Nil"
        if ctx.structLit():
            return self.visit(ctx.structLit())
        

    def visitCallSuffix(self, ctx:MiniGoParser.CallSuffixContext):
        return self.visit(ctx.argList()) if ctx.argList() else []

    def visitArgList(self, ctx:MiniGoParser.ArgListContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitArraySuffix(self, ctx:MiniGoParser.ArraySuffixContext):
        return [self.visit(expr) for expr in ctx.expr()]

    # #-------------------Function-------------------
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        funcName = ctx.IDENTIFIER().getText()
        funcParam = self.visit(ctx.funcParam())
        funcType = self.visit(ctx.funcType())
        block = Block([self.visit(i) for i in ctx.statement()])

        return FuncDecl(funcName,funcParam,funcType,block)

    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        if ctx.getChildCount() == 0:
            return []
        
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
        methodParam = self.visit(ctx.funcParam())
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
                if typeof(field) == Tuple:
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
        if ctx.getChildCount() == 2:
            return self.visit(ctx.getChild(0))
        return (ctx.IDENTIFIER().getText(), self.visit(ctx.getChild(1)))

    # $ #-------------------Interface Decl-------------------
    def visitInterfaceDeclBlock(self, ctx:MiniGoParser.InterfaceDeclBlockContext):
        return [self.visit(i) for i in ctx.interfaceDeclField()]

    def visitInterfaceDeclField(self, ctx:MiniGoParser.InterfaceDeclFieldContext):
        return Prototype(ctx.IDENTIFIER().getText(), self.visit(ctx.funcParam()), self.visit(ctx.funcType()))

    # #-------------------Statement-------------------
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitDeclarationStatement(self, ctx:MiniGoParser.DeclarationStatementContext):
        return self.visit(ctx.getChild(0))

    def visitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        print("Assign Statement")
        lhs = self.visit(ctx.getChild(0))
        rhs = BinaryOp(ctx.getChild(1).getText(),lhs, self.visit(ctx.getChild(2)))
        return Assign(lhs, rhs)


    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return Break()

    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return Continue()

    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visit(ctx.getChild(0))

    def visitmethodCallStatement(self, ctx:MiniGoParser.methodCallStatementContext):
        pass
        
    def visitFuncCallStatement(self, ctx:MiniGoParser.FuncCallStatementContext):
        name = ctx.IDENTIFIER().getText()
        argList = self.visit(ctx.callStatementParam()) if ctx.callStatementParam() else []
        return FuncCall(name, argList)

    def visitCallStatementParam(self, ctx:MiniGoParser.CallStatementParamContext):
        return [self.visit(i) for i in ctx.expr()]
                
    def visitCallStatementArrayTail(self, ctx:MiniGoParser.CallStatementArrayTailContext):
        return [self.visit(i) for i in ctx.expr()]



    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)

    # $-------------------Assign Statement-------------------
    def visitAssignStateLHS(self, ctx:MiniGoParser.AssignStateLHSContext):
        base = Id(ctx.IDENTIFIER().getText())
        state = self.visit(ctx.getChild(1))

        while state != None:
            if state[0] == "FieldAccess":
                base = FieldAccess(base, state[1])
            elif state[0] == "ArrayCell":
                base = ArrayCell(base, state[1])
            state = state[2]
        return base

    def visitAssignStateLHSTail(self, ctx:MiniGoParser.AssignStateLHSTailContext):
        if ctx.getChildCount() == 0:
            return None
        
        if ctx.getChildCount() == 3:
            return "FieldAccess", ctx.IDENTIFIER().getText(), ctx.getChild(2)
        
        if ctx.getChildCount() == 4:
            dimens = []
            context = ctx
            while context.getChildCount() == 4:
                dimens.append(self.visit(context.getChild(1)))
                context = context.getChild(3)
            return "ArrayCell", dimens, context        
# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDetail.
    def visitVarDetail(self, ctx:MiniGoParser.VarDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclType.
    def visitVarDeclType(self, ctx:MiniGoParser.VarDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclExpr.
    def visitVarDeclExpr(self, ctx:MiniGoParser.VarDeclExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDecl.
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayBlock.
    def visitArrayBlock(self, ctx:MiniGoParser.ArrayBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLitContent.
    def visitArrayLitContent(self, ctx:MiniGoParser.ArrayLitContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optionalStructFields.
    def visitOptionalStructFields(self, ctx:MiniGoParser.OptionalStructFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structFieldList.
    def visitStructFieldList(self, ctx:MiniGoParser.StructFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structFieldAssign.
    def visitStructFieldAssign(self, ctx:MiniGoParser.StructFieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcType.
    def visitFuncType(self, ctx:MiniGoParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParam.
    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcListIdentifiers.
    def visitFuncListIdentifiers(self, ctx:MiniGoParser.FuncListIdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeDecl.
    def visitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDeclBlock.
    def visitStructDeclBlock(self, ctx:MiniGoParser.StructDeclBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDeclField.
    def visitStructDeclField(self, ctx:MiniGoParser.StructDeclFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDeclBlock.
    def visitInterfaceDeclBlock(self, ctx:MiniGoParser.InterfaceDeclBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDeclField.
    def visitInterfaceDeclField(self, ctx:MiniGoParser.InterfaceDeclFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicOrExpr.
    def visitLogicOrExpr(self, ctx:MiniGoParser.LogicOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicAndExpr.
    def visitLogicAndExpr(self, ctx:MiniGoParser.LogicAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#equalityExpr.
    def visitEqualityExpr(self, ctx:MiniGoParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniGoParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniGoParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primarySuffix.
    def visitPrimarySuffix(self, ctx:MiniGoParser.PrimarySuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraySuffix.
    def visitArraySuffix(self, ctx:MiniGoParser.ArraySuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callSuffix.
    def visitCallSuffix(self, ctx:MiniGoParser.CallSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argList.
    def visitArgList(self, ctx:MiniGoParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:MiniGoParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStatement.
    def visitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStateLHS.
    def visitAssignStateLHS(self, ctx:MiniGoParser.AssignStateLHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignTail.
    def visitAssignTail(self, ctx:MiniGoParser.AssignTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStateRHS.
    def visitAssignStateRHS(self, ctx:MiniGoParser.AssignStateRHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:MiniGoParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseStatement.
    def visitElseStatement(self, ctx:MiniGoParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicForStatement.
    def visitBasicForStatement(self, ctx:MiniGoParser.BasicForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forCondition.
    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forInitilization.
    def visitForInitilization(self, ctx:MiniGoParser.ForInitilizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forUpdate.
    def visitForUpdate(self, ctx:MiniGoParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRangeStatement.
    def visitForRangeStatement(self, ctx:MiniGoParser.ForRangeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCallStatement.
    def visitMethodCallStatement(self, ctx:MiniGoParser.MethodCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCallHead.
    def visitMethodCallHead(self, ctx:MiniGoParser.MethodCallHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcCallStatement.
    def visitFuncCallStatement(self, ctx:MiniGoParser.FuncCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatementArrayTail.
    def visitCallStatementArrayTail(self, ctx:MiniGoParser.CallStatementArrayTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatementParam.
    def visitCallStatementParam(self, ctx:MiniGoParser.CallStatementParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value.
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forArray.
    def visitForArray(self, ctx:MiniGoParser.ForArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relationOp.
    def visitRelationOp(self, ctx:MiniGoParser.RelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#addOp.
    def visitAddOp(self, ctx:MiniGoParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mulOp.
    def visitMulOp(self, ctx:MiniGoParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryOp.
    def visitUnaryOp(self, ctx:MiniGoParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#noArrayLit.
    def visitNoArrayLit(self, ctx:MiniGoParser.NoArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term.
    def visitTerm(self, ctx:MiniGoParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#intLitOrConstant.
    def visitIntLitOrConstant(self, ctx:MiniGoParser.IntLitOrConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#baseType.
    def visitBaseType(self, ctx:MiniGoParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#endOfStatement.
    def visitEndOfStatement(self, ctx:MiniGoParser.EndOfStatementContext):
        return self.visitChildren(ctx)



del MiniGoParser
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


    # Visit a parse tree produced by MiniGoParser#baseType.
    def visitBaseType(self, ctx:MiniGoParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#endOfStatement.
    def visitEndOfStatement(self, ctx:MiniGoParser.EndOfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayDecl.
    def visitArrayDecl(self, ctx:MiniGoParser.ArrayDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignDecl.
    def visitAssignDecl(self, ctx:MiniGoParser.AssignDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeDecl.
    def visitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDecl.
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDefinition.
    def visitStructDefinition(self, ctx:MiniGoParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structFields.
    def visitStructFields(self, ctx:MiniGoParser.StructFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDefinition.
    def visitInterfaceDefinition(self, ctx:MiniGoParser.InterfaceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceFields.
    def visitInterfaceFields(self, ctx:MiniGoParser.InterfaceFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listParams.
    def visitListParams(self, ctx:MiniGoParser.ListParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listIdentifier.
    def visitListIdentifier(self, ctx:MiniGoParser.ListIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listGroup.
    def visitListGroup(self, ctx:MiniGoParser.ListGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParam.
    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicOrExp.
    def visitLogicOrExp(self, ctx:MiniGoParser.LogicOrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicAndExp.
    def visitLogicAndExp(self, ctx:MiniGoParser.LogicAndExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#equalityExp.
    def visitEqualityExp(self, ctx:MiniGoParser.EqualityExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveExp.
    def visitAdditiveExp(self, ctx:MiniGoParser.AdditiveExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeExp.
    def visitMultiplicativeExp(self, ctx:MiniGoParser.MultiplicativeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExp.
    def visitUnaryExp(self, ctx:MiniGoParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#postfixExp.
    def visitPostfixExp(self, ctx:MiniGoParser.PostfixExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExp.
    def visitPrimaryExp(self, ctx:MiniGoParser.PrimaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraysBlock.
    def visitArraysBlock(self, ctx:MiniGoParser.ArraysBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structExpression.
    def visitStructExpression(self, ctx:MiniGoParser.StructExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structBlock.
    def visitStructBlock(self, ctx:MiniGoParser.StructBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structFieldsAssign.
    def visitStructFieldsAssign(self, ctx:MiniGoParser.StructFieldsAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStatement.
    def visitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#a1.
    def visitA1(self, ctx:MiniGoParser.A1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#a2.
    def visitA2(self, ctx:MiniGoParser.A2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:MiniGoParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forLoop.
    def visitForLoop(self, ctx:MiniGoParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initilization.
    def visitInitilization(self, ctx:MiniGoParser.InitilizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forCondition.
    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forUpdate.
    def visitForUpdate(self, ctx:MiniGoParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forIteration.
    def visitForIteration(self, ctx:MiniGoParser.ForIterationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryCall.
    def visitPrimaryCall(self, ctx:MiniGoParser.PrimaryCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayDims.
    def visitArrayDims(self, ctx:MiniGoParser.ArrayDimsContext):
        return self.visitChildren(ctx)



del MiniGoParser
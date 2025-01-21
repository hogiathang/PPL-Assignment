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


    # Visit a parse tree produced by MiniGoParser#tYPE.
    def visitTYPE(self, ctx:MiniGoParser.TYPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parserRuleSpec.
    def visitParserRuleSpec(self, ctx:MiniGoParser.ParserRuleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
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


    # Visit a parse tree produced by MiniGoParser#typeDefinition.
    def visitTypeDefinition(self, ctx:MiniGoParser.TypeDefinitionContext):
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


    # Visit a parse tree produced by MiniGoParser#funcParams.
    def visitFuncParams(self, ctx:MiniGoParser.FuncParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcParam.
    def visitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term.
    def visitTerm(self, ctx:MiniGoParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MiniGoParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraysBlock.
    def visitArraysBlock(self, ctx:MiniGoParser.ArraysBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStatement.
    def visitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
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


    # Visit a parse tree produced by MiniGoParser#initilization.
    def visitInitilization(self, ctx:MiniGoParser.InitilizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forCondition.
    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forUpdate.
    def visitForUpdate(self, ctx:MiniGoParser.ForUpdateContext):
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


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayDims.
    def visitArrayDims(self, ctx:MiniGoParser.ArrayDimsContext):
        return self.visitChildren(ctx)



del MiniGoParser
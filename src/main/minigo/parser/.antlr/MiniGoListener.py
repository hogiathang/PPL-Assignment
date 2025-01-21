# Generated from d:/HK242/PPL/Assignment/B1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parserRuleSpec.
    def enterParserRuleSpec(self, ctx:MiniGoParser.ParserRuleSpecContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parserRuleSpec.
    def exitParserRuleSpec(self, ctx:MiniGoParser.ParserRuleSpecContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#varDecl.
    def enterVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#varDecl.
    def exitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcDecl.
    def enterFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcDecl.
    def exitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typeDecl.
    def enterTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typeDecl.
    def exitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#constDecl.
    def enterConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#constDecl.
    def exitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typeDefinition.
    def enterTypeDefinition(self, ctx:MiniGoParser.TypeDefinitionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typeDefinition.
    def exitTypeDefinition(self, ctx:MiniGoParser.TypeDefinitionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structDefinition.
    def enterStructDefinition(self, ctx:MiniGoParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structDefinition.
    def exitStructDefinition(self, ctx:MiniGoParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structFields.
    def enterStructFields(self, ctx:MiniGoParser.StructFieldsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structFields.
    def exitStructFields(self, ctx:MiniGoParser.StructFieldsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interfaceDefinition.
    def enterInterfaceDefinition(self, ctx:MiniGoParser.InterfaceDefinitionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interfaceDefinition.
    def exitInterfaceDefinition(self, ctx:MiniGoParser.InterfaceDefinitionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interfaceFields.
    def enterInterfaceFields(self, ctx:MiniGoParser.InterfaceFieldsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interfaceFields.
    def exitInterfaceFields(self, ctx:MiniGoParser.InterfaceFieldsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#listParams.
    def enterListParams(self, ctx:MiniGoParser.ListParamsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#listParams.
    def exitListParams(self, ctx:MiniGoParser.ListParamsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#listIdentifier.
    def enterListIdentifier(self, ctx:MiniGoParser.ListIdentifierContext):
        pass

    # Exit a parse tree produced by MiniGoParser#listIdentifier.
    def exitListIdentifier(self, ctx:MiniGoParser.ListIdentifierContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcParams.
    def enterFuncParams(self, ctx:MiniGoParser.FuncParamsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcParams.
    def exitFuncParams(self, ctx:MiniGoParser.FuncParamsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcParam.
    def enterFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcParam.
    def exitFuncParam(self, ctx:MiniGoParser.FuncParamContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression.
    def enterExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expression.
    def exitExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#term.
    def enterTerm(self, ctx:MiniGoParser.TermContext):
        pass

    # Exit a parse tree produced by MiniGoParser#term.
    def exitTerm(self, ctx:MiniGoParser.TermContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statement.
    def enterStatement(self, ctx:MiniGoParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statement.
    def exitStatement(self, ctx:MiniGoParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignStatement.
    def enterAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignStatement.
    def exitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:MiniGoParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:MiniGoParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ifStatement.
    def enterIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ifStatement.
    def exitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forStatement.
    def enterForStatement(self, ctx:MiniGoParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forStatement.
    def exitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forLoop.
    def enterForLoop(self, ctx:MiniGoParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forLoop.
    def exitForLoop(self, ctx:MiniGoParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MiniGoParser#initilization.
    def enterInitilization(self, ctx:MiniGoParser.InitilizationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#initilization.
    def exitInitilization(self, ctx:MiniGoParser.InitilizationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forCondition.
    def enterForCondition(self, ctx:MiniGoParser.ForConditionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forCondition.
    def exitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forUpdate.
    def enterForUpdate(self, ctx:MiniGoParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forUpdate.
    def exitForUpdate(self, ctx:MiniGoParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block.
    def enterBlock(self, ctx:MiniGoParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block.
    def exitBlock(self, ctx:MiniGoParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arrayDims.
    def enterArrayDims(self, ctx:MiniGoParser.ArrayDimsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arrayDims.
    def exitArrayDims(self, ctx:MiniGoParser.ArrayDimsContext):
        pass



del MiniGoParser
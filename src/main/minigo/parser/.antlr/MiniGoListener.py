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


    # Enter a parse tree produced by MiniGoParser#mainFunction.
    def enterMainFunction(self, ctx:MiniGoParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#mainFunction.
    def exitMainFunction(self, ctx:MiniGoParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#baseType.
    def enterBaseType(self, ctx:MiniGoParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#baseType.
    def exitBaseType(self, ctx:MiniGoParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#endOfStatement.
    def enterEndOfStatement(self, ctx:MiniGoParser.EndOfStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#endOfStatement.
    def exitEndOfStatement(self, ctx:MiniGoParser.EndOfStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declaration.
    def enterDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declaration.
    def exitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
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


    # Enter a parse tree produced by MiniGoParser#methodDecl.
    def enterMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methodDecl.
    def exitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
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


    # Enter a parse tree produced by MiniGoParser#interfaceFields.
    def enterInterfaceFields(self, ctx:MiniGoParser.InterfaceFieldsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interfaceFields.
    def exitInterfaceFields(self, ctx:MiniGoParser.InterfaceFieldsContext):
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


    # Enter a parse tree produced by MiniGoParser#logicOrExp.
    def enterLogicOrExp(self, ctx:MiniGoParser.LogicOrExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logicOrExp.
    def exitLogicOrExp(self, ctx:MiniGoParser.LogicOrExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logicAndExp.
    def enterLogicAndExp(self, ctx:MiniGoParser.LogicAndExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logicAndExp.
    def exitLogicAndExp(self, ctx:MiniGoParser.LogicAndExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#equalityExp.
    def enterEqualityExp(self, ctx:MiniGoParser.EqualityExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#equalityExp.
    def exitEqualityExp(self, ctx:MiniGoParser.EqualityExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#additiveExp.
    def enterAdditiveExp(self, ctx:MiniGoParser.AdditiveExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#additiveExp.
    def exitAdditiveExp(self, ctx:MiniGoParser.AdditiveExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#multiplicativeExp.
    def enterMultiplicativeExp(self, ctx:MiniGoParser.MultiplicativeExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#multiplicativeExp.
    def exitMultiplicativeExp(self, ctx:MiniGoParser.MultiplicativeExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#unaryExp.
    def enterUnaryExp(self, ctx:MiniGoParser.UnaryExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#unaryExp.
    def exitUnaryExp(self, ctx:MiniGoParser.UnaryExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primaryExp.
    def enterPrimaryExp(self, ctx:MiniGoParser.PrimaryExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primaryExp.
    def exitPrimaryExp(self, ctx:MiniGoParser.PrimaryExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#postfixExp.
    def enterPostfixExp(self, ctx:MiniGoParser.PostfixExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#postfixExp.
    def exitPostfixExp(self, ctx:MiniGoParser.PostfixExpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#postfixOp.
    def enterPostfixOp(self, ctx:MiniGoParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#postfixOp.
    def exitPostfixOp(self, ctx:MiniGoParser.PostfixOpContext):
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


    # Enter a parse tree produced by MiniGoParser#arrayLit.
    def enterArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arrayLit.
    def exitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arraysBlock.
    def enterArraysBlock(self, ctx:MiniGoParser.ArraysBlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arraysBlock.
    def exitArraysBlock(self, ctx:MiniGoParser.ArraysBlockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structExpression.
    def enterStructExpression(self, ctx:MiniGoParser.StructExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structExpression.
    def exitStructExpression(self, ctx:MiniGoParser.StructExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structBlock.
    def enterStructBlock(self, ctx:MiniGoParser.StructBlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structBlock.
    def exitStructBlock(self, ctx:MiniGoParser.StructBlockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structFieldsAssign.
    def enterStructFieldsAssign(self, ctx:MiniGoParser.StructFieldsAssignContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structFieldsAssign.
    def exitStructFieldsAssign(self, ctx:MiniGoParser.StructFieldsAssignContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignStatement.
    def enterAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignStatement.
    def exitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#a1.
    def enterA1(self, ctx:MiniGoParser.A1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#a1.
    def exitA1(self, ctx:MiniGoParser.A1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#a2.
    def enterA2(self, ctx:MiniGoParser.A2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#a2.
    def exitA2(self, ctx:MiniGoParser.A2Context):
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


    # Enter a parse tree produced by MiniGoParser#forIteration.
    def enterForIteration(self, ctx:MiniGoParser.ForIterationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forIteration.
    def exitForIteration(self, ctx:MiniGoParser.ForIterationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#breakStatement.
    def enterBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#breakStatement.
    def exitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continueStatement.
    def enterContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continueStatement.
    def exitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#callStatement.
    def enterCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#callStatement.
    def exitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#returnStatement.
    def enterReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#returnStatement.
    def exitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
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
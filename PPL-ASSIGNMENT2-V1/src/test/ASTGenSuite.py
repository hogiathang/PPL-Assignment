import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
        # def test_simple_program(self):
        # """Simple program: int main() {} """
        # input = """func main() {}"""
        # expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
        # self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """func main () {}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_more_complex_varDecl(self):
        """More complex program"""
        input = """var x int = foo().too().zoo[3][4];
                """
        expect = str(Program([VarDecl("x",IntType(),ArrayCell(FieldAccess(MethCall(FuncCall(Id("foo"),[]),"too",[]),"zoo"),[IntLiteral(3),IntLiteral(4)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_function_with_parameter(self):
        """More complex program"""
        input = """func main (x, y int) {
            return 1 + 1
        }
        """
        expect = str(Program([FuncDecl("main",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],VoidType(),Block([Return(BinaryOp("+",IntLiteral(1),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_assign_statement(self):
        """More complex program"""
        input = """func main () {
            x := 1;
        }

        func (c Jedi) foo (x, y, z int, t float) {
            x := 1;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block(
                [Assign(Id("x"),BinaryOp(":=",Id("x"),IntLiteral(1)))]
            )),
            MethodDecl("c",Id("Jedi"),
            FuncDecl("foo",[ParamDecl("x",IntType()),
            ParamDecl("y",IntType()),
            ParamDecl("z",IntType()),
            ParamDecl("t",FloatType())],
            VoidType(),Block([Assign(Id("x"),
            BinaryOp(":=",Id("x"),IntLiteral(1)))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
   
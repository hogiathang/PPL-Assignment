import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_000(self):
        input = """
        type hgt struct {
            a int;
            b int;
            a float;
        };
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Field: a\n", 400))

    def test_001(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_002(self):
        """
var VoTien = 1; 
var VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien\n", 402))

    def test_003(self):
        """
var VoTien = 1; 
const VoTien = 2;
        """
        input = Program([VarDecl("VoTien", None,IntLiteral(1)),ConstDecl("VoTien",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: VoTien\n", 403))

    def test_004(self):
        """
const VoTien = 1; 
var VoTien = 2;
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),VarDecl("VoTien", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien\n", 404))

    def test_005(self):
        """
const VoTien = 1; 
func VoTien () {return;}
        """
        input = Program([ConstDecl("VoTien",None,IntLiteral(1)),FuncDecl("VoTien",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: VoTien\n", 405))

    def test_006(self):
        """ 
func VoTien () {return;}
var VoTien = 1;
        """
        input = Program([FuncDecl("VoTien",[],VoidType(),Block([Return(None)])),VarDecl("VoTien", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VoTien\n", 406))

    def test_007(self):
        """ 
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt\n", 407))

    def test_008(self):
        """ 
type  Votien struct {
    Votien int;
}
type TIEN struct {
    Votien string;
    TIEN int;
    TIEN float;
}
        """
        input = Program([StructType("Votien",[("Votien",IntType())],[]),StructType("TIEN",[("Votien",StringType()),("TIEN",IntType()),("TIEN",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: TIEN\n", 408))

    def test_009(self):
        """
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    Votien int;
}
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", 409))

    def test_010(self):
        """ 
type VoTien interface {
    VoTien ();
    VoTien (a int);
}
        """
        input = Program([InterfaceType("VoTien",[Prototype("VoTien",[],VoidType()),Prototype("VoTien",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: VoTien\n", 410))

    def test_011(self):
        """ 
func Votien (a, a int) {return;}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", 411))

    def test_012(self):
        """ 
func Votien (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: b\n", 412))

    def test_013(self):
        """ 
func Votien (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", 413))

    # def test_014(self):
    #     """
    #     func Votien () int {return 1;}

    #     func foo () {
    #         var b = Votien();
    #         foo_votine();
    #         return;
    #     }
    #     """
    #     input = Program([FuncDecl("Votien",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Votien",[])),FuncCall("foo_votine",[]),Return(None)]))])
    #     self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine\n", 414))

#     def test_015(self):
#         """
#         type TIEN struct {
#             Votien int;
#         }

#         func (v TIEN) getInt () {
#             const c = v.Votien;
#             var d = v.tien;
#         }
#         """
#         input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Votien")),VarDecl("d", None,FieldAccess(Id("v"),"tien"))])))])
#         self.assertTrue(TestChecker.test(input, "Undeclared Field: tien\n", 415))

#     def test_016(self):
#         """
#         func getString() {return;}
#         """
#         input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
#         self.assertTrue(TestChecker.test(input, "Redeclared Function: getString\n", 416))

#     def test_017(self):
#         """
#         type TIEN struct {
#             Votien int;
#         }
#         func (v TIEN) foo (v int) {return;}
#         func foo () {return;}
#         """
#         input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
#         self.assertTrue(TestChecker.test(input, "Redeclared Parameter: v\n", 417))

#     def test_018(self):
#         """        
#         var a = foo();
#         func foo () int {
#             var a =  koo();
#             var c = getInt();
#             putInt(c);
#             putIntLn(c);
#             return 1;
#         }
#         var d = foo();
#         func koo () int {
#             var a =  foo ();
#             return 1;
#         }
#         """
#         input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
#         self.assertTrue(TestChecker.test(input, "", 418))

    # def test_019(self):
    #     """
    #     var v TIEN;
    #     const b = v.b;
    #     type TIEN struct {
    #         a int;
    #         b int;
    #         c int;
    #     }
    #     const a = v.a;
    #     const e = v.e;
    #     """
    #     input = Program([VarDecl("v",Id("TIEN"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("TIEN",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
    #     self.assertTrue(TestChecker.test(input, "Undeclared Field: e\n", 419))

    # def test_020(self):
    #     """
    #     var v int = 1.2;
    #     """
    #     input = Program([VarDecl("v",IntType(),FloatLiteral(1.2))])
    #     self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.2))\n", 420))

    # def test_021(self):
    #     """
    #     type S1 struct {votien int;}
    #     type S2 struct {votien int;}

    #     var v S1;
    #     const x = v;
    #     var z S1 = x;
    #     var k S2 = x;
    #     """
    #     input = Program([StructType("S1",[("votien",IntType())],[]),StructType("S2",[("votien",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
    #     self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,S2,Id(x))\n", 421))
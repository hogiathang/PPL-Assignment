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
var aa = 1; 
var aa = 2;
        """
        input = Program([VarDecl("aa", None,IntLiteral(1)),VarDecl("aa", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: aa\n", 402))

    def test_003(self):
        """
var aa = 1; 
const aa = 2;
        """
        input = Program([VarDecl("aa", None,IntLiteral(1)),ConstDecl("aa",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: aa\n", 403))

    def test_004(self):
        """
const aa = 1; 
var aa = 2;
        """
        input = Program([ConstDecl("aa",None,IntLiteral(1)),VarDecl("aa", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: aa\n", 404))

    def test_005(self):
        """
const aa = 1; 
func aa () {return;}
        """
        input = Program([ConstDecl("aa",None,IntLiteral(1)),FuncDecl("aa",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: aa\n", 405))

    def test_006(self):
        """ 
func aa () {return;}
var aa = 1;
        """
        input = Program([FuncDecl("aa",[],VoidType(),Block([Return(None)])),VarDecl("aa", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: aa\n", 406))

    def test_007(self):
        """ 
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt\n", 407))

    def test_008(self):
        """ 
type  aa struct {
    aa int;
}

type AAAA struct {
    aa string;
    AAAA int;
    AAAA float;
}
        """
        input = Program([StructType("aa",[("aa",IntType())],[]),StructType("AAAA",[("aa",StringType()),("AAAA",IntType()),("AAAA",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: AAAA\n", 408))

    def test_009(self):
        """
func (v AAAA) putIntLn () {return;}
func (v AAAA) getInt () {return;}
func (v AAAA) getInt () {return;}
type AAAA struct {
    aaa int;
}
        """
        input = Program([MethodDecl("v",Id("AAAA"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("AAAA"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("AAAA"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("AAAA",[("aaa",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", 409))

    def test_010(self):
        """ 
type aaa interface {
    aaa ();
    aaa (a int);
}
        """
        input = Program([InterfaceType("aaa",[Prototype("aaa",[],VoidType()),Prototype("aaa",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: aaa\n", 410))

    def test_011(self):
        """ 
func aaa (a, a int) {return;}
        """
        input = Program([FuncDecl("aaa",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", 411))

    def test_012(self):
        """ 
func aaa (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("aaa",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", 412))

    def test_013(self):
        """ 
func aaa (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        input = Program([FuncDecl("aaa",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", 413))

    def test_014(self):
        """
        func aaa () [2][3]int {return 1;}

        func foo () {
            var b = aaa();
            foo_abc();
            return;
        }
        """
        input = Program([FuncDecl("aaa",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("aaa",[])),FuncCall("foo_abc",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_abc\n", 414))

    def test_015(self):
        """
        type AAAA struct {
            aa int;
        }

        func (v AAAA) getInt () {
            const c = v.aa;
            var d = v.AAAA;
        }
        """
        input = Program([StructType("AAAA",[("aa",IntType())],[]),MethodDecl("v",Id("AAAA"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"aa")),VarDecl("d", None,FieldAccess(Id("v"),"AAAA"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: AAAA\n", 415))

    def test_016(self):
        """
        func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString\n", 416))

    def test_017(self):
        """
        type AAAA struct {
            aa int;
        }
        func (v AAAA) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("AAAA",[("aa",IntType())],[]),MethodDecl("v",Id("AAAA"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: v\n", 417))

    def test_018(self):
        """        
        var a = foo();
        func foo () int {
            var a =  koo();
            var c = getInt();
            putInt(c);
            putIntLn(c);
            return 1;
        }
        var d = foo();
        func koo () int {
            var a =  foo ();
            return 1;
        }
        """
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "", 418))

    def test_019(self):
        """
        var v AAAA;
        const b = v.b;
        type AAAA struct {
            a int;
            b int;
            c int;
        }
        const a = v.a;
        const e = v.e;
        """
        input = Program([VarDecl("v",Id("AAAA"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("AAAA",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e\n", 419))

    def test_020(self):
        """
        var v int = 1.2;
        """
        input = Program([VarDecl("v",IntType(),FloatLiteral(1.2))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.2))\n", 420))

    def test_021(self):
        """
        type S1 struct {aa int;}
        type S2 struct {aa int;}

        var v S1;
        const x = v;
        var z S1 = x;
        var k S2 = x;
        """
        input = Program([StructType("S1",[("aa",IntType())],[]),StructType("S2",[("aa",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(S2),Id(x))\n", 421))


    def test_022(self):
        input = """
        var a [1][2]int = [1][2]int{{1,2},{3,4}};
        var b [2][2]int = [1][2]int{{1,2},{3,4}};
        const thang = "THANG 10 CHAM PPL";
        const thang = "THANG 10 CHAM PPL";
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(b,ArrayType(IntType,[IntLiteral(2),IntLiteral(2)]),ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType,[[IntLiteral(1),IntLiteral(2)],[IntLiteral(3),IntLiteral(4)]]))\n", 422))

    def test_023(self):
        input = """
        var a = 1;
        var b = a;
        var c = d;
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", 423))

    def test_024(self):
        input = """
        type DEF struct {
            a int;
            b int;
        }
        type ABC struct {
            a int;
            b int;
            c DEF;
        }
        var a ABC;
        var b = a;
        var c = ABC{a:1, b:2, c:DEF{a:3, b:4, c:5}};
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Field: c\n", 424))

    def test_025(self):
        input ="""
        type TIEN struct {
            Votien int;
        }

        func (v TIEN) getInt () {
            v.getInt ();    
            v.putInt ();
        };"""
        #input = Program([StructType("TIEN",[("Votien",IntType())],[]),MethodDecl("v",Id("TIEN"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt\n", 425))

    def test_026(self):
        input = """
            type TIEN struct {
                Votien int;
            }
            func (v TIEN) foo (a, b int) {return;}
            func foo (a, a int) {return;}
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", 426))

    def test_027(self):
        input = """
            var v TIEN;
            const b = v.foo();        
            type TIEN struct {
                a int;
            } 
            func (v TIEN) foo() int {return 1;}
            func (v TIEN) koo() int {return 1;}
            const c = v.koo();  
            const d = v.zoo();
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Method: zoo\n", 427))

    def test_028(self):
        """
        var v TIEN;      
        type TIEN struct {
            a int;
        } 
        type VO interface {
            foo() int;
        }

        func (v TIEN) foo() int {return 1;}
        func (b TIEN) koo() {b.koo();}
        func foo() {
            var x VO;  
            const b = x.foo(); 
            x.koo(); 
        }
        """
        input = Program([VarDecl("v",Id("TIEN"), None),StructType("TIEN",[("a",IntType())],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("TIEN"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: foo\n", 428))

    def test_029(self):
        input = """
        var v TIEN;      
        type TIEN struct {
            a int;
        } 
        type VO interface {
            foo() int;
            akazam() int;
        }
        func (z VO) akazam(a int, b float) int {return 1;}
        func (b TIEN) koo(a int) {b.koo(a);}
        func foo() {
            var x VO;
            const c = x.akazam(1);  
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(x),akazam,[IntLiteral(1)])\n", 429))

    def test_030(self):
        input = """
        func swap(a, b int) {
            var temp = a;
            a := b;
            b := temp;
        }
        func main() {
            var x = 5;
            var y = 10.5;
            swap(x, y);
            putIntLn(x);
            putIntLn(y);
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(swap,[Id(x),Id(y)])\n", 430))

    def test_031(self):
        input = """
        var A int;
        func (a A) b (x int) int {
            var A = 5;
            var b = a + x;
            return b;
        }
        type A struct{
            a int;
        }
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Type: A\n", 431))

    def test_032(self):
        input = """
        const a = 2;
        func foo () {
            const a = 1;
            for a < 1 {
                const a = 1;
                for a < 1 {
                    const a = 1;
                    const b = 1;
                }
                const b = 1;
                var a = 1;
            }
        };"""
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a\n", 432))

    def test_033(self):
        input =         '''
    func (v TIEN) foo (a, b int) {
        const v = 1;
        const a = 1;
    }

    type TIEN struct {
        Votien int;
    }

    func (v VO) foo () {
        const a = 1;
    }

    type VO struct {
        Votien int;
    }

    func (v VO) foo (a, b int) {
        const a = 1;
    }
        '''
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo\n", 433))

    def test_034(self):
        input = """
        type S1 struct {votien int;}
        func (s S1) votien() int {
            s.votien();
            return 1;
        }
        type S1 struct {votien int;}
        type S2 struct {votien int;}
        type I1 interface {votien();}
        type I2 interface {votien();}

        func (s S1) votien() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Method: votien\n", 434))

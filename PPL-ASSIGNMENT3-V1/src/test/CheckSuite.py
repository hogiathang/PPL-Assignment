import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_000(self):
        input = """
        type abc struct {
            m int;
            n int;
            m float;
        };
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Field: m\n", 400))

    def test_001(self):
        input = """var m int; var n int; var m int; """
        expect = "Redeclared Variable: m\n"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_002(self):
        """
var cc = 1; 
var cc = 2;
        """
        input = Program([VarDecl("cc", None, IntLiteral(1)), VarDecl("cc", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: cc\n", 402))

    def test_003(self):
        """
var cc = 1; 
const cc = 2;
        """
        input = Program([VarDecl("cc", None, IntLiteral(1)), ConstDecl("cc", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: cc\n", 403))

    def test_004(self):
        """
const cc = 1; 
var cc = 2;
        """
        input = Program([ConstDecl("cc", None, IntLiteral(1)), VarDecl("cc", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: cc\n", 404))

    def test_005(self):
        """
const cc = 1; 
func cc () {return;}
        """
        input = Program([ConstDecl("cc", None, IntLiteral(1)), FuncDecl("cc", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: cc\n", 405))

    def test_006(self):
        """ 
func cc () {return;}
var cc = 1;
        """
        input = Program([FuncDecl("cc", [], VoidType(), Block([Return(None)])), VarDecl("cc", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: cc\n", 406))

    def test_007(self):
        """ 
var getFloat = 2.5;
        """
        input = Program([VarDecl("getFloat", None, FloatLiteral(2.5))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getFloat\n", 407))

    def test_008(self):
        """ 
type  cc struct {
    cc int;
}

type CCCC struct {
    cc string;
    CCCC int;
    CCCC float;
}
        """
        input = Program([StructType("cc", [("cc", IntType())], []), StructType("CCCC", [("cc", StringType()), ("CCCC", IntType()), ("CCCC", FloatType())], [])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: CCCC\n", 408))

    def test_009(self):
        """
func (v CCCC) putDoubleLn () {return;}
func (v CCCC) getDouble () {return;}
func (v CCCC) getDouble () {return;}
type CCCC struct {
    ccc int;
}
        """
        input = Program([MethodDecl("v", Id("CCCC"), FuncDecl("putDoubleLn", [], VoidType(), Block([Return(None)]))), MethodDecl("v", Id("CCCC"), FuncDecl("getDouble", [], VoidType(), Block([Return(None)]))), MethodDecl("v", Id("CCCC"), FuncDecl("getDouble", [], VoidType(), Block([Return(None)]))), StructType("CCCC", [("ccc", IntType())], [])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getDouble\n", 409))

    def test_010(self):
        """ 
type ccc interface {
    ccc ();
    ccc (y int);
}
        """
        input = Program([InterfaceType("ccc", [Prototype("ccc", [], VoidType()), Prototype("ccc", [IntType()], VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: ccc\n", 410))

    def test_011(self):
        """ 
func ccc (y, y int) {return;}
        """
        input = Program([FuncDecl("ccc", [ParamDecl("y", IntType()), ParamDecl("y", IntType())], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: y\n", 411))

    def test_012(self):
        """ 
func ccc (z int) {
    var z = 1;
    var y = 1;
    const y = 1;
}
        """
        input = Program([FuncDecl("ccc", [ParamDecl("z", IntType())], VoidType(), Block([VarDecl("z", None, IntLiteral(1)), VarDecl("y", None, IntLiteral(1)), ConstDecl("y", None, IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: y\n", 412))

    def test_013(self):
        """ 
func ccc (z int) {
    for var y = 1; y < 1; y += 1 {
        const y = 2;
    }
}
        """
        input = Program([FuncDecl("ccc", [ParamDecl("z", IntType())], VoidType(), Block([ForStep(VarDecl("y", None, IntLiteral(1)), BinaryOp("<", Id("y"), IntLiteral(1)), Assign(Id("y"), BinaryOp("+", Id("y"), IntLiteral(1))), Block([ConstDecl("y", None, IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: y\n", 413))

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
        self.assertTrue(TestChecker.test(input, "", 417))

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
        type AAAA struct {
            BB int;
        }

        func (v AAAA) getInt () {
            v.getInt ();    
            v.putInt ();
        };"""
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt\n", 425))

    def test_026(self):
        input = """
            type AAAA struct {
                BB int;
            }
            func (v AAAA) foo (a, b int) {return;}
            func foo (a, a int) {return;}
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", 426))

    def test_027(self):
        input = """
            var v AAAA;
            const b = v.foo();        
            type AAAA struct {
                a int;
            } 
            func (v AAAA) foo() int {return 1;}
            func (v AAAA) koo() int {return 1;}
            const c = v.koo();  
            const d = v.zoo();
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Method: zoo\n", 427))

    def test_028(self):
        """
        var v AAAA;      
        type AAAA struct {
            a int;
        } 
        type cccc interface {
            foo() int;
        }

        func (v AAAA) foo() int {return 1;}
        func (b AAAA) koo() {b.koo();}
        func foo() {
            var x cccc;  
            const b = x.foo(); 
            x.koo(); 
        }
        """
        input = Program([VarDecl("v",Id("AAAA"), None),StructType("AAAA",[("a",IntType())],[]),InterfaceType("cccc",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("AAAA"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("AAAA"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("cccc"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo\n", 428))

    def test_029(self):
        input = """
        var v AAAA;      
        type AAAA struct {
            a int;
        } 
        type cccc interface {
            foo() int;
            akazam() int;
        }
        func (z AAAA) akazam(a int, b float) int {return 1;}
        func (b AAAA) koo(a int) {b.koo(a);}
        func foo() {
            var x cccc;
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
    func (v AAAA) foo (a, b int) {
        const v = 1;
        const a = 1;
    }

    type AAAA struct {
        BB int;
    }

    func (v cccc) foo () {
        const a = 1;
    }

    type cccc struct {
        BB int;
    }

    func (v cccc) foo (a, b int) {
        const a = 1;
    }
        '''
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo\n", 433))

    def test_034(self):
        input = """
        type S1 struct {BB int;}
        type S2 struct {BB int;}
        type I1 interface {BB();}
        type I2 interface {BB();}

        func (s S1) BB() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
       # input = Program([StructType("S1",[("BB",IntType())],[]),StructType("S2",[("BB",IntType())],[]),InterfaceType("I1",[Prototype("BB",[],VoidType())]),InterfaceType("I2",[Prototype("BB",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("BB",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(b))\n", 434))

    def test_035(self):
        input = """
        type T1 struct {
            FAKER int;
            ZEUS int;
        }
        type T2 interface {
            JACK(a int);
            VIRUS(b string);
        }
        func (a T1) JACK(thienAN int) {
            var a = 1;
            var b = 3;
        }

        func (b T1) VIRUS(CORONA, PETER string) {
            const a = 1;
            var b = 2;
            var c = 3;
        }

        var a T1;
        var b T2 = a;
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(b,Id(T2),Id(a))\n", 435))

    def test_036(self):
        input = """
        type S1 struct {BB int;}
        type S2 struct {BB int;}
        type I1 interface {BB();}
        type I2 interface {BB() int;}

        func (s S1) BB() {return;}

        var a S1;
        var b S2;
        var c I2 = a;
        """
        # input= Program([StructType("S1",[("BB",IntType())],[]),StructType("S2",[("BB",IntType())],[]),InterfaceType("I1",[Prototype("BB",[],VoidType())]),InterfaceType("I2",[Prototype("BB",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("BB",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,Id(I2),Id(a))\n", 436))

    def test_037(self):
        input = """
            type S1 struct {BB int;}
            type S2 struct {BB int;}
            type I1 interface {BB() S1;}
            type I2 interface {BB() S2;}

            func (s S1) BB() S1 {return s;}

            var a S1;
            var c I1 = a;
            var d I2 = a;
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n", 437))

    def test_038(self):
        input = """
            type S1 struct {BB int;}
            type S2 struct {BB int;}
            type I1 interface {BB(e, e int) S1;}
            type I2 interface {BB(a int) S1;}

            func (s S1) BB(a, b int) S1 {return s;}

            var a S1;
            var c I1 = a;
            var d I2 = a;
        """
        # input = Program([StructType("S1",[("BB",IntType())],[]),StructType("S2",[("BB",IntType())],[]),InterfaceType("I1",[Prototype("BB",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("BB",[IntType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("BB",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n", 438))

    def test_039(self):
        input ="""
        func foo(){
            if (true) {
                var a float = 1.02;
            } else {
                var a int = 1.02;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.02))\n", 439))

    def test_040(self):
        input = """
        var a int;
        var b float;
        var a string;
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a\n", 440))

    def test_041(self):
        input = """
        type A struct {
            x int;
        }
        type A struct {
            y float;
        }
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Type: A\n", 441))

    def test_042(self):
        input = """
        func foo() {}
        func foo() {}
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Function: foo\n", 442))

    def test_043(self):
        input = """
        var a = 1;
        var b = a + c;
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: c\n", 443))

    def test_044(self):
        input = """
        type A struct {
            x int;
        }
        var a A;
        var b = a.y;
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Field: y\n", 444))

    def test_045(self):
        input = """
        func foo(a int, b int) {}
        func foo(a int, a float) {}
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Function: foo\n", 445))

    def test_046(self):
        input = """
        var a int;
        var b = a + "string";
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(Id(a),+,StringLiteral("string"))\n""", 446))

    def test_047(self):
        input = """
        var a [2]int = [2]int{1, 2};
        var b [3]int = a;
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(b,ArrayType(IntType,[IntLiteral(3)]),Id(a))\n", 447))

    def test_048(self):
        input = """
        func foo() int {
            return 1.5;
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(FloatLiteral(1.5))\n", 448))

    def test_049(self):
        input = """
        func foo() {
            var a int;
            a := "string";
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(a),StringLiteral("string"))\n""", 449))

    def test_050(self):
        input = """
        func foo() {
            if (1) {}
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: If(IntLiteral(1),Block([]))\n", 450))

    def test_051(self):
        input = """        
        type AAAA struct {
            BB int;
        }
        func (v AAAA) foo (v int) {return;}
        func foo () {return;}
        """
        self.assertTrue(TestChecker.test(input, "", 451))

    def test_052(self):
        input = """
        func foo() {
            for i := 0; i < 10; i+=1 {
                putInt(i);
            }
            putInt(i);
        }
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: i\n", 452))

    def test_053(self):
        input = """        
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b := 2 {
                const b = 1;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: b\n", 453))

    def test_054(self):
        input = """
        func (a vector) foo (b int) {
            for i := 0; i < 10; i+=1 {
                putInt(i);
            }
            a.foo(i);
        }
        type vector struct {
            x int;
            y int;
        }
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: i\n", 454))

    def test_055(self):
        input = """
            type S1 struct {aa int;}
            func (s S1) cccc() {return ;}
            func (s S1) aa() {
                s.aa();
                var a = s.cccc();
            }        
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(s),cccc,[])\n""", 455))

    def test_056(self):
        input = """
            func foo()  {return ;}
            func  a()  {
                foo();
                return a();
            }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(a,[])\n", 456))

    def test_057(self):
        input = """    
            func foo()  {return ;}
            func  BB() int {
            foo();
            return foo();
            }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])\n", 457))

    def test_058(self):
        input = """
            var a THANG;
            func foo() THANG {
                return a;
                return THANG;
            }

            type THANG struct {aa int;}
        """
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: THANG\n", 458))

    def test_059(self):
        input = """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b := 2 {
                const b = 1;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: b\n", 459))

    def test_060(self):
        """
        func foo() int {
            return [2] int {1, 2}[a];
        }

        var a = foo();
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))])),VarDecl("a", None,FuncCall("foo",[]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a\n", 460))

    def test_061(self):
        """
        var a = 1;
        func foo() {
            return a;
        }
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(Id(a))\n", 461))

    def test_062(self):
        """
            type AAAA struct {a [2]int;} 
            type cccc interface {foo() int;}

            func (v AAAA) foo() int {return 1;}

            func foo(a cccc) {
                var b cccc = AAAA{a: [2]int{1, 2}};
                foo(b)
            }
        """
        input = Program([StructType("AAAA",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("cccc",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("AAAA"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("cccc"))],VoidType(),Block([VarDecl("b",Id("cccc"),StructLiteral("AAAA",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        self.assertTrue(TestChecker.test(input, "", 462))

    def test_063(self):
        """
        type AAAAA struct {a [2]int;} 
        type CCCC interface {foo() int;}

        func (v AAAAA) foo() int {return 1;}

        func foo(a CCCC) {
            var b = nil;
            foo(nil)
        }
        """
        input = Program([StructType("AAAAA",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("CCCC",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("AAAAA"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("CCCC"))],VoidType(),Block([VarDecl("b", None,NilLiteral()),FuncCall("foo",[NilLiteral()])]))])
        self.assertTrue(TestChecker.test(input, "", 463))

    def test_064(self):
        input ="""
        type THANG struct {a [2]int;} 

        func foo() THANG {
            return nil
        }
        """
        self.assertTrue(TestChecker.test(input, "", 464))

    def test_065(self):
        input = """
func foo() int {
    if (true) {
        var a = 1;
    } else {
        var a = 2;
    }
    return a;
}
  """
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a\n", 465))
    def test_066(self):
        input = """
func foo() int {
    var a = 1;
    if (a < 3) {
        var a = 1;
    } else if(a > 2) {
        var a = 2;
    }
    return a;
}
  """
        self.assertTrue(TestChecker.test(input, "", 466))
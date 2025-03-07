import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    count = 299
    def test_300(self):
        input = "const a = 1;\n"
        # Nếu không có type, conType được để là None
        expect = str(Program([ConstDecl("a", None, IntLiteral(1))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
    
    def test_301(self):
        input = "var b int = 2;\n"
        expect = str(Program([VarDecl("b", IntType(), IntLiteral(2))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_302(self):
        input = "var c int;\n"
        expect = str(Program([VarDecl("c", IntType(), None)]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_303(self):
        input = "var arr [3]int = [3]int {1,2,3};\n"
        expect = str(Program([VarDecl("arr",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_304(self):
        input = "func main() {};"
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        

    def test_305(self):
        input = "const d = 1+2;\n"
        expect = str(Program([ConstDecl("d", None, BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_306(self):
        input = "const e = -3;\n"
        expect = str(Program([ConstDecl("e", None, UnaryOp("-", IntLiteral(3)))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_307(self):
        input = 'const s = Person { name: "John" };\n'
        expect = str(Program([ConstDecl("s", None, StructLiteral("Person", [("name", StringLiteral("\"John\""))]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_308(self):
        input = "func main() { foo(1,2); };"
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([FuncCall("foo", [IntLiteral(1), IntLiteral(2)])]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
        
    def test_309(self):
        input = "const x = arr[0][1];\n"
        expect = str(Program([ConstDecl("x", None, ArrayCell(arr=Id("arr"), idx=[IntLiteral(0), IntLiteral(1)]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
    
    def test_310(self):
        input = "const y = person.name;\n"
        expect = str(Program([ConstDecl("y", None, FieldAccess(receiver=Id("person"), field="name"))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
    
    def test_311(self):
        input = "func main() { for i := 0; i < 10; i := i+1 { }; };\n"
        init = Assign(lhs=Id("i"), rhs=IntLiteral(0))
        cond = BinaryOp("<", Id("i"), IntLiteral(10))
        upda = Assign(lhs=Id("i"), rhs=BinaryOp("+", Id("i"), IntLiteral(1)))
        loop = Block(member=[])
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            ForStep(init, cond, upda, loop)
        ]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_312(self):
        input = "func main() { for _,v := range lam { }; };"
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([ForEach(Id("_"), Id("v"), Id("lam"), Block([]))]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_313(self):
        input = "func main() { for var i int = 0; i < 5; i := i+1 { }; };"
        init = VarDecl("i", IntType(), IntLiteral(0))
        cond = BinaryOp(op="<", left=Id("i"), right=IntLiteral(5))
        upda = Assign(lhs=Id("i"), rhs=BinaryOp(op="+", left=Id("i"), right=IntLiteral(1)))
        loop = Block(member=[])
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(init, cond, upda, loop)
            ]))
        ]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_314(self):
        input = """const x = foo( 1 ); """
        expect = str(Program([ConstDecl("x", None, FuncCall("foo", [IntLiteral(1)]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_315(self):
        input = """const x = foo( 1.0,true,false,nil,\"a\" ); """
        expect = str(Program([ConstDecl("x", None, FuncCall("foo", [FloatLiteral(1.0), BooleanLiteral(True), BooleanLiteral(False), NilLiteral(), StringLiteral("\"a\"")]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_316(self):
        input = """const x = foo( id ); """
        expect = str(Program([ConstDecl("x", None, FuncCall("foo", [Id("id")]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_317(self):
        input = """const x = foo( (1+2-3) && (5--1) ); """
        expect = str(Program([ConstDecl("x", None, FuncCall("foo", [BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-", IntLiteral(1))))]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_318(self):
        input = """const x = foo( a > b <= c ); """
        expect = str(Program([ConstDecl("x", None, FuncCall("foo", [BinaryOp("<=", BinaryOp(">", Id("a"), Id("b")), Id("c"))]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_319(self):
        input = """
            func x() {
                if(1) {return;}
            }
"""
        expect = str(Program([
            FuncDecl("x", [], VoidType(), Block([
                If(IntLiteral(1), Block([Return(None)]), None)
            ]))
        ]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_320(self):
        input = """
            func x() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = str(Program([
            FuncDecl("x", [], VoidType(), Block([
                If(IntLiteral(1), Block([Assign(Id("a"), IntLiteral(1))]), Block([Assign(Id("a"), IntLiteral(1))]))
            ]))
        ]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_321(self):
        input = """
            func x() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = str(Program([
            FuncDecl("x", [], VoidType(), Block([
                If(IntLiteral(1), Block([Return(None)]), 
                    If(IntLiteral(1), Block([Assign(Id("a"), IntLiteral(1))]), 
                        If(IntLiteral(2), Block([Assign(Id("a"), IntLiteral(1))]), None)))
            ]))
        ]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_322(self):
        """Function declaration with for loop"""
        input = """
            func x() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = str(Program([
            FuncDecl("x", [], VoidType(), Block([
                ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)), Block([Return(None)])),
                ForStep(VarDecl("i", None, IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([Return(None)]))
            ]))
        ]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_323(self):
        input = """
            func x() {
                for index, value := range array[2] {return;}
            }
"""
        expect = str(Program([
            FuncDecl("x", [], VoidType(), Block([
                ForEach(Id("index"), Id("value"), ArrayCell(Id("array"), [IntLiteral(2)]), Block([Return(None)]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = """
            const a = foo()[2];
"""
        expect = str(Program([ConstDecl("a",None,ArrayCell(FuncCall("foo",[]),[IntLiteral(2)]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_325(self):
        input = """
            const a = a;
"""
        expect = str(Program([ConstDecl("a",None,Id("a"))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_326(self):
        """More complex program"""
        input = """
            var a X = 1.;
"""
        expect = str(Program([VarDecl("a",Id("X"),FloatLiteral(1.0))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_327(self):
        input = """
            var a [2][3]int;
"""
        expect = str(Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
    
    def test_328(self):
        input = """
            var a = 1;
"""
        expect = str(Program([VarDecl("a", None,IntLiteral(1))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_329(self):
        input = """
            type X struct {
                a int;
            }
"""
        expect = str(Program([StructType("X",[("a",IntType())],[])]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_330(self):
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_331(self):
        input = """const a = 1 * 2 / 3 % 4; """
        expect = str(Program([ConstDecl("a", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_332(self):
        input = """
        func foo () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))




    def test_333(self):
        input = """
            var a = 1;
            var a int;
            var aab int = 1;
"""
        expect = str(Program([VarDecl("a", None,IntLiteral(1)),
			VarDecl("a",IntType(), None),
			VarDecl("aab",IntType(),IntLiteral(1))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_334(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = str(Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_335(self):
        input = """
            func (a v) foo(a int) {return;}
"""
        expect = str(Program([MethodDecl("a",Id("v"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([Return(None)])))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_336(self):
        input = """
            type a struct {
                a int;
            }
"""
        expect = str(Program([StructType("a",[("a",IntType())],[])
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_337(self):
        input = """
            type a struct {
                a int;
            }
"""
        expect = str(Program([StructType("a",[("a",IntType())],[])
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

#     def test_338(self):
#         input = """
#             type a interface {
#                 Add(x, y int) int;
#             }
# """
#         expect = str(Program([InterfaceType("a",[Prototype("Add",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType())])]))

#         ASTGenSuite.count +=1
#         self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_339(self):
        input = """
            func a() {
                var a int;
                const a = nil;
            }
"""
        expect = str(Program([FuncDecl("a",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_340(self):
        input = """const a = a.b.c; """
        expect = str(Program([ConstDecl("a", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_341(self):
        input = """const a = a.b().c(1, 2); """
        expect = str(Program([ConstDecl("a", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_342(self):
        input = """const a = a.b[2].c.d(); """
        expect = str(Program([ConstDecl("a", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_343(self):
        input = """
    var a int = 1;
    var a float = 1;
    var a boolean;
    var a string = 1;
    var a = 1;
    var a ID = 1;
    var a [ID][1] int = 1;
"""
        expect = str(Program([VarDecl("a",IntType(),IntLiteral(1)),
			VarDecl("a",FloatType(),IntLiteral(1)),
			VarDecl("a",BoolType(), None),
			VarDecl("a",StringType(),IntLiteral(1)),
			VarDecl("a", None,IntLiteral(1)),
			VarDecl("a",Id("ID"),IntLiteral(1)),
			VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_344(self):
        input = """
    const a = 1;
"""
        expect = str(Program([ConstDecl("a",None,IntLiteral(1))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_345(self):
        input = """
    type ID struct {
        a int;
        b ID;
        c [2]int;
    }
"""
        expect = str(Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_346(self):
        input = """
    func foo () {var a = 1;}
    func foo () int {var a = 1;}
    func foo () [2] ID {var a = 1;}
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_347(self):
        input = """
    func foo (a int) {var a = 1;}
    func foo (a int, b ID) {var a = 1;}
    func foo (a, b int) {var a = 1;}
"""
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))



    def test_348(self):
        input = """
    func (ID ID) foo () {var a = 1;}
    func (ID ID) foo () int {var a = 1;}
    func (ID ID) foo () [2] ID {var a = 1;}
"""
        expect = str(Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))])))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_349(self):
        input = """
    func (ID ID) foo (a int) {var a = 1;}
    func (ID ID) foo (a int, b ID) {var a = 1;}
    func (ID ID) foo (a, b int) {var a = 1;}
"""
        expect = str(Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

#     def test_350(self):
#         input = """
#         type INTERFACE interface {
#             foo();
#             foo() int;
#             foo() [2]ID;
#             foo(a int);
#             foo(a int, b int);
#             foo(a, b int);
#         }
# """
#         expect = str(Program([InterfaceType("INTERFACE",[
#             Prototype("foo",[],VoidType()),Prototype("foo",[],IntType()),
#             Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
#             Prototype("foo",[ParamDecl("a",IntType())],VoidType()),
#             Prototype("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType()),
#             Prototype("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType())])
# 		]))
#         ASTGenSuite.count +=1
#         self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_351(self):
        input = """
    func foo () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_352(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_353(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_354(self):
        input = """
    func foo () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_355(self):
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_356(self):
        input = """
    func foo () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))
    
    def test_357(self):
        input = """
        func foo () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_358(self):
        input = """
        func foo () {
            for(1) {return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_359(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_360(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_361(self):
        input = """
        func foo () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),
            ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_362(self):
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),

            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_363(self):
        input = """const xxx = 1; """
        expect = str(Program([ConstDecl("xxx", None, IntLiteral(1))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_364(self):
        input = """const xxx = 0b11; """
        expect = str(Program([ConstDecl("xxx", None, IntLiteral(0b11))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_365(self):
        input = """const xxx = 0o70; """
        expect = str(Program([ConstDecl("xxx", None, IntLiteral(56))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_366(self):
        input = """const xxx = 0Xa1; """
        expect = str(Program([ConstDecl("xxx", None, IntLiteral(161))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_367(self):
        input = """const xxx = 01.e-1; """
        expect = str(Program([ConstDecl("xxx", None, FloatLiteral(0.1))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_368(self):
        input = """const xxx = true; """
        expect = str(Program([ConstDecl("xxx", None, BooleanLiteral(True))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_369(self):
        input = """const xxx = false; """
        expect = str(Program([ConstDecl("xxx", None, BooleanLiteral(False))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_370(self):
        input = """const xxx = "xxx"; """
        expect = str(Program([ConstDecl("xxx", None, StringLiteral("\"xxx\""))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_371(self):
        input = """const xxx = nil; """
        expect = str(Program([ConstDecl("xxx", None, NilLiteral())]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    
    def test_372(self):
        input = """const xxx = STRUCT {}; """
        expect = str(Program([ConstDecl("xxx", None, StructLiteral("STRUCT",[]))]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_373(self):
        input = """const kkk = foo( a[2][3] ); """
        expect = str(Program([ConstDecl("kkk",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_374(self):
        input = """const kkk = foo( a.b.c ); """
        expect = str(Program([ConstDecl("kkk",None,FuncCall("foo",[FieldAccess(FieldAccess(Id("a"),"b"),"c")]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_375(self):
        input = """const kkk = foo( a(),b.a(2, 3) ); """
        expect = str(Program([ConstDecl("kkk",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_376(self):
        input = """const kkk = foo( a * (1+2) ); """
        expect = str(Program([ConstDecl("kkk",None,FuncCall("foo",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_377(self):
        input = """const kkk = foo( kkk {}, kkk {a: 1} ); """
        expect = str(Program([ConstDecl("kkk",None,FuncCall("foo",[StructLiteral("kkk",[]),StructLiteral("kkk",[("a",IntLiteral(1))])]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_378(self):
        input = """
        func matrixSum(arr [3][3]int) int {
            sum := 0;
            for i := 0; i < 3; i := i + 1 {
                for j := 0; j < 3; j := j + 1 {
                    sum := sum + arr[i][j];
                };
            };
            return sum;
        };
    """
        expect = str(Program([
        FuncDecl("matrixSum", 
            [ParamDecl("arr", ArrayType([IntLiteral(3), IntLiteral(3)],IntType()))], 
            IntType(), 
            Block([
                Assign(Id("sum"), IntLiteral(0)),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)), 
                    BinaryOp("<", Id("i"), IntLiteral(3)), 
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), 
                    Block([
                        ForStep(
                            Assign(Id("j"), IntLiteral(0)), 
                            BinaryOp("<", Id("j"), IntLiteral(3)), 
                            Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))), 
                            Block([
                                Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("arr"), [Id("i"), Id("j")])))
                            ])
                        )
                    ])
                ),
                Return(Id("sum"))
            ])
        )
    ]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))



    def test_379(self):
        input = """const kkk = foo( [1]int{1}, [1][1]int{2} ); """
        expect = str(Program([ConstDecl("kkk",None,FuncCall("foo",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_380(self):
        input = """
            var kkk = 1;
            var kkk int;
            var Votine int = 1;
"""
        expect = str(Program([VarDecl("kkk", None,IntLiteral(1)),
			VarDecl("kkk",IntType(), None),
			VarDecl("Votine",IntType(),IntLiteral(1))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_381(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = str(Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_382(self):
        input = """
            func (kkk v) foo(kkk int) {return;}
"""
        expect = str(Program([MethodDecl("kkk",Id("v"),FuncDecl("foo",[ParamDecl("kkk",IntType())],VoidType(),Block([Return(None)])))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_383(self):
        input = """
            type kkk struct {
                a int;
            }
"""
        expect = str(Program([StructType("kkk",[("a",IntType())],[])
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_384(self):
        input = """
            type kkk struct {
                a int;
            }
"""
        expect = str(Program([StructType("kkk",[("a",IntType())],[])
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_385(self):
        input = """
            func kkk() {
                var a int;
                const a = nil;
            }
"""
        expect = str(Program([FuncDecl("kkk",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_386(self):
        input = """
            func kkk() {
                a += 1;
            }
"""
        expect = str(Program([FuncDecl("kkk",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_387(self):
        input = """
            func kkk() {
                break;
                continue;
            }
"""
        expect = str(Program([FuncDecl("kkk",[],VoidType(),Block([Break(),Continue()]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_388(self):
        input = """
            func kkk() {
                foo(1, 2);
                a[2].foo(1,3);
            }
"""
        expect = str(Program([FuncDecl("kkk",[],VoidType(),Block([FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])]))
		]))
        ASTGenSuite.count +=1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


    def test_3891(self):
        input = "const a = 1;"
        expect = str(Program([ConstDecl("a", None, IntLiteral(1))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_390(self):
        input = "func main() {};"
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_391(self):
        input = "var x = true;"
        expect = str(Program([VarDecl("x", None, BooleanLiteral(True))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_392(self):
        input = "const y = 3.14;"
        expect = str(Program([ConstDecl("y", None, FloatLiteral(3.14))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_393(self):
        input = "func add(a int, b int) { return a + b; };"
        expect = str(Program([FuncDecl("add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), 
                         Block([Return(BinaryOp("+", Id("a"), Id("b")))]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_394(self):
        input = "func foo() { print(123); };"
        expect = str(Program([FuncDecl("foo", [], VoidType(), Block([FuncCall("print", [IntLiteral(123)])]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_395(self):
        input = "var arr = [3]int{1,2,3};"
        expect = str(Program([VarDecl("arr", None, ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_396(self):
        input = "func test() { if (x > 10) { return true; }; };"
        expect = str(Program([FuncDecl("test", [], VoidType(), Block([
                         If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([Return(BooleanLiteral(True))]),None)]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_397(self):
        input = "func loop() { for i := 0; i < 5; i := i + 1 { print(i); }; };"
        expect = str(Program([FuncDecl("loop", [], VoidType(), Block([
                         ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(5)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                         Block([FuncCall("print", [Id("i")])]))]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))

    def test_398(self):
        input = "func callMethod() { obj.method(42); };"
        expect = str(Program([FuncDecl("callMethod", [], VoidType(), Block([
                         MethCall(Id("obj"), "method", [IntLiteral(42)])]))]))
        ASTGenSuite.count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.count))


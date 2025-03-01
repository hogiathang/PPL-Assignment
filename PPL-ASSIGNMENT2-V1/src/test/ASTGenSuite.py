import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    test_count = 300
    def test_var_declare_1(self):
        input = """var x int;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_var_declare_2(self):
        """More complex program"""
        input = """var x int = [2]int{1,"Foo"};"""
        expect = str(Program([
            VarDecl("x",
            IntType(),
            ArrayLiteral(
                [IntLiteral(2)],IntType(),
                [IntLiteral(1),StringLiteral("\"Foo\"")]
            )
        )]))
        
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))
    
    def test_var_declare_3(self):
        """More complex program"""
        input = """var arr [10][20][30]int = [10][20][30]int{sampleStruct{a1 : "Hello", a2: "World"}};"""
        expect = str(Program([
            VarDecl("arr",
            ArrayType([IntLiteral(10),IntLiteral(20),IntLiteral(30)],IntType()),
            ArrayLiteral(
                [IntLiteral(10),IntLiteral(20),IntLiteral(30)],IntType(),
                [StructLiteral("sampleStruct",[("a1",StringLiteral("\"Hello\"")),("a2",StringLiteral("\"World\""))])]
            )
        )]))
        
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_var_declare_4(self):
        input = """var test = 1 + 20 - 3 * 4 || 5 && 6 + test.foo(1,2,3).bar[1];"""
        expect = str(Program([
            VarDecl('test',
            None,
            BinaryOp(
                '||',
                BinaryOp(
                    '-',
                    BinaryOp(
                        '+',
                        IntLiteral(1),
                        IntLiteral(20)
                    ),
                    BinaryOp(
                        '*',
                        IntLiteral(3),
                        IntLiteral(4)
                    )
                ),
                BinaryOp(
                    '&&',
                    IntLiteral(5),
                    BinaryOp(
                        '+',
                        IntLiteral(6),
                        ArrayCell(
                            FieldAccess(
                                MethCall(
                                    Id('test'),
                                    'foo',
                                    [IntLiteral(1),IntLiteral(2),IntLiteral(3)]
                                ),
                                'bar'
                            ),
                            [IntLiteral(1)]
                        )
                    )
                )
            )
        )])
        )
        
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_var_declare_5(self):
        input = """var t helloworld = identifier{a1: 1, a2: !zelo, a3: 001.e-2};"""
        expect = str(Program([
            VarDecl(
                't',
                Id('helloworld'),
                StructLiteral(
                    'identifier',
                    [
                        ('a1',IntLiteral(1)),
                        ('a2',UnaryOp('!',Id('zelo'))),
                        ('a3',FloatLiteral(0.01))
                    ]
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_const_declare_6(self):
        input = """const x = 1.e-3;"""
        expect = str(Program([ConstDecl('x',None,FloatLiteral(1.e-3))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_const_declare_7(self):
        input = """const x boolean = a && !b || c >= 5;"""
        expect = str(Program([ConstDecl('x',BoolType(),BinaryOp('||',BinaryOp('&&',Id('a'),UnaryOp('!',Id('b'))),BinaryOp('>=',Id('c'),IntLiteral(5))))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_const_declare_8(self):
        input = """const x = a.b.c[1][2].d[2][3][4][5][6].e();"""
        expect = str(Program([
            ConstDecl(
                'x',
                None,
                MethCall(
                    ArrayCell(
                        FieldAccess(
                            ArrayCell(
                                FieldAccess(
                                    FieldAccess(
                                        Id('a'),
                                        'b'
                                    ),
                                    'c'
                                ),
                                [IntLiteral(1),IntLiteral(2)]
                            ),
                            'd'
                        ),
                        [IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)]
                    ),
                'e',
                []
            ))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_const_declare_9(self):
        input = """
            const complexStruct = Person{
                name: "John", 
                age: 25, 
                scores: [5]float{90.5, 85.0, 92.3, 88.7, 95.2},
                address: Address{
                    street: "123 Main St",
                    city: "Boston",
                    zip: 2108},
                graduated: true && !failed};
        """
        
        expect = str(Program([
            ConstDecl(
                'complexStruct',
                None,
                StructLiteral(
                    'Person',
                    [
                        ('name', StringLiteral('"John"')),
                        ('age', IntLiteral(25)),
                        ('scores', ArrayLiteral(
                            [IntLiteral(5)], 
                            FloatType(),
                            [FloatLiteral(90.5), FloatLiteral(85.0), FloatLiteral(92.3), 
                            FloatLiteral(88.7), FloatLiteral(95.2)]
                        )),
                        ('address', StructLiteral(
                            'Address',
                            [
                                ('street', StringLiteral('"123 Main St"')),
                                ('city', StringLiteral('"Boston"')),
                                ('zip', IntLiteral(2108))
                            ]
                        )),
                        ('graduated', BinaryOp('&&', BooleanLiteral(True), UnaryOp('!', Id('failed'))))
                    ]
                )
            )
        ]))
        
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))
    
    def test_const_declare_10(self):
        input = """const nestedExpr = -foo(bar[1][2], baz.qux()) * (a + b[i+j] - c / d) || !(x > y && z <= w);"""
        
        expect = str(Program([
            ConstDecl(
                'nestedExpr',
                None,
                BinaryOp(
                    '||',
                    BinaryOp(
                        '*',
                        UnaryOp(
                            '-',
                            FuncCall(
                                'foo',
                                [
                                    ArrayCell(
                                        Id('bar'),
                                        [IntLiteral(1), IntLiteral(2)]
                                    ),
                                    MethCall(
                                        Id('baz'),
                                        'qux',
                                        []
                                    )
                                ]
                            )
                        ),
                        BinaryOp(
                            '-',
                            BinaryOp(
                                '+',
                                Id('a'),
                                ArrayCell(
                                    Id('b'),
                                    [BinaryOp('+', Id('i'), Id('j'))]
                                )
                            ),
                            BinaryOp(
                                '/',
                                Id('c'),
                                Id('d')
                            )
                        )
                    ),
                    UnaryOp(
                        '!',
                        BinaryOp(
                            '&&',
                            BinaryOp(
                                '>',
                                Id('x'),
                                Id('y')
                            ),
                            BinaryOp(
                                '<=',
                                Id('z'),
                                Id('w')
                            )
                        )
                    )
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_func_declare_11(self):
        input = """func main() {};"""
        expect = str(Program([FuncDecl('main',[],VoidType(),Block([]))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))
    
    def test_func_declare_12(self):
        input = """func main() int {return 0;};"""
        expect = str(Program([FuncDecl('main',[],IntType(),Block([Return(IntLiteral(0))]))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_func_declare_13(self):
        input = """func foo(a int, b float) int {return 0;};"""
        expect = str(Program([FuncDecl('foo',[ParamDecl('a',IntType()),ParamDecl('b',FloatType())],IntType(),Block([Return(IntLiteral(0))]))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_func_declare_14(self):
        input = """func foo(a, b int, c float, d Foo) Bar {return a+b;};"""
        expect = str(Program([FuncDecl('foo',[ParamDecl('a',IntType()),ParamDecl('b',IntType()),ParamDecl('c',FloatType()),ParamDecl('d',Id('Foo'))],Id('Bar'),Block([Return(BinaryOp('+',Id('a'),Id('b')))]))]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_func_declare_15(self):
        input = """
            func wikiList(a, b int, c float, d Foo) [abc123][def456]Wiki {
                return [20]Wiki{Wiki{title: "Hello", content: "World"},
                Wiki{title: "Abraham", content: "Lincon"},
                Wiki{title: "John", content: "Wick"},
                Wiki{title: "Mickey", content: "Mouse"}};
            }
        """
        expect = str(Program([
            FuncDecl(
                'wikiList',
                [ParamDecl('a', IntType()), ParamDecl('b', IntType()), ParamDecl('c', FloatType()), ParamDecl('d', Id('Foo'))],
                ArrayType([Id('abc123'), Id('def456')], Id('Wiki')),
                Block([
                    Return(
                        ArrayLiteral(
                            [IntLiteral(20)],
                            Id('Wiki'),
                            [StructLiteral(
                                'Wiki',
                                [
                                    ('title', StringLiteral('"Hello"')),
                                    ('content', StringLiteral('"World"'))
                                ]
                            ),
                            StructLiteral(
                                'Wiki',
                                [
                                    ('title', StringLiteral('"Abraham"')),
                                    ('content', StringLiteral('"Lincon"'))
                                ]
                            ),
                            StructLiteral(
                                'Wiki',
                                [
                                    ('title', StringLiteral('"John"')),
                                    ('content', StringLiteral('"Wick"'))
                                ]
                            ),
                            StructLiteral(
                                'Wiki',
                                [
                                    ('title', StringLiteral('"Mickey"')),
                                    ('content', StringLiteral('"Mouse"'))
                                ]
                            )]
                        )
                    )
                ])
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input,expect,ASTGenSuite.test_count))

    def test_func_declare_16(self):
        input = """func (r Rectangle) area() float {
            return r.width * r.height;
        }
        """
        expect = str(Program([
            MethodDecl(
                'r',
                Id('Rectangle'),
                FuncDecl(
                    'area',
                    [],
                    FloatType(),
                    Block([
                        Return(
                            BinaryOp(
                                '*',
                                FieldAccess(Id('r'), 'width'),
                                FieldAccess(Id('r'), 'height')
                            )
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))
        
    def test_func_declare_17(self):
        input = """
        func calculateSum(numbers [10]int) int {
            var sum = 0;
            for i := 0; i < 10; i := i + 1 {
                sum := sum + numbers[i];
            }
            return sum;
        }
        """
        expect = str(Program([
            FuncDecl(
                'calculateSum',
                [ParamDecl('numbers', ArrayType([IntLiteral(10)], IntType()))],
                IntType(),
                Block([
                    VarDecl('sum', None, IntLiteral(0)),
                    ForStep(
                        Assign(Id('i'), IntLiteral(0)),
                        BinaryOp('<', Id('i'), IntLiteral(10)),
                        Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                        Block([
                            Assign(
                                Id('sum'), 
                                BinaryOp('+', Id('sum'), ArrayCell(Id('numbers'), [Id('i')]))
                            )
                        ])
                    ),
                    Return(Id('sum'))
                ])
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_func_declare_18(self):
        input = """func processData(matrix [3][3]float) [3]float {
            var result [3]float;
            for i := 0; i < 3; i := i + 1 {
                result[i] := 0;
                for j := 0; j < 3; j := j + 1 {
                    result[i] := result[i] + matrix[i][j];
                }
            }
            return result;
        }
        """
        expect = str(Program([
            FuncDecl(
                'processData',
                [ParamDecl('matrix', ArrayType([IntLiteral(3), IntLiteral(3)], FloatType()))],
                ArrayType([IntLiteral(3)], FloatType()),
                Block([
                    VarDecl('result', ArrayType([IntLiteral(3)], FloatType()), None),
                    ForStep(
                        Assign(Id('i'), IntLiteral(0)),
                        BinaryOp('<', Id('i'), IntLiteral(3)),
                        Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                        Block([
                            Assign(ArrayCell(Id('result'), [Id('i')]), IntLiteral(0)),
                            ForStep(
                                Assign(Id('j'), IntLiteral(0)),
                                BinaryOp('<', Id('j'), IntLiteral(3)),
                                Assign(Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
                                Block([
                                    Assign(
                                        ArrayCell(Id('result'), [Id('i')]),
                                        BinaryOp(
                                            '+',
                                            ArrayCell(Id('result'), [Id('i')]),
                                            ArrayCell(Id('matrix'), [Id('i'), Id('j')])
                                        )
                                    )
                                ])
                            )
                        ])
                    ),
                    Return(Id('result'))
                ])
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_func_declare_19(self):
        input = """
        func recursiveFunc(n int) int {
            if (n <= 1) {
                return 1;
            } else if (n == 2) {
                return 2;
            } 
            return n * recursiveFunc(n - 1);
        }
        """
        expect = str(Program([
            FuncDecl(
                'recursiveFunc',
                [ParamDecl('n', IntType())],
                IntType(),
                Block([
                    If(
                        BinaryOp('<=', Id('n'), IntLiteral(1)),
                        Block([Return(IntLiteral(1))]),
                        Block([
                            If(
                                BinaryOp('==', Id('n'), IntLiteral(2)),
                                Block([Return(IntLiteral(2))]),
                                None
                            )
                        ])
                    ),
                    Return(
                        BinaryOp(
                            '*', 
                            Id('n'), 
                            FuncCall(
                                'recursiveFunc', 
                                [BinaryOp('-', Id('n'), IntLiteral(1))]
                            )
                        )
                    )
                ])
            )
        ]))
        
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_func_declare_20(self):
        input = """func createPerson(name string, age int) Person {
            return Person{
                name: name,
                age: age,
                address: Address{
                    street: "Default Street",
                    city: "Default City"},
                isActive: true};
        };"""
        expect = str(Program([
            FuncDecl(
                'createPerson',
                [ParamDecl('name', StringType()), ParamDecl('age', IntType())],
                Id('Person'),
                Block([
                    Return(
                        StructLiteral(
                            'Person',
                            [
                                ('name', Id('name')),
                                ('age', Id('age')),
                                ('address', StructLiteral(
                                    'Address',
                                    [
                                        ('street', StringLiteral('"Default Street"')),
                                        ('city', StringLiteral('"Default City"'))
                                    ]
                                )),
                                ('isActive', BooleanLiteral(True))
                            ]
                        )
                    )
                ])
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))
   
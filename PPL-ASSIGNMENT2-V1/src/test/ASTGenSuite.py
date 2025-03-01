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

    # def test_func_declare_16(self):
    #     input = """func (r Rectangle) area() float {
    #         return r.width * r.height;
    #     }"""
    #     expect = str(Program([
    #         MethodDecl(
    #             'r',
    #             Id('Rectangle'),
    #             FuncDecl(
    #                 'area',
    #                 [],
    #                 FloatType(),
    #                 Block([
    #                     Return(
    #                         BinaryOp(
    #                             '*',
    #                             FieldAccess(Id('r'), 'width'),
    #                             FieldAccess(Id('r'), 'height')
    #                         )
    #                     )
    #                 ])
    #             )
    #         )
    #     ]))
    #     ASTGenSuite.test_count += 1
    #     self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))
        
    # def test_func_declare_17(self):
    #     input = """func calculateSum(numbers [10]int) int {
    #         var sum = 0;
    #         for i := 0; i < 10; i = i + 1 {
    #             sum = sum + numbers[i];
    #         }
    #         return sum;
    #     }"""
    #     expect = str(Program([
    #         FuncDecl(
    #             'calculateSum',
    #             [ParamDecl('numbers', ArrayType([IntLiteral(10)], IntType()))],
    #             IntType(),
    #             Block([
    #                 VarDecl('sum', None, IntLiteral(0)),
    #                 ForStep(
    #                     Assign(Id('i'), IntLiteral(0)),
    #                     BinaryOp('<', Id('i'), IntLiteral(10)),
    #                     Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
    #                     Block([
    #                         Assign(
    #                             Id('sum'), 
    #                             BinaryOp('+', Id('sum'), ArrayCell(Id('numbers'), [Id('i')]))
    #                         )
    #                     ])
    #                 ),
    #                 Return(Id('sum'))
    #             ])
    #         )
    #     ]))
    #     ASTGenSuite.test_count += 1
    #     self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    # def test_func_declare_18(self):
    #     input = """func processData(matrix [3][3]float) [3]float {
    #         var result [3]float;
    #         for i := 0; i < 3; i = i + 1 {
    #             result[i] = 0;
    #             for j := 0; j < 3; j = j + 1 {
    #                 result[i] = result[i] + matrix[i][j];
    #             }
    #         }
    #         return result;
    #     }"""
    #     expect = str(Program([
    #         FuncDecl(
    #             'processData',
    #             [ParamDecl('matrix', ArrayType([IntLiteral(3), IntLiteral(3)], FloatType()))],
    #             ArrayType([IntLiteral(3)], FloatType()),
    #             Block([
    #                 VarDecl('result', ArrayType([IntLiteral(3)], FloatType()), None),
    #                 ForStep(
    #                     Assign(Id('i'), IntLiteral(0)),
    #                     BinaryOp('<', Id('i'), IntLiteral(3)),
    #                     Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
    #                     Block([
    #                         Assign(ArrayCell(Id('result'), [Id('i')]), IntLiteral(0)),
    #                         ForStep(
    #                             Assign(Id('j'), IntLiteral(0)),
    #                             BinaryOp('<', Id('j'), IntLiteral(3)),
    #                             Assign(Id('j'), BinaryOp('+', Id('j'), IntLiteral(1))),
    #                             Block([
    #                                 Assign(
    #                                     ArrayCell(Id('result'), [Id('i')]),
    #                                     BinaryOp(
    #                                         '+',
    #                                         ArrayCell(Id('result'), [Id('i')]),
    #                                         ArrayCell(Id('matrix'), [Id('i'), Id('j')])
    #                                     )
    #                                 )
    #                             ])
    #                         )
    #                     ])
    #                 ),
    #                 Return(Id('result'))
    #             ])
    #         )
    #     ]))
    #     ASTGenSuite.test_count += 1
    #     self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    # def test_func_declare_19(self):
    #     input = """func recursiveFunc(n int) int {
    #         if n <= 1 {
    #             return 1;
    #         }
    #         return n * recursiveFunc(n - 1);
    #     }"""
    #     expect = str(Program([
    #         FuncDecl(
    #             'recursiveFunc',
    #             [ParamDecl('n', IntType())],
    #             IntType(),
    #             Block([
    #                 If(
    #                     BinaryOp('<=', Id('n'), IntLiteral(1)),
    #                     Block([Return(IntLiteral(1))]),
    #                     None
    #                 ),
    #                 Return(
    #                     BinaryOp(
    #                         '*',
    #                         Id('n'),
    #                         FuncCall(
    #                             'recursiveFunc',
    #                             [BinaryOp('-', Id('n'), IntLiteral(1))]
    #                         )
    #                     )
    #                 )
    #             ])
    #         )
    #     ]))
    #     ASTGenSuite.test_count += 1
    #     self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    # def test_func_declare_20(self):
    #     input = """func createPerson(name string, age int) Person {
    #         return Person{
    #             name: name,
    #             age: age,
    #             address: Address{
    #                 street: "Default Street",
    #                 city: "Default City"
    #             },
    #             isActive: true
    #         };
    #     }"""
    #     expect = str(Program([
    #         FuncDecl(
    #             'createPerson',
    #             [ParamDecl('name', StringType()), ParamDecl('age', IntType())],
    #             Id('Person'),
    #             Block([
    #                 Return(
    #                     StructLiteral(
    #                         'Person',
    #                         [
    #                             ('name', Id('name')),
    #                             ('age', Id('age')),
    #                             ('address', StructLiteral(
    #                                 'Address',
    #                                 [
    #                                     ('street', StringLiteral('"Default Street"')),
    #                                     ('city', StringLiteral('"Default City"'))
    #                                 ]
    #                             )),
    #                             ('isActive', BooleanLiteral(True))
    #                         ]
    #                     )
    #                 )
    #             ])
    #         )
    #     ]))
    #     ASTGenSuite.test_count += 1
    #     self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    # def test_call_without_parameter(self):
    #     input = """func main () {}; var x int ;"""
    #     expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
   
    # def test_var_init(self):
    #     input = """var x int = 3;"""
    #     expect = str(Program([VarDecl('x',IntType(),IntLiteral(3))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,304))

    # def test_var_init_float(self):
    #     input = """var x float = 3.0e5 + 5.;"""
    #     expect = str(Program([VarDecl('x',FloatType(),BinaryOp('+',FloatLiteral(3.0e5),FloatLiteral(5.)))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # def test_var_init_complex_expression_1(self):
    #     input = """var x int = 1 + -3 * ( 5 + 2);"""
    #     expect = str(Program([VarDecl('x',IntType(),BinaryOp('+',IntLiteral(1),BinaryOp('*',UnaryOp('-',IntLiteral(3)),BinaryOp('+',IntLiteral(5),IntLiteral(2)))))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))

    # def test_var_init_complex_expression_2(self):
    #     input = """var y float = 2.0 * (3 + 4.5) / -2.0;"""
    #     expect = str(Program([VarDecl('y',FloatType(),BinaryOp('/',BinaryOp('*',FloatLiteral(2.0),BinaryOp('+',IntLiteral(3),FloatLiteral(4.5))),UnaryOp('-',FloatLiteral(2.0))))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))

    # def test_bool_init(self):
    #     input = """var x boolean = a + b >=5 && c || d && e;"""
    #     expect = str(Program([VarDecl('x',BoolType(),BinaryOp('||',BinaryOp('&&',BinaryOp('>=',BinaryOp('+',Id('a'),Id('b')),IntLiteral(5)),Id('c')),BinaryOp('&&',Id('d'),Id('e'))))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))

    # def test_string_init(self):
    #     input = """var x = "hello";"""
    #     expect = str(Program([VarDecl('x',None,StringLiteral("\"hello\""))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))

    # def test_const_init(self):
    #     input = """const x = 5;"""
    #     expect = str(Program([ConstDecl('x',None,IntLiteral(5))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # def test_array_init_1(self):
    #     input = """var x = [5]int{1, 2};"""
    #     expect = str(
    #         Program([VarDecl('x',None,ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2)]))])
    #     )
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))

    # def test_array_init_2(self):
    #     input = """var x = [4][2]int{{1,2,3,4},{5,6,7,8}};"""
    #     expect = str(Program([VarDecl('x',ArrayType([IntLiteral(4),IntLiteral(2)],IntType()),ArrayLiteral([IntLiteral(4),IntLiteral(2)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)],[IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8)]]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))

    # def test_func_statements_1(self):
    #     input = """func main() {a:= 5
    #       b:= 6;};"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([Assign(Id('a'),BinaryOp(':=',Id('a'),IntLiteral(5))),Assign(Id('b'),BinaryOp(':=',Id('b'),IntLiteral(6)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))

    # def test_func_statements_2(self):
    #     input = """func main() int {a:= 5
    #       b:= 6
    #       return a+b;};"""
    #     expect = str(Program([FuncDecl('main',[],IntType(),Block([Assign(Id('a'),BinaryOp(':=',Id('a'),IntLiteral(5))),Assign(Id('b'),BinaryOp(':=',Id('b'),IntLiteral(6))),Return(BinaryOp('+',Id('a'),Id('b')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,314))

    # def test_array_cell_1(self):
    #     input = """func main() {
    #         a[5] := 6;
    #     };"""
    #     expect = str(Program([
    #         FuncDecl('main',[],VoidType(),
    #             Block([
    #                 Assign(
    #                     ArrayCell(Id(a),[IntLiteral(5)]),
    #                     BinaryOp(ArrayCell(Id(a),[IntLiteral(5)]),:=,IntLiteral(6))
    #                 )])
    #             )
    #         ]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # def test_array_cell_2(self):
    #     input = """func main() {a[5][b] = 6;}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([Assign(ArrayCell(Id('a'),[IntLiteral(5),Id('b')]),IntLiteral(6))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,316))

    # def test_field_access_1(self):
    #     input = """func main() {a.b = 5;}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([Assign(FieldAccess(Id('a'),'b'),IntLiteral(5))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,317))

    # def test_if_1(self):
    #     input = """func main() {if a > 5 {return 1;}}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(5)),Block([Return(IntLiteral(1))]),None)]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,318))

    # def test_if_else_1(self):
    #     input = """func main() {if a > 5 {return 1;} else {return 0;};}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(5)),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,319))

    # def test_if_else_chain_1(self):
    #     input = """func main() {if a > 5 {return 1;} else if a > 3 {return 2;} else {return 0;};}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(5)),Block([Return(IntLiteral(1))]),If(BinaryOp('>',Id('a'),IntLiteral(3)),Block([Return(IntLiteral(2))]),Block([Return(IntLiteral(0))])))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # def test_array_type_decl(self):
    #     input = "var arr [10]int ;"
    #     expect = str(Program([VarDecl("arr", ArrayType([IntLiteral(10)], IntType()), None)]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    # def test_for_loop_1(self):
    #     input = """func main() {for i<10 {return i;}}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([ForBasic(BinaryOp('<',Id('i'),IntLiteral(10)),Block([Return(Id('i'))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,322))

    # def test_for_loop_2(self):
    #     input = """func main() {for i:=0; i<10; i=i+1 {if i==5 {return i;}}; return 0;}"""
    #     expect=str(Program([FuncDecl('main',[],VoidType(),Block([ForStep(VarDecl('i',IntLiteral(0),None),BinaryOp('<',Id('i'),IntLiteral(10)),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('==',Id('i'),IntLiteral(5)),Block([Return(Id('i'))]),None)])),Return(IntLiteral(0))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,323))

    # def test_for_loop_3(self):
    #     input = """func main() {for idx, val := range arr {return 0;}}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([ForEach(Id('idx'),Id('val'),Id('arr'),Block([Return(IntLiteral(0))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,324))

    
    # def test_for_loop_4(self):
    #     input = """func main() {for _, _ := range [3]int{1,2,3} {return 0;}}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([ForEach(None,None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([Return(IntLiteral(0))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,325))

    # def test_method_call_1(self):
    #     input = """func main() {a.c();}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([MethCall(Id('a'),'c',[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,326))

    # def test_method_call_2(self):
    #     input = """func main() {a.b.c(1,d,e);}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([MethCall(FieldAccess(Id('a'),'b'),'c',[IntLiteral(1),Id('d'),Id('e')])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,326))
    
    # def test_func_decl_1(self):
    #     input = """func foo(a int, b float) int {return 0;}"""
    #     expect = str(Program([FuncDecl('foo',[ParamDecl('a',IntType()),ParamDecl('b',FloatType())],IntType(),Block([Return(IntLiteral(0))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,327))

    # def test_func_decl_2(self):
    #     input = """func foo(a, b int, c float, d Foo) Bar {return a+b;}"""
    #     expect = str(Program([FuncDecl('foo',[ParamDecl('a',IntType()),ParamDecl('b',IntType()),ParamDecl('c',FloatType()),ParamDecl('d',Id('Foo'))],Id('Bar'),Block([Return(BinaryOp('+',Id('a'),Id('b')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,328))

    # def test_break_continue_1(self):
    #     input = """func main() {for i<10 {break; continue;}; break;}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([ForBasic(BinaryOp('<',Id('i'),IntLiteral(10)),Block([Break(),Continue()])),Break()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,329))

    # def test_interface_decl_1(self):
    #     input = """type I interface {foo(a int) int;}"""
    #     expect = str(Program([InterfaceType('I',[Prototype('foo',[ParamDecl('a',IntType())],IntType())])]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,330))

    # def test_interface_decl_2(self):
    #     input = """type I interface {foo(a int) int; bar(b, c float, d Foo) Bar;}"""
    #     expect = str(Program([InterfaceType('I',[Prototype('foo',[ParamDecl('a',IntType())],IntType()),Prototype('bar',[ParamDecl('b',FloatType()),ParamDecl('c',FloatType()),ParamDecl('d',Id('Foo'))],Id('Bar'))])]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,331))

    # def test_struct_decl_1(self):
    #     input = """type Foo struct {a int; b float;}"""
    #     expect = str(Program([StructType('Foo',[('a',IntType()),('b',FloatType())],[])]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,332))

    # def test_struct_decl_2(self):
    #     input = """type Foo struct {a,b int; c float; d Foo;}"""
    #     expect = str(Program([StructType('Foo',[('a',IntType()),('b',IntType()),('c',FloatType()),('d',Id('Foo'))],[])]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,333))

    # def test_struct_lit_decl_1(self):
    #     input = """var x = Foo{a:1, b:2.0};"""
    #     expect = str(Program([VarDecl('x',Id('Foo'),StructLiteral('Foo',[('a',IntLiteral(1)),('b',FloatLiteral(2.0))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,334))

    # def test_struct_lit_decl_2(self):
    #     input = """var x = Bar{a:1, b:2.0, c:Foo{a:1, b:2.0}};"""
    #     expect = str(Program([VarDecl('x',Id('Bar'),StructLiteral('Bar',[('a',IntLiteral(1)),('b',FloatLiteral(2.0)),('c',StructLiteral('Foo',[('a',IntLiteral(1)),('b',FloatLiteral(2.0))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))

    # def test_func_call_2(self):
    #     input = """const foo = bar(1)"""
    #     expect = str(Program([ConstDecl('foo',None,FuncCall('bar',[IntLiteral(1)]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,336))

    # def test_meth_decl_1(self):
    #     input = """func (a Foo) bar(b int) int {return 0;}"""
    #     expect = str(Program([MethodDecl('a',Id('Foo'),FuncDecl('bar',[ParamDecl('b',IntType())],IntType(),Block([Return(IntLiteral(0))])))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,337))

    # def test_meth_decl_2(self):
    #     input = """func (a Foo) bar(b int, c Bar) Foo {return a+b;}"""
    #     expect = str(Program([MethodDecl('a',Id('Foo'),FuncDecl('bar',[ParamDecl('b',IntType()),ParamDecl('c',Id('Bar'))],Id('Foo'),Block([Return(BinaryOp('+',Id('a'),Id('b')))])))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,338))

    # def test_tank_1(self):
    #     input = """func main() {abc.x.y.z[3].t[10][2][5] = 1;}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(FieldAccess(FieldAccess(Id('abc'),'x'),'y'),'z'),[IntLiteral(3)]),'t'),[IntLiteral(10),IntLiteral(2),IntLiteral(5)]),IntLiteral(1))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,339))

    # def test_tank_3(self):
    #     input = """func main() {abc.x.y.z[3].t[10][2][5] = ":))" + foo[1].bar.code(a, b).baz[mez().conz().chauz];}"""
    #     expect = str(Program([FuncDecl('main',[],VoidType(),Block([Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(FieldAccess(FieldAccess(Id('abc'),'x'),'y'),'z'),[IntLiteral(3)]),'t'),[IntLiteral(10),IntLiteral(2),IntLiteral(5)]),BinaryOp('+',StringLiteral("\":))\""),ArrayCell(FieldAccess(MethCall(FieldAccess(ArrayCell(Id('foo'),[IntLiteral(1)]),'bar'),'code',[Id('a'),Id('b')]),'baz'),[FieldAccess(MethCall(FuncCall('mez',[]),'conz',[]),'chauz')])))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,340))
   
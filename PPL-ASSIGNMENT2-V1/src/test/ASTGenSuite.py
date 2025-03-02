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
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

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

    def test_interface_declare_21(self):
        input = """
        type book interface {
            area() float;
            perimeter() float;
        };"""
        expect = str(Program([
            InterfaceType(
                'book',
                [
                    Prototype('area',[],FloatType()),
                    Prototype('perimeter',[],FloatType())
                ]
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_22(self):
        input = """
        type shape interface {
            area(x, y int) float;
            perimeter(a, b float, c int) float;
            draw() string;
        };"""
        expect = str(Program([
            InterfaceType(
                'shape',
                [
                    Prototype('area',[IntType(), IntType()],FloatType()),
                    Prototype('perimeter',[FloatType(), FloatType(), IntType()],FloatType()),
                    Prototype('draw',[],StringType())
                ]
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_23(self):
        input = """
        type animal interface {
            eat(x [20]int, y [id345]float) string;
            sleep() string;
            makeSound() string;
        };"""
        expect = str(Program([
            InterfaceType(
                'animal',
                [
                    Prototype('eat',[ArrayType([IntLiteral(20)],IntType()),ArrayType([Id('id345')],FloatType())],StringType()),
                    Prototype('sleep',[],StringType()),
                    Prototype('makeSound',[],StringType())
                ]
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_24(self):
        input = """
        type vehicle interface {
            move(x, y float) string;
            stop() string;
            honk() string;
        };"""
        expect = str(Program([
            InterfaceType(
                'vehicle',
                [
                    Prototype('move',[FloatType(), FloatType()],StringType()),
                    Prototype('stop',[],StringType()),
                    Prototype('honk',[],StringType())
                ]
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_25(self):
        input = """
        type database interface {
        connect(host string, port int) boolean;
        query(sql string) [100]Record;
        disconnect() boolean;
        };"""
        expect = str(Program([
        InterfaceType(
            'database',
            [
                Prototype('connect', [StringType(), IntType()], BoolType()),
                Prototype('query', [StringType()], ArrayType([IntLiteral(100)], Id('Record'))),
                Prototype('disconnect', [], BoolType())
            ]
        )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_26(self):
        input = """
        type composite interface {
        add(component Component) Component;
        remove(id string) boolean;
        getChild(index int) Component;
        };"""
        expect = str(Program([
        InterfaceType(
            'composite',
            [
                Prototype('add', [Id('Component')], Id('Component')),
                Prototype('remove', [StringType()], BoolType()),
                Prototype('getChild', [IntType()], Id('Component'))
            ]
        )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_27(self):
        input = """
        type collection interface {
            iterator() Iterator;
            add(item Object) boolean;
            size() int;
            get(index int) Object;
            remove(index int) Object;
        };"""
        expect = str(Program([
        InterfaceType(
            'collection',
            [
                Prototype('iterator', [], Id('Iterator')),
                Prototype('add', [Id('Object')], BoolType()),
                Prototype('size', [], IntType()),
                Prototype('get', [IntType()], Id('Object')),
                Prototype('remove', [IntType()], Id('Object'))
            ]
        )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_28(self):
        input = """
        type matrix interface {
        getElement(row, col int) float;
        setElement(row, col int, value float) boolean;
        transpose() [10][10]float;
        determinant() float;
        };"""
        expect = str(Program([
        InterfaceType(
            'matrix',
            [
                Prototype('getElement', [IntType(), IntType()], FloatType()),
                Prototype('setElement', [IntType(), IntType(), FloatType()], BoolType()),
                Prototype('transpose', [], ArrayType([IntLiteral(10), IntLiteral(10)], FloatType())),
                Prototype('determinant', [], FloatType())
            ]
        )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_interface_declare_29(self):
        input = """
        type serializable interface {
        serialize() string;
        deserialize(data string) boolean;
        validate() boolean;
        getVersion() string;
        };"""
        expect = str(Program([
        InterfaceType(
            'serializable',
            [
                Prototype('serialize', [], StringType()),
                Prototype('deserialize', [StringType()], BoolType()),
                Prototype('validate', [], BoolType()),
                Prototype('getVersion', [], StringType())
            ]
        )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))
    
    def test_struct_interface_30(self):
        input = """
        type Address struct {
            street string;
            city string;
            zipCode int;
        };

        type Person struct {
            name string;
            age int;
            homeAddress Address;
            workAddress Address;
            employed boolean;
        };

        type Printable interface {
            toString() string;
            format(style string) string;
            print();
        };

        type PersonManager interface {
            addPerson(p Person) boolean;
            findPerson(name string) Person;
            updateAddress(person Person, newAddress Address) boolean;
            listEmployed() [100]Person;
            countPeople() int;
        };
        """
        expect = str(Program([
            StructType(
                'Address',
                [
                    ('street', StringType()),
                    ('city', StringType()),
                    ('zipCode', IntType())
                ],
                []
            ),
            StructType(
                'Person',
                [
                    ('name', StringType()),
                    ('age', IntType()),
                    ('homeAddress', Id('Address')),
                    ('workAddress', Id('Address')),
                    ('employed', BoolType())
                ],
                []
            ),
            InterfaceType(
                'Printable',
                [
                    Prototype('toString', [], StringType()),
                    Prototype('format', [StringType()], StringType()),
                    Prototype('print', [], VoidType())
                ]
            ),
            InterfaceType(
                'PersonManager',
                [
                    Prototype('addPerson', [Id('Person')], BoolType()),
                    Prototype('findPerson', [StringType()], Id('Person')),
                    Prototype('updateAddress', [Id('Person'), Id('Address')], BoolType()),
                    Prototype('listEmployed', [], ArrayType([IntLiteral(100)], Id('Person'))),
                    Prototype('countPeople', [], IntType())
                ]
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_31(self):
        input = """func (r Rectangle) area() float {
            return r.width * r.height;
        };"""
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

    def test_method_declare_32(self):
        input = """func (c Circle) diameter() float {
            return 2 * 3.14 * c.radius;
        };"""
        expect = str(Program([
            MethodDecl(
                'c', 
                Id('Circle'),
                FuncDecl(
                    'diameter',
                    [],
                    FloatType(),
                    Block([
                        Return(
                            BinaryOp(
                                '*',
                                BinaryOp(
                                    '*',
                                    IntLiteral(2),
                                    FloatLiteral(3.14)
                                ),
                                FieldAccess(Id('c'), 'radius')
                            )
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_33(self):
        input = """func (p Person) fullName() string {
            return p.firstName + " " + p.lastName;
        };"""
        expect = str(Program([
            MethodDecl(
                'p', 
                Id('Person'),
                FuncDecl(
                    'fullName',
                    [],
                    StringType(),
                    Block([
                        Return(
                            BinaryOp(
                                '+',
                                BinaryOp(
                                    '+',
                                    FieldAccess(Id('p'), 'firstName'),
                                    StringLiteral('" "')
                                ),
                                FieldAccess(Id('p'), 'lastName')
                            )
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_34(self):
        input = """func (a Account) withdraw(amount float) boolean {
            if (a.balance >= amount) {
                a.balance := a.balance - amount;
                return true;
            }
            return false;
        };"""
        expect = str(Program([
            MethodDecl(
                'a', 
                Id('Account'),
                FuncDecl(
                    'withdraw',
                    [ParamDecl('amount', FloatType())],
                    BoolType(),
                    Block([
                        If(
                            BinaryOp('>=', FieldAccess(Id('a'), 'balance'), Id('amount')),
                            Block([
                                Assign(
                                    FieldAccess(Id('a'), 'balance'),
                                    BinaryOp('-', FieldAccess(Id('a'), 'balance'), Id('amount'))
                                ),
                                Return(BooleanLiteral(True))
                            ]),
                            None
                        ),
                        Return(BooleanLiteral(False))
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_35(self):
        input = """func (s Student) isPassingGrade(subject string) boolean {
            var grade = s.grades[subject];
            return grade >= 60;
        };"""
        expect = str(Program([
            MethodDecl(
                's', 
                Id('Student'),
                FuncDecl(
                    'isPassingGrade',
                    [ParamDecl('subject', StringType())],
                    BoolType(),
                    Block([
                        VarDecl(
                            'grade',
                            None,
                            ArrayCell(
                                FieldAccess(Id('s'), 'grades'),
                                [Id('subject')]
                            )
                        ),
                        Return(
                            BinaryOp('>=', Id('grade'), IntLiteral(60))
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_36(self):
        input = """func (m Matrix) getElement(row int, col int) float {
            return m.data[row][col];
        };"""
        expect = str(Program([
            MethodDecl(
                'm', 
                Id('Matrix'),
                FuncDecl(
                    'getElement',
                    [ParamDecl('row', IntType()), ParamDecl('col', IntType())],
                    FloatType(),
                    Block([
                        Return(
                            ArrayCell(
                                FieldAccess(Id('m'), 'data'),
                                [Id('row'), Id('col')]
                            )
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_37(self):
        input = """func (c Car) startEngine() {
            c.engine.start();
            c.fuelLevel := c.fuelLevel - 0.1;
            c.status := "running";
        };"""
        expect = str(Program([
            MethodDecl(
                'c', 
                Id('Car'),
                FuncDecl(
                    'startEngine',
                    [],
                    VoidType(),
                    Block([
                        MethCall(
                            FieldAccess(Id('c'), 'engine'),
                            'start',
                            []
                        ),
                        Assign(
                            FieldAccess(Id('c'), 'fuelLevel'),
                            BinaryOp('-', FieldAccess(Id('c'), 'fuelLevel'), FloatLiteral(0.1))
                        ),
                        Assign(
                            FieldAccess(Id('c'), 'status'),
                            StringLiteral('"running"')
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_38(self):
        input = """func (s ShoppingCart) calculateTotal() float {
            var total = 0.5;
            for i := 0; i < s.itemCount; i := i + 1 {
                total := total + (s.items[i].price * s.items[i].quantity);
            }
            if (s.hasDiscount) {
                total := total * 0.9;
            }
            return total;
        };"""
        expect = str(Program([
            MethodDecl(
                's', 
                Id('ShoppingCart'),
                FuncDecl(
                    'calculateTotal',
                    [],
                    FloatType(),
                    Block([
                        VarDecl('total', None, FloatLiteral(0.5)),
                        ForStep(
                            Assign(Id('i'), IntLiteral(0)),
                            BinaryOp('<', Id('i'), FieldAccess(Id('s'), 'itemCount')),
                            Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                            Block([
                                Assign(
                                    Id('total'),
                                    BinaryOp(
                                        '+',
                                        Id('total'),
                                        BinaryOp(
                                            '*',
                                            FieldAccess(
                                                ArrayCell(FieldAccess(Id('s'), 'items'), [Id('i')]),
                                                'price'
                                            ),
                                            FieldAccess(
                                                ArrayCell(FieldAccess(Id('s'), 'items'), [Id('i')]),
                                                'quantity'
                                            )
                                        )
                                    )
                                )
                            ])
                        ),
                        If(
                            FieldAccess(Id('s'), 'hasDiscount'),
                            Block([
                                Assign(
                                    Id('total'),
                                    BinaryOp('*', Id('total'), FloatLiteral(0.9))
                                )
                            ]),
                            None
                        ),
                        Return(Id('total'))
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_39(self):
        input = """func (t Triangle) isValid() boolean {
            return (t.a + t.b > t.c) && (t.a + t.c > t.b) && (t.b + t.c > t.a);
        };"""
        expect = str(Program([
            MethodDecl(
                't', 
                Id('Triangle'),
                FuncDecl(
                    'isValid',
                    [],
                    BoolType(),
                    Block([
                        Return(
                            BinaryOp(
                                '&&',
                                BinaryOp(
                                    '&&',
                                    BinaryOp(
                                        '>',
                                        BinaryOp(
                                            '+',
                                            FieldAccess(Id('t'), 'a'),
                                            FieldAccess(Id('t'), 'b')
                                        ),
                                        FieldAccess(Id('t'), 'c')
                                    ),
                                    BinaryOp(
                                        '>',
                                        BinaryOp(
                                            '+',
                                            FieldAccess(Id('t'), 'a'),
                                            FieldAccess(Id('t'), 'c')
                                        ),
                                        FieldAccess(Id('t'), 'b')
                                    )
                                ),
                                BinaryOp(
                                    '>',
                                    BinaryOp(
                                        '+',
                                        FieldAccess(Id('t'), 'b'),
                                        FieldAccess(Id('t'), 'c')
                                    ),
                                    FieldAccess(Id('t'), 'a')
                                )
                            )
                        )
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))

    def test_method_declare_40(self):
        input = """func (node TreeNode) traverseInOrder() [100]int {
            var result [100]int;
            var index = 0;
            
            if (node.left != nil) {
                var leftResult = node.left.traverseInOrder();
                for i := 0; i < leftResult.length; i := i + 1 {
                    result[index] := leftResult[i];
                    index := index + 1;
                }
            }
            
            result[index] := node.value;
            index := index + 1;
            
            if (node.right != nil) {
                var rightResult = node.right.traverseInOrder();
                for i := 0; i < rightResult.length; i := i + 1 {
                    result[index] := rightResult[i];
                    index := index + 1;
                }
            }
            
            return;
        };"""
        expect = str(Program([
            MethodDecl(
                'node', 
                Id('TreeNode'),
                FuncDecl(
                    'traverseInOrder',
                    [],
                    ArrayType([IntLiteral(100)], IntType()),
                    Block([
                        VarDecl('result', ArrayType([IntLiteral(100)], IntType()), None),
                        VarDecl('index', None, IntLiteral(0)),
                        
                        If(
                            BinaryOp('!=', FieldAccess(Id('node'), 'left'), NilLiteral()),
                            Block([
                                VarDecl(
                                    'leftResult',
                                    None,
                                    MethCall(
                                        FieldAccess(Id('node'), 'left'),
                                        'traverseInOrder',
                                        []
                                    )
                                ),
                                ForStep(
                                    Assign(Id('i'), IntLiteral(0)),
                                    BinaryOp('<', Id('i'), FieldAccess(Id('leftResult'), 'length')),
                                    Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                    Block([
                                        Assign(
                                            ArrayCell(Id('result'), [Id('index')]),
                                            ArrayCell(Id('leftResult'), [Id('i')])
                                        ),
                                        Assign(
                                            Id('index'),
                                            BinaryOp('+', Id('index'), IntLiteral(1))
                                        )
                                    ])
                                )
                            ]),
                            None
                        ),
                        
                        Assign(
                            ArrayCell(Id('result'), [Id('index')]),
                            FieldAccess(Id('node'), 'value')
                        ),
                        Assign(
                            Id('index'),
                            BinaryOp('+', Id('index'), IntLiteral(1))
                        ),
                        
                        If(
                            BinaryOp('!=', FieldAccess(Id('node'), 'right'), NilLiteral()),
                            Block([
                                VarDecl(
                                    'rightResult',
                                    None,
                                    MethCall(
                                        FieldAccess(Id('node'), 'right'),
                                        'traverseInOrder',
                                        []
                                    )
                                ),
                                ForStep(
                                    Assign(Id('i'), IntLiteral(0)),
                                    BinaryOp('<', Id('i'), FieldAccess(Id('rightResult'), 'length')),
                                    Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1))),
                                    Block([
                                        Assign(
                                            ArrayCell(Id('result'), [Id('index')]),
                                            ArrayCell(Id('rightResult'), [Id('i')])
                                        ),
                                        Assign(
                                            Id('index'),
                                            BinaryOp('+', Id('index'), IntLiteral(1))
                                        )
                                    ])
                                )
                            ]),
                            None
                        ),
                        
                        Return(None)
                    ])
                )
            )
        ]))
        ASTGenSuite.test_count += 1
        self.assertTrue(TestAST.checkASTGen(input, expect, ASTGenSuite.test_count))
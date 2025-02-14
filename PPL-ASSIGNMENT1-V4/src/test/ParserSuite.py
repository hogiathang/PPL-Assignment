import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def testcase_206(self):
        input = """
            type Address struct {
                street string;
                city   string;
            }

            type Person struct {
                name    string;
                age     int;
                address Address;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def testcase_207(self):
        input = """
            type Address struct {
                street string;
                city   string;
            }

            type Person struct {
                name    string;
                age     int;
                address Address;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def testcase_208(self):
        input = """
            type Outer struct {
                field1 int;
                type Inner struct {  // Not allowed
                    field2 string;
                };
            }
        """
        expect = "Error on line 4 col 17: type"
        self.assertTrue(TestParser.checkParser(input, expect, 208))
    
    def testcase_209(self):
        input = """
            manager := ShapeManager{
            id: 1,
            name: "Manager",
            coordinates: [5]Point{{0,0}, {1,1}, {2,2}, {3,3}, {4,4}},
            active: true,
            drawer: Circle{center: Point{x: 10, y: 20}, radius: 5.0},
            metadata: Metadata{
                createdBy: "John Doe",
                version: 1.0,
            },
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def testcase_209(self):
        input = """
        manager := ShapeManager{
            id: 1,
            name: "Manager",
            coordinates: [5]Point{{0,0}, {1,1}, {2,2}, {3,3}, {4,4}},
            active: true,
            drawer: Circle{center: Point{x: 10, y: 20}, radius: 5.0},
            metadata: struct {
                createdBy string
                version float
            } {
                createdBy: "John Doe",
                version: 1.0,   
            },
        };
        """
        expect = "Error on line 8 col 23: struct"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def testcase_210(self):
        input = """
        p := Person{}
        PutStringLn(p.name) // Output: Alice
        PutIntLn(p.age) // Output: 30
        var people []Person
        const Greeting = "Hello, MiniGo!"
        const MaxSize = 100 + 50;
        const Pi = 3.14;
        testPerson.people.aiw(people).lost.pole(3)
        
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))
    def testcase_211(self):
        input = """
        func Add(x int, y int) int {
            return x + y;
        }
             type Calculator struct {
            value int;
            }
            
            func (c Calculator) Add(x int) int {
            c.value += x;
            return c.value;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def testcase_212(self):
        input = """
        if (x > 10) {
            println("x is greater than 10")
        } else if (x < 10) {
            println("x is less than 10")
        } else {
            println("x is equal to 10")
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    
    def testcase_213(self):
        input = """
        for condition {
            // statements
        }
        for i < 10 {
            // loop body
        }
        for i := 0; i < 10; i += 1 {
            // loop body
        }
                    for index, value := range array {
            // statements
            }      arr := [3]int{10, 20, 30}
            for index, value := range arr {
            // index: 0, 1, 2
            // value: 10, 20, 30
            }
"""
        expect = "Error on line 4 col 9: }"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    
    def testcase_214(self):
        input = """
        a[2][3] := b[2] + 1;
        person.name := "John";
        person.age := 30;
        arr := [3]int{10, 20, 30}
        marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        p := Person{name: "Alice", age: 30}
        q := Person{}
        add(3, 4)
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def testcase_215(self):
        input = """
        arr := [3]int{10, 20, 30}
        for _, value := range arr {
            // value: 10, 20, 30
            modify(value)
        }
        
        for i := 0; i < 10; i+=1 {
        
            if (i == 5) {
                break;
            }
            // other statements
        }
        
        for i := 0; i < 10; i+=1 {
            if (i == 5) {
                continue;
            }
            // statements that will not execute when i == 5
        }// Errorr
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))
    def testcase_216(self):
        input = """
        foo(2 + x, 4 / y); m.goo();
        func foo(x int, y int) {
        }; func goo() {
        } func (c Test) goo() {
        }; func (c Test) goo() int {
        }"""
        expect = "Error on line 5 col 11: func"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def testcase_217(self):
        input = """
        {}"""
        expect = "Error on line 2 col 10: }"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def testcase_218(self):
        input = """x := true.x;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def testcase_219(self):
        input = """
            for index, value := range arr {
                for _, v := range pointer {
                    println(v);
                }

                for i := 0; i < 10; i += 1 {
                    println(i);

                    if (i == 5) {
                        break;
                    } else if (i == 3) {
                        continue;
                    }
                    else {
                        println(i);
                    }
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def testcase_220(self):
        input = """
        type Address struct {
            street string;
            city   string;
        }

        type DateCreated struct {
            day   int;
            month int;
            year  int;
        }

        type Account struct {
            username string;
            password string;
            address Address;
            created DateCreated;
        }

        func (a Account) GetUsername() string {
            return a.username;
        }

        func (a Account) GetPassword() string {
            return a.password;
        }

        func (a Account) GetAddress() Address {
            return a.address;
        }

        func (a Account) GetCreated() DateCreated {
            return a.created;
        }

        func (a Account) SetUsername(username string) {
            a.username := username;
        }

        func (a Account) CopyAnInstance(b Account) {
            a.username := b.username;
            a.password := b.password;
            a.address := b.address;
            a.created := b.created;
        }

        func foo() {
            a := Account{
                username: "John Doe",
                password: "123456",
                address: Address{
                    street: "123 Main St",
                    city: "New York",
                },
                created: DateCreated{
                    day: 1,
                    month: 1,
                    year: 2020,
                },
            };

            b := Account{};
            b.CopyAnInstance(a);
            b.SetUsername("Jane Doe");
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 220))
    
    def test_logic_expression_221(self):
        input = """
        func main() {
            var x boolean
            x := (true && false) || (true || false) && !true
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_logic_expression_222(self):
        input = """
        func main() {
            var x boolean;
            x := -x || !x && x;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_array_expression_223(self):
        input = """
        func main() {
            arr := [3]int{1,2,3}
            arr[0] := 5;
            arr[1] := arr[0] + 5;
            arr[2] := arr[1] + arr[0];

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    
    def test_struct_expression_224(self):
        input = """
        type Point struct { x int; y int; };
        func main() {
            var p Point;
            p.x := 5;
            p.y := 6;
            p.z := (p.x * p.x + p.y * p.y) % 2 + foo(a, b) == 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_if_null_expression_225(self):
        input = """
        func main() {
            var x int;
            if x == nil {
            } else {
                return;
            }
        }
        """
        expect = "Error on line 5 col 13: }"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_nested_functioncall_226(self):
        input = """
        func (p Person) Greet() string {
            return "Hello, " + p.getName + "!" + "from" + p.GetAddress().city;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_nested_functionl_227(self):
        input = """
        func (p Person) Greet() string {
            str := "Hello, " + p.getName + "!" + "from" + p.GetAddress().city;

            k := func hello() string {
                return "Hello";
            }

            return str + k();
        }
        """
        expect = "Error on line 5 col 18: func"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_nested_array_228(self):
        input = """
        var matrix [2][3]int = {{1, 2, 3}, {4, 5, 6}};
        var matrix2 [1]int = {1};
        arr2 := [1]int{1};
        arr := [2][3]int{{1, 2, 3}, {4, 5, 6}};
        putIntLn(matrix[1][2]);  // In ra 6
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    


    
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
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def testcase_207(self):
        input = """
            type Outer struct {
                field1 int;
                type Inner struct {  // Not allowed
                    field2 string;
                };
            }
        """
        expect = "Error on line 4 col 17: type"
        self.assertTrue(TestParser.checkParser(input, expect, 207))
    
    def testcase_208(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 208))

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
        expect = "Error on line 13 col 20: arr"
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
        """
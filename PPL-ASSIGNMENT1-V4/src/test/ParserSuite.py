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
        testPerson.people.aiw(people).lost.pole(3)
        if (x > 10) {
            println("x is greater than 10")
        } else if (x < 10) {
            println("x is less than 10")
        } else {
            println("x is equal to 10")
        }
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))
    
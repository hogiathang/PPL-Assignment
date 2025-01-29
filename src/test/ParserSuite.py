import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_201(self):
        """Simple program: void main() {} """
        input = """func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program_202(self):
        """More complex program"""
        input = """func foo () {
            var a int;
            a := 1;
            print(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_global_declaration_before_main_203(self):
        """Global variable before main"""
        input = """var x int = 5;
                   func main() { putInt(x); }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_struct_declaration_204(self):
        """Struct type declaration"""
        input = """type Point struct { x int; y int; };
                   func main() { var p Point; }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_if_else_statement_205(self):
        """If-else control structure"""
        input = """func main() {
                    if (x > 0) {
                        putString("Positive");
                    } else {
                        putString("Non-positive");
                    }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_invalid_missing_main_206(self):
        """Program without main function"""
        input = """var x = 10;
                   func helper() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_array_declaration_207(self):
        """Multidimensional array declaration"""
        input = """func main() {
                    var matrix [2][3]int;
                    matrix[1][2] := 5;
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_invalid_identifier_208(self):
        """Variable name starting with digit"""
        input = """func main() { var 2var int; }"""
        expect = "Error on line 1 col 19: 2"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_for_loop_range_209(self):
        """For loop with range iteration"""
        input = """func main() {
                    arr := [3]int{1,2,3}
                    for idx, val := range arr {
                        putIntLn(val);
                    }
                   }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_interface_declaration_210(self):
        """Interface with method signatures"""
        input = """type Shape interface {
                     area() float;
                     perimeter() float;
                   }
                   func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_structural_211(self):
        """Struct literal missing required field"""
        input = """type Person struct {name string; age int;}
                   func main() { p := Person{age: 30}; }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_nested_comments_212(self):
        """Nested multi-line comments"""
        input = """/* Outer /* Inner */ comment */
                   func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_method_declaration_213(self):
        """Method with struct receiver"""
        input = """ type Counter struct { value int; }
                    func (c Counter) increment() { c.value+=1; }
                    func main() {}
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_invalid_operator_precedence_214(self):
        """Malformed expression with operator"""
        input = """func main() { x := 5 + * 3; }"""
        expect = "Error on line 1 col 24: *"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_constant_declaration_215(self):
        """Global constant declaration"""
        input = """const MAX_SIZE = 100;
                   func main() { putInt(MAX_SIZE); }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_invalid_seperator_216(self):
        """Newline instead of semicolon"""
        input = """func main() {
            var x int var y float
            x := 10
            putInt(x)
        }"""
        expect = "Error on line 2 col 23: var"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_mixed_newline_and_semicolon_217(self):
        """Mixed semicolon and newline"""
        input = """func main() {
            var x int; var y float; var z boolean = true
            x := 10
            putInt(x)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
    
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: void main() {} """
    #     input = """func main() {}"""
    #     expect = "successfull"
    #     self.assertTrue(TestParser.checkParser(input,expect,201))

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
    def test_function(self):
        print("-----------------------Test 206----------------------------------")
        input = """
            func main() {
                var a int var b float var c string
                a := 1
                print(a)
                for i := 0; i < 10; i += 1 {
                    print(i);
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_function(self):
        print("-----------------------Test 207----------------------------------")
        input = """
            func foo() {
            }; foo();
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_type_def(self):
        print("-----------------------Test 208----------------------------------")
        input = """
            func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))
    
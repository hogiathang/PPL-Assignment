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
    
    def test_if_statement_218(self):
        """If statement missing '('"""
        input = """func main() { if (x > 10) { }; return;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))
    
    def test_missing_return_value_219(self):
        """Missing return value in function with return type"""
        input = """
        func add(x int, y int) int {
            var mutexArr[3][3] int;
            var mutexArr[0x44][0x77] int;
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_a_valid_function_220(self):
        """A valid function"""
        input = """
        func quicksort(arr [3]int) [3]int {
            if len(arr) < 2 {
                return arr;
            }
            pivot := arr[0]; /*
            var less, greater [3]int;
            for _, val := range arr[1:] {
                if val <= pivot {
                    less = append(less, val);
                } else {
                    greater = append(greater, val);
                }
            }
            return append(append(quicksort(less), pivot), quicksort(greater)); */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_expression_221(self):
        input = """
        func main() {
            var x int
            x := 5 + 6 * 7 - (8 / 9) - 3 % 4
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_logic_expression_222(self):
        input = """
        func main() {
            var x boolean
            x := (true && false) || (true || false) && !true
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_logic_expression_223(self):
        input = """
        func main() {
            var x boolean;
            x := -x || !x && x;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_array_expression_224(self):
        input = """
        func main() {
            x := [3]int{4};
            x[0] := 5;
            x[1] := x[0] + 5;
            x[2] := x[1] + x[0];

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))
    
    def test_struct_expression_225(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_quicksort_226(self):
        input = """
        func partition(arr[3] int, low int, high int) int {
            pivot := arr[high]
            i := low - 1
            for j := low; j < high; j+=1 {
                if arr[j] < pivot {
                    i+=1
                    arr[i], arr[j] := arr[j], arr[i]
                }
            }
            arr[i + 1], arr[high] := arr[high], arr[i + 1]
            return i + 1
        }

        func quickSort(arr[3] int, low int, high int) {
            if low < high {
                pi := partition(arr, low, high)
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)
            }
        }
        
        func main() {
            var arr[3] int
            var n int
            n := len(arr)
            quickSort(arr, 0, n - 1)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_merge_sort_227(self):
        input = """
        func merge(arr[3] int, l int, m int, r int) {
            n1 := m - l + 1
            n2 := r - m
            var L[3] int
            var R[3] int
            for i := 0; i < n1; i+=1 {
                L[i] := arr[l + i]
            }
            for j := 0; j < n2; j+=1 {
                R[j] := arr[m + 1 + j]
            }
            i := 0
            j := 0
            k := l 
            for i < n1 && j < n2 {
                if L[i] <= R[j] {
                    arr[k] := L[i]
                    i+=1
                } else {
                    arr[k] := R[j]
                    j+=1
                }
                k+=1;
            }
            for i < n1 {
                arr[k] := L[i]
                i+=1
                k+=1
            }
            for j < n2 {
                arr[k] := R[j]
                j+=1
                k+=1
            }
        }
        
        func mergeSort(arr[3] int, l int, r int) {
            if l < r {
                m := l + (r - l) / 2
                mergeSort(arr, l, m)
                mergeSort(arr, m + 1, r)
                merge(arr, l, m, r)
            }
        }

        func main() {
            var arr[3] int
            var n int
            n := len(arr)
            mergeSort(arr, 0, n - 1)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_function_return_array_228(self):
        """Function returning an array"""
        input = """
        func getNumbers() [5]int {
            return [5]int{1,2,3,4,5};
        }
        func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229(self):
        input = """
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_variable_shadowing_230(self):
        """Variable shadowing in nested scope"""
        input = """
        func main() {
            var x int = 10;
            {
                var x float = 5.5;
                putFloat(x);
            }
            {
                var x string = "Hello";
                putString(x);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
    
    def test_struct_with_array_231(self):
        """Struct containing an array field"""
        input = """
        type Matrix struct {
            data [3][3]float;
        }
        func main() {
            var m Matrix;
            m.data[0][0] := 1.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_nested_struct_232(self):
        input = """
        type Point struct {
            x int;
            y int;
        }
        type Circle struct {
            center Point;
            radius float;
        }
        func main() {
            var c Circle;
            c.center.x := 1;
            c.center.y := 2;
            c.radius := 3.0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))
    
    def test_keyword_as_identifier_233(self):
        """Using 'if' as a variable name"""
        input = """func main() { var if int = 5; }"""
        expect = "Error on line 1 col 19: if"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_unterminated_comment_234(self):
        """Unterminated multi-line comment"""
        input = """/* This comment is not closed
        func main() {}"""
        expect = "Error on line 1 col 1: /"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_method_multiple_params_235(self):
        """Method with multiple parameters"""
        input = """
        type Counter struct { value int; }
        func (c Counter) add(x int, y int) int {
            return x + y + c.value;
        }
        func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_interface_multiple_methods_236(self):
        """Interface with multiple methods"""
        input = """
        type Writer interface {
            write(data string) int;
            close();
        }
        func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236)) 

    def test_interface_struct(self):
        input = """
        type Drawable interface {
            Draw() string;
        }

        type Point struct {
            x int;
            y int;
        }

        type Circle struct {
            center Point;
            radius float;
        }

        func (c Circle) Draw() string {
            return "Drawing circle at (" + toString(c.center.x) + "," + toString(c.center.y) + ")";
        }
    
        type ShapeManager struct {
            id int;                  
            name string;             
            coordinates [5]Point;    
            active bool;             
            drawer Drawable;         
            metadata struct {createdBy string;version float;};
        }
        
        func main() {
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
            putStringLn(manager.name);                  
            putStringLn(manager.drawer.Draw());       
            putBoolLn(manager.coordinates[2].x == 2);
            arr := [3][3] int {1,2,3}
            attr().attr := 5;
            test.test[2][3].test().find();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_error_sample_238(self):
        input = """
            var t int
            
            func (c c) Add(x int) {}
                                        
            func Add(x int) {} var c int;
                                        
            var c int; type Calculator struct{} type Calculator struct{} var c int;
        """
        expect = "Error on line 8 col 49: type"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_if_sample_239(self):
        input = """
            func main() {
                if (a > 10) {
                    print("Bigger");
                } 
                else if (a == 10) {
                    print("Same")
                }; else {
                    print("Less")
                }

            }
        """
        expect = "Error on line 8 col 20: else"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_sample_240(self):
        input = """
            type Color interface {
                getColor() string
                setColor(s string)
            }
            type Car struct {
                color string
            }
            func (c Car) getColor() string {
                return c.color
            }
            func (c Car) setColor(s string) {
                c.color := s
            }

            func main() {
                car := Car{color: "white"}
                col := Color(car)
                car := col(Car)         // L(1)
                car.setColor("yellow")
                fmt.Println(col)        // L(2)
                fmt.Println(car)
                car.color := "black"
                fmt.Println(col)        // L(3)
                fmt.Println(car)
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
    
    def test_interface_struct_241(self):
        input = """
        type Drawable interface {
            Draw() string;
        }

        type Point struct {
            x int;
            y int;
        }

        type Circle struct {
            center Point;
            radius float;
        }

        func (c Circle) Draw() string {
            return "Drawing circle at (" + toString(c.center.x) + "," + toString(c.center.y) + ")";
        }
    
        type MetaData struct {
            createdBy string;
            version float;
        }

        type ShapeManager struct {
            id int;                  
            name string;             
            coordinates [5]Point;    
            active bool;             
            drawer Drawable;         
            metadata MetaData;
        }
        
        func main() {
            manager := ShapeManager{
                id: 1,
                name: "Manager",
                coordinates: [5]Point{{0,0}, {1,1}, {2,2}, {3,3}, {4,4}},
                active: true,
                drawer: Circle{center: Point{x: 10, y: 20}, radius: 5.0},
                metadata: MetaData {
                    createdBy: "John Doe",
                    version: 1.0,
                },
            };
            putStringLn(manager.name);                  
            putStringLn(manager.drawer.Draw());       
            putBoolLn(manager.coordinates[2].x == 2);
            arr := [3][3] int {1,2,3}
            attr().attr := 5;
            test.test[2][3].test().find();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_interface_struct_242(self):
        input= """
        type Shape interface {
            Area() float
            Perimeter() float
        }

        type Rectangle struct {
            Width  float
            Height float
        }

        func (r Rectangle) Area() float {
            return r.Width * r.Height
        }

        func (r Rectangle) Perimeter() float {
            return 2 * (r.Width + r.Height)
        }

        type Circle struct {
            Radius float
        }

        func (c Circle) Area() float {
            return 3.14 * c.Radius * c.Radius
        }

        func (c Circle) Perimeter() float {
            return 2 * 3.14 * c.Radius
        }

        type Geometry struct {
            Name    string        // Primitive type (string)
            Sides   []int         // Array
            Shape   Shape         // Interface field
            Details Rectangle     // Nested struct
        }

        func main() {
            rect := Rectangle{Width: 10, Height: 5}

            geo1 := Geometry{
                Name:    "My Rectangle",
                Sides:   []int{10, 5, 10, 5},
                Shape:   rect,
                Details: rect,
            }

            fmt.Println("Geometry 1:", geo1.Name)
            fmt.Println("Area:", geo1.Shape.Area())
            fmt.Println("Perimeter:", geo1.Shape.Perimeter())

            circle := Circle{Radius: 7}

            geo2 := Geometry{
                Name:    "My Circle",
                Sides:   []int{1}, // Array
                Shape:   circle,
                Details: rect,   // Nested struct
            }

            fmt.Println("\nGeometry 2:", geo2.Name)
            fmt.Println("Area:", geo2.Shape.Area())
            fmt.Println("Perimeter:", geo2.Shape.Perimeter())
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))
        
    def test_parser_error_243(self):
        input = """
            func main() {
                if x > 10 {
                    putIntLn(x)
                else {
                    putIntLn(0);
                }
            }
        """
        expect = "Error on line 5 col 17: else"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_parser_error_244(self):
        input = """ 
        type Person struct {
            name string,
            age int;
        }
        """
        expect = "Error on line 3 col 24: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_parser_error_245(self):
        input = """ 
        arr := [3]int{10, 20, };
        """
        expect = "Error on line 2 col 9: arr"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    # def test_parser_error_246(self):
    #     input = """ 
    #     for i := 0; i < 10; i++ {
    #         putIntLn(i);
    #     }
    #     """
    #     expect = "Error on line 2 col 9: for"
    #     self.assertTrue(TestParser.checkParser(input, expect, 246))

    # def test_parser_error_247(self):
    #     input = """ 
    #     const Pi = 3.14
    #     """
    #     expect = "Error on line 2: Missing semicolon"
    #     self.assertTrue(TestParser.checkParser(input, expect, 247))

    # def test_parser_error_248(self):
    #     input = """ 
    #     func add(x int y int) int {
    #         return x + y;
    #     }
    #     """
    #     expect = "Error on line 2: y"
    #     self.assertTrue(TestParser.checkParser(input, expect, 248))

    # def test_parser_error_249(self):
    #     input = """ 
    #     type Calculator interface {
    #         Add(x int) int;
    #         Subtract(x, y int)
    #     }
    #     """
    #     expect = "Error on line 4: }"
    #     self.assertTrue(TestParser.checkParser(input, expect, 249))

    # def test_parser_error_250(self):
    #     input = """ 
    #     var x = 5
    #     x += 1;
    #     """
    #     expect = "Error on line 2: Missing semicolon"
    #     self.assertTrue(TestParser.checkParser(input, expect, 250))

    # def test_parser_error_251(self):
    #     input = """ 
    #     func main() {
    #         for i := 0; i < 10; i += {
    #             putIntLn(i);
    #         }
    #     }
    #     """
    #     expect = "Error on line 3: {"
    #     self.assertTrue(TestParser.checkParser(input, expect, 251))


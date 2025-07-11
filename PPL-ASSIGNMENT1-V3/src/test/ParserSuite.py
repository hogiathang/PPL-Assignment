import unittest
from TestUtils import TestParser
expect = "successful"
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

    def testcase_210(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def testcase_211(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 211))
    def testcase_212(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def testcase_213(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    
    def testcase_214(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 214))
    
    def testcase_215(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def testcase_216(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 216))
    def testcase_217(self):
        input = """
        foo(2 + x, 4 / y); m.goo();
        func foo(x int, y int) {
        }; func goo() {
        } func (c Test) goo() {
        }; func (c Test) goo() int {
        }"""
        expect = "Error on line 5 col 11: func"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def testcase_218(self):
        input = """
        {}"""
        expect = "Error on line 2 col 9: {"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def testcase_219(self):
        input = """x := true.x;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def testcase_220(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def testcase_221(self):
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
            arr := [3]int{1,2,3}
            arr[0] := 5;
            arr[1] := arr[0] + 5;
            arr[2] := arr[1] + arr[0];

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

    def test_if_null_expression_226(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_nested_functioncall_227(self):
        input = """
        func (p Person) Greet() string {
            return "Hello, " + p.getName + "!" + "from" + p.GetAddress().city;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_nested_functionl_228(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_nested_array_229(self):
        input = """
        var matrix [2][3]int = {{1, 2, 3}, {4, 5, 6}};
        var matrix2 [1]int = {1};
        arr2 := [1]int{1};
        arr := [2][3]int{{1, 2, 3}, {4, 5, 6}};
        putIntLn(matrix[1][2]);  // In ra 6
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_quicksort_230(self):
        input = """
        func partition(arr[] int, low int, high int) int {
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

        func quickSort(arr[] int, low int, high int) {
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
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_merge_sort_231(self):
        input = """
        func merge(arr[] int, l int, m int, r int) {
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
        
        func mergeSort(arr[] int, l int, r int) {
            if l < r {
                m := l + (r - l) / 2
                mergeSort(arr, l, m)
                mergeSort(arr, m + 1, r)
                merge(arr, l, m, r)
            }
        }

        func main() {
            var arr[] int
            var n int
            n := len(arr)
            mergeSort(arr, 0, n - 1)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
    
    def test_array(self):
        input = """var a = [2][2]int{{1, 2}, {3, 4}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_eol(self): 
        input = """var a int \nvar b int \r\nvar c int; var d int"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_wrong_eol(self): 
        input = """var a int var b int var c int"""
        expect = "Error on line 1 col 11: var"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_expression(self):
        input = """a := -(5 + 3 - 2) * 4 / 2 % 1 == true && false"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_function(self):
        input = """
        func foo(x int, y int) int {
            return x + -y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_if(self):
        input = """
        func main() {
            if (x > 0) {
                print("Positive");
            } else {
                print("Negative");
            }
        }"""
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_struct_var_decl(self):
        input = """
        func main() {
            var a = A{x: 1, y: 2}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_interface_decl(self):
        input = "type A interface { foo() int; }"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_multiple_eol(self):
        input = """
        func main() {
            ;
        }
        """
        expect = "Error on line 3 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_array_expr_size(self):
        input = """var a = [a+1-2%3 || 4 && 5][2 + a.test.funct().tar.pot]int{{1, 2}, {3, 4}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    # def test_vardecl_multi_1(self):
    #     input = """var a, b int;"""
    #     self.assertTrue(TestParser.checkParser(input,expect,228))

    # def test_vardecl_multi_2(self):
    #     input = """var a, b = 1, 2;"""
    #     self.assertTrue(TestParser.checkParser(input,expect,229))

    # def test_vardecl_multi_3(self):
    #     input = """var a, b int = 1, 2;"""
    #     self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_array_struct(self):
        input = """var a [2]A;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_tank_1(self):
        input = """func main() {
            abc.x.y.z[3].t[10][2][5] := 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_tank_2(self):
        input = """func main() {
            abc.x.y.z[3].t[10][2][5] := foo.baz() * bar.code();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_tank_3(self):
        input = """func main() {
            abc.x.y.z[3].t[10][2][5] := ":))" + foo[1].bar.code(a, b).baz[mez().conz().chauz]
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_interface_2(self):
        input = """type empty interface {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_interface_3(self):
        input = """type empty interface {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_interface_4(self):
        input = """type Comparable interface {
            compare(other interface) int;
        }"""
        expect = "Error on line 2 col 27: interface"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_interface_7(self):
        input = """type Complex interface {
            getValue() [2]float;
            setValue(real, imag float);
            toString() string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_interface_8(self):
        input = """type Container interface {
            push(element [3]Point);
            pop() [3]Point;
            isEmpty() bool;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_interface_9(self):
        input = """type Animal interface {
            makeSound() string;
            move(distance float);
            getSpecies() string;
            age() int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_interface_10(self):
        input = """type Database interface {
            connect(host string, port int) bool;
            query(sql []string) [2]string;
            execute(command []string) bool;
            disconnect();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_struct_1(self):
        input = """type Point struct {
            x, y float;
            a [3]int;
            b [2][2]Matrix;
        }"""
        expect = "Error on line 2 col 14: ,"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_struct_2(self):
        input = """type Rectangle struct {
            width, height float;
            color string;
        }"""
        expect = "Error on line 2 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_struct_3(self):
        input = """type Student struct {
            name string;
            grades [10]float
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_struct_4(self):
        input = """type LinkedList struct {
            data int;
            next Node;
        }"""
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_struct_8(self):
        input = """type Car struct {
            brand string;
            year int;
            specs [5]string;
            engine Engine;
        }"""
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_struct_10(self):
        input = """type Employee struct {
            id int;
            salary float;
            department struct;
        }"""
        expect = "Error on line 4 col 24: struct"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_method_decl_1(self):
        input = """func (p Point) distance(q Point) float {
            return sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_method_decl_4(self):
        input = """func (l LinkedList) insert(value int) {
            l.next := Node{data: value, next: l.next};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_method_decl_6(self):
        input = """func (c Complex) add(other Complex) Complex {
            return Complex{real: c.real + other.real, imaginary: c.imaginary + other.imaginary};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_method_decl_7(self):
        input = """func (b BankAccount) transfer(amount float, target BankAccount) bool {
            if b.balance >= amount { return true; };
            return false;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_method_decl_8(self):
        input = """func (c Car) start() string {
            return c.brand + " engine starting...";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_method_decl_9(self):
        input = """func (t Tree) insert(val int) Tree {
            if t == nil { return Tree{value: val}; };
            return t;
        }"""
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_method_decl_10(self):
        input = """func (e Employee) promote( int float) {
            e.salary := e.salary * (1.0 + raise);
        }"""
        expect = "Error on line 1 col 28: int"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_complex_program_1(self):
        input = """
       /* type Point struct {
            x, y int;
        }*/
        func (p Point) distance(q Point) float {
            return sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y));
        }
        func main() {
            var a [5]Point;
            for i := 0; i < 5; i+=1 {
                a[i] := Point{x: i, y: i};
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))    

    def test_complex_program_2(self):
        input = """
        type Shape interface {
            area() float;
            perimeter() float;
        }
        /*type Rectangle struct {
            width, height float;
        }*/
        func (r Rectangle) area() float {
            return r.width * r.height;
        }
        func main() {
            var shapes [2]Shape;
            shapes[0] := Rectangle{width: 5.0, height: 3.0};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_complex_program_3(self):
        input = """
        type Stack struct {
            elements [100]int;
            size int;
        }
        func (s Stack) push(element int) {
            s.elements[s.size] := element;
            s.size := s.size + 1;
        }
        func (s Stack) pop() int {
            s.size := s.size - 1;
            return s.elements[s.size];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_complex_program_4(self):
        input = """
        type BankAccount struct {
            balance float;
            owner string;
        }
        func (b BankAccount) withdraw(amount float) bool {
            if b.balance >= amount {
                b.balance := b.balance - amount;
                return true;
            }
            return false;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_complex_program_5(self):
        input = """
        type Animal interface {
            makeSound() string;
            move(distance float);
        }
        type Dog struct {
            name string;
            age int;
        }
        func (d Dog) makeSound() string {
            return "Woof!";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_complex_program_6(self):
        input = """
        type Matrix struct {
            data [3][3]float;
        }
        func (m Matrix) multiply(n Matrix) Matrix {
            var result Matrix;
            for i := 0; i < 3; i+=1 {
                for j := 0; j < 3; j+=1 {
                    result.data[i][j] := m.data[i][j] * n.data[i][j];
                }
            }
            return result;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_complex_program_7(self):
        input = """
        type LinkedList struct {
            value int;
            next LinkedList;
        }
        func (l LinkedList) insert(val int) LinkedList {
            if l.next == nil {
                l.next := LinkedList{value: val, next: nil};
            }
            return l;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_complex_program_9(self):
        input = """
        type Tree struct {
            value int;
        //    left, right Tree;
        }
        func (t Tree) insert(val int) {
            if val < t.value {
                if t.left == nil {
                    t.left := Tree{value: val};
                } else {
                    t.left.insert(val);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_complex_program_10(self):
        input = """
        type Calculator interface {
            calculate(x float, y float) float;
        }
        type Addition struct {}
        func (a Addition) calculate(x float, y float) float {
            return x + y;
        }
        func main() {
            var calc Calculator = Addition{};
            result := calc.calculate(10.5, 20.5);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_complex_program_12(self):
        input = """
        type Database interface {
            connect(host string) bool;
            query(sql string) [100]string;
            close();
        }
        func executeQuery(db Database, query string) {
            if db.connect("localhost") {
                results := db.query(query);
                db.close();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_complex_program_13(self):
        input = """
        type Circle struct {
            radius float;
            center Point;
        }
        func (c Circle) area() float {
            return 3.14 * c.radius * c.radius;
        }
        func main() {
            circles := [3]Circle{
                Circle{radius: 1.0, center: Point{x: 0, y: 0}},
                Circle{radius: 2.0, center: Point{x: 1, y: 1}},
                Circle{radius: 3.0, center: Point{x: 2, y: 2}}
            };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_complex_program_14(self):
        input = """
        type Stack interface {
            push(value int);
            pop() int;
            peek() int;
        }
        type ArrayStack struct {
            items [100]int;
            top int;
        }
        func (s ArrayStack) push(value int) {
            s.items[s.top] := value;
            s.top := s.top + 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_complex_program_16(self):
        input = """
        type Sorter interface {
            sort(a [100]int) [100]int;
        }
        type BubbleSort struct {}
        func (bs BubbleSort) sort(arr [100]int) [100]int {
            for i := 0; i < 100; i+=1 {
                for j := 0; j < 99; j+=1 {
                    if arr[j] > arr[j+1] {
                        temp := arr[j];
                        arr[j] := arr[j+1];
                        arr[j+1] := temp;
                    }
                }
            }
            return arr;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_complex_program_18(self):
        input = """
        type Game struct {
            players [2]Player;
            score [2]int;
            isFinished bool;
        }
        func (g Game) start() {
            g.isFinished := false;
            for i := 0; i < 2; i+=1 {
                g.score[i] := 0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_complex_program_20(self):
        input = """
        type HashTable struct {
            buckets [100]LinkedList;
            size int;
        }
        func (ht HashTable) hash(key, val, exp, lowcode, nonstop string) int {
            sum := 0;
            for i := 0; i < len(key); i+=1 {
                sum := sum + key[i];
            }
            return sum % 100;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_lhs_error(self):
        input = """func main() {
            1 = 2;
        }"""
        expect = "Error on line 2 col 13: 1"
        self.assertTrue(TestParser.checkParser(input,expect,280))
        
    def test_inline_statements_error(self):
        input = """func main() {
            var a = 1 + 2 a.b = 3;
        }"""
        expect = "Error on line 2 col 27: a"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_extra_token_after_function_error(self):
        input = """
func main() {} extra"""
        expect = "Error on line 2 col 16: extra"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_nested_block_error(self):
        input = """func main() { { x := 5; } } var a int = 10"""
        expect = "Error on line 1 col 15: {"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_inline_declarations_error(self):
        input = """func main() {  x := 5;  } var a int = 10"""
        expect = "Error on line 1 col 27: var"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_invalid_short_declaration_error(self):
        input = """func main() { := 5; }"""
        expect = "Error on line 1 col 15: :="
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_invalid_function_parameter_error(self):
        input = """func test(x,) int { return 1; }"""
        expect = "Error on line 1 col 13: )"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_missing_type_array_error(self):
        input = """var arr = []{1,2,3};"""
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_invalid_struct_field_error(self):
        input = """type Person struct { ,name string; }"""
        expect = "Error on line 1 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_invalid_interface_method_error(self):
        input = """type Drawable interface { draw(,) int; }"""
        expect = "Error on line 1 col 32: ,"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_invalid_multiple_return_types_error(self):
        input = """func divide(x, y float) float { return x/y, 0; }"""
        expect = "Error on line 1 col 43: ,"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_invalid_range_syntax_error(self):
        input = """func main() { for i := range { print(i); } }"""
        expect = "Error on line 1 col 24: range"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_invalid_channel_syntax_error(self):
        input = """func main() { ch <- 5 <- 3; }"""
        expect = "Error on line 1 col 18: <"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_invalid_function_literal_error(self):
        input = """var f = func(x int) { return x + 1 };"""
        expect = "Error on line 1 col 9: func"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_commented_semicolon(self):
        input = """func main() { 
            var a = 0 //; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_string_error(self):
        input = """func main() { 
            var a = "abc;\q";
        }"""
        expect = "abc;\\q"
        self.assertTrue(TestParser.checkParser(input,expect,296))
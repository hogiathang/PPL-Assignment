import unittest
from TestUtils import TestParser
expect = "successful"
class ParserSuite(unittest.TestCase):
    def test_sample_1(self):
        input = """var t,q,r,z = 10
                    var teq = "test" + 10
                    var argv [10]int = a[1] + 10
                    var a [5]Point;
                var circles = [3]Circle{
                            Circle{radius: 1.0, center: Point{x: 0, y: 0}},
                            Circle{radius: 2.0, center: Point{x: 1, y: 1}},
                            Circle{radius: 3.0, center: Point{x: 2, y: 2}}};
                var pole = [1023]Cirlce{"Hello", {"World", {"AQUA"}, "PKP", {1,2,3,45}}, {1,2,3,4,5,67,8,9}}
                var testKimJongUn = NorthKorea{
                    name: "Mr Kim Jong Un",
                    ability: "Like Rocket"}

            const t,q,r,z = 10
                    var teq = "test" + 10
                    var argv [10]int = a[1] + 10
                    var a [5]Point;
                const circles = [3]Circle{
                            Circle{radius: 1.0, center: Point{x: 0, y: 0}},
                            Circle{radius: 2.0, center: Point{x: 1, y: 1}},
                            Circle{radius: 3.0, center: Point{x: 2, y: 2}}};
                const pole = [1023]Cirlce{"Hello", {"World", {"AQUA"}, "PKP", {1,2,3,45}}, {1,2,3,4,5,67,8,9}}
                const testKimJongUn = NorthKorea{
                    name: "Mr Kim Jong Un",
                    ability: "Like Rocket"}

        func foo(a, b int, c float) {
            x := 10

            if (x > 10) { 
                x := 10

                if (b) {
                    var c = 5
                } else {
                    b := true
                }
            } else {
                x := 20
            }
        }
        func zoo() {
            t := 1000 + 30 -20 + 3 -a.b.c[20] || 4 && 5
            q := Cal{
                left: 10,
                right: 20}

            teqz:= [3]Circle{
                Circle{radius: 1.0, center: Point{x: 0, y: 0}},
                Circle{radius: 2.0, center: Point{x: 1, y: 1}},
                Circle{radius: 3.0, center: Point{x: 2, y: 2}}}
        }
        func (z Z) test() {}
        func (z Z) test() int {}    

        type Point struct {
            z int
            tdwduwhu idjwajjdwj
            todo [10]int
        }

         type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
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
        func foo() {
            manager := ShapeManager{
            id: 1,
            name: "Manager",
            coordinates: [5]Point{{0,0}, {1,1}, {2,2}, {3,3}, {4,4}},
            active: true,
            drawer: Circle{center: Point{x: 10, y: 20}, radius: 5.0},
            metadata: Metadata{
                createdBy: "John Doe",
                version: 1.0}};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def testcase_210(self):
        input = """
        func foo() {
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
        }
        """
        expect = "Error on line 9 col 23: struct"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def testcase_211(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        func main() {
        p := Person{}
        PutStringLn(p.name) // Output: Alice
        PutIntLn(p.age) // Output: 30
        var people [3]Person
        const Greeting = "Hello, MiniGo!"
        const MaxSize = 100 + 50;
        const Pi = 3.14;
        testPerson.people.aiw(people).lost.pole(3);
        tq := 4 || 5 || 6
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
        func main() {
        if (x > 10) {
            println("x is greater than 10")
        } else if (x < 10) {
            println("x is less than 10")
        } else {
            println("x is equal to 10")
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    
    def testcase_214(self):
        input = """
        func main() {
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
        }
"""
        expect = "Error on line 14 col 20: arr"
        self.assertTrue(TestParser.checkParser(input, expect, 214))
    
    def testcase_215(self):
        input = """
        func main() {
        a[2][3] := b[2] + 1;
        person.name := "John";
        person.age := 30;
        arr := [3]int{10, 20, 30}
        marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        p := Person{name: "Alice", age: 30}
        q := Person{}
        add(3, 4);}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def testcase_216(self):
        input = """
        func modify(x int) {
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
        }
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
        expect = "Error on line 2 col 9: foo"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def testcase_218(self):
        input = """
        {}"""
        expect = "Error on line 2 col 9: {"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def testcase_219(self):
        input = """x := true.x;"""
        expect = """Error on line 1 col 1: x"""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def testcase_220(self):
        input = """
        func main() {
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
                    }else {
                        println(i);
                    }
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
                    city: "New York"},
                created: DateCreated{
                    day: 1,
                    month: 1,
                    year: 2020}};

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
        func foo () {
        var matrix [2][3]int = {{1, 2, 3}, {4, 5, 6}};
        var matrix2 [1]int = {1};
        arr2 := [1]int{1};
        arr := [2][3]int{{1, 2, 3}, {4, 5, 6}};
        putIntLn(matrix[1][2]);  // In ra 6
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_quicksort_230(self):
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
        expect = "Error on line 48 col 21: ]"
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
        expect = "Error on line 1 col 11: +"
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
            left, right Tree;
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
        expect = "Error on line 4 col 17: ,"
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
        expect = "Error on line 13 col 64: ;"
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

    def test_expression_297(self):
        input = """a := -(5 + 3 - 2) * 4 / 2 % 1 == true && false"""
        expect = "Error on line 1 col 1: a"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_298(self):
        input = """
        //const a = 2.x;
        var a [2]int;
        var b [345]Too;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
#     parserTest = 199

#     def test_parser_00(self):
#         inp = \
#             """ // Test case 0: Basic program with simple arithmetic and output
# func main() {
#     var x int = 5;
#     var y int = 10
#     var result int = x + y * 2
#     println(result);
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_01(self):
#         inp = \
#             """// Test case 1: String manipulation and conditional output
# func main() {
#     var name string = "MiniGo";
#     var greeting string = "Hello, " + name + "!";
#     if (len(greeting) > 10) {
#         println(greeting)
#     }
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_02(self):
#         inp = \
#             """// Test case 2: Function with parameters, local variables, and return
# func add(a int, b int) int {
#     var sum int = a + b;
#     return sum
# }
# func main() {
#     var result int = add(5, 3);
#     println(result);
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_03(self):
#         inp = \
#             """// Test case 3: Struct definition, instantiation, and field access
# type Point struct {
#     x int
#     y int;
# }
# func main() {
#     var p Point = {x: 10, y: 20};
#     p.x = p.x + 5;
#     println(p.x)
#     println(p.y)
# }
# """
#         out = "Error on line 7 col 19: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_04(self):
#         inp = \
#             """/* Test case 4: Array declaration, initialization, and iteration*/
# func main() {
#     var numbers [5.6]int = [6]{1, 2, 3, 4, 5}
#     var sum int = 0
#     for i := 0; i < 5; i += 1 {
#         sum = sum + numbers[i];
#     }
#     println(sum)
# }
# """
#         out = "Error on line 3 col 18: 5.6"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_05(self):
#         inp = \
#             """// Test case 5: Nested if statements with logical operators
# func main() {
#     var age int = 25;
#     var isStudent boolean = true;
#     if (age > 18 && age < 30) {
#         if (isStudent) {
#             println("Eligible for student discount");
#         } else {
#             println("Eligible for adult fare");
#         }
#     } else {
#         println("Not eligible");
#     }
# }"""
#         out = "Error on line 14 col 2: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_06(self):
#         inp = \
#             """
# // Test case 6: For loop with break and continue statements
# func main() {
#     for i := 0; i < 10; i += 1 {
#         if (i % 2 == 0) {
#             continue;
#         }
#         if (i > 5) {
#             break;
#         }
#         println(i);
#     }
#     println("Loop finished");
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_07(self):
#         inp = \
#             """// Test case 7: Multiple function calls with different parameters
# func square(x int) int {
#     return x * x;
# }
# func cube(x int) int {
#     return x * x * x;
# }
# func main() {
#     var sq int = square(5);
#     var cb int = cube(3);
#     println(sq)
#     println(cb)
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_08(self):
#         inp = \
#             """// Test case 8: Interface definition and empty implementation
# type Printable interface {
#     print();
# }
# type Empty struct {}
# func (e Empty) print() {}
# func main() {
#     var p Printable = Empty{};
#     p.print();
# }
# """
#         out = "Error on line 5 col 20: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_09(self):
#         inp = \
#             """// Test case 9: Function with multiple local variables and complex calculations
# func calculate(a int, b,c int, c float) int {
#     var x int = a + b;
#     var y int = b * c
#     var z int = x - y
#     return z * 2;
# }
# func main() {
#     var result int = calculate(10, 5, 2);
#     println(result);
# }"""
#         out = "Error on line 11 col 2: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_10(self):
#         inp = \
#             """// Test case 10: Error: Missing semicolon
# func main() { var x int = 5 }
# """
#         out = "Error on line 2 col 29: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_11(self):
#         inp = \
#             """// Test case 11: Error: Unclosed parenthesis
# func main() { if (true  { }
# """
#         out = "Error on line 2 col 25: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_12(self):
#         inp = \
#             """// Test case 12: Error: Undeclared variable
# func main() { x = 5; }
# """
#         out = "Error on line 2 col 17: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_13(self):
#         inp = \
#             """// Test case 13: Error: Type mismatch
# func main() { var x int = "hello"; }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_14(self):
#         inp = \
#             """// Test case 14: Error: Invalid operator
# func main() { var x int = 5 @ 3; }"""
#         out = "@"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_15(self):
#         inp = \
#             """
# // Test case 15: Error: Missing brace
# func main()  }

# """
#         out = "Error on line 3 col 14: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_16(self):
#         inp = \
#             """// Test case 16: Error: Invalid return type
# func foo() int { return "hello"; }
# func main() {}
# """
#         out = "Error on line 3 col 14: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_17(self):
#         inp = \
#             """// Test case 17: Error: Array index out of bounds (for completeness - may not be a parsing error)
# func main() { var arr [3]int = {1, 2, 3}; var x int = arr[5]; }
# }
# """
#         out = "Error on line 2 col 32: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_18(self):
#         inp = \
#             """// Test case 18: Error: Struct field does not exist
# type Point struct { x int; }
# func main() { var p Point = Point{x: 1, y: 2}; var z int = p.z; }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_19(self):
#         inp = \
#             """
# // Test case 19: Error: Invalid character
# func main() { var x int = 5$; }
# """
#         out = "$"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_20(self):
#         inp = \
#             """
# // Test case 20: More complex if-else structure
# func main() {
#     var num int = 15;
#     if (num < 10) {
#         println("Less than 10");
#     } else if (num > 20) {
#         println("Greater than 20");
#     } else {
#         println("Between 10 and 20");
#     }
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_21(self):
#         inp = \
#             """// Test case 21: Multi-dimensional array
# func main() {
#     var matrix [2][1]int = [2][1]int{{1, 2, 3}, 4};
#     println(matrix[1][2]); // Output: 6
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_22(self):
#         inp = \
#             """// Test case 22: Multiple struct instances
# type Rectangle struct {
#     width int;
#     height int;
# }
# func main() {
#     var rect1 Rectangle = {width: 10, height: 5};
#     var rect2 Rectangle = {width: 7, height: 3};
#     println(rect1.width * rect1.height + rect2.width * rect2.height);
# }"""
#         out = "Error on line 7 col 27: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_23(self):
#         inp = \
#             """// Test case 23: More complex function with nested loops
# func processArray(arr [5]int) int {
#     var sum int = 0;
#     for i := 0; i < 5; i += 1 {
#         for j := 0; j < arr[i]; j += 1 {
#             sum = sum + 1;
#         }
#     }
#     return sum;
# }
# func main() {
#     var data [5]int = {1, 2, 3, 4, 5};
#     var result int = processArray(data);
#     println(result); // Output: 15
# }
# """
#         out = "Error on line 6 col 17: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_24(self):
#         inp = \
#             """ 
# // Test case 24: Method call on struct
# type Circle struct {
#     radius int;
# }
# func (c Circle) area() int {
#     return 3 * c.radius * c.radius;
# }
# func main() {
#     var myCircle Circle = {radius: 5};
#     println(myCircle.area()); // Output: 75
# }
# """
#         out = """Error on line 10 col 27: {"""
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_25(self):
#         inp = \
#             """ 
# // Test case 25: Nested comments (valid)
# func main() {
#     /*
#     Outer comment
#     /* Inner comment */
#     */
#     println("Hello");
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_26(self):
#         inp = \
#             """// Test case 26: Multi-line string
# func main() {
#     var message string = "This is a very long string\n" +
#                            "that spans multiple lines.";
#     println(message);
# }
# """
#         out = """"This is a very long string\n"""
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_27(self):
#         inp = \
#             """ 
# // Test case 27: Global and local variable shadowing
# var globalVar int = 10;
# func main() {
#     var globalVar int = 20; // Shadows the global variable within main
#     println(globalVar);         // Output: 20
#     {
#         var globalVar int = 30; // Shadows in an inner block
#         println(globalVar);     // Output: 30
#     }
#     println(globalVar);         // Output: 20 (back to the outer main scope)
# }
# """
#         out = "Error on line 7 col 5: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_28(self):
#         inp = \
#             """ // Test case 28: Nil pointer check and usage (check if parser allows nil)
# func main() {
#     var ptr *int = nil;
#     if (ptr == nil) {
#         println("Pointer is nil");
#     }
#     // The following line might cause a runtime error if nil pointers aren't handled
#     // println(*ptr);  // Remove or comment out for parser testing, address in later stages.
# }
# """
#         out = "Error on line 3 col 13: *"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_29(self):
#         inp = \
#             """ // Test case 29: Test for "range" with a single value
# func main() {
# 	arr := [3]int{1,2,3}
# 	for _, value := range arr {
# 		println(value)
# 	}
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_30(self):
#         inp = \
#             """ 
# // Test case 30:  Use Struct and function calls within a statement.
# type example_t struct {
# 	x int
# }
# func calc(e example_t) int{
# 	return e.x + 10
# }
# func main() {
# 	var e example_t = example_t{x: 10}

# 	println(calc(e))
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_31(self):
#         inp = \
#             """// Test case 31:  Boolean Expression nesting
# func main() {

# 	var x int = 10
# 	var y int = 5

# 	if (((x > 5) && (y < 10)) || (x == y)){
# 		println("True")
# 	} else {
# 		println("False")
# 	}
# }"""
#         out = "Error on line 12 col 2: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_32(self):
#         inp = \
#             """// Test case 32: Missing colon in struct initialization (Error)
# type Foo struct {
#     bar int;
# }

# func main() {
#      var f Foo = {bar 5};
# }
# """
#         out = "Error on line 7 col 18: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_33(self):
#         inp = \
#             """// Test case 34: Invalid Character in identifier (Error)
# func main() {
#     var x$y int = 10;
# }
# """
#         out = "$"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_34(self):
#         inp = \
#             """// Test case 35: Missing Return in function declared to return type
# func exampleFunc(i int ) int {

# }

# func main() { }
# """
#         out = "Error on line 4 col 1: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_35(self):
#         inp = \
#             """
# // Test case 35: Assigning a constant
# func main() {
#     const testConst int = 12
#     testConst = 10
# }
# """
#         out = "Error on line 4 col 21: int"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_36(self):
#         inp = \
#             """
# // Test case 36: More Complex struct Declaration

# type Address struct {
#   Street string
#   City string
#   Zip int
# }

# type Person struct {
#   Name string
#   Age int
#   Address Address
# }

# func main() {
#   var p Person = {
#     Name: "John Doe",
#     Age: 30,
#     Address: {
#       Street: "123 Main St",
#       City: "Anytown",
#       Zip: 12345,
#     },
#   }
#   println(p.Address.City)
# }
# """
#         out = "Error on line 17 col 18: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_37(self):
#         inp = \
#             """// Test case 37: Multiple variable declarations

# func main() {
#   var (
#     x int = 10
#     y string = "hello"
#     z float = 3.14
#   )
#   println(x,y,z)

# }
# """
#         out = "Error on line 4 col 7: ("
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_38(self):
#         inp = \
#             """// Test case 38: Global variable declaration

# var globalString string = "hello"

# func main() {
#    println(globalString)

# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_39(self):
#         inp = \
#             """// Test case 39: For range loop
# func main() {
# 	arr := [3]int{1,2,3}
# 	for index, value := range arr {
# 		println(value)
# 	}
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_40(self):
#         inp = \
#             """
# // Test case 40: Correct associativity and Precedence

# func main() {

# 	var x int = 2 * (3 + 4) / 2

# 	println(x)

# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_41(self):
#         inp = \
#             """

# // Test case 41:  Simple Array Literal test
# func main() {
# 	var arr [3]string = [3]string{"Hello", World, {1,2,3}}

# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_42(self):
#         inp = \
#             """// Test case 42:  Test continue statement with label

# func main() {

# 	for i := 0; i < 10; i+= 1{
# 		if(i % 2 == 0) {
# 			continue
# 		}

# 		println(i)
# 	}

# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_43(self):
#         inp = \
#             """// Test case 43:  Nil comparison with type assertion
# func main() {
# 	var inter int = nil
# 	if (inter == nil) {
# 		println("It is nil")
# 	}
# 	}
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_44(self):
#         inp = \
#             """
# // Test case 44: Nested loops and branching logic

# func main() {

# 	for i := 0; i < 5; i += 1 {
# 		for j := 0; j < 5; j += 1 {
# 			if (i == j) {
# 				println("Diagonal")
# 			} else if (i > j) {
# 				println("Below Diagonal")
# 			} else {
# 				println("Above Diagonal")
# 			}
# 		}
# 	}
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_45(self):
#         inp = \
#             """


# // Test case 45:  Invalid type in array literal (error)
# func main() {
#    var arr [3]int = int{1, "2", 3}
# }
# """
#         out = "Error on line 6 col 21: int"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_46(self):
#         inp = \
#             """// Test case 46: Variable redeclaration within inner scope (valid)
# func main() {
#     var x int = 10
#     if (true) {
#       var x string = "hello"
#       println(x)
#     }
#     println(x)
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_47(self):
#         inp = \
#             """// Test case 47: Missing semicolon in for loop (Error)
# func main() {
#   for i := 0 i < 10 ;i++ {

#   }
# }
# """
#         out = "Error on line 3 col 14: i"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

# #     def test_parser_48(self):
# #         inp = \
# #             """// Test case 48: Type mismatch in assignment (Error)
# # func main() {
# #     var x
# # }
# # """
# #         out = "Error on line 3 col 10: ;"
# #         ParserSuite.parserTest += 1
# #         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_49(self):
#         inp = \
#             """// Test case 49: Invalid expression in return statement (Error)
# func exampleFunc() int {
#   return "hello" + 5;
# }"""
#         out = "Error on line 4 col 2: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_50(self):
#         inp = \
#             """ for i := 0; i < 10; i += 1 {
#     if (x % i = 0) {return false;}
# }
# """
#         out = "Error on line 1 col 2: for"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_51(self):
#         inp = \
#             """func main () {return 1;}

# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_52(self):
#         inp = \
#             """for i; i <= x / 2; i += 1
# {
#     if (x % i = 0) {return false
#     }
# }
# """
#         out = "Error on line 1 col 1: for"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_53(self):
#         inp = \
#             """func main(x string, y float)  {
# }
# """
#         out = "Error on line 2 col 1: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

# #     def test_parser_54(self):
# #         inp = \
# #             """func foo(str string) boolean
# # writeString(str)
# # var x = 7 + (t - false)
# # """
# #         out = "Error on line 1 col 29: ;"
# #         ParserSuite.parserTest += 1
# #         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_55(self):
#         inp = \
#             """func bar( arr int){
# x[2][8] := [3][1,2,\"3\"] + [2][4,\"5\",6]
# }"""
#         out = "Error on line 2 col 17: ,"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

# #     def test_parser_56(self):
# #         inp = \
# #             """
# # func min(a int, b string){  
# # if (x <= false){
# #         main(a,2,\"b\")
# #     }
# # for var i int; i <= x / 2; i += 1{ 

# #     loop1(arr[a(b)][b(a)])
# #     loop2(arr[a(b)],b[2])
# # }

# # }
# # """
# #         out = "Error on line 6 col 14: ;"
# #         ParserSuite.parserTest += 1
# #         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_57(self):
#         inp = \
#             """func min(a int, b string){ 
# if (boolean) {
# doSomething(a,2,\"b\");}
# elif (abc > \"abc\") {doSomethingElif(b,true,foo(x,2))
# }
# else doSomethingElse(doSomethingElse,foo[3.2,3])
# }

# """
#         out = "Error on line 2 col 5: boolean"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_58(self):
#         inp = \
#             """//func max(a int, b number)
# /* begin
# ## Comment 1
# ##if (x == 6) else {doSomething();}
# ## Comment 2
# */
# """
#         out = "Error on line 7 col 1: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_59(self):
#         inp = \
#             """func bar(arr float, b boolean) {
# x[a(b)][b(a)] := foo(1,2,\"abcd\",154/4)
# var x int= readString()
# """
#         out = "Error on line 4 col 1: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_60(self):
#         inp = \
#             """const GREETING string = "Hello, World!"

# var message string

# func main() {
#     message = GREETING
#     println(message)
# }
# """
#         out = "Error on line 1 col 16: string"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_61(self):
#         inp = \
#             """var a int = 10
# var b int = 5
# var result int

# func main() {
#     result = a + b*2 - b/2
#     println(result)
# }
# """
#         out = "Error on line 6 col 12: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_62(self):
#         inp = \
#             """var x int = 7

# func main() {
#     if (x > 5) {
#         println("x is greater than 5")
#     } else {
#         println("x is not greater than 5")
#     }
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_63(self):
#         inp = \
#             """var numbers [5]int = [5]int{1, 2, 3, 4, 5}

# func main() {
#     for , value := range numbers {
#         println(index, value)
#     }
# }
# """
#         out = "Error on line 4 col 9: ,"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_64(self):
#         inp = \
#             """type Point struct {
#     x int
#     y int
# }

# var p Point

# func main() {
#     p.x := 10
#     p.y := 20
#     println(p.x, p.y)
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_65(self):
#         inp = \
#             """
# type Printer interface {
#     print(message string)
# }

# func main() {
#     // No implementation here to test just declaration
# }

# """
#         out = "Error on line 8 col 1: }"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_66(self):
#         inp = \
#             """type Rectangle struct {
#     width int
#     height int
# }

# func (r Rectangle) area() int {
#     return r.width * r.height
# }

# var rect Rectangle

# func main() {
#     rect.width = 5
#     rect.height = 10
#     println(rect.area())
# }
# """
#         out = "Error on line 13 col 16: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_67(self):
#         inp = \
#             """func calculate(a int, b int) (int, int) {  // Invalid: Multiple return values
#     return a + b, a - b
# }

# func main() {
#     var sum, diff int
#     sum, diff = calculate(10, 5)
#     println(sum, diff)
# }
# """
#         out = "Error on line 1 col 30: ("
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_68(self):
#         inp = \
#             """var age int = 25
# var isStudent bool = false

# func main() {
#     if (age < 30) {
#         if (!isStudent) {
#             println("Young professional")
#         } else {
#             println("Young student")
        
#     } else {
#         println("Experienced")
#     }
# }
# """
#         out = "Error on line 11 col 7: else"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_69(self):
#         inp = \
#             """
# func main() {
#     for i := 0; i < 10; i += 1 {
#         if (i % 3 == 0) {
#             continue  // Skip multiples of 3
#         }
#         if (i > 7) {
#             break     // Exit loop if i is greater than 7
#         }
#         println(i)
#     }
#     break
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_70(self):
#         inp = \
#             """
# type Circle struct {
#     radius int
# }

# var circles [3]Circle

# func main() {
#     circles[0].radius := 5
#     circles[1].radius := 7
#     circles[2].radius := 9

#     for _, c := range circles {
#         println(c.radius)
#     }
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_71(self):
#         inp = \
#             """func main() {
#     for i < 3 {
#         for j += 1 {
#             println(i, j)
#         }
#     }
# }"""
#         out = "Error on line 3 col 20: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_72(self):
#         inp = \
#             """/*
#     This is a multi-line comment.
#     It spans multiple lines.
# */

# // This is a single-line comment.

# var   x  int  =   10;  //  Declaration with extra whitespace

# func main()  {
#     //  More comments inside the function
#     println ( x  ) ;
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_73(self):
#         inp = \
#             """var maxInt int = 2147483647  // Maximum 32-bit integer (adjust if needed)

# func main() {
#     var overflow int = maxInt + 1
#     println(overflow)  //  What happens when we overflow?
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_74(self):
#         inp = \
#             """ 
# var message string = "This string contains a newline\nand a tab\t."

# func main() {
#     println(message)
# }
# """
#         out = """"This string contains a newline\n"""
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_75(self):
#         inp = \
#             """ 
# var x int = 5

# func main(x int, y,z float, t [2][3]int, k) {
#     println(x)
# }
# """
#         out = "Error on line 4 col 43: )"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

# #     def test_parser_76(self):
# #         inp = \
# #             """var message string = "This string is not terminated"

# # func main() {
# #     println(message
# # }
# # """
# #         out = """Error on line 4 col 20: ;"""
# #         ParserSuite.parserTest += 1
# #         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_77(self):
#         inp = \
#             """ 
# var x int = 5
# var y int = 10 // /* */
# func main() {
#     println(x + y)
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_78(self):
#         inp = \
#             """ var x int = 5

# func main() {
#     var x [1]float = Person{x: int, y: float} // x redeclared in the same scope
#     println(x)
# }
# """
#         out = "Error on line 4 col 32: int"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_79(self):
#         inp = \
#             """ var globalVar int = 20

# func myFunction() {
#     var localVar int = 10
#     println(globalVar + localVar)
# }

# func main() {
#     myFunction()
#     println(globalVar) // Access global variable from main
#     //println(localVar) // Error: localVar is not defined in main
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_80(self):
#         inp = \
#             """ 
# var a int = 10
# var b int = 5
# var c string = "hello"

# func main() {
#     if ((a > 5 && b < 10) || c == "world") {
#         if (a + b == 15) {
#             println("Condition met")
#         } else {
#             println("Inner condition failed")
#         }
#     } else {
#         println("Outer condition failed")
#     }
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_81(self):
#         inp = \
#             """var x int
# var y int
# var z int

# func main() {
#     x, y, z = 1, 2 + 3, 4 * 5 - 1 // Note multi-assignment is illegal in MiniGo
#     println(x, y, z) // Illegal because it's not a function
# }"""
#         out = "Error on line 6 col 6: ,"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_82(self):
#         inp = \
#             """func main() {
#     for i := 0; i < 20; i+= 1 {
#         if (i % 5 == 0) {
#             continue // Skip multiples of 5
#         }
#         if (i > 12 && i < 15) {
#             break    // Exit if between 13 and 14
#         }
#         println(i)
#     }
# }"""
#         out = "Error on line 11 col 2: <EOF>"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_83(self):
#         inp = \
#             """type Person struct {
#     name string
#     age int
# }

# var p Person

# func main() {
#     p.name := "Alice"
#     p.age := 30
#     println(p.name, p.age)
#     var message string = p.name + " is " + p.age + " years old" // Concatenation with integer will cause a type error

# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_84(self):
#         inp = \
#             """var data = [4]int{10, 20, 30, 40}

# func main() {
#     for index, value := range data {
#         println(index * value)
#     }
#     data[index] := 
#     z; y := 10
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_85(self):
#         inp = \
#             """
# func findValue(arr [5]int, target int) int {
#     for i := 0; i < 5; i+=1 {
#         if (arr[i] == target) {
#             return i // Return index if found
#         }
#     }
#     return -1  // Return -1 if not found
# }

# var numbers [5]int = [5]{1, 2, 3, 4, 5}

# func main() {
#     var index int = findValue(numbers, 3)
#     println(index)
# }
# """
#         out = "Error on line 11 col 25: {"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_86(self):
#         inp = \
#             """var x int = 10
# var y string = "hello"
# var z bool = true
# const PI float = 3.14

# func main() {
#     println(x, y, z, PI)
# }
# """
#         out = "Error on line 4 col 10: float"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_87(self):
#         inp = \
#             """type Address struct {
#     street string
#     city string
# }

# type Person struct {
#     name string
#     address Address
# }

# var p Person

# func main() {
#     p.name = "Bob"
#     p.address.street = "123 Main St"
#     p.address.city = "Anytown"
#     println(p.name, p.address.street, p.address.city)
# }
# """
#         out = "Error on line 14 col 12: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_88(self):
#         inp = \
#             """func isEven(n int) bool {
#     return n % 2 == 0
# }

# var num int = 8

# func main() {
#     if (isEven(num)) {
#         println("Even")
#     } else {
#         println("Odd")
#     }
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_89(self):
#         inp = \
#             """var a int = 5
# var b int = 10
# var result bool

# func main() {
#     result := a + b > 12 && a * b < 60 // Will cause a type error because an int is compared to a bool
#     println(result)
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_90(self):
#         inp = \
#             """
# func main() {
#     for i = 0; i < 10; i++ { 
#         println(i) 
#     }
# }
# """
#         out = "Error on line 3 col 11: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

# #     def test_parser_91(self):
# #         inp = \
# #             """
# # var x int = 10

# # func main() {
# #     if (x > 5)
# #         println("x > 5")  // Missing braces - should cause an error
# #     else
# #         println("x <= 5")
# # }
# # """
# #         out = "Error on line 5 col 15: ;"
# #         ParserSuite.parserTest += 1
# #         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_92(self):
#         inp = \
#             """type MyInterface interface {
# 	doSomething()
# }
# type MyType struct{x MyInterface
# }

# func (m MyType) doSomething() {
# 	println("Hello")
# }

# func main() {
# 	var i MyInterface
# 	var m MyType
# 	i := m
#     y[6].x[6].doSomething()
#     Arr[i + 1] := 10

# 	//i.doSomething()// Calling method doSomething of MyInterface

# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_93(self):
#         inp = \
#             """
# var a bool = true
# var b bool = false
# var c bool = true

# func main() {
#     var result bool = (a && b) ||+ (!c && a)
#     println(result)
# }
# """
#         out = "Error on line 7 col 34: +"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_94(self):
#         inp = \
#             """


# var numbers [3]int = int{1, "hello", 3} // "hello" is not an int. Error expected.

# func main() {
#     println(numbers[0], numbers[1], numbers[2])
# }
# """
#         out = "Error on line 4 col 22: int"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_95(self):
#         inp = \
#             """var notAnArray int = 5;

# func main() {
#     for index, value := notAnArray {
#         println(index, value);
#     }
# }
# """
#         out = "Error on line 4 col 25: notAnArray"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_96(self):
#         inp = \
#             """func someOtherFunction() {
#     println(x = 5)
# }
# """
#         out = "Error on line 2 col 15: ="
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     # def test_parser_97(self):
#     #     inp = \
#     #         """
#     #     type Circle struct {
#     #         radius float;
#     #         center Point;
#     #     }
#     #     func (c Circle) area() float {
#     #         return 3.14 * c.radius * c.radius;
#     #     }
#     #     func main() {
#     #         circles := [3]Circle{
#     #             Circle{radius: 1.0, center: Point{x: 0, y: 0}},
#     #             Circle{radius: 2.0, center: Point{x: 1, y: 1}},
#     #             Circle{radius: 3.0, center: Point{x: 2, y: 2}}
#     #         };
#     #     }"""
#     #     out = "Error on line 13 col 63: ;"
#     #     ParserSuite.parserTest += 1
#     #     self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_98(self):
#         inp = \
#             """type MyType struct {
# 	Name string
# }

# func (mt MyType) someMethod() string {
# 	for i := 0; i < 10; i+=1 {
# 		if (i == 5) {
# 			return "Found 5!"
# 		}
# 	}
# 	return "Not found"
# }

# func main() {
# 	mt := MyType{Name: "Example"}
# 	result := mt[y].f(z).someMethod()
# 	println(result)
# }
# """
#         out = "successful"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))

#     def test_parser_99(self):
#         inp = \
#             """
#         const a = 2.x;
# """
#         out = "Error on line 2 col 21: x"
#         ParserSuite.parserTest += 1
#         self.assertTrue(TestParser.checkParser(inp, out, ParserSuite.parserTest))
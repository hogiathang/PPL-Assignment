import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_identifier_101(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 101))

    def test_identifier_102(self):
        input = "abc123"
        expect = "abc123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test_identifier_103(self):
        input = "abc_123"
        expect = "abc_123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_identifier_104(self):
        input = "abc_123xYz"
        expect = "abc_123xYz,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_identifier_105(self):
        input = "aXc_123_Xc_Z"
        expect = "aXc_123_Xc_Z,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_identifier_106(self):
        input = "Xc_123_Xc1_Z"
        expect = "Xc_123_Xc1_Z,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_identifier_107(self):
        input = "_123_Xc1_Z"
        expect = "_123_Xc1_Z,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_identifier_108(self):
        input = "123_Xc1_Z"
        expect = "123,_Xc1_Z,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_identifier_109(self):
        input = "myVar"
        expect = "myVar,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_identifier_110(self):
        input = "MyVar"
        expect = "MyVar,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_identifier_111(self):
        input = "123a@bc"
        expect = "123,a,ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_identifier_112(self):
        input = "123abc"
        expect = "123,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test_identifier_113(self):
        input = "ifFunction"
        expect = "ifFunction,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_identifier_114(self):
        input = "return123 function_1"
        expect = "return123,function_1,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_identifier_115(self):
        input = "var123"
        expect = "var123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test_identifier_116(self):
        input = "var_123"
        expect = "var_123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_identifier_117(self):
        input = "var_123abc"
        expect = "var_123abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_identifier_118(self):
        input = "var_123_abc"
        expect = "var_123_abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_identifier_119(self):
        input = "var_123_abc_XYZ"
        expect = "var_123_abc_XYZ,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_keywords_120(self):
        input = "if (a > b) a = b;"
        expect = "if,(,a,>,b,),a,=,b,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    def test_keywords_121(self):
        input = "If (a > b) a = b; else b = a;"
        expect = "If,(,a,>,b,),a,=,b,;,else,b,=,a,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_keywords_122(self):
        input = "if (b == True) b *= 2;"
        expect = "if,(,b,==,True,),b,*=,2,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_keywords_123(self):
        input = "for i > 10 {//Looop\n}"
        expect = "for,i,>,10,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_keywords_124(self):
        input = "for i := 0; i < 10; i += 1 {var x int; x += 1;}"
        expect = "for,i,:=,0,;,i,<,10,;,i,+=,1,{,var,x,int,;,x,+=,1,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_keywords_125(self):
        input = "func add(x int, y int) int {\treturn x + y;}"
        expect = "func,add,(,x,int,,,y,int,),int,{,return,x,+,y,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_keywords_126(self):
        input = "while (a < b) {a = a + 1;}"
        expect = "while,(,a,<,b,),{,a,=,a,+,1,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_keywords_127(self):
        input = "func (c Calculator) add(x int, y int) int {return x + y;}"
        expect = "func,(,c,Calculator,),add,(,x,int,,,y,int,),int,{,return,x,+,y,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_keywords_128(self):
        input = "break;"
        expect = "break,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_keywords_129(self):
        input = "continue;"
        expect = "continue,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_literals_130(self):
        input = "123"
        expect = "123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_literals_131(self):
        input = "0b101001001"
        expect = "0b101001001,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_literals_132(self):
        input = "0B101011001"
        expect = "0B101011001,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_literals_133(self):
        input = "0o1234567"
        expect = "0o1234567,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

    def test_literals_134(self):
        input = "0O1234567"
        expect = "0O1234567,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_literals_135(self):
        input = "0x1234567890abcdef"
        expect = "0x1234567890abcdef,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_literals_136(self):
        input = "123.456"
        expect = "123.456,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_literals_137(self):
        input = "123."
        expect = "123.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_literals_138(self):
        input = "123.456e-2"
        expect = "123.456e-2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_literals_139(self):
        input = "123.456e+2"
        expect = "123.456e+2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_literals_140(self):
        input = "2.0e10"
        expect = "2.0e10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_assign_141(self):
        input = "str1 := \"Hello, World!\""
        expect = "str1,:=,\"Hello, World!\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    def test_assign_142(self):
        input = "str3 := str1 + \" \" + str2;"
        expect = "str3,:=,str1,+,\" \",+,str2,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    def test_assign_143(self):
        input = "str4 := \"apple\";"
        expect = "str4,:=,\"apple\",;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_assign_144(self):
        input = "str5 := \"banana\";"
        expect = "str5,:=,\"banana\",;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test_assign_145(self):
        input = "x := 10;"
        expect = "x,:=,10,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test_assign_146(self):
        input = "y := x + 20;"
        expect = "y,:=,x,+,20,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_assign_147(self):
        input = "z := y - 5;"
        expect = "z,:=,y,-,5,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_array_148(self):
        input = "var arr [5] int; // defines an array of 5 integers."
        expect = "var,arr,[,5,],int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_array_149(self):
        input = "var multiarr [2][5]int; // defines an array of 2 x 5 integers."
        expect = "var,multiarr,[,2,],[,5,],int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_array_150(self):
        input = "var arr [10] float;"
        expect = "var,arr,[,10,],float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_array_151(self):
        input = "var matrix [3][3]float;"
        expect = "var,matrix,[,3,],[,3,],float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_struct_152(self):
        input = "type Calculator struct {\n value int;\n}"
        expect = "type,Calculator,struct,{,value,int,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_struct_153(self):
        input = "type Person struct {\nname string ;\nage int ;}"
        expect = "type,Person,struct,{,name,string,;,age,int,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_struct_154(self):
        input = "p := Person{name: \"Alice\", age: 30}"
        expect = "p,:=,Person,{,name,:,\"Alice\",,,age,:,30,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_struct_155(self):
        input = " p := Person{}"
        expect = "p,:=,Person,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_struct_156(self):
        input = "PutStringLn(p.name) // Output: Alice"
        expect = "PutStringLn,(,p,.,name,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_struct_157(self):
        input = "PutIntLn(p.age)"
        expect = "PutIntLn,(,p,.,age,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_struct_158(self):
        input = "p.name = \"Bob\""
        expect = "p,.,name,=,\"Bob\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_struct_159(self):
        input = "p.age = 20"
        expect = "p,.,age,=,20,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test_struct_160(self):
        input = "PutStringLn(p.name) // Output: Bob"
        expect = "PutStringLn,(,p,.,name,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_struct_161(self):
        input = "func (p Person) Greet() string {return \"Hello, \" + p.name}"
        expect = "func,(,p,Person,),Greet,(,),string,{,return,\"Hello, \",+,p,.,name,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_struct_162(self):
        input = "PutStringLn(p.Greet()) // Output: Hello, Bob"
        expect = "PutStringLn,(,p,.,Greet,(,),),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_struct_163(self):
        input = "type Rectangle struct {\n width, height float;\n}"
        expect = "type,Rectangle,struct,{,width,,,height,float,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test_struct_164(self):
        input = "rect := Rectangle{width: 10.5, height: 20.5}"
        expect = "rect,:=,Rectangle,{,width,:,10.5,,,height,:,20.5,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_struct_165(self):
        input = "rect.width = 15.0"
        expect = "rect,.,width,=,15.0,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_interface_166(self):
        input = "type Calculator interface {Add(x, y int) int; Subtract(a, b float, c int) float; Reset() SayHello(name string)}"
        expect = "type,Calculator,interface,{,Add,(,x,,,y,int,),int,;,Subtract,(,a,,,b,float,,,c,int,),float,;,Reset,(,),SayHello,(,name,string,),},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    def test_interface_167(self):
        input = "type Guard interface {CheckAge(age int) bool}"
        expect = "type,Guard,interface,{,CheckAge,(,age,int,),bool,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_interface_168(self):
        input = "type Shape interface {Area() float; Perimeter() float}"
        expect = "type,Shape,interface,{,Area,(,),float,;,Perimeter,(,),float,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_interface_169(self):
        input = "type Drawable interface {Draw()}"
        expect = "type,Drawable,interface,{,Draw,(,),},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_function_170(self):
        input = "func add(a, b int) int {return a + b}"
        expect = "func,add,(,a,,,b,int,),int,{,return,a,+,b,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_function_171(self):
        input = "func sub(a, b int) int {return a - b}"
        expect = "func,sub,(,a,,,b,int,),int,{,return,a,-,b,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_function_172(self):
        input = "func mul(a, b int) int {return a * b}"
        expect = "func,mul,(,a,,,b,int,),int,{,return,a,*,b,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_function_173(self):
        input = "func div(a, b int) int {return a / b}"
        expect = "func,div,(,a,,,b,int,),int,{,return,a,/,b,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_function_174(self):
        input = "func mod(a, b int) int {return a % b}"
        expect = "func,mod,(,a,,,b,int,),int,{,return,a,%,b,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_others_175(self):
        input = "var x int = 10;"
        expect = "var,x,int,=,10,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_others_176(self):
        input = "var y float = 10.5;"
        expect = "var,y,float,=,10.5,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_others_177(self):
        input = "var z bool = true;"
        expect = "var,z,bool,=,true,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_others_178(self):
        input = "var s string = \"Hello, World!\";"
        expect = "var,s,string,=,\"Hello, World!\",;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_others_179(self):
        input = "const PI = 3.14159;"
        expect = "const,PI,=,3.14159,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_others_180(self):
        input = "const Greeting = \"Hello, World!\";"
        expect = "const,Greeting,=,\"Hello, World!\",;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_others_181(self):
        input = "const MaxSize = 100 + 25;"
        expect = "const,MaxSize,=,100,+,25,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_others_182(self):
        input = "var x [5][5][5][5]int;"
        expect = "var,x,[,5,],[,5,],[,5,],[,5,],int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_others_183(self):
        input = '''
            func main() {
                var x int = 10;
                var y int = 20;
                var z int = x + y;
                PutIntLn(z);
            }
        '''
        expect = "func,main,(,),{,var,x,int,=,10,;,var,y,int,=,20,;,var,z,int,=,x,+,y,;,PutIntLn,(,z,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_others_184(self):
        input = '''
            // Recursive function to calculate the factorial of a number
            func factorial(n int) int {
                if n == 0 {
                    return 1;
                }
                return n * factorial(n - 1);
            }
        '''
        expect = "func,factorial,(,n,int,),int,{,if,n,==,0,{,return,1,;,},return,n,*,factorial,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_comment_185(self):
        input = "// This is a single-line comment."
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_multi_comment_186(self):
        input = '''
            /* This is a
            multi-line comment */
        '''
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_nested_comment_187(self):
        input = "12"
        expect = ""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))
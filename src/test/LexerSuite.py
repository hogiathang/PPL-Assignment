import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_single_line_comment_101(self):
        input = "// Single-line comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 101))

    def test_multi_line_comment_102(self):
        input = "/* Multi-line\ncomment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test_nested_comment_103(self):
        input = "/* Nested /* //PPPPPPPP comment */ */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_unclosed_comment_104(self):
        input = "/* Unclosed comment"
        expect = "/,*,Unclosed,comment,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_valid_identifier_105(self):
        input = "aXc_123_Xc_Z"
        expect = "aXc_123_Xc_Z,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_invalid_id_start_with_number_106(self):
        input = "123var"
        expect = "123,var,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_keyword_as_id_107(self):
        input = "If"
        expect = "If,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_keyword_func_108(self):
        input = "func"
        expect = "func,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_keyword_true_109(self):
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_keyword_nil_110(self):
        input = "nil"
        expect = "nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_operator_plus_111(self):
        input = "+"
        expect = "+,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_operator_declare_112(self):
        input = ":="
        expect = ":=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test_operator_mod_assign_113(self):
        input = "%="
        expect = "%=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_separator_comma_114(self):
        input = ","
        expect = ",,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_separator_semicolon_115(self):
        input = ";"
        expect = ";,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test_decimal_int_116(self):
        input = "42"
        expect = "42,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_hex_int_117(self):
        input = "0x1F"
        expect = "0x1F,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_invalid_bin_int_118(self):
        input = "0b12"
        expect = "0b1,2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_valid_float_119(self):
        input = "2.0e+10"
        expect = "2.0e+10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_invalid_float_120(self):
        input = "1.2.3"
        expect = "1.2,.,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    def test_string_escape_121(self):
        input = "\"Hello\\nWorld\""
        expect = "Hello\\nWorld,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_unclosed_string_122(self):
        input = "\"Unclosed string"
        expect = """Unclosed string: Unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_boolean_literal_123(self):
        input = "false"
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_nil_literal_124(self):
        input = "nil"
        expect = "nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_arithmetic_expr_125(self):
        input = "x := 10 + 5 * 3"
        expect = "x,:=,10,+,5,*,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_array_access_126(self):
        input = "arr[2][3]"
        expect = "arr,[,2,],[,3,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_invalid_char_127(self):
        input = "@var"
        expect = "ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_invalid_escape_128(self):
        input = "\"Hello\\q\""
        expect = """Illegal escape in string: Hello\\q"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_struct_literal_129(self):
        input = "Person{name: \"Alice\"}"
        expect = "Person,{,name,:,Alice,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_function_decl_130(self):
        input = "func main() { }"
        expect = "func,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_error_token_131(self):
        input = "var@value = 10"  # Ký tự '@' không hợp lệ
        expect = "var,ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_error_token_132(self):
        input = "x# = 5"  # Ký tự '#' không hợp lệ
        expect = "x,ErrorToken #"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_error_token_133(self):
        input = "price$ = 100.5"  # Ký tự '$' không hợp lệ
        expect = "price,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

    def test_unclosed_string_134(self):
        input = "\"Hello World"  # Thiếu dấu đóng "
        expect = '''Unclosed string: Hello World'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_replace_newline_by_semi(self):
        input = '''
        AAAA
        "This is a test \\n "
        BBB
        2222
        ydywgdywg
        '''
        expect = '''AAAA,;,This is a test \\n ,;,BBB,;,2222,;,ydywgdywg,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_error_string_literal_136(self):
        input = '''
        "this is a string"
        '''
        expect = """this is a string,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_backslash(self):
        input = """
        "C:\\\\Document\\\\Download\\\\hello.py"
        """
        expect = "C:\\\\Document\\\\Download\\\\hello.py,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_newline_backslash(self):
        input = '''"This is line 1\\nThis is line 2\\nThis is line 3"'''
        expect = "This is line 1\\nThis is line 2\\nThis is line 3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_illegal_hex_escape_139(self):
        input = "\"Invalid escape \\x1F\""  # \x không được hỗ trợ
        expect = """Illegal escape in string: Invalid escape \\x"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_mixed_errors_140(self):
        input = "func main() {\n  str = \"Unclosed\\e\n  x@ = 5;\n}"
        expect = """func,main,(,),{,str,=,Illegal escape in string: Unclosed\\e"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_empty_unclosed_string_141(self):
        input = "\""  # Chuỗi rỗng không đóng
        expect = "Unclosed string: "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    def test_escape_before_eof_142(self):
        input = "\"Backslash at end\\x\""  # Thêm ký tự 'x' và đóng chuỗi
        expect = '''Illegal escape in string: Backslash at end\\x'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    def test_mixed_valid_and_error_143(self):
        input = '''
            x := 10 + "Hello\\mWorld"  // Illegal escape
            arr[5] = {1, 2, 3}


            y@ = 5.5 
        '''
        expect = '''x,:=,10,+,Illegal escape in string: Hello\\m'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_mixed_unclosed_string_144(self):
        input = '''/* Start of code *//* Start of code *//* Start of code *//* Start of code *//* Start of code */ 
            /* Start of code */
            func main() {
                s = "Unclosed string
                print(s)
                x = 10 % 3
            }
            Hello World

        '''
        expect = '''func,main,(,),{,s,=,Unclosed string: Unclosed string'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test_complex_expression_145(self):
        input = ''' 
            type Point struct { x, y int }
            points := [3]Point{{1,2}, {3,4}, {5,6}}
            distance := points[0].x * points[1].y 
        '''
        expect = "type,Point,struct,{,x,,,y,int,},;,points,:=,[,3,],Point,{,{,1,,,2,},,,{,3,,,4,},,,{,5,,,6,},},;,distance,:=,points,[,0,],.,x,*,points,[,1,],.,y,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test_mixed_illegal_escape_146(self):
        input = ''' 
            s = "Line1\\nLine2\\kLine3"
            if s == "Error" { 
                return true 
            }
        '''
        expect = '''s,=,Illegal escape in string: Line1\\nLine2\\k'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_multiple_errors_147(self):
        input = ''' 
            func main() {
                x = 0xF3  // Hex Value
                s = "Hello\\"
                y = 5.67  // Float Value
                z = $value 
            }
        '''
        expect = '''func,main,(,),{,x,=,0xF3,;,s,=,Unclosed string: Hello\\"'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_error_token_148(self):
        input = '''x = 5 $ y = 10'''
        expect = "x,=,5,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_error_token_149(self):
        input = '''func main() { print("Hi"); # }'''
        expect = "func,main,(,),{,print,(,Hi,),;,ErrorToken #"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_function_declaration_150(self):
        input = """func sum(a int, b int) int { return a + b }"""
        expect = "func,sum,(,a,int,,,b,int,),int,{,return,a,+,b,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_for_range_array_151(self):
        input = """for i, v := range arr { putIntLn(v) }"""
        expect = "for,i,,,v,:=,range,arr,{,putIntLn,(,v,),},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_nested_struct_152(self):
        input = """type Address struct { city string; zip int }
                   type Person struct { name string; addr Address }"""
        expect = "type,Address,struct,{,city,string,;,zip,int,},;,type,Person,struct,{,name,string,;,addr,Address,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_operator_precedence_153(self):
        input = """x := (a + b) * c / d % e"""
        expect = "x,:=,(,a,+,b,),*,c,/,d,%,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_mixed_escape_string_154(self):
        input = """s = "Line1\\nLine2\\kLine3" """
        expect = "s,=,Illegal escape in string: Line1\\nLine2\\k"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_invalid_char_in_expression_155(self):
        input = """result = x @ y + z"""
        expect = "result,=,x,ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_nested_if_else_156(self):
        input = """if (a > b) { 
            if (c < d) { return true } 
        } else { return false }"""
        expect = "if,(,a,>,b,),{,if,(,c,<,d,),{,return,true,},;,},else,{,return,false,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_multi_dim_array_157(self):
        input = """var matrix [3][3]int = [[1,2,3], [4,5,6], [7,8,9]]"""
        expect = "var,matrix,[,3,],[,3,],int,=,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],,,[,7,,,8,,,9,],],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_unclosed_string_in_func_158(self):
        input = """func greet() { s = "Hello, World }"""
        expect = "func,greet,(,),{,s,=,Unclosed string: Hello, World }"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_break_continue_159(self):
        input = """for i := 0; i < 10; i++ { 
            if i == 5 { break } 
            else { continue } 
        }"""
        expect = "for,i,:=,0,;,i,<,10,;,i,+,+,{,if,i,==,5,{,break,},;,else,{,continue,},;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test_struct_assignment_160(self):
        input = """p.name = "Alice"; p.age = 30"""
        expect = "p,.,name,=,Alice,;,p,.,age,=,30,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_invalid_hex_161(self):
        input = """x = 0xGHI"""
        expect = "x,=,0,xGHI,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_interface_method_162(self):
        input = """type Shape interface { Area() float }"""
        expect = "type,Shape,interface,{,Area,(,),float,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_dollar_in_variable_163(self):
        input = """var $count = 10"""
        expect = "var,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test_for_no_condition_164(self):
        input = """for { /* Infinite loop */ }"""
        expect = "for,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_invalid_float_165(self):
        input = """x = 12.34.56"""
        expect = "x,=,12.34,.,56,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_array_in_struct_166(self):
        input = """s.points[0] = 100"""
        expect = "s,.,points,[,0,],=,100,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    def test_unclosed_comment_167(self):
        input = """/* This is an unclosed comment"""
        expect = "/,*,This,is,an,unclosed,comment,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_complex_logic_expr_168(self):
        input = """if (a > 5 && b < 10 || c == 0) { return }"""
        expect = "if,(,a,>,5,&&,b,<,10,||,c,==,0,),{,return,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_escape_at_end_169(self):
        input = """s = "End with backslash\\" """
        expect = '''s,=,Unclosed string: End with backslash\\" '''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_const_with_expr_170(self):
        input = """const MAX = 100 + 50"""
        expect = "const,MAX,=,100,+,50,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_unclosed_struct_171(self):
        input = """type Point struct { x int; y int"""
        expect = "type,Point,struct,{,x,int,;,y,int,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_compound_assignment_172(self):
        input = """x += y * z / 2"""
        expect = "x,+=,y,*,z,/,2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_special_char_in_func_173(self):
        input = """func calc$sum() { return 0 }"""
        expect = "func,calc,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_empty_string_escape_174(self):
        input = """s = ""; t = "\\t" """
        expect = "s,=,,;,t,=,\\t,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_array_missing_size_175(self):
        input = """var arr []int = {1,2,3}"""
        expect = "var,arr,[,],int,=,{,1,,,2,,,3,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_func_missing_param_176(self):
        input = """func add(int, int) int { return 0 }"""
        expect = "func,add,(,int,,,int,),int,{,return,0,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_string_comparison_177(self):
        input = """if (s1 == s2) { print("Equal") }"""
        expect = "if,(,s1,==,s2,),{,print,(,Equal,),},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_invalid_octal_178(self):
        input = """x = 0o89"""
        expect = "x,=,0,o89,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_method_call_179(self):
        input = """calc.Add(5, 3)"""
        expect = "calc,.,Add,(,5,,,3,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_duplicate_var_180(self):
        input = """var x = 5; var x = 10"""
        expect = "var,x,=,5,;,var,x,=,10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_logical_not_181(self):
        input = """if !(a && b) { return }"""
        expect = "if,!,(,a,&&,b,),{,return,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_unicode_in_string_182(self):
        input = """s = "DOG" """
        expect = "s,=,DOG,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_struct_missing_name_183(self):
        input = """type struct { x int }"""
        expect = "type,struct,{,x,int,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_multi_var_for_184(self):
        input = """for i, j := 0, 10; i < j; i++ { }"""
        expect = "for,i,,,j,:=,0,,,10,;,i,<,j,;,i,+,+,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_empty_interface_185(self):
        input = """type Empty interface { }"""
        expect = "type,Empty,interface,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_bitwise_operator_186(self):
        input = """x = y | z"""
        expect = "x,=,y,ErrorToken |"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_const_no_value_187(self):
        input = """const PI"""
        expect = "const,PI,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test_nil_in_expr_188(self):
        input = """if ptr == nil { return }"""
        expect = "if,ptr,==,nil,{,return,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_special_char_in_number_189(self):
        input = """x = 123$45"""
        expect = "x,=,123,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_slice_decl_190(self):
        input = """s := arr[1:5]"""
        expect = "s,:=,arr,[,1,:,5,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_function_unary_191(self):
        input = """func foo(x int, y int) int { return x + -y }"""
        expect = "func,foo,(,x,int,,,y,int,),int,{,return,x,+,-,y,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_negative_array_size_192(self):
        input = """var arr [-5]int"""
        expect = "var,arr,[,-,5,],int,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test_keyword_as_var_193(self):
        input = """var func = 10"""
        expect = "var,func,=,10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_escape_special_char_194(self):
        input = """s = "Hello\\"World\""""
        expect = "s,=,Hello\\\"World,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test_method_no_receiver_195(self):
        input = """func ( ) Greet() { }"""
        expect = "func,(,),Greet,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_multiple_unary_196(self):
        input = """x = ---5"""
        expect = "x,=,-,-,-,5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test_duplicate_struct_field_197(self):
        input = """type Point struct { x int; x float }"""
        expect = "type,Point,struct,{,x,int,;,x,float,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test_full_program_198(self):
        input= '''
        const Pi = 3.14;  

        func main() {  
            var radius float = 5.0;  
            area := Pi * radius * radius;  
            putString("Area: ")  
            putFloatln(area);  
        }  
        '''
        expect = "const,Pi,=,3.14,;,func,main,(,),{,var,radius,float,=,5.0,;,area,:=,Pi,*,radius,*,radius,;,putString,(,Area: ,),;,putFloatln,(,area,),;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test_full_program_199(self):
        input= '''
        type Shape interface {  
            Area() float;  
        }  

        type Circle struct {  
            radius float;  
        }  

        func (c Circle) Area() float {  
            return 3.14 * c.radius * c.radius;  
        }  

        func main() {  
            c := Circle{radius: 3.0};  
            var s Shape = c;  
            putString("Square: ");  
            putFloatln(s.Area());  
        } 
        '''
        expect= "type,Shape,interface,{,Area,(,),float,;,},;,type,Circle,struct,{,radius,float,;,},;,func,(,c,Circle,),Area,(,),float,{,return,3.14,*,c,.,radius,*,c,.,radius,;,},;,func,main,(,),{,c,:=,Circle,{,radius,:,3.0,},;,var,s,Shape,=,c,;,putString,(,Square: ,),;,putFloatln,(,s,.,Area,(,),),;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

    def test_full_program_200(self):
        input='''
        func main() {  
            // For loop with condition
            for i := 0; i < 5; i += 1 {  
                if i == 2 {  
                    continue;  
                }  
                putIntLn(i);  
            }  

            // For loop with range  
            arr := [3]int{10, 20, 30};  
            sum := 0;  
            for _, val := range arr {  
                sum += val;  
            }  
            putString("Sum: ");  
            putIntLn(sum);  
        } 
        '''
        expect= "func,main,(,),{,for,i,:=,0,;,i,<,5,;,i,+=,1,{,if,i,==,2,{,continue,;,},;,putIntLn,(,i,),;,},;,arr,:=,[,3,],int,{,10,,,20,,,30,},;,sum,:=,0,;,for,_,,,val,:=,range,arr,{,sum,+=,val,;,},;,putString,(,Sum: ,),;,putIntLn,(,sum,),;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
    
    def test_lex_parser_201(self):
        input = '''
        func (c Circle) Draw() string {
            return "Drawing circle at (" + toString(c.center.x) + "," + toString(c.center.y) + ")";
        }
        '''
        expect = "type,Counter,struct,{,value,int,;,},;,func,(,c,Counter,),inc,(,),{,c,.,value,+=,1,;,},;,func,main,(,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 201))
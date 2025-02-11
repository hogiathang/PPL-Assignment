import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))

    def test_valid_identifier_105(self):
        input = "// Single-line comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_multi_line_comment_106(self):
        input = "/* Multi-line\ncomment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_keyword_as_id_107(self):
        input = """
            var x := 100

        """
        expect = "var,x,:=,100,;,<EOF>"
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
        expect = "\"Hello\\nWorld\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_unclosed_string_122(self):
        input = "\"Unclosed string"
        expect = """Unclosed string: "Unclosed string"""
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
        expect = """Illegal escape in string: \"Hello\\q"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_struct_literal_129(self):
        input = "Person{name: \"Alice\"}"
        expect = """Person,{,name,:,"Alice",},<EOF>"""
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
        expect = """Unclosed string: \"Hello World"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_replace_newline_by_semi(self):
        input = '''
        AAAA
        "This is a test \\n "
        BBB
        2222
        ydywgdywg
        '''
        expect = '''AAAA,;,"This is a test \\n ",;,BBB,;,2222,;,ydywgdywg,;,<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_error_string_literal_136(self):
        input = '''
        "this is a string"
        '''
        expect = """\"this is a string\",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_backslash(self):
        input = """
        "C:\\\\Document\\\\Download\\\\hello.py"
        """
        expect = """"C:\\\\Document\\\\Download\\\\hello.py",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_newline_backslash(self):
        input = '''"This is line 1\\nThis is line 2\\nThis is line 3"'''
        expect = '''"This is line 1\\nThis is line 2\\nThis is line 3",<EOF>'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_illegal_hex_escape_139(self):
        input = "\"Invalid escape \\x1F\""  # \x không được hỗ trợ
        expect = """Illegal escape in string: \"Invalid escape \\x"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_mixed_errors_140(self):
        input = "func main() {\n  str = \"Unclosed\\e\n  x@ = 5;\n}"
        expect = """func,main,(,),{,str,=,Illegal escape in string: \"Unclosed\\e"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_empty_unclosed_string_141(self):
        input = "\""  # Chuỗi rỗng không đóng
        expect = "Unclosed string: \""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    def test_escape_before_eof_142(self):
        input = "\"Backslash at end\\x\""  # Thêm ký tự 'x' và đóng chuỗi
        expect = '''Illegal escape in string: \"Backslash at end\\x'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    def test_mixed_valid_and_error_143(self):
        input = '''
            x := 10 + "Hello\\mWorld"  // Illegal escape
            arr[5] = {1, 2, 3}


            y@ = 5.5 
        '''
        expect = '''x,:=,10,+,Illegal escape in string: "Hello\\m'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_mixed_unclosed_string_144(self):
        input = '''func().attr[3][3][4].get(3,4,5).make := 123455'''
        expect = '''func,(,),.,attr,[,3,],[,3,],[,4,],.,get,(,3,,,4,,,5,),.,make,:=,123455,<EOF>'''
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
        expect = '''s,=,Illegal escape in string: \"Line1\\nLine2\\k'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_multiple_errors_147(self):
        input = ''' 
            func main() {
                x = 0xF3  // Hex Value
                s = "Hello\\""
                y = 5.67  // Float Value
                z = $value 
            }
        '''
        expect = '''func,main,(,),{,x,=,0xF3,;,s,=,"Hello\\"",;,y,=,5.67,;,z,=,ErrorToken $'''
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_error_token_148(self):
        input = '''x = 5 $ y = 10'''
        expect = "x,=,5,ErrorToken $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_error_token_149(self):
        input = '''func main() { print("Hi"); # }'''
        expect = "func,main,(,),{,print,(,\"Hi\",),;,ErrorToken #"
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
        expect = "s,=,Illegal escape in string: \"Line1\\nLine2\\k"
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
        expect = """func,greet,(,),{,s,=,Unclosed string: "Hello, World }"""
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
        expect = """p,.,name,=,"Alice",;,p,.,age,=,30,<EOF>"""
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
        expect = '''s,=,Unclosed string: \"End with backslash\\" '''
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
        expect = """s,=,"",;,t,=,"\\t",<EOF>"""
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
        expect = "if,(,s1,==,s2,),{,print,(,\"Equal\",),},<EOF>"
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
        expect = """s,=,"DOG",<EOF>"""
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
        expect = "s,=,\"Hello\\\"World\",<EOF>"
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
        expect = "const,Pi,=,3.14,;,func,main,(,),{,var,radius,float,=,5.0,;,area,:=,Pi,*,radius,*,radius,;,putString,(,\"Area: \",),;,putFloatln,(,area,),;,},;,<EOF>"
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
        expect = "type,Shape,interface,{,Area,(,),float,;,},;,type,Circle,struct,{,radius,float,;,},;,func,(,c,Circle,),Area,(,),float,{,return,3.14,*,c,.,radius,*,c,.,radius,;,},;,func,main,(,),{,c,:=,Circle,{,radius,:,3.0,},;,var,s,Shape,=,c,;,putString,(,\"Square: \",),;,putFloatln,(,s,.,Area,(,),),;,},;,<EOF>"
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
        expect= "func,main,(,),{,for,i,:=,0,;,i,<,5,;,i,+=,1,{,if,i,==,2,{,continue,;,},;,putIntLn,(,i,),;,},;,arr,:=,[,3,],int,{,10,,,20,,,30,},;,sum,:=,0,;,for,_,,,val,:=,range,arr,{,sum,+=,val,;,},;,putString,(,\"Sum: \",),;,putIntLn,(,sum,),;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
    
#     def test_lex(self):
#         input = '''func main() {
#         var x int //;
#         x = 1
#         if x > 0 {
#             putString("Positive")
#         } else {
#             putString("Non-positive")
#         }
#     }'''
#         expect = '''func,main,(,),{,var,x,int,;,x,=,1,;,if,x,>,0,{,putString,(,"Positive",),;,},else,{,putString,(,"Non-positive",),;,},;,},<EOF>'''
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 201))




#     def test_struct_with_method_and_constructor(self):
#         input = """
# type Point struct {
#     x int;
#     y int;
# }

# func newPoint(x int, y int) Point {
#     return Point{x: x, y: y};
# }

# func (p Point) distance() int {
#     return p.x * p.x + p.y * p.y;
# }

# func main() {
#     var p Point = newPoint(3, 4);
#     print(p.distance());
# }
# """
#         expect = """type,Point,struct,{,x,int,;,y,int,;,},;,func,newPoint,(,x,int,,,y,int,),Point,{,return,Point,{,x,:,x,,,y,:,y,},;,},;,func,(,p,Point,),distance,(,),int,{,return,p,.,x,*,p,.,x,+,p,.,y,*,p,.,y,;,},;,func,main,(,),{,var,p,Point,=,newPoint,(,3,,,4,),;,print,(,p,.,distance,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

#     def test_function_with_for_if_1(self):
#         input = """
#         func foo() {
#             for i := 0; i < 5; i+=1 {
#                 if (i % 2 == 0) {
#                     print("Even");
#                 } else {
#                     print("Odd");
#                 }
#             }
#         }"""
#         expect = """func,foo,(,),{,for,i,:=,0,;,i,<,5,;,i,+=,1,{,if,(,i,%,2,==,0,),{,print,(,"Even",),;,},else,{,print,(,"Odd",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

#     def test_function_with_for_if_2(self):
#         input = """
#         func bar() {
#             for i := 1; i <= 10; i+=1 {
#                 if (i % 3 == 0) {
#                     print("Divisible by 3");
#                 } else {
#                     print("Not divisible by 3");
#                 }
#             }
#         }"""
#         expect = """func,bar,(,),{,for,i,:=,1,;,i,<=,10,;,i,+=,1,{,if,(,i,%,3,==,0,),{,print,(,"Divisible by 3",),;,},else,{,print,(,"Not divisible by 3",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

#     def test_function_with_for_if_3(self):
#         input = """
#         func baz() {
#             for i := 0; i < 20; i+=2 {
#                 if (i % 4 == 0) {
#                     print("Divisible by 4");
#                 } else {
#                     print("Not divisible by 4");
#                 }
#             }
#         }"""
#         expect = """func,baz,(,),{,for,i,:=,0,;,i,<,20,;,i,+=,2,{,if,(,i,%,4,==,0,),{,print,(,"Divisible by 4",),;,},else,{,print,(,"Not divisible by 4",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

#     def test_function_with_for_if_4(self):
#         input = """
#         func qux() {
#             for i := 10; i > 0; i-=1 {
#                 if (i % 2 == 0) {
#                     print("Even");
#                 } else {
#                     print("Odd");
#                 }
#             }
#         }"""
#         expect = """func,qux,(,),{,for,i,:=,10,;,i,>,0,;,i,-=,1,{,if,(,i,%,2,==,0,),{,print,(,"Even",),;,},else,{,print,(,"Odd",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

#     def test_function_with_for_if_5(self):
#         input = """
#         func quux() {
#             for i := 5; i <= 15; i+=1 {
#                 if (i % 5 == 0) {
#                     print("Divisible by 5");
#                 } else {
#                     print("Not divisible by 5");
#                 }
#             }
#         }"""
#         expect = """func,quux,(,),{,for,i,:=,5,;,i,<=,15,;,i,+=,1,{,if,(,i,%,5,==,0,),{,print,(,"Divisible by 5",),;,},else,{,print,(,"Not divisible by 5",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

#     def test_function_with_for_if_6(self):
#         input = """
#         func corge() {
#             for i := 0; i < 10; i+=1 {
#                 if (i % 2 == 0) {
#                     print("Even");
#                 } else {
#                     print("Odd");
#                 }
#             }
#         }"""
#         expect = """func,corge,(,),{,for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,%,2,==,0,),{,print,(,"Even",),;,},else,{,print,(,"Odd",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

#     def test_function_with_for_if_7(self):
#         input = """
#         func grault() {
#             for i := 1; i <= 5; i+=1 {
#                 if (i % 2 == 0) {
#                     print("Even");
#                 } else {
#                     print("Odd");
#                 }
#             }
#         }"""
#         expect = """func,grault,(,),{,for,i,:=,1,;,i,<=,5,;,i,+=,1,{,if,(,i,%,2,==,0,),{,print,(,"Even",),;,},else,{,print,(,"Odd",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

#     def test_function_with_for_if_8(self):
#         input = """
#         func garply() {
#             for i := 0; i < 8; i+=1 {
#                 if (i % 4 == 0) {
#                     print("Divisible by 4");
#                 } else {
#                     print("Not divisible by 4");
#                 }
#             }
#         }"""
#         expect = """func,garply,(,),{,for,i,:=,0,;,i,<,8,;,i,+=,1,{,if,(,i,%,4,==,0,),{,print,(,"Divisible by 4",),;,},else,{,print,(,"Not divisible by 4",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

#     def test_function_with_for_if_9(self):
#         input = """
#         func waldo() {
#             for i := 2; i <= 10; i+=2 {
#                 if (i % 3 == 0) {
#                     print("Divisible by 3");
#                 } else {
#                     print("Not divisible by 3");
#                 }
#             }
#         }"""
#         expect = """func,waldo,(,),{,for,i,:=,2,;,i,<=,10,;,i,+=,2,{,if,(,i,%,3,==,0,),{,print,(,"Divisible by 3",),;,},else,{,print,(,"Not divisible by 3",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

#     def test_function_with_for_if_10(self):
#         input = """
#         func fred() {
#             for i := 1; i <= 7; i+=1 {
#                 if (i % 2 == 0) {
#                     print("Even");
#                 } else {
#                     print("Odd");
#                 }
#             }
#         }"""
#         expect = """func,fred,(,),{,for,i,:=,1,;,i,<=,7,;,i,+=,1,{,if,(,i,%,2,==,0,),{,print,(,"Even",),;,},else,{,print,(,"Odd",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

#     def test_var_declaration(self):
#         input = "var x int;"
#         expect = "var,x,int,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

#     def test_var_declaration_with_initialization(self):
#         input = "var x int = 10;"
#         expect = "var,x,int,=,10,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

#     def test_var_declaration_multiple(self):
#         input = "var x, y, z int;"
#         expect = "var,x,,,y,,,z,int,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

#     def test_var_declaration_with_initialization_multiple(self):
#         input = "var x, y, z int = 1, 2, 3;"
#         expect = "var,x,,,y,,,z,int,=,1,,,2,,,3,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

#     def test_var_declaration_with_type_inference(self):
#         input = "var x = 10;"
#         expect = "var,x,=,10,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

#     def test_assignment_1(self):
#         input = "x := 5;"
#         expect = "x,:=,5,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

#     def test_assignment_2(self):
#         input = "y := x + 3;"
#         expect = "y,:=,x,+,3,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

#     def test_assignment_3(self):
#         input = "z := x * y - 2;"
#         expect = "z,:=,x,*,y,-,2,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

#     def test_assignment_4(self):
#         input = "a := b / 2 + 1;"
#         expect = "a,:=,b,/,2,+,1,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

#     def test_assignment_5(self):
#         input = "b := (x + y) * z;"
#         expect = "b,:=,(,x,+,y,),*,z,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

#     def test_complex_expression_1(self):
#         input = "a := (x + y) * (z - w) / (u % v);"
#         expect = "a,:=,(,x,+,y,),*,(,z,-,w,),/,(,u,%,v,),;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

#     def test_complex_expression_2(self):
#         input = "b := (a && b) || (c && !d);"
#         expect = "b,:=,(,a,&&,b,),||,(,c,&&,!,d,),;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

#     def test_complex_expression_3(self):
#         input = "c := (x > y) && (z <= w) || (u != v);"
#         expect = "c,:=,(,x,>,y,),&&,(,z,<=,w,),||,(,u,!=,v,),;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

#     def test_complex_expression_4(self):
#         input = "d := (a + b) * (c - d) / (e % f) == g;"
#         expect = "d,:=,(,a,+,b,),*,(,c,-,d,),/,(,e,%,f,),==,g,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

#     def test_complex_expression_5(self):
#         input = "e := (x && y) || (z && !w) && (u || v);"
#         expect = "e,:=,(,x,&&,y,),||,(,z,&&,!,w,),&&,(,u,||,v,),;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

#     def test_complex_expression_6(self):
#         input = "f := (a + b - c) * (d / e % f) + g;"
#         expect = "f,:=,(,a,+,b,-,c,),*,(,d,/,e,%,f,),+,g,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

#     def test_complex_expression_7(self):
#         input = "g := (x || y) && (z || !w) || (u && v);"
#         expect = "g,:=,(,x,||,y,),&&,(,z,||,!,w,),||,(,u,&&,v,),;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

#     def test_complex_expression_8(self):
#         input = "h := (a * b + c) / (d - e % f) == g;"
#         expect = "h,:=,(,a,*,b,+,c,),/,(,d,-,e,%,f,),==,g,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

#     def test_complex_expression_9(self):
#         input = "i := (x && y) || (z && !w) && (u || v) == w;"
#         expect = "i,:=,(,x,&&,y,),||,(,z,&&,!,w,),&&,(,u,||,v,),==,w,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

#     def test_complex_expression_10(self):
#         input = "j := (a + b) * (c - d) / (e % f) + g == h;"
#         expect = "j,:=,(,a,+,b,),*,(,c,-,d,),/,(,e,%,f,),+,g,==,h,;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

#     def test_whole_program_1(self):
#         input = """
#         var x int = 10;
#         var y int = 20;
#         var z int = x + y;
#         func main() {
#             print(z);
#         }
#         """
#         expect = """var,x,int,=,10,;,var,y,int,=,20,;,var,z,int,=,x,+,y,;,func,main,(,),{,print,(,z,),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

#     def test_whole_program_2(self):
#         input = """
#         type Person struct {
#             name string;
#             age int;
#         }

#         func (p Person) greet() string {
#             return "Hello, " + p.name;
#         }

#         func main() {
#             var p Person;
#             p.name = "Alice";
#             p.age = 30;
#             print(p.greet());
#         }
#         """
#         expect = """type,Person,struct,{,name,string,;,age,int,;,},;,func,(,p,Person,),greet,(,),string,{,return,"Hello, ",+,p,.,name,;,},;,func,main,(,),{,var,p,Person,;,p,.,name,=,"Alice",;,p,.,age,=,30,;,print,(,p,.,greet,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 200))

#     def test_lex(self):
#         input = '''func main() {
#         var x int //;
#         x = 1
#         if x > 0 {
#             putString("Positive")
#         } else {
#             putString("Non-positive")
#         }
#     }'''
#         expect = """func,main,(,),{,var,x,int,;,x,=,1,;,if,x,>,0,{,putString,(,"Positive",),;,},else,{,putString,(,"Non-positive",),;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 401))


#     def test_lower_identifier(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
#     def test_upper_identifier(self):
#         self.assertTrue(TestLexer.checkLexeme("ABC","ABC,<EOF>",102))
    
#     def test_hyphen_identifier(self):
#         self.assertTrue(TestLexer.checkLexeme("_ABC1","_ABC1,<EOF>",103))

#     def test_wrong_token(self):
#         self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",104))
    
#     def test_keyword_var(self):
#         """test keyword var"""
#         self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",105))
    
#     def test_keyword_func(self):
#         """test keyword func"""
#         self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",106))

#     def test_integer(self):
#         """test integers"""
#         self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",107))

#     def test_binary(self):
#         self.assertTrue(TestLexer.checkLexeme("0b101","0b101,<EOF>",108))

#     def test_octal(self):
#         self.assertTrue(TestLexer.checkLexeme("0o123","0o123,<EOF>",109))

#     def test_hex(self):
#         self.assertTrue(TestLexer.checkLexeme("0x123","0x123,<EOF>",110))
    
#     def test_float(self):
#         """test floats"""
#         self.assertTrue(TestLexer.checkLexeme("123.123","123.123,<EOF>",111))
    
#     def test_float_with_dot(self):
#         self.assertTrue(TestLexer.checkLexeme("123.","123.,<EOF>",112))

#     def test_float_with_e(self):
#         """test floats"""
#         self.assertTrue(TestLexer.checkLexeme("123.123e-123","123.123e-123,<EOF>",113))

#     def test_string_abc(self):
#         """test strings"""
#         self.assertTrue(TestLexer.checkLexeme("\"abc\"","\"abc\",<EOF>",114))
    
#     def test_string_abc_def(self):
#         self.assertTrue(TestLexer.checkLexeme("\"abc def\"","\"abc def\",<EOF>",115))
    
#     def test_string_with_escape(self):
#         self.assertTrue(TestLexer.checkLexeme("\"abc\\r\\n\\t\\\"\\\\\"","\"abc\\r\\n\\t\\\"\\\\\",<EOF>",116))
        
#     def test_numerical_operations(self):
#         self.assertTrue(TestLexer.checkLexeme("a := 5", "a,:=,5,<EOF>",117))
    
#     def test_string_declaration(self):
#         self.assertTrue(TestLexer.checkLexeme("var a string = \"lol\";", "var,a,string,=,\"lol\",;,<EOF>",118))

#     def test_declaration_var_arr(self):
#         self.assertTrue(TestLexer.checkLexeme("var arr [5]int;", "var,arr,[,5,],int,;,<EOF>",119))

#     def test_declaration_var_arr_2d(self):
#         self.assertTrue(TestLexer.checkLexeme("var arr [5][5]int{{1,2},{3,4}};", "var,arr,[,5,],[,5,],int,{,{,1,,,2,},,,{,3,,,4,},},;,<EOF>",120))        

#     def test_array_access(self):
#         self.assertTrue(TestLexer.checkLexeme("arr[1][2]", "arr,[,1,],[,2,],<EOF>",121))
    
#     def test_declaration_func_foo(self):
#         self.assertTrue(TestLexer.checkLexeme("func foo(x int, y int) int", "func,foo,(,x,int,,,y,int,),int,<EOF>",122))

#     def test_single_line_comment(self):
#         self.assertTrue(TestLexer.checkLexeme("// faf //","<EOF>",123))
    
#     def test_single_line_comment_with_code(self):
#         self.assertTrue(TestLexer.checkLexeme("// this is a comment \n hello world","hello,world,<EOF>",124))
    
#     def test_block_comment(self):
#         self.assertTrue(TestLexer.checkLexeme("/* faf */","<EOF>",125))
    
#     # def test_unclosed_block_comment(self):
#     #     self.assertTrue(TestLexer.checkLexeme("/* faf","ErrorToken /*",126))

#     def test_block_comment_with_code(self):
#         self.assertTrue(TestLexer.checkLexeme("/* faf */ faf /* faf */","faf,<EOF>",127))
    
#     def test_block_comment_with_single_line_comment(self):
#         self.assertTrue(TestLexer.checkLexeme("/* faf */ // faf /* faf */","<EOF>",128))

#     def test_nested_multi_line_comment(self):
#         self.assertTrue(TestLexer.checkLexeme("/* /* faf */ /* faf */ */","<EOF>",129))
    
#     def test_eol(self): 
#         input = """var a int \nvar b int \r\nvar c int; var d int"""
#         expect = """var,a,int,;,var,b,int,;,var,c,int,;,var,d,int,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,130))

#     def test_expression(self):
#         input = """a := -(5 + 3 - 2) * 4 / 2 % 1 == true && false"""
#         expect = """a,:=,-,(,5,+,3,-,2,),*,4,/,2,%,1,==,true,&&,false,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,131))

#     def test_bool_expression(self):
#         input = """a := !true && b || true"""
#         expect = """a,:=,!,true,&&,b,||,true,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,132))

#     def test_compare_expression(self):
#         input = """a := 5 > 3 && 3 <= 5"""
#         expect = """a,:=,5,>,3,&&,3,<=,5,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,133))

#     def test_string_expression(self):
#         input = """a := "abc" + "def" == "abcdef" """
#         expect = """a,:=,"abc",+,"def",==,"abcdef",<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,134))

#     def test_funcion(self):
#         input = """
#         func foo(x int, y int) int {
#             return x + -y;
#         }"""
#         expect = """func,foo,(,x,int,,,y,int,),int,{,return,x,+,-,y,;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,135))

#     def test_function_call(self):
#         input = """foo(1, 2);"""
#         expect = """foo,(,1,,,2,),;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,136))
    
#     def test_function_with_block(self):
#         input = """func foo() int {
#             if (true) {
#                 return 1;
#             } else {
#                 return 0;
#             }
#         }"""
#         expect = """func,foo,(,),int,{,if,(,true,),{,return,1,;,},else,{,return,0,;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,137))

#     def test_function_with_receiver(self):
#         input = """func (a A) foo() int {
#             return 1;
#         }"""
#         expect = """func,(,a,A,),foo,(,),int,{,return,1,;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,138))

#     def test_if(self):
#         input = """
#         func main() {
#             if (x > 0) {
#                 print("Positive");
#             } else {
#                 print("Negative");
#             }
#         }"""
#         expect = """func,main,(,),{,if,(,x,>,0,),{,print,(,"Positive",),;,},else,{,print,(,"Negative",),;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,139))
    
#     def test_for(self):
#         input = """


#         func main() {
#             for i < 10 {
#                 print(i)
#             }
#             for i := 0; i < 10; i+=1 {
#                 print(i);
#             }
#             for _, range arr {
#             };
#         }"""
#         expect = "func,main,(,),{,for,i,<,10,{,print,(,i,),;,},;,for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,},;,for,_,,,range,arr,{,},;,},<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input,expect,140))

#     def test_for_normal(self):
#         input = """for i := 0; i < 10; i+=1 {
#             print(i);
#         }"""
#         expect = """for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,141))
    
#     def test_for_range(self):
#         input = """for _, range arr {
#         };"""
#         expect = "for,_,,,range,arr,{,},;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input,expect,142))

#     def test_for_break(self):
#         input = """for i := 0; i < 10; i+=1 {
#             if (i == 5) {
#                 break;
#             }
#         }"""
#         expect = """for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,==,5,),{,break,;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,143))

#     def test_for_continue(self):
#         input = """for i := 0; i < 10; i+=1 {
#             if (i == 5) {
#                 continue;
#             }
#         }"""
#         expect = """for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,==,5,),{,continue,;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,144))

#     def test_struct_decl(self):
#         input = """type A struct {
#             x int;
#             y int;
#         }"""
#         expect = """type,A,struct,{,x,int,;,y,int,;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,145))

#     def test_struct_var_decl(self):
#         input = "var a struct = A{x: 1, y: 2};"
#         expect = """var,a,struct,=,A,{,x,:,1,,,y,:,2,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,146))

#     def test_struct_var_short_decl(self):
#         input = "a := A{x: 1, y: 2};"
#         expect = """a,:=,A,{,x,:,1,,,y,:,2,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,147))

#     def test_struct_access(self):
#         input = "a.x"
#         expect = "a,.,x,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input,expect,148))

#     def test_struct_access_in_func(self):
#         input = "func (a A) foo() int { return a.x; }"
#         expect = """func,(,a,A,),foo,(,),int,{,return,a,.,x,;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input,expect,149))

#     def test_interface_decl(self):
#         input = "type A interface { foo() int; };"
#         expect = "type,A,interface,{,foo,(,),int,;,},;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input,expect,150))

#     def test_method_call(self):
#         input = "a.foo();"
#         expect = "a,.,foo,(,),;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input,expect,151))

#     def test_unclosed_string_1(self):
#         self.assertTrue(TestLexer.checkLexeme("\"abc","Unclosed string: \"abc",152))

#     def test_unclosed_string_2(self):
#         self.assertTrue(TestLexer.checkLexeme("\"abc\n\"","Unclosed string: \"abc\n",153))
    
#     def test_illegal_escape_in_string_1(self):
#         self.assertTrue(TestLexer.checkLexeme("\"abc\\d\"","Illegal escape in string: \"abc\\d",154))
    
#     def test_illegal_escape_in_string_2(self):
#         self.assertTrue(TestLexer.checkLexeme("\"abc\\d\"","Illegal escape in string: \"abc\\d",155))

#     def test_float_with_e_2(self):
#         self.assertTrue(TestLexer.checkLexeme("123.e123","123.e123,<EOF>",156))

#     def test_function_for_if(self):
#         input = """
#         func foo() {
#             for i := 0; i < 10; i+=1 {
#                 if (i % 2 == 0) {
#                     print("Even");
#                 } else {
#                     print("Odd");
#                 }
#             }
#         }"""
#         expect = """func,foo,(,),{,for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,%,2,==,0,),{,print,(,"Even",),;,},else,{,print,(,"Odd",),;,},;,},;,},<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

#     def test_interface_struct_methods(self):
#         input = """
# type Shape interface {
#     area() float;
# }

# type Circle struct {
#     radius float;
# }

# func (c Circle) area() float {
#     return 3.14 * c.radius * c.radius;
# }

# func main() {
#     var c Circle;
#     c.radius = 5;
#     var s Shape = c;
#     print(s.area());
# }
# """
#         expect = "type,Shape,interface,{,area,(,),float,;,},;,type,Circle,struct,{,radius,float,;,},;,func,(,c,Circle,),area,(,),float,{,return,3.14,*,c,.,radius,*,c,.,radius,;,},;,func,main,(,),{,var,c,Circle,;,c,.,radius,=,5,;,var,s,Shape,=,c,;,print,(,s,.,area,(,),),;,},;,<EOF>"
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

#     def test_interface_with_method(self):
#         input = """
# type Animal interface {
#     speak() string;
# }

# type Dog struct {
#     name string;
# }

# func (d Dog) speak() string {
#     return "Woof";
# }
# """
#         expect = """type,Animal,interface,{,speak,(,),string,;,},;,type,Dog,struct,{,name,string,;,},;,func,(,d,Dog,),speak,(,),string,{,return,"Woof",;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

#     def test_interface_with_multiple_methods(self):
#         input = """
# type Animal interface {
#     speak() string;
#     move() string;
# }

# type Bird struct {
#     name string;
# }

# func (b Bird) speak() string {
#     return "Tweet";
# }

# func (b Bird) move() string {
#     return "Fly";
# }
# """
#         expect = """type,Animal,interface,{,speak,(,),string,;,move,(,),string,;,},;,type,Bird,struct,{,name,string,;,},;,func,(,b,Bird,),speak,(,),string,{,return,"Tweet",;,},;,func,(,b,Bird,),move,(,),string,{,return,"Fly",;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

#     def test_struct_with_method(self):
#         input = """
# type Rectangle struct {
#     width int;
#     height int;
# }

# func (r Rectangle) area() int {
#     return r.width * r.height;
# }
# """
#         expect = """type,Rectangle,struct,{,width,int,;,height,int,;,},;,func,(,r,Rectangle,),area,(,),int,{,return,r,.,width,*,r,.,height,;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

#     def test_struct_with_multiple_methods(self):
#         input = """
# type Rectangle struct {
#     width int;
#     height int;
# }

# func (r Rectangle) area() int {
#     return r.width * r.height;
# }

# func (r Rectangle) perimeter() int {
#     return 2 * (r.width + r.height);
# }
# """
#         expect = """type,Rectangle,struct,{,width,int,;,height,int,;,},;,func,(,r,Rectangle,),area,(,),int,{,return,r,.,width,*,r,.,height,;,},;,func,(,r,Rectangle,),perimeter,(,),int,{,return,2,*,(,r,.,width,+,r,.,height,),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

#     def test_struct_with_method_call(self):
#         input = """
# type Rectangle struct {
#     width int;
#     height int;
# }

# func (r Rectangle) area() int {
#     return r.width * r.height;
# }

# func main() {
#     var r Rectangle;
#     r.width = 5;
#     r.height = 10;
#     print(r.area());
# }
# """
#         expect = """type,Rectangle,struct,{,width,int,;,height,int,;,},;,func,(,r,Rectangle,),area,(,),int,{,return,r,.,width,*,r,.,height,;,},;,func,main,(,),{,var,r,Rectangle,;,r,.,width,=,5,;,r,.,height,=,10,;,print,(,r,.,area,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

#     def test_interface_with_struct_implementation(self):
#         input = """
# type Animal interface {
#     speak() string;
# }

# type Cat struct {
#     name string;
# }

# func (c Cat) speak() string {
#     return "Meow";
# }

# func main() {
#     var c Cat;
#     c.name = "Kitty";
#     var a Animal = c;
#     print(a.speak());
# }
# """
#         expect = """type,Animal,interface,{,speak,(,),string,;,},;,type,Cat,struct,{,name,string,;,},;,func,(,c,Cat,),speak,(,),string,{,return,"Meow",;,},;,func,main,(,),{,var,c,Cat,;,c,.,name,=,"Kitty",;,var,a,Animal,=,c,;,print,(,a,.,speak,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

#     def test_interface_with_multiple_structs(self):
#         input = """
# type Animal interface {
#     speak() string;
# }

# type Dog struct {
#     name string;
# }

# func (d Dog) speak() string {
#     return "Woof";
# }

# type Cat struct {
#     name string;
# }

# func (c Cat) speak() string {
#     return "Meow";
# }

# func main() {
#     var d Dog;
#     d.name = "Buddy";
#     var c Cat;
#     c.name = "Kitty";
#     var a1 Animal = d;
#     var a2 Animal = c;
#     print(a1.speak());
#     print(a2.speak());
# }
# """
#         expect = """type,Animal,interface,{,speak,(,),string,;,},;,type,Dog,struct,{,name,string,;,},;,func,(,d,Dog,),speak,(,),string,{,return,"Woof",;,},;,type,Cat,struct,{,name,string,;,},;,func,(,c,Cat,),speak,(,),string,{,return,"Meow",;,},;,func,main,(,),{,var,d,Dog,;,d,.,name,=,"Buddy",;,var,c,Cat,;,c,.,name,=,"Kitty",;,var,a1,Animal,=,d,;,var,a2,Animal,=,c,;,print,(,a1,.,speak,(,),),;,print,(,a2,.,speak,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

#     def test_interface_with_struct_method_call(self):
#         input = """
# type Animal interface {
#     speak() string;
# }

# type Dog struct {
#     name string;
# }

# func (d Dog) speak() string {
#     return "Woof";
# }

# func main() {
#     var d Dog;
#     d.name = "Buddy";
#     var a Animal = d;
#     print(a.speak());
# }
# """
#         expect = """type,Animal,interface,{,speak,(,),string,;,},;,type,Dog,struct,{,name,string,;,},;,func,(,d,Dog,),speak,(,),string,{,return,"Woof",;,},;,func,main,(,),{,var,d,Dog,;,d,.,name,=,"Buddy",;,var,a,Animal,=,d,;,print,(,a,.,speak,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

#     def test_struct_with_method_and_field_access(self):
#         input = """
# type Point struct {
#     x int;
#     y int;
# }

# func (p Point) distance() int {
#     return p.x * p.x + p.y * p.y;
# }

# func main() {
#     var p Point;
#     p.x = 3;
#     p.y = 4;
#     print(p.distance());
# }
# """
#         expect = """type,Point,struct,{,x,int,;,y,int,;,},;,func,(,p,Point,),distance,(,),int,{,return,p,.,x,*,p,.,x,+,p,.,y,*,p,.,y,;,},;,func,main,(,),{,var,p,Point,;,p,.,x,=,3,;,p,.,y,=,4,;,print,(,p,.,distance,(,),),;,},;,<EOF>"""
#         self.assertTrue(TestLexer.checkLexeme(input, expect, 167))
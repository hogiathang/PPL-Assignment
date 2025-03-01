import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab#sVN","ab,ErrorToken #",102))
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
        expect = """\"C:\\\\Document\\\\Download\\\\hello.py\",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_newline_backslash(self):
        input = '''"This is line 1\\nThis is line 2\\nThis is line 3"'''
        expect = '''\"This is line 1\\nThis is line 2\\nThis is line 3\",<EOF>'''
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
        expect = '''func,main,(,),{,x,=,0xF3,;,s,=,\"Hello\\"\",;,y,=,5.67,;,z,=,ErrorToken $'''
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

    def test_lexer_193(self):
        input = "00001e279.003"
        expect = "0,0,0,0,1,e279,.,0,0,3,<EOF>"
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
        expect = "func,main,(,),{,for,i,:=,0,;,i,<,5,;,i,+=,1,{,if,i,==,2,{,continue,;,},;,putIntLn,(,i,),;,},;,arr,:=,[,3,],int,{,10,,,20,,,30,},;,sum,:=,0,;,for,_,,,val,:=,range,arr,{,sum,+=,val,;,},;,putString,(,\"Sum: \",),;,putIntLn,(,sum,),;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))

    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>", 700))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>", 700))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>", 700))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_VOTien","_VOTien,<EOF>", 700))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>", 700))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11","0x11,<EOF>", 700))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 700))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", 700))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN","<EOF>", 700))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", 700))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 700))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", 700))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", 700))
        
    #!!! 87 test yêu cầu code chấm sau
    def test_014(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", 700))

    def test_015(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", 700))

    def test_016(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 700))

    def test_017(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 700))

    def test_018(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 700))

    def test_019(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /*
        /* a */ /* b */ 
        // 321231
        */ if /* */ /* */""", "if,<EOF>", 700))

    def test_020(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /*
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", 700))

    def test_021(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /* //123312
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", 700))

    def test_022(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/*", "/,*,<EOF>", 700))

    def test_023(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 700))

    def test_024(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 700))

    def test_025(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 700))

    def test_026(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 700))

    def test_027(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("A_2b_3", "A_2b_3,<EOF>", 700))

    def test_028(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_a__", "_a__,<EOF>", 700))

    def test_029(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("u_2_bB", "u_2_bB,<EOF>", 700))

    def test_030(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0452.", "0452.,<EOF>", 700))

    def test_031(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>", 700))

    def test_032(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("012", "0,12,<EOF>", 700))

    def test_033(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1_2", "1,_2,<EOF>", 700))

    def test_034(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 700))

    def test_035(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-12", "-,12,<EOF>", 700))

    def test_036(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b000", "0b000,<EOF>", 700))

    def test_037(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1e", "0b1,e,<EOF>", 700))

    def test_038(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b12", "0b1,2,<EOF>", 700))

    def test_039(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1101", "0b1101,<EOF>", 700))

    def test_040(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0B111", "0B111,<EOF>", 700))

    def test_041(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00O72", "0,0O72,<EOF>", 700))

    def test_042(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0O72", "-,0O72,<EOF>", 700))

    def test_043(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0o18", "0o1,8,<EOF>", 700))

    def test_044(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0o12", "0o12,<EOF>", 700))

    def test_045(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0Oo1", "0,Oo1,<EOF>", 700))

    def test_046(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0x2g", "-,0x2,g,<EOF>", 700))

    def test_047(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0X0cb", "0X0cb,<EOF>", 700))

    def test_048(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0xae2", "0xae2,<EOF>", 700))

    def test_049(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0Xx2", "0,Xx2,<EOF>", 700))

    def test_050(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-020", "010.010e-020,<EOF>", 700))

    def test_051(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2e+-2", "1.2,e,+,-,2,<EOF>", 700))

    def test_052(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2Ee2", "1.2,Ee2,<EOF>", 700))

    def test_053(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("09.e-002", "09.e-002,<EOF>", 700))

    def test_054(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2", "1.e-2,<EOF>", 700))

    def test_055(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e2", "1.e2,<EOF>", 700))

    def test_056(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e", "1.,e,<EOF>", 700))

    def test_057(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 700))

    def test_058(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00.1e2", "00.1e2,<EOF>", 702))

    def test_059(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme(".e+2", ".,e,+,2,<EOF>", 700))

    def test_060(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 700))

    def test_061(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "votien" """, "\"votien\",<EOF>", 700))

    def test_062(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r" """, "\"\\r\",<EOF>", 700))

    def test_063(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\n" """, "\"\\n\",<EOF>", 700))

    def test_064(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\" """, "\"\\\\\",<EOF>", 700))

    def test_065(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\"" """, "\"\\\"\",<EOF>", 700))

    def test_066(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "a \\r a" """, "\"a \\r a\",<EOF>", 700))

    def test_067(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", 700))

    def test_068(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """, "\"\",<EOF>", 700))

    def test_069(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" ^ """, "ErrorToken ^", 700))

    def test_070(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" /* @@ * */ """, "<EOF>", 700))

    def test_071(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" 
        /* a * */
 """, "<EOF>", 700))

    def test_072(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" // /* */  """, "<EOF>", 700))

    def test_073(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" // /*
                                       */""", "*,/,<EOF>", 700))

    def test_074(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" 
        /* */ /* */ /*a // */ b""", "b,<EOF>", 700))

    def test_075(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* a */ */ b """, "*,/,b,<EOF>", 700))

    def test_076(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* /* */ a """, "a,<EOF>", 700))

    def test_077(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* a /* b */ */ c /* */""", "c,<EOF>", 700))

    def test_078(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* test */ a /* */ """, "a,<EOF>", 700))

    def test_079(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme("""
        /* test
        */ a /* */
""", "a,;,<EOF>", 700))

    def test_080(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" 
    // // //
 """, "<EOF>", 700))

    def test_081(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme("""
// // // """, "<EOF>", 700))

    def test_082(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" // // // """, "<EOF>", 700))

    def test_083(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 700))

    def test_084(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 700))

    def test_085(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 700))

    def test_086(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 700))

    def test_087(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 700))

    def test_088(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("#", "ErrorToken #", 700))

    def test_089(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("\\", "ErrorToken \\", 700))

    def test_090(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("&", "ErrorToken &", 700))

    def test_091(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" 123" """, "123,Unclosed string: \" ", 700))

    def test_092(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123""", "Unclosed string: \"123", 700))

    def test_093(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123 \\n \n" """, "Unclosed string: \"123 \\n ", 700))

    def test_094(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123
        " """, "Unclosed string: \"123", 700))

    def test_095(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123\n" """, "Unclosed string: \"123", 700))

    def test_096(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\" \\\\ \\q" """, "Illegal escape in string: \"\\\" \\\\ \\q", 700))

    def test_097(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "&\\&" """, "Illegal escape in string: \"&\\&", 700))

    def test_098(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\z" """, "Illegal escape in string: \"\\z", 700))

    def test_099(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\0" """, "Illegal escape in string: \"\\0", 700))

    def test_100(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\b" """, "Illegal escape in string: \"\\b", 700))

    def test_101(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            1
""", "1,;,<EOF>", 700))
        
    def test_102(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            0x1
""", "0x1,;,<EOF>", 700))
        
    def test_103(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            "s"
""", "\"s\",;,<EOF>", 700))
        
    def test_104(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            true
""", "true,;,<EOF>", 700))
        
    def test_105(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            2.
""", "2.,;,<EOF>", 700))

    def test_106(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            ID
""", "ID,;,<EOF>", 700))


    def test_107(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            return
""", "return,;,<EOF>", 700))

    def test_108(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            continue
            break
""", "continue,;,break,;,<EOF>", 700))

    def test_109(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            if
            }
            ]
            )
""", "if,},;,],;,),;,<EOF>", 700))

    def test_110(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
        
    def test_111(self):
        self.assertTrue(TestLexer.checkLexeme("""
            1e+7
""", "1,e,+,7,;,<EOF>", 700))
        
    def test_112(self):
        self.assertTrue(TestLexer.checkLexeme("""
           \"12\"\"
""", "\"12\",Unclosed string: \"", 701))
        
    def test_113(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
        
    def test_114(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
        
    def test_115(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
        
    def test_116(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
        
    def test_117(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
        
    def test_118(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil\n/*
*/""", "nil,;,<EOF>", 700))
    
    def test_119(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil/*
*/\n""", "nil,;,<EOF>", 700))
        
    def test_120(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil/*
*/""", "nil,<EOF>", 700))
        
    def test_121(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 700))
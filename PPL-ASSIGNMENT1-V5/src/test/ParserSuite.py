import unittest
from TestUtils import TestParser
expect = "successful"
class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = 1;","successful", 500))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = true;","successful", 501))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [5][0]string{1, \"string\"};","successful", 502))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [1.]ID{1, 3};","Error on line 1 col 17: 1.", 503))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = Person{name: \"Alice\", age: 30};","successful", 504))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", 505))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", 506))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = ca.foo(132) + b.c[2];","successful", 507))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = a.a.foo();","successful", 508))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.checkParser("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", 509))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.checkParser("""
            const VoTien = a.b() + 2;
        ""","successful", 510))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.checkParser("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", 511))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", 512))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", 513))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {}                                                                       
        ""","successful", 514))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","successful", 515))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", 516))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", 517))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", 518))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", 519))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", 520))
       
    def test_021(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 0b11;                         
        ""","successful", 521))

    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 1.;                         
        ""","successful", 522))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN 1;                         
        ""","Error on line 2 col 26: 1", 523))
    
    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int{1};                         
        ""","Error on line 2 col 28: int", 524))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 29: true", 525))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 29: ]", 526))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 29: ]", 527))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1;                         
        ""","Error on line 2 col 36: ;", 528))
    
    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1,3,4;                         
        ""","Error on line 2 col 40: ;", 529))

    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 35: }", 530))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {};                         
        ""","successful", 531))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", 532))

    def test_033(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int {};                         
        ""","Error on line 2 col 28: int", 533))

    def test_034(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID + 3;                         
        ""","successful", 534))
    
    def test_035(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: };                         
        ""","Error on line 2 col 35: }", 535))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", 536))
    
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", 537))

    def test_038(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a + b - [2]int{2} + c - z;                         
        ""","successful", 538))

    def test_039(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a * b / d % e * 2;                         
        ""","successful", 539))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        ""","successful", 540))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", 541))

    def test_042(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 31: ,", 542))

    def test_043(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[];                         
        ""","Error on line 2 col 30: ]", 543))

    def test_044(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo();                         
        ""","successful", 544))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        ""","successful", 545))

    def test_046(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        ""","successful", 546))

    def test_047(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1,);                         
        ""","Error on line 2 col 48: )", 547))

    def test_048(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;                         
        ""","successful", 548))

    def test_049(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
        ""","successful", 549))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo().a[2].goo();                         
        ""","successful", 550))

    def test_051(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = [2]int{1}[3][4].foo();                         
        ""","successful", 551))

    def test_052(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
        ""","successful", 552))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", 553))

    def test_054(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = foo() + foo(a{a:2}) + foo(2, 3,4);                         
        ""","successful", 554))

    def test_055(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  int;                         
        ""","Error on line 2 col 24: int", 555))

    def test_056(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  (1, 2);                         
        ""","Error on line 2 col 26: ,", 556))

    def test_057(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a VOTIEN = 2 + 3 / 4;
        ""","successful", 557))

    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", 558))

    def test_059(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [][3]int = 2 + 3 / 4;
        ""","Error on line 2 col 20: ]", 559))

    def test_060(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = a.foo()[2];
        ""","successful", 560))

    def test_061(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = ;
        ""","Error on line 2 col 21: ;", 561))

    def test_062(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a 1;
        ""","Error on line 2 col 19: 1", 562))

    def test_063(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]int;
        ""","successful", 563))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]ID
        ""","successful", 564))

    def test_065(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a;
        ""","Error on line 2 col 20: ;", 565))

    def test_066(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a := 1 + foo.a[2];
        ""","Error on line 2 col 21: :=", 566))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a =;
        ""","Error on line 2 col 22: ;", 567))

    def test_068(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            
            var a int; var d = 2;
                                        
            var d = 2;
                                        
            const a = 2; var d int = 3;
                                        
            
            var d = 2;""","successful", 568))
        
    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", 569))
        
    def test_070(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() [2]id {return ;}
""","successful", 570))
        
    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a) [2]id {return ;}
""","Error on line 2 col 23: )", 571))
        
    def test_072(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(int a) int {return ;}
""","Error on line 2 col 22: int", 572))
        
    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() {return ;}
""","successful", 573))
        
    def test_074(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a int, ) {}
""","Error on line 2 col 29: )", 574))
        
    def test_075(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int}
""","Error on line 2 col 46: }", 575))
        
    def test_076(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int;}
""","successful", 576))
        
    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", 577))
        
    def test_078(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 23: a", 578))
        
    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 23: =", 579))
        
    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", 580))
        
    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 47: }", 581))
        
    def test_082(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()
        }
""","successful", 582))
        
    def test_083(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}
""","successful", 583))
        
    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", 584))
        
    def test_085(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID){}
        }
""","Error on line 3 col 34: {", 585))
        
    def test_086(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();} type Person struct{value int;}
""","Error on line 2 col 50: type", 586))
        
    def test_087(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}; type Person struct{value int;}
""","successful", 587))
        
    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y int) int  {return ;};
""","successful", 588))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) Add(x int) int {return ;}
""","successful", 589))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 21: int", 590))
        
    def test_090(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;}
""","successful", 591))
        
    def test_091(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x, c int) {return ;}
""","successful", 592))
        
    def test_092(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c [2]c) Add(x int) {return ;}
""","Error on line 2 col 21: [", 593))
        
    def test_093(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (int c) Add(x int) {return ;}
""","Error on line 2 col 19: int", 594))
        
    def test_094(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;};
""","successful", 595))
        
    def test_095(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            func (c c) Add(x int) {return ;}
                                        
            func Add(x int) {return ;}; var c int;
                                        
            var c int; type Calculator struct{c int;}; type Calculator struct{c int;} var c int;
""","Error on line 7 col 87: var", 596))
        
    def test_096(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            var c int func (c c) Add(x int) {return ;}
""","Error on line 3 col 23: func", 597))
        
    def test_097(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const a = 2 func (c c) Add(x int) {return ;}
""","Error on line 3 col 25: func", 598))
        
    def test_098(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const MaxSize = 100 + 50; func (c c) Add() {return ;}
""","successful", 599))
        
    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""


""","Error on line 4 col 1: <EOF>", 600))
        
    def test_100(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
            func Add() {
                                        }
""","successful", 601))
        
    def test_101(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int = 2;      
                                    };""","successful", 602))

    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int;      
                                    };""","successful", 603))
        
    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""","successful", 604))
        
    def test_104(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         const a = a[2].b;      
                                    };""","successful", 605))
        
    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    };""","successful", 606))
        
    def test_106(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b var a = "s";           
                                    };""","Error on line 4 col 56: var", 607))

    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""","successful", 608))
        

    def test_108(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2].b := 2;       
                                    };""","successful", 609))
        

    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""","successful", 610))

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""","Error on line 3 col 49: +=", 611))

    def test_111(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        2 + 2 += 2;       
                                    };""","Error on line 3 col 41: 2", 612))
        
    def test_112(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       ID {id:2}.c += 2;       
                                    };""","Error on line 3 col 43: {", 613))
        
    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""","successful", 614))
        
    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""","successful", 615))
        
    def test_115(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){return;}
                                        } 
                                    };""","Error on line 4 col 49: )", 616))
        
    def test_116(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };""","successful", 617))
        
    def test_117(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return
                                        } else if(){
                                        }
                                    };""","Error on line 4 col 51: )", 618))
        
    def test_118(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return; 
                                        } else if(1){return; 
                                        }else if(1){return; 
                                        }else if(2){return
                                        }else {return; 
                                        }
                                    };""","successful", 619))
        
    def test_119(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true {return; }
                                    };""","successful", 620))
        
    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", 621))
        
    def test_121(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 45: int", 622))
        
    def test_122(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 45: int", 623))
        
    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", 624))
        
    def test_124(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", 625))
        
    def test_125(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 45: const", 626))
        
    def test_126(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 78: [", 627))
        
    def test_127(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: {", 628))
        
    def test_128(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); var i [2]int = 0 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 76: var", 629))
        
    def test_129(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","successful", 630))
        
    def test_130(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 53: ,", 631))
        
    def test_131(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index.ab, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 53: ,", 632))
        
    def test_132(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value[2] := range arr {
                                        // index: 0, 1, 2
                                        return; 
                                        }
                                    };""","Error on line 3 col 57: [", 633))
        
    def test_133(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr[2] {return
                                        }
                                    };""","successful", 634))
        
    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""","successful", 635))
        
    def test_135(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {
                                            for index, value := range 23 {return; }
                                        }
                                    };""","successful", 636))
        
    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", 637))
        
    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", 638))
        
    def test_138(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return return 2 + a[2].b()
                    
                                    };""","Error on line 3 col 48: return", 639))
        
    def test_139(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break continue
                    
                                    };""","Error on line 3 col 47: continue", 640))
        
    def test_140(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo();
                                        foo()
                                    };""","successful", 641))
        
    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", 642))
        
    def test_142(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""","Error on line 3 col 41: (", 643))
        
    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", 644))
        
    def test_144(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {break;}
                                    };""","Error on line 3 col 41: {", 645))
        
    def test_145(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                        break;
                                    func Add() {
                                    };""","Error on line 2 col 41: break", 646))
        
    def test_146(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    };""","Error on line 4 col 51: c", 647))
        
    def test_147(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3)[b]
                                        return -1.c[c]
                                    };""","Error on line 4 col 51: c", 648))
        
    def test_148(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return struct;}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    };""","Error on line 3 col 56: struct", 649))
        
    def test_149(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}
                                    };""","Error on line 3 col 76: string", 650))
        
    def test_150(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}else  {return struct;}
                                    };""","Error on line 3 col 76: string", 651))
        
    def test_151(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{1+1}                    
""","Error on line 1 col 19: +", 652))
        
    def test_152(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", 653))
        
    def test_153(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{}                    
""","Error on line 1 col 18: }", 654))
        
    def test_154(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 18: [", 655))
        
    def test_155(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
""","successful", 656))
        
    def test_156(self):
        self.assertTrue(TestParser.checkParser("""
        func Add(x, y int, b float) {return ;}           
""","successful", 657))
        
    def test_157(self):
        self.assertTrue(TestParser.checkParser("""
        func (c c) Add(x, y int, b float) {return ;}           
""","successful", 658))
        
    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }      
""","successful", 659))
        
    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            c int  c int;                                                    
        }      
""","Error on line 3 col 20: c", 660))
        
    def test_159(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""","Error on line 10 col 29: ;", 661))
        
    def test_160(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };  
""","Error on line 4 col 17: else", 662))
        
    def test_161(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else if (1) {}
            };  
""","successful", 663))
        
    def test_162(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else {}
            };  
""","successful", 664))
        
    def test_163(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {}
            };  
""","successful", 665))
        
    def test_164(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i < 10 {
// loop body
}
            };  
""","successful", 666))
        
    def test_165(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0; i < 10; i += 1 {
// loop body
}
            };  
""","successful", 667))
        
    def test_166(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for index, value := range STRUCT{} {
// loop body                                   
};
            };  
""","successful", 668))

    def test_167(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.2; 
""","Error on line 2 col 21: 2", 669))
        
    def test_168(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.b.c().d().e[2].k()[2]; 
""","successful", 670))
        
    def test_169(self):
        self.assertTrue(TestParser.checkParser("""
        const a = [1]int{1, 2 
""","Error on line 2 col 32: ;", 671))
        
    def test_170(self):
        self.assertTrue(TestParser.checkParser("""
        const a = foo(1, 2
""","Error on line 2 col 28: ;", 672))

    def test_171(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i.b := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 78: .", 673))
        
    def test_172(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[2].c += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 78: [", 674))

    # def test_173(self):
    #     """Statement"""
    #     self.assertTrue(TestParser.checkParser("""
    #                                 func Add() {
    #                                     for i[2] := 1; foo().a.b(); i := 1 {
    #                                         return; 
    #                                     }
    #                                 };""","Error on line 3 col 49: :=", 675))
        
    # def test_174(self):
    #     """Statement"""
    #     self.assertTrue(TestParser.checkParser("""
    #                                 func Add() {
    #                                     for i.c[2] := 1; foo().a.b(); i := 1 {
    #                                         return; 
    #                                     }
    #                                 };""","Error on line 3 col 51: :=", 676))
        
    def test_175(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", 677))
        
    def test_176(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            };                                                 
        }      
""","successful", 678))
        
    def test_177(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 50: ;", 679))

    def test_178(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b int; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 54: ;", 680))

    def test_179(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", 681))

    def test_180(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{{{1}}, ID, a, {b}}                              
                                        ""","successful", 682))

    def test_181(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a;
                                        ""","Error on line 2 col 50: ;", 683))
    def test_182(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 53: {", 684))
                                                                                          
    def test_183(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 53: {", 685))
                                                                                          
    def test_184(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {
                                            return;
                                        }
                                    };""","Error on line 3 col 41: {", 686))

    def test_185(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{a, b, {c}}                              
                                        ""","successful", 687))
        
    def test_186(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                            return;
                                    };""","successful", 688))

    def testcase_201(self):
        input = """
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

    def testcase_202(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def testcase_203(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def testcase_204(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def testcase_205(self):
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
    
    def testcase_222(self):
        input = """
        func main() {
            var x boolean
            x := (true && false) || (true || false) && !true
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def testcase_223(self):
        input = """
        func main() {
            var x boolean;
            x := -x || !x && x;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def testcase_224(self):
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
    
    def testcase_225(self):
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

    def testcase_226(self):
        input = """
        func main() {
            var x int;
            if x == nil {
            } else {
                return;
            }
        }
        """
        expect = "Error on line 4 col 16: x"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def testcase_227(self):
        input = """
        func (p Person) Greet() string {
            return "Hello, " + p.getName + "!" + "from" + p.GetAddress().city;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def testcase_228(self):
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

    def testcase_229(self):
        input = """
        func foo () {
        var matrix [2][3]int = [2][3]int{{1, 2}, 3}
        var matrix2 [1]int = [1]int{1};
        arr2 := [1]int{1};
        arr := [2][3]int{{1, 2, 3}, {4, 5, 6}};
        putIntLn(matrix[1][2]);  // In ra 6
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def testcase_230(self):
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
        expect = "Error on line 6 col 20: arr"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def testcase_231(self):
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
        expect = "Error on line 2 col 24: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
    
    def testcase_232(self):
        input = """var a = [2][2]int{{1, 2}, {3, 4}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def testcase_233(self): 
        input = """var a int \nvar b int \r\nvar c int; var d int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def testcase_234(self): 
        input = """var a int var b int var c int"""
        expect = "Error on line 1 col 11: var"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def testcase_235(self):
        input = """
        func foo(x int, y int) int {
            return x + -y;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def testcase_236(self):
        input = """
        func main() {
            if (x > 0) {
                print("Positive");
            } else {
                print("Negative");
            }
        }
        """
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def testcase_237(self):
        input = """
        func main() {
            var a = A{x: 1, y: 2}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def testcase_238(self):
        input = "type A interface { foo() int; };"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def testcase_239(self):
        input = """
        func main() {
            ;
        }
        """
        expect = "Error on line 3 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def testcase_240(self):
        input = """var a = [a+1-2%3 || 4 && 5][2 + a.test.funct().tar.pot]int{{1, 2}, {3, 4}};"""
        expect = "Error on line 1 col 11: +"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def testcase_241(self):
        input = """var a [2]A;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def testcase_242(self):
        input = """func main() {
            abc.x.y.z[3].t[10][2][5] := 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def testcase_243(self):
        input = """func main() {
            abc.x.y.z[3].t[10][2][5] := foo.baz() * bar.code();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def testcase_244(self):
        input = """func main() {
            abc.x.y.z[3].t[10][2][5] := ":))" + foo[1].bar.code(a, b).baz[mez().conz().chauz]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def testcase_245(self):
        input = """type empty struct {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def testcase_246(self):
        input = """type empty interface {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def testcase_247(self):
        input = """type Comparable interface {
            compare(other interface) int;
        };"""
        expect = "Error on line 2 col 27: interface"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def testcase_248(self):
        input = """type Complex interface {
            getValue() [2]float;
            setValue(real, imag float);
            toString() string;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def testcase_249(self):
        input = """type Container interface {
            push(element [3]Point);
            pop() [3]Point;
            isEmpty() bool;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def testcase_250(self):
        input = """
        type Animal interface {
            makeSound() string;
            move(distance float);
            getSpecies() string;
            age() int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def testcase_251(self):
        input = """
        type Database interface {
            connect(host string, port int) bool;
            query(sql []string) [2]string;
            execute(command []string) bool;
            disconnect();
        };"""
        expect = "Error on line 4 col 24: ]"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def testcase_252(self):
        input = """
        type Point struct {
            x, y float;
            a [3]int;
            b [2][2]Matrix;
        };"""
        expect = "Error on line 3 col 14: ,"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def testcase_253(self):
        input = """
        type Rectangle struct {
            width, height float;
            color string;
        };"""
        expect = "Error on line 3 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def testcase_254(self):
        input = """
        type Student struct {
            name string;
            grades [10]float
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def testcase_255(self):
        input = """
        type LinkedList struct {
            data int;
            next Node;
        };"""
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def testcase_256(self):
        input = """
        type Car struct {
            brand string;
            year int;
            specs [5]string;
            engine Engine;
        };"""
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def testcase_257(self):
        input = """
        type Employee struct {
            id int;
            salary float;
            department struct;
        };"""
        expect = "Error on line 5 col 24: struct"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def testcase_258(self):
        input = """
        func (p Point) distance(q Point) float {
            return sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y));
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def testcase_259(self):
        input = """
        func (l LinkedList) insert(value int) {
            l.next := Node{data: value, next: l.next};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def testcase_260(self):
        input = """
        func (c Complex) add(other Complex) Complex {
            return Complex{real: c.real + other.real, imaginary: c.imaginary + other.imaginary};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def testcase_261(self):
        input = """
        func (b BankAccount) transfer(amount float, target BankAccount) bool {
            if b.balance >= amount { return true; };
            return false;
        };"""
        expect = "Error on line 3 col 16: b"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def testcase_262(self):
        input = """
        func (c Car) start() string {
            return c.brand + " engine starting...";
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def testcase_263(self):
        input = """
        func (t Tree) insert(val int) Tree {
            if t == nil { return Tree{value: val}; };
            return t;
        };"""
        self.assertTrue(TestParser.checkParser(input,"Error on line 3 col 16: t",263))

    def testcase_264(self):
        input = """
        func (e Employee) promote( int float) {
            e.salary := e.salary * (1.0 + raise);
        };"""
        expect = "Error on line 2 col 36: int"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def testcase_265(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))    

    def testcase_266(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def testcase_267(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def testcase_268(self):
        input = """
        type BankAccount struct {
            balance float;
            owner string;
        }
        func (b BankAccount) withdraw(amount float) bool {
            if (b.balance >= amount) {
                b.balance := b.balance - amount;
                return true;
            }
            return false;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def testcase_269(self):
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def testcase_270(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def testcase_271(self):
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
        };"""
        expect = "Error on line 7 col 16: l"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def testcase_272(self):
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
        };"""
        expect = "Error on line 4 col 17: ,"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def testcase_273(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def testcase_274(self):
        input = """
        type Database interface {
            connect(host string) bool;
            query(sql string) [100]string;
            close();
        }
        func executeQuery(db Database, query string) {
            if (db.connect("localhost")) {
                results := db.query(query);
                db.close();
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def testcase_275(self):
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
        };"""
        expect = "Error on line 13 col 64: ;"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def testcase_276(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def testcase_277(self):
        input = """
        type Sorter interface {
            sort(a [100]int) [100]int;
        }
        type BubbleSort struct {}
        func (bs BubbleSort) sort(arr [100]int) [100]int {
            for i := 0; i < 100; i+=1 {
                for j := 0; j < 99; j+=1 {
                    if (arr[j] > arr[j+1]) {
                        temp := arr[j];
                        arr[j] := arr[j+1];
                        arr[j+1] := temp;
                    }
                }
            }
            return arr;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def testcase_278(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def testcase_279(self):
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
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def testcase_280(self):
        input = """func main() {
            1 = 2;
        };"""
        expect = "Error on line 2 col 13: 1"
        self.assertTrue(TestParser.checkParser(input,expect,280))
        
    def testcase_281(self):
        input = """func main() {
            var a = 1 + 2 a.b = 3;
        };"""
        expect = "Error on line 2 col 27: a"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def testcase_282(self):
        input = """
func main() {} extra"""
        expect = "Error on line 2 col 16: extra"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def testcase_283(self):
        input = """func main() { { x := 5; } } var a int = 10"""
        expect = "Error on line 1 col 15: {"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def testcase_284(self):
        input = """func main() {  x := 5;  } var a int = 10"""
        expect = "Error on line 1 col 27: var"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def testcase_285(self):
        input = """func main() { := 5; };"""
        expect = "Error on line 1 col 15: :="
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def testcase_286(self):
        input = """func test(x,) int { return 1; };"""
        expect = "Error on line 1 col 13: )"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def testcase_287(self):
        input = """var arr = []{1,2,3};"""
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def testcase_288(self):
        input = """type Person struct { ,name string; };"""
        expect = "Error on line 1 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def testcase_289(self):
        input = """type Drawable interface { draw(,) int; };"""
        expect = "Error on line 1 col 32: ,"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def testcase_290(self):
        input = """func divide(x, y float) float { return x/y, 0; };"""
        expect = "Error on line 1 col 43: ,"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def testcase_291(self):
        input = """func main() { for i := range { print(i); } };"""
        expect = "Error on line 1 col 24: range"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def testcase_292(self):
        input = """func main() { ch <- 5 <- 3; };"""
        expect = "Error on line 1 col 18: <"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def testcase_293(self):
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def testcase_294(self):
        input = """var f = func(x int) { return x + 1 };"""
        expect = "Error on line 1 col 9: func"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def testcase_295(self):
        input = """func main() { 
            var a = 0 //; 
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def testcase_296(self):
        input ="""
        // Test case 36: More Complex struct Declaration

        type Address struct {
        Street string
        City string
        Zip int
        }

        type Person struct {
        Name string
        Age int
        Address Address
        }

        func main() {
        var p Person = {
            Name: "John Doe",
            Age: 30,
            Address: {
            Street: "123 Main St",
            City: "Anytown",
            Zip: 12345,
            },
        }
        println(p.Address.City)
        }
        """     
        expect = "Error on line 17 col 24: {"
        self.assertTrue(TestParser.checkParser(input,expect,296))
        
    def testcase_297(self):
        input = """a := -(5 + 3 - 2) * 4 / 2 % 1 == true && false"""
        expect = "Error on line 1 col 1: a"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def testcase_298(self):
        input = """
        //const a = 2.x;
        var a [2]int;
        var b [345]Too;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def testcase_299(self):
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
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def testcase_300(self):
        input = """
        func foo(z int) {
            for it, val := range [20]int{1,2,3} {
                for z < 10 {
                    sample := "test tao lao"
                }

                for _,val := range itq{Teq:11, God: 11} {
                    // sample
                }
            }
        
        }
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    def test_struct_999(self):
        input = """
        func wikiList(a, b int, c float, d Foo) [abc123][def456]Wiki {
            return [20]Wiki{Wiki{title: "Hello", content: "World"}}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 999))
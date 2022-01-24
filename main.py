# Calculus Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sympy as sym
from sympy import Symbol, diff, integrate

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Derivatives and Integration Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-math,LLC ©"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
""")

#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    GridLayout:
        cols: 1
        
        Label:
            font_size: 75
            size_hint_y: None
            height: 200
            padding: 10, 10
            text: "Menu"
                
        Button:
            font_size: 75
            background_color: 0, 0, 1, 1
            size_hint_y: None
            height: 200
            text: "Derivatives Calculator"
            on_release:
                app.root.current = "Derivatives"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 1, 1, 1
            size_hint_y: None
            height: 200
            text: "Integration Calculator"
            on_release:
                app.root.current = "Integration"
                root.manager.transition.direction = "left"
                
        Button:
            font_size: 75
            background_color: 0, 0, 0 , 1
            size_hint_y: None
            height: 200
            text: "Visit KSquared,LLC"
            on_release:
                import webbrowser
                webbrowser.open('https://kivy.org/')

""")

#Derivatives Calculator
Builder.load_string("""
<Derivatives>
    id:Derivatives
    name:"Derivatives"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Derivatives Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        prime.text = ""
                        respect.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "f(x)="
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10              
            
            TextInput:
                id: prime
                text: prime.text
                hint_text: "# of times to derive"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10            
                input_filter: lambda text, from_undo: text[:2 - len(prime.text)]
                
            TextInput:
                id: respect
                text: respect.text
                hint_text: "With respect to: x, y or z"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10  
                input_filter: lambda text, from_undo: text[:1 - len(respect.text)]
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Derivative"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        Derivatives.derive(entry.text + "&" + prime.text + "$" + respect.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

#Integration Calculator
Builder.load_string("""
<Integration>
    id:Integration
    name:"Integration"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Integration Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        prime.text = ""
                        respect.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "f(x)="
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10              
            
            TextInput:
                id: prime
                text: prime.text
                hint_text: "# of times to integrate"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10              
                input_filter: lambda text, from_undo: text[:2 - len(prime.text)]
                
            TextInput:
                id: respect
                text: respect.text
                hint_text: "With respect to: x, y or z"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10  
                input_filter: lambda text, from_undo: text[:1 - len(respect.text)]
                
                    
            Button:
                id: steps
                text: "Integrate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1, 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Integration.Integrate(entry.text + "&" + prime.text + "$" + respect.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Derivatives(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Derivatives, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"   
    layouts = []
    def derive(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("DERIVATE")
        
        try:
            print("Entry",entry)
            amp = entry.find("&")
            dollar = entry.find("$")
            
            func = entry[:amp]
            print("func",func)       
            
            prime = entry[amp+1:dollar]
            print("Prime:",prime)
            if prime == "":
                prime = 0
            
            respect = entry[dollar + 1:]
            print("respect:",respect)
            
            x = sym.Symbol(respect)
            y = sym.Symbol(respect)
            z = sym.Symbol(respect)
            
            if int(prime) > 0 and str(respect) != "":
                self.ids.list_of_steps.add_widget(Label(text= "f(" + respect + ") = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z").replace("+"," + ").replace("-"," - ").replace("***","**") ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Derive " + str(prime) + " time(s) with respect to " + str(respect),font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                print("_________________________________________")
                
                i = 0 #     2sin(2x)^2+3x^3+e^x-2ln(3x)
                while i < int(prime):
                    
                    print("Starting",i+1,"derivative")
                    func = func.replace("**","^").replace("*","")
                    print("func:",func)
                    func = str(func).replace(" ","").replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                    func = func.replace("-*x","-1*x").replace("-*y","-1*y").replace("-*z","-1*z")
                    func = func.replace("+*x","+1*x").replace("+*y","+1*y").replace("+*z","+1*z")
                    func = func.replace("(*x","(1*x").replace("(*y","(1*y").replace("(*z","(1*z")
                    func = func.replace("(-*x","(-1*x").replace("(-*y","(-1*y").replace("(-*z","(-1*z")
                    func = func.replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                    func = func.replace("ln","*ln").replace("log","*log")
                    func = func.replace("e","*e").replace("(*e","(e")
                    func = func.replace("+-","-").replace("-+","-")
                    func = func.replace("-*","-1*").replace("+*","+1*").replace("/*","/")
                    func = func.replace("***","**")
                    print("func fixed:",func)
                    
                    if func[0] == "*":
                        func = "1" + func
                        print("func fixed, * = [0]:",func)
                    print("func = ",func)
                    print("func data type",type(func))
                    func = str(sym.diff(func,respect))
                    print("Answer:",func)
                    
                    print()
                    func_display_list = str(func).strip().split(" ")
                    print("func_display_list",func_display_list)
                    
                    if len(func_display_list) > 5 and len(func_display_list) < 12:
                        print("IF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_back_slice = str(func_display_list[5:]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_back_slice",func_display_back_slice)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + respect + ") = " + str(func_display_front_slice).replace("**","^"),font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    elif len(func_display_list) > 12:
                        print("ELIF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_mid_slice = str(func_display_list[5:11]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_mid_slice",func_display_mid_slice)
                        
                        func_display_back_slice = str(func_display_list[11:]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_back_slice",func_display_back_slice)
                        
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + respect + ") = " + str(func_display_front_slice).replace("**","^") ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_mid_slice).replace("**","^"),font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    else:
                        print("ELSE")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("func_display_list",func_display_list)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + respect + ") = " + str(func).replace("**","^"),font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    print("Completed",i+1,"derivative")
                    print("_________________________________________")
                    i = i + 1
                    
            else:
                if int(prime) == 0:
                    self.ids.list_of_steps.add_widget(Label(text= "Prime must be greater than 0!" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif respect == "":
                    self.ids.list_of_steps.add_widget(Label(text= "Respect must be entered" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            
class Integration(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Integration, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"    

    layouts = []
    def Integrate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("INTEGRATE")
        
        try:
            print("Entry",entry)
            amp = entry.find("&")
            dollar = entry.find("$")
            
            func = entry[:amp]
            print("func",func)       
            
            prime = entry[amp+1:dollar]
            print("Prime:",prime)
            if prime == "":
                prime = 0
            
            respect = entry[dollar + 1:]
            print("respect:",respect)
            
            x = sym.Symbol("x")
            y = sym.Symbol("y")
            z = sym.Symbol("z")
            
            if int(prime) > 0 and str(respect) != "":
                self.ids.list_of_steps.add_widget(Label(text= "f(" + respect + ") = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z").replace("-"," - ").replace("+"," + ").replace("***","**") ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Integrate " + str(prime) + " time(s) with respect to " + str(respect),font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                print("_________________________________________")
                
                i = 0
                while i < int(prime):
                    
                    print("Starting",i+1,"integrate")
                    func = func.replace("**","^").replace("*","")
                    print("func:",func)
                    
                    func = str(func).replace(" ","").replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                    func = func.replace("-*x","-1*x").replace("-*y","-1*y").replace("-*z","-1*z")
                    func = func.replace("+*x","+1*x").replace("+*y","+1*y").replace("+*z","+1*z")
                    func = func.replace("(*x","(1*x").replace("(*y","(1*y").replace("(*z","(1*z")
                    func = func.replace("(-*x","(-1*x").replace("(-*y","(-1*y").replace("(-*z","(-1*z")
                    func = func.replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                    func = func.replace("(*sin","(sin").replace("(*cos","(cos").replace("(*tan","(tan").replace("(*sec","(sec").replace("(*csc","(csc").replace("(*cot","(cot")
                    func = func.replace("ln","*ln").replace("log","*log")
                    func = func.replace("e","*e").replace("(*e","(e").replace("*s*ec","*sec")
                    func = func.replace("+-","-").replace("-+","-")
                    func = func.replace("-*","-1*").replace("+*","+1*").replace("/*","/")
                    func = func.replace("***","**")
                    print("func fixed:",func)
                    
                    if func[0] == "*":
                        func = "1" + func
                        print("func fixed, * = [0]:",func)
                    print("func = ",func)
                    print("func data type",type(func))
                    print()
                    func = func.strip().replace("+"," + ").replace("-"," - ")
                    print("Func spaced out",func)
                    temp_list = func.strip().split(" ")
                    print("temp_list:",temp_list)
                    
                    k = 0
                    e_list = []
                    while k < len(temp_list):
                        print("k",k)
                        if temp_list[k].count("e") == 1 and temp_list[k].count(respect) == 1 and temp_list[k].count("s") == 0:
                                print("found!")
                                if temp_list[k-1].strip() == "+" or temp_list[k-1].strip() == "-":
                                    e_list.append(temp_list[k-1])
                                    temp_list[k-1] = " "
                                e_list.append(temp_list[k])
                                temp_list[k] = " "
                                print("temp_list",temp_list)
                                print("e_list",e_list)
                        k = k + 1
                    print()
                    print("loop ended")
                    print("temp_list",temp_list)
                    print("e_list",e_list)
                    
                    func = str(temp_list).replace(" ","").replace("'","").replace("[","").replace("]","").replace(",","").replace("++","+")
                    print()
                    print("func:",func)
                    
                    if func[-1] == "+" or func[-1] == "-":
                        func = func[:-1]
                    
                    func = func.replace("+"," + ").replace("-"," - ")
                    print("func before integration",func)
                    if respect == "x":
                        func = str(sym.integrate(func,x))
                        print("Answer x:",func)
                    elif respect == "y":
                        func = str(sym.integrate(func,y))
                        print("Answer y:",func)
                    elif respect == "z":
                        func = str(sym.integrate(func,z))
                        print("Answer z:",func)
                    
                    print()
                    func_display_list = str(func).strip().split(" ")
                    print("func_display_list",func_display_list)
                    
                    u = 0
                    while u < len(func_display_list):
                        if func_display_list[u].count("/") > 0:
                            div_index = func_display_list[u].find("/")
                            print("Found div sign at: ",div_index)
                            func_display_list[u] = "(" + func_display_list[u][:div_index] + ")" + func_display_list[u][div_index:]
                            print("New func_display",func_display_list[u])
                        u = u + 1
                    
                    j = 0
                    if e_list != []:
                        while j < len(e_list):
                            func_display_list.append("+" + e_list[j])
                            print("func_display_list",func_display_list)
                            j = j + 1
                    
                    if len(func_display_list) > 5 and len(func_display_list) < 12:
                        print("IF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_back_slice = str(func_display_list[5:]).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ")
                        print("func_display_back_slice",func_display_back_slice)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (i+1) + "f" + "(" + respect + ") = " + str(func_display_front_slice).replace("**","^") + " + C",font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    elif len(func_display_list) > 12:
                        print("ELIF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_mid_slice = str(func_display_list[5:11]).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ")
                        print("func_display_mid_slice",func_display_mid_slice)
                        
                        func_display_back_slice = str(func_display_list[11:]).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ")
                        print("func_display_back_slice",func_display_back_slice)
                        
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (i+1) + "f" + "(" + respect + ") = " + str(func_display_front_slice).replace("**","^").replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ") ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_mid_slice).replace("**","^").replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - "),font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^").replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ") + " + C",font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    else:
                        print("ELSE")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("func_display_list",func_display_list)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (i+1) + "f" + "(" + respect + ") = " + str(func_display_list).replace("**","^").replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("+++","+").replace("++","+").replace("+-","-").replace("+"," + ").replace("-"," - ") + " + C",font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    print("Completed",i+1,"integrate")
                    print("_________________________________________")
                    
                    func = str(func_display_list).replace("**","^").replace("[","").replace("]","").replace("'","").replace(",","").replace("+-","-").replace("+"," + ").replace("-"," - ")
                    print("Func before loop",func)
                    i = i + 1
                
            else:
                if int(prime) == 0:
                    self.ids.list_of_steps.add_widget(Label(text= "Prime must be greater than 0!" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif respect == "":
                    self.ids.list_of_steps.add_widget(Label(text= "Respect must be entered" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)        


        
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Derivatives(name="Derivatives"))     
sm.add_widget(Integration(name="Integration"))  
sm.current = "Homepage"   


class Calculus_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Calculus_Calculator().run()

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
                size_hint_y: None
                height: 200
                text: "Visit KSquared-math,LLC ©"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-math,LLC ©"
                    
            Image:
                source: 'KSquared_QR_code.png'
                size_hint_y: None
                height: 300
                
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
                
                func = func.replace(" ","").replace("+"," + ").replace("-"," - ").replace("^ -","^-").replace("^ +","^+")
                print("func",func)
                
                k = 0
                while k < int(prime):
                    if func.count("(") > 0 and func.count(")") > 0:
                        if func.count("(") == func.count(")"):
                            print("Parenthesis Found")
                            i = 0
                            while i < len(func):
                                if func[i] == ")":
                                    right_par_index = i
                                    print("right_par_index",right_par_index)
                                    left_par_index = func[:i].rfind("(")
                                    print("left_par_index",left_par_index)
                                    range_pars = func[left_par_index:right_par_index+1]
                                    print(range_pars)
                                    cleaned = range_pars.replace(" ","")
                                    print("cleaned",cleaned)
                                    func = func[:left_par_index] + cleaned + func[right_par_index+1:] 
                                    print("func cleaned",func)
                                    print()
                                i = i + 1 
                                
                        else:
                            print("Parentheses Unbalanced!")
                    
                    func_list = func.strip().split(" ")
                    print()
                    print("func_list",func_list)
                    print()
                    
                    #If + or - is first element in list
                    new_func_list = []
                    if func_list[0] == "+" or func_list[0] == "-":
                        print("IF")
                        i = 0
                        while i < len(func_list):
                            if func_list[i] == "+" or func_list[i] == "-":
                                new_func_list.append(func_list[i] + func_list[i+1])
                            i = i + 1
                        print("new_func_list",new_func_list)
                    #If + or - is second element in list    
                    elif len(func_list) > 1:
                        if func_list[1] == "+" or func_list[1] == "-":
                           print("ELIF")
                           i = 0
                           while i < len(func_list):
                               if func_list[i] == "+" or func_list[i] == "-":
                                   new_func_list.append(func_list[i] + func_list[i+1])
                               i = i + 1
                           print("new_func_list:",new_func_list)
                           new_func_list = [func_list[0]] + new_func_list
                           print("new_func_list",new_func_list)
                        
                    #If + or - is not apart of list
                    else:
                        print("ELSE")
                        new_func_list.append(func_list[0])
                        print("new_func_list",new_func_list)
                        
                    print()
                    print("integrate each element and store in empty list")
                    print()
                    
                    i = 0
                    while i < len(new_func_list):
                        #finding e
                        if new_func_list[i].count("e") > 0 and new_func_list[i].count("s") == 0 and new_func_list[i].count("c") == 0 and new_func_list[i].count("t") == 0:
                            print()
                            print("Found e")
                            carrot_index = new_func_list[i].find("^")
                            print("carrot_index: ",carrot_index)
                            exponent_range = new_func_list[i][carrot_index+1:]
                            print("exponent_range:",exponent_range)
                            if exponent_range[0] == "x" or exponent_range[0] == "y" or exponent_range[0] == "z":
                                exponent_range = "1" + exponent_range
                                print("e^x fixed: ",exponent_range)
                                new_func_list[i] = new_func_list[i][:carrot_index] + "^" + exponent_range
                                print("new_func_list[i]:",new_func_list[i])
                                if new_func_list[i][0] == "*":
                                    new_func_list[i] = new_func_list[i][1:]
                                    print("found stray *")
                                    print("Cleaned:",new_func_list[i])
                            else:
                                print("e element okay for integration: ",new_func_list[i])
                                if new_func_list[i][0] == "*":
                                    new_func_list[i] = new_func_list[i][1:]
                                    print("found stray *")
                                    print("Cleaned:",new_func_list[i])
                        #finding all other elements
                        else:
                            print()
                            print("Found non-e element:",new_func_list[i])
                            if new_func_list[i][0] == "*":
                                new_func_list[i] = new_func_list[i][1:]
                                print("found stray *")
                                print("Cleaned:",new_func_list[i])
                            
                        i = i + 1
                        
                    print()
                    print("new_func_list with fixed e elements: ",new_func_list)
                    print()
                    
                    answer_integrated = []
                    #While loop to clean each element
                    i = 0
                    while i < len(new_func_list):
                        print("Cleaning ",new_func_list[i])
                        new_func_list[i] = new_func_list[i].replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                        new_func_list[i] = new_func_list[i].replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                        new_func_list[i] = new_func_list[i].replace("e","*e").replace("-*","-").replace("+*","+").replace("(*x","(x").replace("(*y","(y").replace("(*z","(z")
                        print("new_func_list[i]: ",new_func_list[i])
                        
                        if new_func_list[i][0] == "*":
                            new_func_list[i] = new_func_list[i][1:]
                            print("found stray *")
                            print("Cleaned:",new_func_list[i])
                        
                        print()
                        i = i + 1
                        
                    print()
                    print("new_func_list with cleaned elements: ",new_func_list)
                    print()
                        
                    #Concat all cleaned elements and integrate
                    #OR while loop to integrate each element and then concat
                    
                    func_concat = str(new_func_list).replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","").replace("+"," + ").replace("-"," - ")
                    print("func_concat: ",func_concat)
                    print()
                    if respect == "x":
                        print("Integrating with respect to X")
                        func_integrated = str(sym.integrate(str(func_concat),x)).replace("**","^")
                        print("func_integrated",func_integrated)
                    elif respect == "y":
                        print("Integrating with respect to Y")
                        func_integrated = str(sym.integrate(str(func_concat),y)).replace("**","^")
                        print("func_integrated",func_integrated)
                    elif respect == "z":
                        print("Integrating with respect to Z")
                        func_integrated = str(sym.integrate(str(func_concat),z)).replace("**","^")
                        print("func_integrated",func_integrated)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________",font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "∫" * (k+1) + "f" + "(" + respect + ") = " + func_integrated,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    func = func_integrated.replace("**","^").replace("*","")
                    print("func ready for next loop, func = ",func_integrated)
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    k = k + 1
                
                
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

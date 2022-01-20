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
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Calculus Calculator"
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
            background_color: 0, 0 , 1, 1
            size_hint_y: None
            height: 200
            text: "Calculus Calculator"
            on_release:
                app.root.current = "Calculus_Calculator"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 1 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Visit KSquared,LLC"
            on_release:
                import webbrowser
                webbrowser.open('https://kivy.org/')

""")

#Calculus Calculator
Builder.load_string("""
<Calculus_Calculator>
    id:Calculus_Calculator
    name:"Calculus_Calculator"

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
                text: "Calculus Calculator"
                
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
                hint_text: "# of times to derive or integrate"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10              
                
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
                        Calculus_Calculator.derive(entry.text + "&" + prime.text + "$" + respect.text)
                        
                Button:
                    id: steps
                    text: "Integral"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        Calculus_Calculator.Integrate(entry.text + "&" + prime.text + "$" + respect.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Calculus_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Calculus_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = sm.previous()    
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
            
            func = entry[:amp].replace("^","**")
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
                self.ids.list_of_steps.add_widget(Label(text= "Entry = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z") ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Derive " + str(prime) + " time(s) with respect to " + str(respect),font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                i = 1
                while i - 1 < int(prime):
                    try:
                        print("func:",func)
                        func = sym.diff(func,respect)
                        print("Answer:",func)
                    except Exception:
                        print("func:",func)
                        func = func.replace("x","*x").replace("y","*y").replace("z","*z")
                        func = func.replace("+*x","+1*x").replace("+*y","+1*y").replace("+*z","+1*z").replace("-*x","-1*x").replace("-*y","-1*y").replace("-*z","-1*z")
                        print("func fixed:",func)
                        
                        if func[0] == "*":
                            func = "1" + func
                            print("func fixed:",func)
                        
                        func = sym.diff(func,respect)
                        print("Answer:",func)
                    self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * i + "(" + respect + ") = " + str(func).replace("**","^").replace("*","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
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
            
            func = entry[:amp].replace("^","**")
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
                self.ids.list_of_steps.add_widget(Label(text= "Entry = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z") ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Integrate " + str(prime) + " time(s) with respect to " + str(respect),font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                i = 1
                while i - 1 < int(prime):
                    try:
                        print("func:",func)
                        if respect == "x":
                            func = str(sym.integrate(func,x))
                            print("Answer x:",func)
                        elif respect == "y":
                            func = str(sym.integrate(func,y))
                            print("Answer y:",func)
                        elif respect == "z":
                            func = str(sym.integrate(func,z))
                            print("Answer z:",func)
                        
                    except Exception:
                        print("func,exception:",func)
                        func = str(func).replace("x","*x").replace("y","*y").replace("z","*z")
                        func = func.replace("+*x","+1*x").replace("+*y","+1*y").replace("+*z","+1*z").replace("-*x","-1*x").replace("-*y","-1*y").replace("-*z","-1*z")
                        print("func fixed:",func)
                        
                        if func[0] == "*":
                            func = "1" + func
                            print("func fixed:",func)
                            
                        if respect == "x":
                            func = str(sym.integrate(func,x))
                            print("Answer except x:",func)
                        elif respect == "y":
                            func = str(sym.integrate(func,y))
                            print("Answer except y:",func)
                        elif respect == "z":
                            func = str(sym.integrate(func,z))
                            print("Answer except z:",func)
                        print("Answer:",str(func))
                        
                    print()
                    print("answer before () edit: ",func)
                    func_list = str(func).split(" ")
                    print("func_list",func_list)
                    print()
                    
                    func_display = ""
                    j = 0
                    while j < len(func_list):
                        if func_list[j].count("/") == 1:
                            print("Found div sign in:", func_list[j])
                            div_sign_index = func_list[j].find("/")
                            print("index of div sign:",div_sign_index)
                            func_edited = "(" + func_list[j][:div_sign_index] + ")" + func_list[j][div_sign_index:]
                            print("edited:",func_edited)
                            func_display = func_display + " " + func_edited
                        else:
                            func_display = func_display + " " + func_list[j]
                        j = j + 1
                    print("func_display",func_display)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "∫" * i + "f(" + respect + ") = " + str(func_display).replace("**","^").replace("*","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
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
sm.add_widget(Calculus_Calculator(name="Calculus_Calculator"))     
sm.current = "Homepage"   


class Calculus_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Calculus_Calculator().run()

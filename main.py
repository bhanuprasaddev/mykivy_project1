from kivy.app import App  # Importing the App class from the kivy module
from kivy.uix.boxlayout import BoxLayout  # Importing the BoxLayout class for layout
from kivy.uix.label import Label  # Importing the Label class for text display
from kivy.uix.textinput import TextInput  # Importing the TextInput class for text input
from kivy.uix.button import Button  # Importing the Button class for buttons
from kivy.uix.screenmanager import ScreenManager, Screen  # Importing the ScreenManager and Screen classes for managing screens

# Definition of the LoginScreen class which inherits from Screen class
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)  # Calling the constructor of the superclass
        self.layout = BoxLayout(orientation='vertical')  # Creating a vertical BoxLayout for the screen
        
        # Creating and adding Username label and input field to the layout
        self.username_label = Label(text='Username:')
        self.layout.add_widget(self.username_label)
        self.username_input = TextInput(hint_text='Enter username')
        self.layout.add_widget(self.username_input)
        
        # Creating and adding Password label and input field to the layout
        self.password_label = Label(text='Password:')
        self.layout.add_widget(self.password_label)
        self.password_input = TextInput(hint_text='Enter password', password=True)
        self.layout.add_widget(self.password_input)
        
        # Creating and adding Login button to the layout, and binding its press event to verify_credentials method
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.verify_credentials)
        self.layout.add_widget(self.login_button)
        
        # Adding the layout to the screen
        self.add_widget(self.layout)

    # Method to verify credentials entered by the user
    def verify_credentials(self, instance):
        # verification 
        if self.username_input.text == 'admin' and self.password_input.text == 'admin':
            self.manager.current = 'dashboard'  # Switching to the 'dashboard' screen if credentials are correct
        else:
            print("Invalid credentials. Please try again.")  # Printing error message if credentials are incorrect


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.welcome_label = Label(text='Welcome to the Dashboard!')
        self.layout.add_widget(self.welcome_label)
        
        self.home_button = Button(text='Home')
        self.home_button.bind(on_press=self.go_to_home)
        self.layout.add_widget(self.home_button)
        
        self.about_button = Button(text='About Our Company')
        self.about_button.bind(on_press=self.go_to_about)
        self.layout.add_widget(self.about_button)
        
        self.contact_button = Button(text='Contact Details')
        self.contact_button.bind(on_press=self.go_to_contact)
        self.layout.add_widget(self.contact_button)
        
        self.add_widget(self.layout)

    def go_to_home(self, instance):
        self.manager.current = 'home'

    def go_to_about(self, instance):
        self.manager.current = 'about'

    def go_to_contact(self, instance):
        self.manager.current = 'contact'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.home_label = Label(text='Welcome Home')
        self.layout.add_widget(self.home_label)
        
        self.back_button = Button(text='<', size_hint=(None, None), size=(50, 30))
        self.back_button.bind(on_press=self.go_to_dashboard)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)
    
    def go_to_dashboard(self, instance):
        self.manager.current = 'dashboard'

class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.about_label = Label(text='Hi, this is our company')
        self.layout.add_widget(self.about_label)
        
        self.back_button = Button(text='<', size_hint=(None, None), size=(50, 30))
        self.back_button.bind(on_press=self.go_to_dashboard)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)
    
    def go_to_dashboard(self, instance):
        self.manager.current = 'dashboard'

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super(ContactScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.contact_label = Label(text='Bhanu Prasad & SNV')
        self.layout.add_widget(self.contact_label)
    
        self.back_button = Button(text='<', size_hint=(None, None), size=(50, 30))
        self.back_button.bind(on_press=self.go_to_dashboard)
        self.layout.add_widget(self.back_button)

        
        self.add_widget(self.layout)
    
    def go_to_dashboard(self, instance):
        self.manager.current = 'dashboard'
        
# Definition of the MyApp class which inherits from the App class
class MyApp(App):
    # Method to build the application's UI
    def build(self):
        sm = ScreenManager()  # Creating a ScreenManager instance
        # Adding all defined screens to the ScreenManager
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ContactScreen(name='contact'))
        return sm  # Returning the ScreenManager instance as the application's UI

# Entry point of the application
if __name__ == '__main__':
    MyApp().run()  # Running the application

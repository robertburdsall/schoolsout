from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class yourapp(App):
    def build(self):
        root_widget = Label(text="Hello world!")
        return root_widget


yourapp().run()
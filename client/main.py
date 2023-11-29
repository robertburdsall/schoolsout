from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class YourApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title = Label()
        title.text = "Wait time: x"
        title.pos()

        graph = Rectangle()

        layout.add_widget(title)

        return layout


YourApp().run()

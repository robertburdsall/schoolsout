from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class YourApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        b1 = Button(text='button 1')
        b2 = Button (text='button 2')
        b3 = Button(text='button 3')

        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)

        return layout


YourApp().run()


"""
        root_widget = Label()
        root_widget.text = '[color=#ff0000]Hello[/color] [color=#00ff00]world![/color]'
        root_widget.font_size = 100
        root_widget.italic = True
        root_widget.markup = True

        return root_widget
"""
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import matplotlib as plt
import numpy as np

class YourApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title = Label()
        title.text = "Wait time: x"
        x = np.linspace(0, 2 * np.pi, 200)
        y = np.sin(x)

        fig, ax = plt.subplots()
        ax.plot(x, y)

        graph = plt.show()

        layout.add_widget(title)
        layout.add_widget(graph)

        return layout


YourApp().run()

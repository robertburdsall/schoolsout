from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

# create 1000 equally spaced points between -10 and 10
x = np.linspace(-10, 10, 1000)

# calculate the y value for each element of the x vector
y = -x ** 2 + 2 * x + 2

fig, ax = plt.subplots()
ax.plot(x, y)

plt.plot(x, y)
plt.ylabel("Wait time")
plt.xlabel("Time")


# add this to add background image
"""
MDScreen:
md_bg_color: 239 / 255, 239 / 255, 239 / 255, 1
name: "entrance"
FitImage:
source: "background_cropped.jpg"
"""

class Matty(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        Builder.load_file('matty.kv')

        return Matty()


MainApp().run()
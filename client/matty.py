from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
import json
import requests


class Matty(FloatLayout):

    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(0, 10, 1000)

    # calculate the y value for each element of the x vector
    y = x ** 2 + 2 * x + 2

    fig, ax = plt.subplots()
    line, = ax.plot(x, y)

    plt.plot(x, y)
    plt.ylabel("Wait time")
    plt.xlabel("Minutes")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # work on matplotlib background being transparent
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        self.wait_time_label = self.ids.wait_time_label


    def update_plot(self, slider_value):
        # Update y values based on the slider value
        y_vals = -self.x ** 2 + 2 * self.x + slider_value

        # Update the plot data
        self.line.set_ydata(y_vals)

        # Redraw the plot
        self.fig.canvas.draw()

    # work on color set
    def slide_it(self, *args):
        slider_value = args[1]
        self.slide_text.text = f"Enter a wait time: {str(int(args[1]))} mins"
        self.slide_text.font_size = 30

        # get this to work - color needs to change
        self.slide_text.text_color = 1, 0, 0, 1
        self.update_plot(slider_value)

        return args[1]
    
    def submit_pressed(self, instance):
        # Get the slider value
        slider_value = self.ids.waittime.value

        # Update the text of the wait time label
        self.wait_time_label.text = f"The current wait is: [color=#ADD8E6][u]{int(slider_value)}[/u][/color] Minutes!"



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        Builder.load_file('matty.kv')

        return Matty()



    # URL of the Flask server
    flask_server_url = 'http://127.0.0.1:5000/receive_data'

    # Data to be sent as JSON
    data_to_send = {'key': 'value', 'another_key': 'another_value'}

    # Package data as JSON
    json_data = json.dumps(data_to_send)

    # Set headers for the request
    headers = {'Content-Type': 'application/json'}


# work done after class will make the connection work!
"""
    # Send POST request to Flask server
    response = requests.post(flask_server_url, data=json_data, headers=headers)

    # Print the response from the server
    print(response.json())
"""

MainApp().run()

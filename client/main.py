from kivy.app import App
from kivy.uix.widget import Widget


class App(App):
    def build(self):
        return App()

# test

if __name__ == '__main__':
    App().run()

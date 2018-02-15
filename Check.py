from kivy.app import App
from kivy import Config
from kivy.lang import Builder
from kivy.metrics import cm
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.vkeyboard import VKeyboard

Builder.load_file('kivycheck.kv')
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 935)
Config.set('graphics', 'height', 470)


class Menu(BoxLayout):
    pass


class MycheckApp(App):
    def build(self):
        return Menu()


MycheckApp().run()

from kivy.app import App
from kivy import Config
from kivy.lang import Builder
from kivy.metrics import cm
from kivy.uix import dropdown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.vkeyboard import VKeyboard
import datetime


Builder.load_file('menu.kv')
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1250)
Config.set('graphics', 'height', 640)


class Menu(BoxLayout):

    def menu(self, text, count, price):
        layout = BoxLayout(orientation='horizontal')

        lbl1 = Label(text=text, color=[.17, .17, .17, 1],
                     size_hint=[.6, 1],
                     text_size=[cm(9), cm(0)])
        lbl2 = Label(text=count, color=[.17, .17, .17, 1],
                     size_hint=[.2, 1])
        lbl3 = Label(text=price, color=[.17, .17, .17, 1],
                     size_hint=[.2, 1])

        layout.add_widget(lbl1)
        layout.add_widget(lbl2)
        layout.add_widget(lbl3)
        self.ids.addLabel.add_widget(layout)


class MymenuApp(App):
    def build(self):
        return Menu()


if __name__ == '__main__':
    MymenuApp().run()

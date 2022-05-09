#from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.base import runTouchApp
from kivy.core.window import Window
import sys

#Window.size = (1280, 1024)
#Window.borderless = True
#Window.top = 0
#Window.left = 801
Window.fullscreen = 1

Builder.load_string("""

<PrinterLayout>:

    Image:
        id: img
        source: ''                     

""")

class PrinterLayout(Screen):
    def go_two(a, self):
        print("Display layer in two.py")
        self.ids.img.source = a

    def __init__(self, **kwargs):
        super(PrinterLayout, self).__init__(**kwargs)
        PrinterLayout.go_two(sys.argv[1], self)

runTouchApp(PrinterLayout())

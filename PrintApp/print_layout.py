from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.base import runTouchApp
from kivy.core.window import Window

Window.size = (800, 480)
Window.borderless = True
Window.top = 0
Window.left = 800
#Window.fullscreen = 1

Builder.load_string("""

<PrinterLayout>:

    Image:
        source: '../../Static/Images/cyrcle.png'                    

""")

class PrinterLayout(Screen):


    def __init__(self, **kwargs):
        super(PrinterLayout, self).__init__(**kwargs)

runTouchApp(PrinterLayout())

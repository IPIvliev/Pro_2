from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.base import runTouchApp
from kivy.core.window import Window
import os, time

import subprocess

Window.size = (800, 480)
#Window.borderless = True
Window.top = 100
Window.left = 200
#Window.fullscreen = 1

Builder.load_string("""

<PrinterLayout>:
    BoxLayout:
        Button:
            text: 'cyrcle'
            on_release:
                root.go()                 
        Button:
            text: 'communicate'
            on_release:
                root.com()   
""")

class PrinterLayout(Screen):

    def go(self):
        temp_dir = 'Temp'
        dir = os.listdir(temp_dir)
        with os.scandir(temp_dir) as files:
            for layer in files:

                t = subprocess.Popen(['python', 'two.py', layer], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=False)
        #subprocess.run(['python', 'two.py'], text=True, input='subprocess.PIPE', shell=True)
        #p = t.communicate(input=b'go_two()')[0]
        #print(p.decode())
                time.sleep(2)
                t.terminate()
    def com(self):
        p = PrinterLayout.t.communicate(input=go_two())

    def __init__(self, **kwargs):
        super(PrinterLayout, self).__init__(**kwargs)

runTouchApp(PrinterLayout())

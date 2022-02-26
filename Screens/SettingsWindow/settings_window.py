from kivy.uix.screenmanager import Screen
import os, sys


class SettingsWindow(Screen):
    def restart(self):
        os.execv(sys.executable, ['python'] + sys.argv)



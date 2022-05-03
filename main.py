from kivy.config import Config

Config.read('config.ini')

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from Screens.MainWindow.main_window import MainWindow
from Screens.ManageWindow.manage_window import ManageWindow
from Screens.SettingsWindow.settings_window import SettingsWindow
from Screens.AboutWindow.about_window import AboutWindow
from Screens.PrintWindow.print_window import PrintWindow
from Screens.CalibrationWindow.calibration_window import CalibrationWindow
from Screens.ZMovingWindow.z_moving_window import ZMovingWindow
from Screens.VatManageWindow.vat_manage_window import VatManageWindow
from Screens.DeveloperWindow.developer_window import DeveloperWindow
from Screens.PrintProcessWindow.print_process_window import PrintProcessWindow
from Screens.NetWindow.net_window import NetWindow
from Screens.PrintProcessWindow._popup_finish_printing import PopupFinishPrinting

# from Moduls.ping import Ping

Window.top = 0
Window.left = 0

class WindowManager(ScreenManager):

class MainApp(App):
    net_status = 'OffLine'

    def build(self):
        windows = Builder.load_file('main.kv')
        # Ping.callPing(windows)

        return windows

if __name__=='__main__':

    MainApp().run()


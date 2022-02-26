from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

class PopupFinishPrinting(Screen):

    def show_popup():
        show = PopupFinishPrinting() # Create a new instance of the P class 

        popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400)) 
        # Create the popup window

        popupWindow.open() # show the popup

    def close_popup(a):
        print('yes')
        a.dismiss()
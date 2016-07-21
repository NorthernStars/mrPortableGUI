import os
os.environ['KIVY_BCM_DISPMANX_ID'] = '4'


import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RootLayout(BoxLayout):
	pass


class MRPortableGui(App):

    def build(self):
        return RootLayout()


if __name__ == '__main__':
    MRPortableGui().run()
    

import os
os.environ['KIVY_BCM_DISPMANX_ID'] = '4'


import kivy
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MRPortableGui(App):

    def build(self):
        return Label(text='mrPortableGUI')


if __name__ == '__main__':
    MRPortableGui().run()
    

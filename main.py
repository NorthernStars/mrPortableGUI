import os
os.environ['KIVY_BCM_DISPMANX_ID'] = '4'


import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image

class MRPortableGui(App):

    def build(self):
    	self.screenManager = ScreenManager()
    	self.screenManager.add_widget( MainScreen(name="MainScreen") )
    	self.screenManager.add_widget( PowerOffScreen(name="PowerOffScreen") )
        return self.screenManager;
        
class MainScreen(Screen):
	pass
	
class PowerOffScreen(Screen):
	pass

class ImageButton(Button):

	source = ""

	def __init__(self, **kwargs):
		super(ImageButton, self).__init__(**kwargs)
		self.background_color = (0,0,0,0)
	pass
	

if __name__ == '__main__':
    MRPortableGui().run()
    

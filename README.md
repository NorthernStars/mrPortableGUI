# mrPortable
mrPortable is a portable Mixed-Reality (MR) system in a box. It includes a regular pc monitor horizontal mounted into a box.
The MR system works on a Raspberry Pi. The system also includes the official Raspberry Pi 7" touch screen for displaying a simple GUI to control der MR-System.
The system is designed to work with up to 6 MR-robots.

## mrPortableGUI
mrPortableGUI uses the kivy touch framework to display a simple user interface for controlling the MR system.

## Installation
This installation was tested on a Raspian.
On your Raspberry Pi update and upgrade your operating system to it's latest version and than install kivy, xinput and git:

    sudo apt-get install python-kivy xinput git

Now clone the mrPortableGUI into your home directoy

    cd ~
    git clone https://github.com/NorthernStars/mrPortableGUI.git

If you already installed the touch screen, also connect the pc monitor and edit your configuration to use the HDMI output as default screen.
Add to your /boot/config.txt the following line:

    display_default_lcd=0

Reboot and now the pc monitor should be your primary screen.
Now you need to enable the touch input inside kivy.
First you need to load python kivy module once. Open python console:

    python
    
Load kivy module and exit python console:

    import kivy
    exit()

Edit the kivy config file ~/.kivy/config.ini :

    nano ~/.kivy/config.ini

and add/replace content of [input] section with the following:

    mouse = mouse
    mtdev_%(name)s = probesysfs,provider=mtdev
    hid_%(name)s = probesysfs,provider=hidinput

Now you have to disable touch event inside the x server because otherwise touch on the touch screen GUI will effect the pc monitor output. First you need to identify the id of the touch input device:

    xinput --list | grep FT5406

which shows you the touch input device and it's id you need to remember. Normally it's id=8. This is only possible on real device screen, not using SSH!

To disable x server touch events and automatically start mrPortableGUI edit ~/.config/lxsession/LXDE-pi/autostart

    sudo nano ~/.config/lxsession/LXDE-pi/autostart

Add the following lines

    @xinput disable <ID>
    @lxterminal -e "/home/pi/mrPortableGUI/start.sh"

Replace <ID> with the id of your touch device (normally 8). If you used another path to clone mrPortableGUI repository you have to change the path to the start script in the second line above.
Now simply reboot and that's all.


### Hint: Running kivy application on touch screen
Currently it's not possible to use the second screen as extendes or seperate desktop. But you can run kivy application on it.
For that you can set the display where kivy should show the application on console before you start the kivy application using environment variable VC_DISPLAY :

    export VC_DISPLAY=4

or add the following lines at the very top of your kivy application code (before importing kivy!):

    import os
    os.environ['KIVY_BCM_DISPMANX_ID'] = '4'


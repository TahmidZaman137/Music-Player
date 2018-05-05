# ===================================================================================
#
# This is the main script which makes use of the Kivy module to design and construct
# the GUI. By running this script, the GUI of the music player app is executed.
#
# ===================================================================================

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

sm = None
position = 0



def PlayPauseSong(instance):
    global position
    if song.state == "stop":
        song.play()
        song.seek(position)
        instance.text = "Pause"
    elif song.state == "play":
        position = song.get_pos()
        print(position)
        song.stop()
        instance.text = "Play"


song = SoundLoader.load("DoIt.mp3")




def CreateToolbarButtons():
    # anchored toolbar buttons to centre of toolbar
    toolbarButtonsAnchor = AnchorLayout(anchor_x="center", anchor_y="center")

    # created gridlayout for 5 toolbar buttons
    toolbarButtons = GridLayout(size_hint=(0.5, 0.5))
    toolbarButtons.cols = 5
    toolbarButtonsAnchor.add_widget(toolbarButtons)

    # Creates the toolbar buttons
    shuffleBtn = Button(text="Shuffle")
    backBtn = Button(text="Back")
    playBtn = Button(text="Play")
    playBtn.bind(on_press=PlayPauseSong)



    forwardBtn = Button(text="Forward")
    loopBtn = Button(text="Loop")

    # adding buttons to the toolbar
    toolbarButtons.add_widget(shuffleBtn)
    toolbarButtons.add_widget(backBtn)
    toolbarButtons.add_widget(playBtn)
    toolbarButtons.add_widget(forwardBtn)
    toolbarButtons.add_widget(loopBtn)

    return toolbarButtonsAnchor

def CreateScreenManager():
    global sm
    sm = ScreenManager(size_hint=(1, 5))
    screen = Screen(name='Page 1')
    sm.add_widget(screen)
    screen.add_widget(Button(text="Main Page"))
    screen2 = Screen(name="Page 2")
    sm.add_widget(screen2)
    screen2.add_widget(Button(text="Playlist Page"))

    return sm

def screenChange(instance): # functionality for "switch" button
    if sm.current == "Page 1":
        sm.current = "Page 2"
    elif sm.current == "Page 2":
        sm.current = "Page 1"

def CreateSwitchButton():
    # anchored switch button to right of toolbar
    sbAnchor = AnchorLayout(anchor_x="right", anchor_y="center")

    # created boxlayout to contain switch button
    sbBox = BoxLayout(size_hint=(0.125, 0.5))
    sbAnchor.add_widget(sbBox)

    # Creates switch button
    changeButton = Button(text="Switch")
    changeButton.bind(on_press=screenChange)
    sbBox.add_widget(changeButton)

    return sbAnchor


class BaseGUI(GridLayout): # root widget for entire GUI

    def __init__(self, **kwargs):
        super(BaseGUI, self).__init__(**kwargs)
        self.rows = 2

        self.add_widget(CreateScreenManager())

        toolbar = FloatLayout()
        self.add_widget(toolbar)

        toolbar.add_widget(CreateSwitchButton())
        toolbar.add_widget(CreateToolbarButtons())


class MyApp(App):

    def build(self):
        return BaseGUI()  # Build according to the BaseGUI.


def DisplayGUI():
    if __name__ == '__main__':
        MyApp().run()


DisplayGUI()
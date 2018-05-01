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

class BaseGUI(GridLayout): # root widget for entire GUI

    def __init__(self, **kwargs):  # defines initial properties of the GUI
        super(BaseGUI, self).__init__(**kwargs)  # this has to be here, trust me...
        self.rows = 2

        # added screenmanager widget with two screens to top row
        sm = ScreenManager(size_hint = (1, 5))
        screen = Screen(name='Page 1')
        sm.add_widget(screen)
        screen.add_widget(Button(text = "Main Page"))
        screen2 = Screen(name="Page 2")
        sm.add_widget(screen2)
        screen2.add_widget(Button(text = "Playlist Page"))

        self.add_widget(sm)

        # adds empty toolbar to bottom row
        toolbar = FloatLayout()
        self.add_widget(toolbar)

        # function for switching between screens
        def screenChange(instance):
            if sm.current == "Page 1":
                sm.current = "Page 2"
            elif sm.current == "Page 2":
                sm.current = "Page 1"

        # anchored switch button to right of toolbar
        cbAnchor = AnchorLayout(anchor_x = "right", anchor_y = "center")
        toolbar.add_widget(cbAnchor)

        # created boxlayout to contain switch button
        cbBox = BoxLayout(size_hint = (0.125, 0.5))
        cbAnchor.add_widget(cbBox)

        # Creates switch button
        changeButton = Button(text="Switch")
        changeButton.bind(on_press=screenChange)
        cbBox.add_widget(changeButton)

        # anchored toolbar buttons to centre of toolbar
        toolbarButtonsAnchor = AnchorLayout(anchor_x = "center", anchor_y = "center")
        toolbar.add_widget(toolbarButtonsAnchor)

        # created gridlayout for 5 toolbar buttons
        toolbarButtons = GridLayout(size_hint = (0.5, 0.5))
        toolbarButtons.cols = 5
        toolbarButtonsAnchor.add_widget(toolbarButtons)

        # Creates the toolbar buttons
        shuffleBtn = Button(text="Shuffle")
        backBtn = Button(text="Back")
        playBtn = Button(text = "Play")
        forwardBtn = Button(text="Forward")
        loopBtn = Button(text="Loop")

        #adding buttons to the toolbar
        toolbarButtons.add_widget(shuffleBtn)
        toolbarButtons.add_widget(backBtn)
        toolbarButtons.add_widget(playBtn)
        toolbarButtons.add_widget(forwardBtn)
        toolbarButtons.add_widget(loopBtn)

class MyApp(App):

    def build(self):
        return BaseGUI()  # Build according to the BaseGUI.


def DisplayGUI():
    if __name__ == '__main__':
        MyApp().run()


DisplayGUI()
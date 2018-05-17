# ===================================================================================
#
# This is the main script which makes use of the Kivy module to design and construct
# the GUI. By running this script, the GUI of the music player app is executed.
#
# ===================================================================================

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

position = 0


class BaseGUI(GridLayout):
    def __init__(self, **kwargs):
        super(BaseGUI, self).__init__(**kwargs)

    song = SoundLoader.load("DoIt.mp3")

    def ScreenChange(self):
        myScreenManager = self.ids["sm"]
        if myScreenManager.current == "Main":
            myScreenManager.current = "Playlist"
        elif myScreenManager.current == "Playlist":
            myScreenManager.current = "Main"

    def PlayPauseSong(self):
        global position
        playButton = self.ids["Playbtn"]
        if self.song.state == "stop":
            self.song.play()
            self.song.seek(position)
            print("played at " + str(position))
            playButton.text = "Pause"
        elif self.song.state == "play":
            position = self.song.get_pos()
            print("stopped at " + str(position))
            self.song.stop()
            playButton.text = "Play"

    def Skip(self):
        global position
        mySlider = self.ids["slider"]
        position = mySlider.value
        self.song.seek(position)
        print("skipped to " + str(position))

    def ChangeVolume(self):
        volumeSlider = self.ids["volumebar"]
        self.song.volume = volumeSlider.value


root_widget = Builder.load_string("""

BaseGUI: 
    rows: 2
    ScreenManager:
        id: sm
        size_hint: (1,4)
        Screen:
            name: "Main"
            Button:
                text: "Main Page"
        Screen:
            name: "Playlist"
            Button:
                text: "Playlist Page"
    FloatLayout:
        id: toolbar
        AnchorLayout:
            anchor_x: "right"
            anchor_y: "center"
            Button:
                size_hint: (0.125, 0.5)
                text: "Switch"
                on_release: root.ScreenChange()
        AnchorLayout:
            anchor_x: "center"
            anchor_y: "center"
            GridLayout:
                size_hint: (0.5, 0.5)
                cols: 5
                Button:
                    text: "Shuffle"
                Button:
                    text: "Back"
                Button:
                    id: Playbtn
                    text: "Play"
                    on_release: root.PlayPauseSong()
                Button:
                    text: "Forward"
                Button:
                    text: "Loop"
        AnchorLayout:
            anchor_x: "center"
            anchor_y: "bottom"
            Slider:
                id: slider
                min: 0
                max: root.song.length
                size_hint: (0.6, 0.3)
                on_value: root.Skip()
        AnchorLayout:
            anchor_x: "left"
            anchor_y: "center"
            Slider:
                id: volumebar
                min: 0
                max: 1
                value: 0.5
                size_hint: (0.2, 0.4)
                on_value: root.ChangeVolume()
                
                
                
""")


class ExperimentalApp(App):
    def build(self):
        return root_widget  # Build according to the BaseGUI.


ExperimentalApp().run()

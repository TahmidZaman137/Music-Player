from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

import threading


position = 0
tbSlider = None
isSliderTracking = False
shouldSliderTrack = False


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
        global position, isSliderTracking, shouldSliderTrack
        playButton = self.ids["Playbtn"]
        if self.song.state == "stop":
            self.song.play()
            self.song.seek(position)
            print("play " + str(position))
            playButton.text = "Pause"
            shouldSliderTrack = True
        elif self.song.state == "play":
            position = self.song.get_pos()
            print("stop " + str(position))
            shouldSliderTrack = False
            self.song.stop()
            playButton.text = "Play"

    def skip(self):
        global position
        mySlider = self.ids["slider"]
        self.song.seek(mySlider.value)
        position = mySlider.value
        print("skipped to " + str(position))



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
                on_touch_up: root.skip()
                
            
""")


class ExperimentalApp(App):
    def build(self):
        return root_widget  # Build according to the BaseGUI.


ExperimentalApp().run()

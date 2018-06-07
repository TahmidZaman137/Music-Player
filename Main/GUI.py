# ===================================================================================
#
# This is the main script which makes use of the Kivy module to design and construct
# the GUI. By running this script, the GUI of the music player app is executed.
#
# ===================================================================================

# Kivy imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

position = 0 # Position variable for the currently loaded track

class BaseGUI(GridLayout):
    def __init__(self, **kwargs):
        super(BaseGUI, self).__init__(**kwargs)

    PathToAudio = r"C:\Users\tahmi\OneDrive\Documents\Git\Music-Player\Audio\\"
    song = SoundLoader.load(PathToAudio + "DoIt.mp3") # Variable contains the currently loaded track.

    def SwitchCurrentTrack(self, track): # Stops current track, loads new track and plays it from start.
        global position
        trackSlider = self.ids["slider"]
        volumeSlider = self.ids["volumebar"]
        playButton = self.ids["Playbtn"]
        self.song.stop()
        self.song = SoundLoader.load(track) # loads new hardcoded track into song variable
        trackSlider.max = self.song.length # Changes slider values to correspond with new song values.
        trackSlider.value = 0
        position = 0 # Sends song position back to zero for new song
        playButton.text = "Pause"
        self.song.volume = volumeSlider.value # Ensures volume stays consistent between track changes.
        self.song.play()
        self.song.seek(position)
        print("played at " + str(position))

    def ScreenChange(self): # Functionality for the switch button which switches between two screens.
        myScreenManager = self.ids["sm"]
        if myScreenManager.current == "Main":
            myScreenManager.current = "Playlist"
        elif myScreenManager.current == "Playlist":
            myScreenManager.current = "Main"

    def PlayPauseSong(self): # Function that controls playing/pausing current track.
        global position
        playButton = self.ids["Playbtn"]
        volumeSlider = self.ids["volumebar"]
        self.song.volume = volumeSlider.value
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

    def Skip(self): # Function used to skip to different parts of the current track using slider.
        global position
        trackSlider = self.ids["slider"]
        position = trackSlider.value
        self.song.seek(position)
        print("skipped to " + str(position))


    def ChangeVolume(self): # Changes volume using volume slider.
        volumeSlider = self.ids["volumebar"]
        self.song.volume = volumeSlider.value

# Kivy script returned by running the build function/creates and assigns functionality to the GUI.
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
            BoxLayout:
                orientation: "vertical"
                spacing: 10
                Button:
                    text: "Songs"
                    size_hint: (0.5, None)
                StackLayout:
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(root.PathToAudio + "DoIt.mp3") 
                    Label:
                        text: "Do It"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Tuxedo"
                        size_hint: (0.4, 0.25)
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(root.PathToAudio + "Here.mp3") 
                    Label:
                        text: "Here"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Alessia Cara (Lucian Remix)"
                        size_hint: (0.4, 0.25)
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(root.PathToAudio + "Infected.mp3") 
                    Label:
                        text: "Infected"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Sickick"
                        size_hint: (0.4, 0.25)
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(root.PathToAudio + "WaitForIt.mp3") 
                    Label:
                        text: "Wait For it"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Lin-Manuel Miranda (Hamilton)"
                        size_hint: (0.4, 0.25)
                    
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

# Builds the GUI when run.
class ExperimentalApp(App):
    def build(self):
        return root_widget  # Build according to the BaseGUI.


ExperimentalApp().run()

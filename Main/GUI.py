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

from random import randrange

position = 0 # Position variable for the currently loaded track

class BaseGUI(GridLayout):
    def __init__(self, **kwargs):
        super(BaseGUI, self).__init__(**kwargs)

    PathToAudio = r"C:\Users\tahmi\OneDrive\Documents\Git\Music-Player\Audio\\"

    songNames = ["DoIt", "Here", "Infected", "WaitForIt"]
    songTitles = ["Do It", "Here", "Infected", "Wait For It"]
    songImages = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg"]
    songNumber = 0

    song = SoundLoader.load(PathToAudio + songNames[songNumber] + ".mp3")  # Variable contains the currently loaded track.

    def SwitchCurrentTrack(self, playlistNumber): # Stops current track, loads new track and plays it from start.
        global position

        trackSlider = self.ids["slider"]
        volumeSlider = self.ids["volumebar"]
        playButton = self.ids["Playbtn"]
        titleWidget = self.ids["titlewidget"]
        imageWidget = self.ids["imagewidget"]

        self.song.stop()
        self.song = SoundLoader.load(self.PathToAudio + self.songNames[playlistNumber] + ".mp3") # loads new hardcoded track into song variable
        self.songNumber = playlistNumber

        titleWidget.text = self.songTitles[self.songNumber]
        imageWidget.source = self.songImages[self.songNumber]
        trackSlider.max = self.song.length # Changes slider values to correspond with new song values.
        trackSlider.value = 0
        self.song.volume = volumeSlider.value # Ensures volume stays consistent between track changes.
        playButton.text = "Pause"

        self.song.play()

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

    def Loop(self):
        if self.song.loop == False:
            self.song.loop = True
        elif self.song.loop == True:
            self.song.loop = False

    def Forward(self):
        trackSlider = self.ids["slider"]
        volumeSlider = self.ids["volumebar"]
        playButton = self.ids["Playbtn"]
        titleWidget = self.ids["titlewidget"]
        imageWidget = self.ids["imagewidget"]

        self.song.stop()

        if self.songNumber < 3:
            self.songNumber += 1
        else:
            self.songNumber = 0

        self.song = SoundLoader.load(self.PathToAudio + self.songNames[self.songNumber] + ".mp3")

        titleWidget.text = self.songTitles[self.songNumber]
        imageWidget.source = self.songImages[self.songNumber]
        playButton.text = "Pause"
        trackSlider.max = self.song.length  # Changes slider values to correspond with new song values.
        trackSlider.value = 0
        self.song.volume = volumeSlider.value  # Ensures volume stays consistent between track changes.

        self.song.play()

    def Back(self):
        trackSlider = self.ids["slider"]
        volumeSlider = self.ids["volumebar"]
        playButton = self.ids["Playbtn"]
        titleWidget = self.ids["titlewidget"]
        imageWidget = self.ids["imagewidget"]

        self.song.stop()

        if self.songNumber > 0:
            self.songNumber -= 1
        else:
            self.songNumber = 3

        self.song = SoundLoader.load(self.PathToAudio + self.songNames[self.songNumber] + ".mp3")

        titleWidget.text = self.songTitles[self.songNumber]
        imageWidget.source = self.songImages[self.songNumber]
        playButton.text = "Pause"
        trackSlider.max = self.song.length  # Changes slider values to correspond with new song values.
        trackSlider.value = 0
        self.song.volume = volumeSlider.value  # Ensures volume stays consistent between track changes.

        self.song.play()

    def Shuffle(self):
        trackSlider = self.ids["slider"]
        volumeSlider = self.ids["volumebar"]
        playButton = self.ids["Playbtn"]
        titleWidget = self.ids["titlewidget"]
        imageWidget = self.ids["imagewidget"]

        self.song.stop()

        self.songNumber = randrange(0, 3)
        self.song = SoundLoader.load(self.PathToAudio + self.songNames[self.songNumber] + ".mp3")

        titleWidget.text = self.songTitles[self.songNumber]
        imageWidget.source = self.songImages[self.songNumber]
        playButton.text = "Pause"
        trackSlider.max = self.song.length  # Changes slider values to correspond with new song values.
        trackSlider.value = 0
        self.song.volume = volumeSlider.value  # Ensures volume stays consistent between track changes.

        self.song.play()

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
            BoxLayout:
                orientation: "vertical"
                Label:
                    id: titlewidget
                    text: "Do it"
                AnchorLayout:
                    anchor_x: "center"
                    anchor_y: "center"
                    size_hint_y: 4 
                    Image:
                        id: imagewidget
                        source: "pic1.jpg"
                        
        Screen:
            name: "Playlist"
            BoxLayout:
                orientation: "vertical"
                spacing: 10
                Label:
                    text: "Songs"
                    size_hint: (1, None)
                StackLayout:
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(0) 
                    Label:
                        text: "Do It"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Tuxedo"
                        size_hint: (0.4, 0.25)
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(1) 
                    Label:
                        text: "Here"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Alessia Cara (Lucian Remix)"
                        size_hint: (0.4, 0.25)
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(2) 
                    Label:
                        text: "Infected"
                        size_hint: (0.4, 0.25)
                    Label:
                        text: "Sickick"
                        size_hint: (0.4, 0.25)
                    Button:
                        text: "Play"
                        size_hint: (0.15, 0.25)
                        on_press: root.SwitchCurrentTrack(3) 
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
                    on_release: root.Shuffle()
                Button:
                    text: "Back"
                    on_release: root.Back()
                Button:
                    id: Playbtn
                    text: "Play"
                    on_release: root.PlayPauseSong()
                Button:
                    text: "Forward"
                    on_release: root.Forward()
                ToggleButton:
                    text: "Loop"
                    on_press: root.Loop()
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

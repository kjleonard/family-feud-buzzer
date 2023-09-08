# This python script serves as a way to detect directional keys, enter and space to run a family feud style
# buzzer system.
from pygame import mixer
import keyboard
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    playAudio("assets/audio/AllClear.mp3")
    playAudio("assets/audio/BlueTeam.mp3")
    playAudio("assets/audio/RedTeam.mp3")


# This method will be used to play an audio file.
def playAudio(fileLoction):
    mixer.init()
    mixer.music.load(fileLoction)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

def getArrowInput():
    global systemArmed
    while True:
        if keyboard.is_pressed("left arrow") & systemArmed:
            systemArmed = False
            playAudio("assets/audio/BlueTeam.mp3")
        elif keyboard.is_pressed("right arrow") & systemArmed:
            systemArmed = False
            playAudio("assets/audio/RedTeam.mp3")
        elif keyboard.is_pressed("space bar"):
            systemArmed = True
            playAudio("assets/audio/AllClear.mp3")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global systemArmed
    systemArmed = True
    getArrowInput()
    #print_hi('PyCharm')


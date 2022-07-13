from pygame import mixer
from datetime import datetime
from time import time

# Functions for Playlist to play and stop
def music(playlist, stop):
    # Music load and play
    mixer.init()
    mixer.music.load(playlist)
    mixer.music.play(-1)
    # Music Stop
    while True:
        command = input()
        if command == stop:
            mixer.music.stop()
            break

# Save the date and time with activity
def log(container):
    with open("logfiles.txt", "a") as file:
        file.write(f"{container}{datetime.now()}\n")

# loops for every activity
while True:
    # You have to drink your water in every 50 minutes
    if time() - time() > 50*60:
        print(f"You have to drink water and then press 'Drank' to stop remainder: ")
        music('water.mp3', 'Drank')
        log("You drank your water in ")

    # You have to do eye exercise in every one hour
    if time() - time() > 60*60:
        print(f"You have to eye exercise and then press 'EyDone' to stop remainder: ")
        music('eyes.mp3', 'EyDone')
        log("You exercised your eye in ")

    # You have to do physical exercise in every 2 hours
    if time() - time() > 120*60:
        print(f"You have to exercise you body and then press 'ExDone' to stop remainder: ")
        music('physical.mp3', 'ExDone')
        log("You exercised your body in ")

    if time() - time() > 8*60*60:
        print("Your work is finish for today. Glad to have your time.")
        break

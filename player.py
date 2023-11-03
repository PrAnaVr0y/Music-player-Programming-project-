import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
import random

root = tk.Tk()
root.title("Pranavs Music Player")
root.geometry("485x700+290+10")
root.configure(background="#d3d3d3")
root.resizable(False, False)
mixer.init()

frameCnt = 30
frames = [PhotoImage(file="aa1.gif", format='gif -index %i' % i) for i in range(frameCnt)]
ind = 0

def update(ind):
    frame = frames[ind]
    ind = (ind + 1) % frameCnt
    label.configure(image=frame)
    root.after(100, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, ind)

def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_music():
    music_name = playlist.get(ACTIVE)
    print(music_name)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def shuffle_music():
    current_playlist = list(playlist.get(0, END))
    random.shuffle(current_playlist)
    playlist.delete(0, END)
    for song in current_playlist:
        playlist.insert(END, song)

lower_frame = Frame(root, bg="#d3d3d3", width=485, height=180)
lower_frame.place(x=0, y=400)

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

menu_image = PhotoImage(file="menu.png")
Label(root, image=menu_image).place(x=0, y=580, width=485, height=100)

frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=0, y=585, width=485, height=100)

play_button_image = PhotoImage(file="play1.png")
play_button = Button(root, image=play_button_image, bg="#d3d3d3", bd=0, height=60, width=60, command=play_music)
play_button.image = play_button_image  # Keeping a reference to the image
play_button.place(x=215, y=487)

stop_button_image = PhotoImage(file="stop.png")
stop_button = Button(root, image=stop_button_image, bg="#d3d3d3", bd=0, height=60, width=60, command=stop_music)
stop_button.image = stop_button_image  # Keeping a reference to the image
stop_button.place(x=130, y=487)

pause_button_image = PhotoImage(file="pause.png")
pause_button = Button(root, image=pause_button_image, bg="#d3d3d3", bd=0, height=60, width=60, command=pause_music)
pause_button.image = pause_button_image  # Keeping a reference to the image
pause_button.place(x=300, y=487)

volume_image = PhotoImage(file="volume.png")
volume_label = Label(root, image=volume_image)
volume_label.place(x=20, y=487)

volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, bg="#d3d3d3")
volume_scale.place(x=80, y=400)

shuffle_button_image = PhotoImage(file="shuffle.png")
Button(root, image=shuffle_button_image, bg="#d3d3d3", bd=0, height=60, width=60, command=shuffle_music).place(x=385, y=487)

Button(root, text="Browse Music", width=59, height=1, font=("Arial", 12, "bold"), fg="black", bg="#d3d3d3", command=add_music).place(x=0, y=550)

scroll = Scrollbar(frame_music)
playlist = Listbox(frame_music, width=100, font=("Arial", 10), bg="#d3d3d3", fg="black", selectbackground="#a3a3a3", cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()

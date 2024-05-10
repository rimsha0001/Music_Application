from tkinter import filedialog
from tkinter import *
import pygame
import os
window = Tk()
window.title("Music Player")
window.geometry("500x500")
pygame.mixer.init()
menubar = Menu(window)
window.config(menu=menubar)
songs = []
current_song = ""
paused = False
def load_music():
    global current_song
    window.directory = filedialog.askdirectory()

    for song in os.listdir(window.directory):
       name, ext = os.path.splitext(song)
       if ext == '.mp3':
           songs.append(song)

    for song in songs:
        songList.insert("end",song)

    songList.selection_set(0)
    current_song = songs[songList.curselection()[0]]

def play_music():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory,current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused= False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    pause = True

def next_music():
    global current_song,paused
    try:
        songList.selection_clear(0,END)
        index = songs.index(current_song)
        if index < len(songs) - 1:
            songList.selection_set(songs.index(current_song)+1)
            current_song = songs[songList.curselection()[0]]
        else:
            songList.select_set(0)
            current_song = songs[0]
        play_music()
    except:
        if songs:
            current_song = songs[0]
            play_music()
def previous_song():
    global current_song, paused
    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) - 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar,tearoff=False)
organise_menu.add_command(label='select Folder',command=load_music)
menubar.add_cascade(label='organise',menu=organise_menu)
songList = Listbox(window,bg="black",fg="white",width=100,height=15)
songList.pack()
next_btn_image = PhotoImage(file="next.png")
pause_btn_image = PhotoImage(file="pause.png")
play_btn_image = PhotoImage(file="play.png")
previous_btn_image = PhotoImage(file="previous.png")
control_frame = Frame(window)
control_frame.pack()
play_btn = Button(control_frame,image=play_btn_image,borderwidth=0,command=play_music)
pause_btn = Button(control_frame,image=pause_btn_image,borderwidth=0,command=pause_music)
next_btn = Button(control_frame,image=next_btn_image,borderwidth=0,command=next_music)
previous_btn = Button(control_frame,image=previous_btn_image,borderwidth=0,command=previous_song)
play_btn.grid(row=0,column=0,padx=7,pady=10)
pause_btn.grid(row=0,column=1,padx=7,pady=10)
next_btn.grid(row=0,column=2,padx=7,pady=10)
previous_btn.grid(row=0,column=3,padx=7,pady=10)
window.mainloop()

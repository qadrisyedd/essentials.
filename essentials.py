'''
Name: Syed Qadri
Date: 05/21/2024
Program: Essentials Program (CPT)
Class: ICU4U1-02
'''

import pickle  # Import pickle for object serialization
import time  # Import time for time-related functions
from random import randint  # Import random for password related functions
# Imports
from tkinter import *  # Import all classes, functions, and variables from the tkinter module
from tkinter import Tk, PhotoImage, Frame, Label, Button, LabelFrame, Toplevel, messagebox, Text, RAISED, END, CENTER, \
    ttk  # Specific imports from tkinter
from tkinter.filedialog import askopenfilename, \
    asksaveasfilename  # Import file dialog functions for opening and saving files

import customtkinter as ctk  # Import customtkinter for custom Tkinter widgets (Slider)
import pygame  # Import pygame for audio playback and other multimedia functionalities

from directory import MP3, Whiteboard, Stopwatch  # Import from essentials directory (custom)


# Functions
def clock():
    """Update the clock label with the current time."""
    Time = time.strftime('%I:%M %p')  # Format the current time
    lbl_clock.config(text=Time)  # Update the label with the current time
    lbl_clock.after(1000, clock)  # Call the clock function again after 1000 milliseconds

def delete_item():
    """Delete the selected item from the listbox."""
    listbox.delete(ANCHOR)  # Delete the currently selected item from the listbox

def add_item():
    """Add a new item to the listbox."""
    listbox.insert(END, f' • {tasks.get()}')  # Insert the new task at the end of the listbox
    tasks.delete(0, END)  # Clear the entry widget

def new_rand():
    pw_entry.config(state='normal')
    pw_entry.delete(0, END)
    pw_entry.config(state='readonly')
    try:
        pw_length = int(pswd_entry.get())
        my_pswd = ''
        for x in range(pw_length):
            my_pswd += chr(randint(33, 126))
        pw_entry.config(state='normal')
        pw_entry.insert(0, my_pswd)
        pw_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror('Error!', "Please enter a 'real' numerical value")
        return

def clipper():
    mainframe.clipboard_clear()
    mainframe.clipboard_append(pw_entry.get())

def cross_item():
    """Cross out the selected item in the listbox."""
    global light  # Access the global variable 'light'
    try:
        if light:
            listbox.itemconfig(listbox.curselection(), fg='Gray')  # Change the color of the selected item to brown
            listbox.selection_clear(0, END)  # Clear the selection
        else:
            listbox.itemconfig(listbox.curselection(), fg='#212121')  # Change the color of the selected item to dark gray
        listbox.selection_clear(0, END)  # Clear the selection
    except:
        pass  # Ignore any exceptions

def clear_list():
    """Clear all items from the listbox."""
    listbox.delete(0, END)  # Delete all items from the listbox

def save_list():
    """Save the current listbox items to a file."""
    file_name = asksaveasfilename(title='Save File', filetypes=(('Dat Files', "*.dat"), ('All Files', '*.*')))  # Open a file save dialog
    if file_name:
        if not file_name.endswith('.dat'):
            file_name = f'{file_name}.dat'  # Ensure the file name ends with '.dat'
        items = listbox.get(0, END)  # Get all items from the listbox
        output_file = open(file_name, 'wb')  # Open the file in write-binary mode
        pickle.dump(items, output_file)  # Serialize the listbox items to the file

def open_list():
    """Open a file and load the listbox items from it."""
    file_name = askopenfilename(title='Open File', filetypes=(('Dat Files', "*.dat"), ('All Files', '*.*')))  # Open a file open dialog
    if file_name:
        listbox.delete(0, END)  # Clear the listbox
        input_file = open(file_name, 'rb')  # Open the file in read-binary mode
        items = pickle.load(input_file)  # Deserialize the listbox items from the file
        for item in items:
            listbox.insert(END, item)  # Insert each item into the listbox

def close_music_player():
    """Stop the music and close the music player window."""
    global state  # Access the global variable 'state'
    pygame.mixer.music.stop()  # Stop the music
    app_music.withdraw()  # Hide the music player window
    mwindow.deiconify()  # Show the main window
    state = False  # Set the state to False


def music_player():
    """Open and configure the music player window."""
    global singledisplay, lbl_cn, cover, btn_play  # Access global variables
    if singledisplay:
        mwindow.withdraw()  # Hide the main window if single display is enabled
    app_music.deiconify()  # Show the music player window
    app_music.title('Music Player - Essentials')  # Set the title of the music player window
    app_music.protocol('WM_DELETE_WINDOW', close_music_player)  # Set the close window protocol
    app_music.resizable(False, False)  # Make the window non-resizable
    app_music.iconphoto(False, icon)  # Set the window icon
    pygame.mixer.init()  # Initialize the pygame mixer

    if light:
        # Configure the music player window for light theme
        app_music.geometry(
            f'400x480+{app_music.winfo_screenwidth() // 2 - 400 // 2}+{app_music.winfo_screenheight() // 2 - 400 // 2}')
        ctk.set_default_color_theme('blue')
        background = Frame(app_music, bg='#F1EFE7', width=400, height=480)
        background.place(x=0, y=0)
        btn_backward = Button(app_music, image=img_lbackward, bd=0, command=back)
        btn_backward.place(relx=0.25, rely=0.7, anchor=CENTER)
        btn_play = Button(app_music, image=img_lplay, bd=0, command=play)
        btn_play.place(relx=0.50, rely=0.7, anchor=CENTER)
        btn_forward = Button(app_music, image=img_lforward, bd=0, command=skip)
        btn_forward.place(relx=0.75, rely=0.7, anchor=CENTER)
        soundbar = ctk.CTkSlider(master=app_music, from_=0, to=1, command=volume, width=210)
        soundbar.place(relx=0.5, rely=0.78, anchor=CENTER)
        lbl_cn = Label(app_music, text='essentials.', bg='#F1EFE7', fg='#222222', font=('Time New Roman', 10, 'bold'))
        lbl_cn.place(relx=0.4, rely=0.6)
        cover = Label(app_music, width=250, height=250, image=img_lcover)
        cover.place(relx=0.19, rely=0.06)
        btn_p1 = Button(app_music, text='Hype', fg='#F1EFE7', bg='#222222', font=('Time New Roman', 10, 'bold'),
                        width=10, command=lambda p='hype': playlist(p))
        btn_p1.place(relx=0.5, rely=0.87, anchor=CENTER)
        btn_p2 = Button(app_music, text='Chill', fg='#F1EFE7', bg='#222222', font=('Time New Roman', 10, 'bold'),
                        width=10, command=lambda p='chill': playlist(p))
        btn_p2.place(relx=0.25, rely=0.87, anchor=CENTER)
        btn_p3 = Button(app_music, text='Spanish', fg='#F1EFE7', bg='#222222', font=('Time New Roman', 10, 'bold'),
                        width=10, command=lambda p='spanish': playlist(p))
        btn_p3.place(relx=0.75, rely=0.87, anchor=CENTER)

    if dark:
        # Configure the music player window for dark theme
        app_music.geometry(
            f'480x550+{app_music.winfo_screenwidth() // 2 - 480 // 2}+{app_music.winfo_screenheight() // 2 - 550 // 2}')
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')
        background = Label(app_music, image=img_dmusicui, width=480, height=550, highlightthickness=0)
        background.pack()
        btn_backward = Button(app_music, image=img_dbackward, bd=-1, width=38, height=38, activebackground='#212121',
                              command=back)
        btn_backward.place(x=156, y=365, anchor=CENTER)
        btn_play = Button(app_music, image=img_dplay, bd=-1, width=38, height=38, activebackground='#212121',
                          command=play)
        btn_play.place(x=240, y=365, anchor=CENTER)
        btn_forward = Button(app_music, image=img_dforward, bd=-1, width=38, height=38, activebackground='#212121',
                             command=skip)
        btn_forward.place(x=324, y=365, anchor=CENTER)
        soundbar = ctk.CTkSlider(master=app_music, from_=0, to=1, width=200, command=volume)
        soundbar.place(relx=0.5, y=421, anchor=CENTER)
        lbl_cn = Label(app_music, text='essentials.', bg='#303030', fg='#BB86FC', font=('Time New Roman', 10, 'bold'))
        lbl_cn.place(relx=0.2, y=485)
        lbl_dp = Label(app_music, text='essentials. MP3 Music Player; Syed Qadri', bg='#303030', fg='#BB86FC',
                       font=('Time New Roman', 7, 'bold'))
        lbl_dp.place(relx=0.2, y=505)
        cover = Label(app_music, width=250, height=250, image=img_dcover)
        cover.place(relx=0.5, y=186, anchor=CENTER)
        btn_p1 = Button(app_music, text='Hype', fg='#F1EFE7', bd=0, bg='#303030', activebackground='#303030',
                        activeforeground='#BB86FC', font=('Time New Roman', 6, 'bold'), width=7,
                        command=lambda p='hype': playlist(p))
        btn_p1.place(relx=0.855, rely=0.889, anchor=CENTER)
        btn_p2 = Button(app_music, text='Chill', fg='#F1EFE7', bd=0, bg='#303030', activebackground='#303030',
                        activeforeground='#BB86FC', font=('Time New Roman', 6, 'bold'), width=7,
                        command=lambda p='chill': playlist(p))
        btn_p2.place(relx=0.855, rely=0.921, anchor=CENTER)
        btn_p3 = Button(app_music, text='Spanish', fg='#F1EFE7', bd=0, bg='#303030', activebackground='#303030',
                        activeforeground='#BB86FC', font=('Time New Roman', 6, 'bold'), width=7,
                        command=lambda p='spanish': playlist(p))
        btn_p3.place(relx=0.855, rely=0.953, anchor=CENTER)


def playlist(current):
    """Switch to the selected playlist and start playing from the first song."""
    global plist1, plist2, song_index  # Access global variables
    if current == 'hype':
        plist1 = True
        plist2 = False
        song_index = 1  # Set the song index to the first song
        back()  # Start playing the first song in the playlist
    elif current == 'chill':
        plist1 = False
        plist2 = True
        song_index = 1  # Set the song index to the first song
        back()  # Start playing the first song in the playlist
    elif current == 'spanish':
        plist1 = False
        plist2 = False
        song_index = 1  # Set the song index to the first song
        back()  # Start playing the first song in the playlist


def play():
    """Play the selected song or resume playback if paused."""
    global song_index, btn_play, state, plist1, plist2  # Access global variables
    if state == False:
        current_song = song_index
        if plist1:
            song_name = playlist_one[song_index]  # Get the song name from the first playlist
        elif plist2:
            song_name = playlist_two[song_index]  # Get the song name from the second playlist
        else:
            song_name = playlist_three[song_index]  # Get the song name from the third playlist
        pygame.mixer.music.load(song_name)  # Load the song into the mixer
        pygame.mixer.music.set_volume(0.5)  # Set the volume to 50%
        pygame.mixer.music.play(loops=0)  # Play the song once
        album_cover(song_name, song_index)  # Update the album cover
    state = True  # Set the state to True (playing)
    if state:
        if light:
            btn_play.config(image=img_lpause, command=pause)  # Update the play button to pause
        if dark:
            btn_play.config(image=img_dpause, command=pause)  # Update the play button to pause

        pygame.mixer.music.unpause()  # Unpause the music


def pause():
    """Pause the current playback."""
    global state, btn_play  # Access global variables
    pygame.mixer.music.pause()  # Pause the music
    state = None  # Set the state to None (paused)
    if light:
        btn_play.config(image=img_lplay, command=play)  # Update the pause button to play
    if dark:
        btn_play.config(image=img_dplay, command=play)  # Update the pause button to play


def album_cover(name, index):
    """Update the album cover and song title."""
    global lbl_cn, cover, plist1, plist2  # Access global variables
    current_name = name[6:-4]  # Extract the song name from the file path
    lbl_cn.config(text=current_name)  # Update the song title label
    app_music.title(f'Music Player - {current_name}')  # Update the window title
    if plist1:
        cover.config(image=coverlist_one[index])  # Update the album cover for the first playlist
    elif plist2:
        cover.config(image=coverlist_two[index])  # Update the album cover for the second playlist
    else:
        cover.config(image=coverlist_three[index])  # Update the album cover for the third playlist


def skip():
    """Skip to the next song in the playlist."""
    global song_index, state  # Access global variables
    song_index += 1  # Increment the song index
    if song_index > 9:
        song_index = 0  # Wrap around if the index exceeds the playlist length
    state = False  # Set the state to False (not playing)
    play()  # Play the next song


def back():
    """Go back to the previous song in the playlist."""
    global song_index, state  # Access global variables
    song_index -= 1  # Decrement the song index
    if song_index < 0:
        song_index = 9  # Wrap around if the index is less than 0
    state = False  # Set the state to False (not playing)
    play()  # Play the previous song


def volume(sound):
    """Set the volume of the music player."""
    pygame.mixer.music.set_volume(sound)  # Set the volume based on the slider value


def close_notepad():
    """Close the notepad window after asking for confirmation."""
    check_save = messagebox.askquestion('Warning!','Are you sure you want to quit this session?\nAll unsaved data will be lost.')
    if check_save == 'yes':
        app_notepad.withdraw()  # Hide the notepad window
        mwindow.deiconify()  # Show the main window
    else:
        return  # Do nothing if the user chooses 'no'


def notepad():
    """Open and configure the notepad window."""

    def save_note():
        """Save the current note to a file."""
        file_location = asksaveasfilename(defaultextension='txt',
                                          filetypes=[('Text files', '*.txt'), ['All files', '*.*']])
        if not file_location:
            return  # Return if no file location is selected
        with open(file_location, 'w') as file_output:
            text = txt_box.get(1.0, END)  # Get the text from the text box
            file_output.write(text)  # Write the text to the file
            app_notepad.title(f'Notes - Essentials ({file_location})')  # Update the window title with the file location

    def open_note():
        """Open a note from a file."""
        global light, dark  # Access global variables
        file_location = askopenfilename(defaultextension='txt',
                                        filetypes=[('Text files', '*.txt'), ['All files', '*.*']])
        if not file_location:
            return  # Return if no file location is selected
        txt_box.delete(1.0, END)  # Clear the text box
        with open(file_location, 'r') as file_input:
            text = file_input.read()  # Read the text from the file
            txt_box.insert(END, text)  # Insert the text into the text box
            app_notepad.title(f'Notes - Essentials ({file_location})')  # Update the window title with the file location

    global singledisplay  # Access global variables
    if singledisplay:
        mwindow.withdraw()  # Hide the main window if single display is enabled
    app_notepad.deiconify()  # Show the notepad window
    app_notepad.title('Notes - Essentials (New Note)')  # Set the title of the notepad window
    app_notepad.protocol('WM_DELETE_WINDOW', close_notepad)  # Set the close window protocol
    app_notepad.iconphoto(False, icon)  # Set the window icon
    app_notepad.resizable(False, False)  # Make the window non-resizable
    app_notepad.geometry(
        f'595x500+{app_notepad.winfo_screenwidth() // 2 - 595 // 2}+{app_notepad.winfo_screenheight() // 2 - 500 // 2}')
    app_notepad.rowconfigure(0, minsize=500)
    app_notepad.columnconfigure(1, minsize=500)

    if light:
        # Configure the notepad window for light theme
        txt_box = Text(app_notepad, bg='#DBC293', width=30)
        txt_box.grid(row=0, column=1, sticky='nsew')
        f_btns = Frame(app_notepad, relief=RAISED, bd=0, bg='#FFF4DF')
        f_btns.grid(row=0, column=0, sticky='ns')
        btn_open = Button(f_btns, image=img_lightopen, command=open_note)
        btn_open.grid(row=0, column=0, padx=5, pady=5)
        btn_save = Button(f_btns, image=img_lightsave, command=save_note)
        btn_save.grid(row=1, column=0, padx=5)

    if dark:
        # Configure the notepad window for dark theme
        txt_box = Text(app_notepad, bg='#070117', fg='#BFA75D', insertbackground='#BFA75D', width=50)
        txt_box.grid(row=0, column=1, sticky='nsew')
        f_btns = Frame(app_notepad, relief=RAISED, bd=0, bg='black')
        f_btns.grid(row=0, column=0, sticky='ns')
        btn_open = Button(f_btns, image=img_darkopen, command=open_note)
        btn_open.grid(row=0, column=0, padx=5, pady=5)
        btn_save = Button(f_btns, image=img_darksave, command=save_note)
        btn_save.grid(row=1, column=0, padx=5)

# Function to toggle menu
def toggle_menu():
    # Function to close the menu
    def close_menu():
        menu.destroy()  # Destroys the menu widget
        btn_menu.config(text='☰', command=toggle_menu)  # Changes the button text and command

    # Function to switch to light mode
    def light_mode():
        global light, dark
        light, dark = True, False  # Sets the light mode to True and dark mode to False
        btn_light.config(image=img_ltriggered, relief='sunken', command=0)  # Updates the light mode button
        btn_dark.config(image=img_dark, relief='raised', command=dark_mode)  # Updates the dark mode button
        ui.config(image=lightui)  # Updates the UI to light mode

        # Update various UI components to light mode colors and configurations
        fillONE.config(bg='#F8A37A')
        fillTWO.config(bg='#F8A37A')
        fillTHREE.config(bg='#F8A37A')
        fillFOUR.config(bg='#FFF4DF')
        lbl_clock.config(bg='#FDF0D7', fg='#32012F')
        btn_menu.config(bg='#F8A37A', fg='#467372', activebackground='#467372', activeforeground='#F8A37A')
        btn_notepad.config(bg='#FFF4DF', image=img_lnotepad, activebackground='#FFF4DF')
        btn_music.config(bg='#FFF4DF', image=img_lmusic, activebackground='#FFF4DF')
        btn_whiteboard.config(bg='#FFF4DF', image=img_lwhiteboard, activebackground='#FFF4DF')
        btn_calculator.config(bg='#FFF4DF', image=img_lcalculator, activebackground='#FFF4DF')
        btn_stopwatch.config(bg='#FFF4DF', image=img_lstopwatch, activebackground='#FFF4DF')
        btn_delete.config(bg='#DDD2C1', activebackground='black', activeforeground='white', fg='black', bd=1)
        btn_add.config(bg='#DDD2C1', activebackground='black', activeforeground='white', fg='black', bd=1)
        btn_cross.config(bg='#DDD2C1', activebackground='black', activeforeground='white', fg='black', bd=1)
        btn_clear.config(bg='#DDD2C1', activebackground='black', activeforeground='white', fg='black', bd=1)
        btn_openlist.config(bg='#DDD2C1', activebackground='black', activeforeground='white', fg='black', bd=1)
        btn_savelist.config(bg='#DDD2C1', activebackground='black', activeforeground='white', fg='black', bd=1)
        todo_app.config(bg='#DDD2C1')
        todo.config(bg='#DDD2C1')
        listbox.config(selectbackground='#a6a6a6', bg='#DDD2C1', fg='black')
        scrollbar.config(bg='#DDD2C1')
        tasks.config(bg='#DDD2C1')
        btn_frame.config(bg='#DDD2C1')
        pswd.config(bg='#DDD2C1')
        title.config(bg='#DDD2C1', fg='black')
        plf.config(bg='#DDD2C1', fg='black')
        pswd_entry.config(bg='#bab0a0', fg='black')
        pw_entry.config(readonlybackground='#bab0a0', fg='black')
        pbtn_frame.config(bg='#DDD2C1')
        btn_generate.config(bg='#DDD2C1', fg='black', activebackground='#DDD2C1', activeforeground='gray')
        btn_copy.config(bg='#DDD2C1', fg='black', activebackground='#DDD2C1', activeforeground='gray')
        mwindow.update()  # Updates the window to reflect changes

    # Function to switch to dark mode
    def dark_mode():
        global light, dark
        light, dark = False, True  # Sets the light mode to False and dark mode to True
        btn_dark.config(image=img_dtriggered, relief='sunken', command=0)  # Updates the dark mode button
        btn_light.config(image=img_light, relief='raised', command=light_mode)  # Updates the light mode button
        ui.config(image=darkui)  # Updates the UI to dark mode

        # Update various UI components to dark mode colors and configurations
        fillONE.config(bg='#3C0753')
        fillTWO.config(bg='#3C0753')
        fillTHREE.config(bg='#3C0753')
        fillFOUR.config(bg='#070117')
        lbl_clock.config(bg='#121212', fg='#BB86FC')
        btn_menu.config(bg='#3C0753', fg='#CB6CE6', activebackground='#CB6CE6', activeforeground='#3C0753')
        btn_notepad.config(bg='#070117', image=img_dnotepad, activebackground='#070117')
        btn_music.config(bg='#070117', image=img_dmusic, activebackground='#070117')
        btn_whiteboard.config(bg='#070117', image=img_dwhiteboard, activebackground='#070117')
        btn_calculator.config(bg='#070117', image=img_dcalculator, activebackground='#070117')
        btn_stopwatch.config(bg='#070117', image=img_dstopwatch, activebackground='#070117')
        btn_delete.config(bg='#121212', fg='#03DAC6', activebackground='black', activeforeground='white', bd=0)
        btn_add.config(bg='#121212', fg='#03DAC6', activebackground='black', activeforeground='white', bd=0)
        btn_cross.config(bg='#121212', fg='#03DAC6', activebackground='black', activeforeground='white', bd=0)
        btn_clear.config(bg='#121212', fg='#03DAC6', activebackground='black', activeforeground='white', bd=0)
        btn_openlist.config(bg='#121212', fg='#03DAC6', activebackground='black', activeforeground='white', bd=0)
        btn_savelist.config(bg='#121212', fg='#03DAC6', activebackground='black', activeforeground='white', bd=0)
        todo_app.config(bg='#121212')
        todo.config(bg='#121212')
        listbox.config(selectbackground='#212121', bg='#121212', fg='#BB86FC')
        scrollbar.config(bg='#121212')
        tasks.config(bg='#121212', fg='#BB86FC')
        btn_frame.config(bg='#121212')

        pswd.config(bg='#121212')
        title.config(bg='#121212', fg='#BB86FC')
        plf.config(bg='#121212', fg='#BB86FC')
        pswd_entry.config(bg='#212121', fg='white')
        pw_entry.config(readonlybackground='#212121', fg='#ed856d')
        pbtn_frame.config(bg='#121212')
        btn_generate.config(bg='#121212', fg='#03DAC6', activebackground='#121212', activeforeground='white')
        btn_copy.config(bg='#121212', fg='#03DAC6', activebackground='#121212', activeforeground='white')

        mwindow.update()  # Updates the window to reflect changes

    # Function to enable multiple displays
    def multiple_displays():
        global singledisplay
        singledisplay = False  # Sets the single display to False
        btn_yes.config(relief='sunken', command=0)  # Updates the YES button
        btn_no.config(relief='raised', command=single_display)  # Updates the NO button

    # Function to enable single display
    def single_display():
        global singledisplay
        singledisplay = True  # Sets the single display to True
        btn_no.config(relief='sunken', command=0)  # Updates the NO button
        btn_yes.config(relief='raised', command=multiple_displays)  # Updates the YES button

    global light, dark, city_entry

    # Creates the menu frame
    menu = Frame(mainframe, bg='#467372')
    menu.place(x=0, y=43, height=mheight, width=200)
    btn_menu.config(text='X', command=close_menu)  # Changes the button text and command

    # Creates the menu items frame
    menu_items = LabelFrame(menu, width=180, height=635, text=' QUICK ACCESS ', padx=10, pady=10, font="TkDefaultFont 12 bold", relief="solid", borderwidth=3, bg='#467372')
    menu_items.place(x=10, y=10)

    items_frame = Frame(menu_items, bg='#467372')
    items_frame.place(x=0, y=0)

    # Adds theme label
    theme = Label(items_frame, text='Theme:', font=('Time New Roman', 10, 'bold'), bg='#467372')
    theme.grid(row=0, column=0)

    # Adds light and dark mode buttons
    if light:
        btn_light = Button(items_frame, image=img_ltriggered, bd=0, bg='#467372', activebackground='#467372', command=light_mode, relief='sunken')
        btn_light.grid(row=1, column=0, pady=15, padx=10)
        btn_dark = Button(items_frame, image=img_dark, bd=0, bg='#467372', activebackground='#467372', command=dark_mode)
        btn_dark.grid(row=1, column=1, pady=15, padx=10)
    elif dark:
        btn_light = Button(items_frame, image=img_light, bd=0, bg='#467372', activebackground='#467372', command=light_mode)
        btn_light.grid(row=1, column=0, pady=15, padx=10)
        btn_dark = Button(items_frame, image=img_dtriggered, bd=0, bg='#467372', activebackground='#467372', command=dark_mode, relief='sunken')
        btn_dark.grid(row=1, column=1, pady=15, padx=10)

    # Label for Multiple Displays option
    md = Label(items_frame, text='Mutliple\nDisplays:', font=('Time New Roman', 10, 'bold'), bg='#467372', justify='left')
    md.grid(row=2, column=0)

    # Setting relief and commands for YES and NO buttons based on singledisplay variable
    if singledisplay:
        mdrelief = 'raised'  # Raised relief if single display is enabled
        mdcommand = multiple_displays  # Command to enable multiple displays
        sdrelief = 'sunken'  # Sunken relief if single display is enabled
        sdcommand = 0  # No command when single display is enabled
    else:
        mdrelief = 'sunken'  # Sunken relief if single display is disabled
        mdcommand = 0  # No command when single display is disabled
        sdrelief = 'raised'  # Raised relief if single display is disabled
        sdcommand = single_display  # Command to enable single display

    # YES button for Multiple Displays option
    btn_yes = Button(items_frame, text='YES', font=('Time New Roman', 10, 'bold'), bg='#467372',
                     activebackground='#467372', command=mdcommand, relief=mdrelief)
    btn_yes.grid(row=3, column=0, pady=15, padx=10, ipadx=5, ipady=5)

    # NO button for Multiple Displays option
    btn_no = Button(items_frame, text='NO', font=('Time New Roman', 10, 'bold'), bg='#467372',
                    activebackground='#467372', command=sdcommand, relief=sdrelief)
    btn_no.grid(row=3, column=1, pady=15, padx=10, ipadx=5, ipady=5)

# Function to close the whiteboard window
def close_whiteboard():
    global app_whiteboard
    app_whiteboard.destroy()  # Destroy the whiteboard window
    mwindow.deiconify()  # Restore the main window

# Function to open the whiteboard window
def whiteboard():
    global singledisplay, app_whiteboard
    app_whiteboard = Toplevel()  # Create a new top-level window for the whiteboard
    if singledisplay:
        mwindow.withdraw()  # Hide the main window if in single display mode
    app_whiteboard.deiconify()  # Display the whiteboard window
    app_whiteboard.title('Whiteboard - Essentials')  # Set the title of the whiteboard window
    app_whiteboard.protocol('WM_DELETE_WINDOW', close_whiteboard)  # Define close behavior
    app_whiteboard.iconphoto(False, icon)  # Set the window icon
    if light:
        wb = Whiteboard(app_whiteboard)  # Initialize a light-themed whiteboard
    if dark:
        wb = Whiteboard(app_whiteboard, light=False)  # Initialize a dark-themed whiteboard

# Function to close the calculator window
def close_calculator():
    app_calculator.withdraw()  # Withdraw (hide) the calculator window
    mwindow.deiconify()  # Restore the main window

# Function to open the calculator window
def calculator():

    # Function to add a number to the display
    def add_num(num):
        value = display.get()
        if value == '0':
            value = num
        else:
            value += num
        display.delete(0, END)
        display.insert(0, value)

    # Function to add an operator to the calculation
    def add_op(operator):
        global first_num, math_operator
        first_num = int(display.get())
        math_operator = operator
        display.delete(0, END)

    # Function to perform the calculation
    def calculate():
        try:
            second_num = int(display.get())
            display.delete(0, END)
            if math_operator == '+':
                result = first_num + second_num
            elif math_operator == '-':
                result = first_num - second_num
            elif math_operator == '*':
                result = first_num * second_num
            else:
                result = first_num / second_num
            display.insert(0, result)
        except Exception as exception:
            messagebox.showerror('Error', f'Could not execute: {exception}')

    # Function to clear the calculator display
    def clear():
        global first_num, math_operator
        first_num, math_operator = 0, '+'
        display.delete(0, END)
        display.insert(0, '0')

    global singledisplay, light, dark
    if singledisplay:
        mwindow.withdraw()  # Hide the main window if in single display mode
    app_calculator.deiconify()  # Display the calculator window
    app_calculator.title('Calculator - essentials.')  # Set the title of the calculator window
    app_calculator.protocol('WM_DELETE_WINDOW', close_calculator)  # Define close behavior
    app_calculator.iconphoto(False, icon)  # Set the window icon
    app_calculator.resizable(False, False)  # Disable resizing of the calculator window
    # Position the calculator window in the center of the screen
    app_calculator.geometry(f'316x192+{app_calculator.winfo_screenwidth() // 2 - 316 // 2}+{app_calculator.winfo_screenheight() // 2 - 192 // 2}')
    if dark:
        background = Label(app_calculator, bg='black', width=316, height=192).place(x=0, y=0)

    # Entry field for calculator display
    display = ttk.Entry(app_calculator, font=('Helvetica', 20), justify=RIGHT)
    display.insert(0, '0')
    display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    # If light mode is set
    if light:
        num_bg = '#505050'
        num_fg = '#FFFFFF'
        op_bg = '#FF9500'
        op_fg = '#FFFFFF'
        func_bg = '#D4D4D2'
        func_fg = 'black'

    # If dark mode is set
    else:
        num_bg = '#505050'
        num_fg = '#FFFFFF'
        op_bg = '#FF9500'
        op_fg = '#FFFFFF'
        func_bg = '#D4D4D2'
        func_fg = 'black'

    # Button configurations for calculator (numbers, operators, functions)
    btn_1 = Button(app_calculator, text='1', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('1')).grid(row=3, column=0, padx=5, pady=5)
    btn_2 = Button(app_calculator, text='2', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('2')).grid(row=3, column=1, padx=5, pady=5)
    btn_3 = Button(app_calculator, text='3', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('3')).grid(row=3, column=2, padx=5, pady=5)
    btn_4 = Button(app_calculator, text='4', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('4')).grid(row=2, column=0, padx=5, pady=5)
    btn_5 = Button(app_calculator, text='5', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('5')).grid(row=2, column=1, padx=5, pady=5)
    btn_6 = Button(app_calculator, text='6', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('6')).grid(row=2, column=2, padx=5, pady=5)
    btn_7 = Button(app_calculator, text='7', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('7')).grid(row=1, column=0, padx=5, pady=5)
    btn_8 = Button(app_calculator, text='8', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('8')).grid(row=1, column=1, padx=5, pady=5)
    btn_9 = Button(app_calculator, text='9', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('9')).grid(row=1, column=2, padx=5, pady=5)
    btn_0 = Button(app_calculator, text='0', width=8, bg=num_bg, fg=num_fg, command=lambda: add_num('0')).grid(row=4, column=0, padx=5, pady=5)
    btn_add = Button(app_calculator, text='+', width=8, bg=op_bg, fg=op_fg, command=lambda: add_op('+')).grid(row=1, column=3, padx=5, pady=5)
    btn_subtract = Button(app_calculator, text='-', bg=op_bg, fg=op_fg, width=8, command=lambda: add_op('-')).grid(row=2, column=3, padx=5, pady=5)
    btn_multiply = Button(app_calculator, text='*', bg=op_bg, fg=op_fg, width=8, command=lambda: add_op('*')).grid(row=3, column=3, padx=5, pady=5)
    btn_divide = Button(app_calculator, text='/', bg=op_bg, fg=op_fg, width=8, command=lambda: add_op('/')).grid(row=4, column=3, padx=5, pady=5)
    btn_equal = Button(app_calculator, text='=', width=8, bg=func_bg, fg=func_fg, command=calculate).grid(row=4, column=1, padx=5, pady=5)
    btn_clear = Button(app_calculator, text='AC', width=8, bg=func_bg, fg=func_fg, command=clear).grid(row=4, column=2, padx=5, pady=5)


# Function to close the stopwatch window
def close_stopwatch():
    # Ask user for confirmation before closing
    close = messagebox.askquestion('Close Stopwatch?', 'If you exit, the time will reset.\nDo you wish to proceed?')
    if close == 'yes':  # If user confirms to close
        app_stopwatch.destroy()  # Destroy the stopwatch window
        mwindow.deiconify()  # Restore the main window
    else:
        return  # Return if user cancels the close action

# Function to open the stopwatch window
def stopwatch():
    global singledisplay, app_stopwatch
    app_stopwatch = Toplevel()  # Create a new top-level window for the stopwatch
    if singledisplay:
        mwindow.withdraw()  # Hide the main window if in single display mode
    app_stopwatch.deiconify()  # Display the stopwatch window
    app_stopwatch.title('Stopwatch - essentials.')  # Set the title of the stopwatch window
    app_stopwatch.protocol('WM_DELETE_WINDOW', close_stopwatch)  # Define close behavior
    app_stopwatch.iconphoto(False, icon)  # Set the window icon
    app_stopwatch.resizable(False, False)  # Disable resizing of the stopwatch window
    # Position the stopwatch window in the center of the screen
    app_stopwatch.geometry(f'325x350+{app_stopwatch.winfo_screenwidth() // 2 - 325 // 2}+{app_stopwatch.winfo_screenheight() // 2 - 350 // 2}')
    if light:
        sw = Stopwatch(app_stopwatch)  # Initialize a light-themed stopwatch
    else:
        sw = Stopwatch(app_stopwatch, light=False)  # Initialize a dark-themed stopwatch

# Function to handle quitting the program
def quit_program():
    # Ask user for confirmation before quitting
    close = messagebox.askquestion('Exit','Are you sure you would like to exit?')
    if close == 'yes':  # If user confirms to quit
        messagebox.showinfo('Goodbye', 'Thank you for choosing essentials.')  # Show goodbye message
        quit()  # Quit the program
    else:
        return  # Return if user cancels the quit action


# Main Window
mwindow = Tk()

# Variables
mwidth = 1250  # Width of the main window
mheight = 700  # Height of the main window
mwindow_x = (mwindow.winfo_screenwidth() // 2 - mwidth // 2)  # X position of the main window
mwindow_y = (mwindow.winfo_screenheight() // 2 - mheight // 2)  # Y position of the main window
icon = PhotoImage(file='objects/icon.png')  # Icon image for the main window
light = True  # Flag for light UI theme
dark = False  # Flag for dark UI theme
singledisplay = True  # Flag for single display mode
darkui = PhotoImage(file='objects/darkUI.png')  # Dark UI image
lightui = PhotoImage(file='objects/lightUI.png')  # Light UI image
img_light = PhotoImage(file='objects/lightbtn.png')  # Image for light button
img_dark = PhotoImage(file='objects/darkbtn.png')  # Image for dark button
img_ltriggered = PhotoImage(file='objects/lightbtn_triggered.png')  # Image for light button (triggered)
img_dtriggered = PhotoImage(file='objects/darkbtn_triggered.png')  # Image for dark button (triggered)
img_lnotepad = PhotoImage(file='objects/light_notepad.png')  # Image for light notepad
img_dnotepad = PhotoImage(file='objects/dark_notepad.png')  # Image for dark notepad
img_lightopen = PhotoImage(file='objects/lopennote.png')  # Image for light open notepad
img_darkopen = PhotoImage(file='objects/dopennote.png')  # Image for dark open notepad
img_lightsave = PhotoImage(file='objects/lsavenote.png')  # Image for light save notepad
img_darksave = PhotoImage(file='objects/dsavenote.png')  # Image for dark save notepad
img_lmusic = PhotoImage(file='objects/light_music.png')  # Image for light music player
img_dmusic = PhotoImage(file='objects/dark_music.png')  # Image for dark music player
img_dmusicui = PhotoImage(file='objects/music_ui.png')  # Image for dark music player UI
img_lcover = PhotoImage(file='objects/light_cover.png')  # Image for light music cover
img_dcover = PhotoImage(file='objects/dark_cover.png')  # Image for dark music cover
img_lplay = PhotoImage(file='objects/light_play.png')  # Image for light play button
img_dplay = PhotoImage(file='objects/dark_play.png')  # Image for dark play button
img_lpause = PhotoImage(file='objects/light_pause.png')  # Image for light pause button
img_dpause = PhotoImage(file='objects/dark_pause.png')  # Image for dark pause button
img_lforward = PhotoImage(file='objects/light_forward.png')  # Image for light forward button
img_dforward = PhotoImage(file='objects/dark_forward.png')  # Image for dark forward button
img_lbackward = PhotoImage(file='objects/light_backward.png')  # Image for light backward button
img_dbackward = PhotoImage(file='objects/dark_backward.png')  # Image for dark backward button
img_lwhiteboard = PhotoImage(file='objects/light_whiteboard.png')  # Image for light whiteboard
img_dwhiteboard = PhotoImage(file='objects/dark_whiteboard.png')  # Image for dark whiteboard
img_lcalculator = PhotoImage(file='objects/light_calculator.png')  # Image for light calculator
img_dcalculator = PhotoImage(file='objects/dark_calculator.png')  # Image for dark calculator
img_lstopwatch = PhotoImage(file='objects/light_stopwatch.png')  # Image for light stopwatch
img_dstopwatch = PhotoImage(file='objects/dark_stopwatch.png')  # Image for dark stopwatch
mp3 = MP3()  # MP3 instance for music player
playlist_one = mp3.get_playlist1()  # Playlist 1 for music player
coverlist_one = mp3.get_coverlist1()  # Cover art list for playlist 1
playlist_two = mp3.get_playlist2()  # Playlist 2 for music player
coverlist_two = mp3.get_coverlist2()  # Cover art list for playlist 2
playlist_three = mp3.get_playlist3()  # Playlist 3 for music player
coverlist_three = mp3.get_coverlist3()  # Cover art list for playlist 3
plist1 = True  # Flag for playlist 1 selection
plist2 = False  # Flag for playlist 2 selection
song_index = 0  # Index of the current song
lbl_cn = None  # Label for clock display
cover = None  # Cover image display
btn_play = None  # Play button
state = False  # State of music player (playing or paused)

# Program Code
mwindow.resizable(False, False)  # Disable window resizing
mwindow.geometry(f'{mwidth}x{mheight}+{mwindow_x}+{mwindow_y}')  # Set window size and position
mwindow.title('Essentials')  # Set window title
mwindow.iconphoto(False, icon)  # Set window icon
mwindow.protocol('WM_DELETE_WINDOW', quit_program)  # Define close behavior

mainframe = Frame(mwindow, width=mwidth, height=mheight)  # Main frame for UI elements
mainframe.pack()  # Pack main frame

ui = Label(mainframe, width=mwidth, height=mheight, image=lightui)  # UI label with background image
ui.place(x=0, y=0)  # Place UI label

# UI decorative frames
fillONE = Frame(mainframe, bg='#F8A37A')
fillONE.place(x=-5, y=0, height=10, width=1500)
fillTWO = Frame(mainframe, bg='#F8A37A')
fillTWO.place(x=0, y=0, width=10, height=42)
fillTHREE = Frame(mainframe, bg='#F8A37A')
fillTHREE.place(x=0, y=40, height=3, width=mwidth)
fillFOUR = Frame(mainframe, bg='#FFF4DF')
fillFOUR.place(x=0, y=43, width=5, height=mheight)

# Clock display label
lbl_clock = Label(mainframe, bg='#FDF0D7', fg='#32012F', text='', font=('Time New Roman', 70, 'bold'))
lbl_clock.place(x=425, y=77)

# Menu button
btn_menu = Button(mainframe, text='☰', bg='#F8A37A', bd=0, fg='#467372', font=('Bold', 14),
                  activebackground='#467372', activeforeground='#F8A37A', command=toggle_menu)
btn_menu.place(x=3, y=4)

mwindow.update()  # Update main window

# Buttons for various applications
btn_notepad = Button(mainframe, width=100, height=100, bg='#FFF4DF', image=img_lnotepad, bd=0,
                     activebackground='#FFF4DF', command=notepad)
btn_notepad.place(x=(mwindow.winfo_reqwidth() // 2) - 50, y=250)

app_notepad = Toplevel()  # Notepad application window
app_notepad.withdraw()  # Hide notepad window initially

btn_music = Button(mainframe, width=100, height=100, bg='#FFF4DF', image=img_lmusic, bd=0,
                   activebackground='#FFF4DF', command=music_player)
btn_music.place(x=(mwindow.winfo_reqwidth() // 2) - 200, y=250)

app_music = Toplevel()  # Music player application window
app_music.withdraw()  # Hide music player window initially

btn_whiteboard = Button(mainframe, width=100, height=100, bg='#FFF4DF', image=img_lwhiteboard, bd=0,
                        activebackground='#FFF4DF', command=whiteboard)
btn_whiteboard.place(x=(mwindow.winfo_reqwidth() // 2) + 100, y=250)

app_whiteboard = None  # Whiteboard application window

btn_calculator = Button(mainframe, width=100, height=100, bg='#FFF4DF', image=img_lcalculator, bd=0,
                        activebackground='#FFF4DF', command=calculator)
btn_calculator.place(x=(mwindow.winfo_reqwidth() // 2) + 250, y=250)

app_calculator = Toplevel()  # Calculator application window
app_calculator.withdraw()  # Hide calculator window initially

btn_stopwatch = Button(mainframe, width=100, height=100, bg='#FFF4DF', image=img_lstopwatch, bd=0,
                       activebackground='#FFF4DF', command=stopwatch)
btn_stopwatch.place(x=(mwindow.winfo_reqwidth() // 2) - 350, y=250)

app_stopwatch = None  # Stopwatch application window

# To-Do List frame and widgets
todo_app = Frame(mainframe, width=212, height=200, bg='#DDD2C1')  # To-Do List frame
todo_app.place(x=853.5, y=514, anchor='center')  # Place To-Do List frame
todo = Frame(todo_app, bg='#DDD2C1')  # Inner frame for listbox and scrollbar
todo.place(x=0, y=0)  # Place inner frame
listbox = Listbox(todo, width=33, height=6, highlightthickness=0, selectbackground='#a6a6a6', activestyle='none', bg='#DDD2C1', bd=0)  # Listbox widget for tasks
listbox.pack(side=LEFT, fill=BOTH)  # Pack listbox
scrollbar = Scrollbar(todo, width=13, bg='#DDD2C1', bd=0)  # Scrollbar for listbox
scrollbar.pack(side=RIGHT, fill=BOTH)  # Pack scrollbar
listbox.config(yscrollcommand=scrollbar.set)  # Configure listbox scrollbar
scrollbar.config(command=listbox.yview)  # Configure scrollbar command
todo_list_display = ['To-Do List! (delete me)']  # Initial to-do list items
for item in todo_list_display:
    listbox.insert(END, item)  # Insert initial items into listbox

tasks = Entry(todo_app, font=('bold', 10), width=29, bg='#DDD2C1')  # Entry widget for new task input
tasks.place(x=0, y=99)  # Place entry widget for tasks

btn_frame = Frame(todo_app, width=212, height=90, bg='#DDD2C1')  # Frame for buttons
btn_frame.place(x=0, y=120)  # Place button frame

# Buttons for managing to-do list
btn_delete = Button(btn_frame, text='Delete Item', font=('bold', 7), width=12, bg='#DDD2C1', activebackground='black', activeforeground='white', command=delete_item)
btn_add = Button(btn_frame, text='Add Item', font=('bold', 7), width=12, bg='#DDD2C1', activebackground='black', activeforeground='white',  command=add_item)
btn_cross = Button(btn_frame, text='Cross Off Item', font=('bold', 7), width=12, bg='#DDD2C1', activebackground='black', activeforeground='white',  command=cross_item)
btn_clear = Button(btn_frame, text='Clear List', font=('bold', 7), width=12, bg='#DDD2C1', activebackground='black', activeforeground='white',  command=clear_list)
btn_savelist = Button(btn_frame, text='Save List', font=('bold', 7), width=12, bg='#DDD2C1', activebackground='black', activeforeground='white',  command=save_list)
btn_openlist = Button(btn_frame, text='Open List', font=('bold', 7), width=12, bg='#DDD2C1', activebackground='black', activeforeground='white',  command=open_list)

# Place buttons in button frame
btn_delete.place(x=20, y=7)
btn_add.place(x=110, y=7)
btn_cross.place(x=20, y=32)
btn_clear.place(x=110, y=32)
btn_openlist.place(x=20, y=57)
btn_savelist.place(x=110, y=57)

pswd = Frame(mainframe, bg='#DDD2C1', bd=0, width=350, height=185)
pswd.place(x=474, y=514, anchor='center')
title = Label(pswd, text='Password Generator', font=('Times New Roman', 20), bg='#DDD2C1', fg='black')
title.pack()
plf = LabelFrame(pswd, text='Select Number of Characters (in password)', width=300, height=50, bg='#DDD2C1', fg='black')
plf.pack(pady=10)
pswd_entry = Entry(plf, font=('Helvetica', 10), justify='center', bg='#bab0a0', fg='black', cursor="xterm #0000FF")
pswd_entry.pack(pady=20, padx=20)
pw_entry = Entry(pswd, text='', font=('Helvetica', 10), width=45, justify='center', readonlybackground='#bab0a0', fg='black', state='readonly')
pw_entry.pack(pady=5)
pbtn_frame = Frame(pswd, bg='#DDD2C1')
pbtn_frame.pack()
btn_generate = Button(pbtn_frame, text='Generate Password', command=new_rand, bd=0, bg='#DDD2C1', fg='black', activebackground='#DDD2C1', activeforeground='gray')
btn_generate.grid(row=0, column=0, padx=10)
btn_copy = Button(pbtn_frame, text='Copy Password', command=clipper, bd=0, bg='#DDD2C1', fg='black', activebackground='#DDD2C1', activeforeground='gray')
btn_copy.grid(row=0, column=1, padx=10)

clock()  # Start the clock function
mwindow.update()  # Update the main window
mwindow.mainloop()  # Start the main event loop

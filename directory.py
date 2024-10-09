'''
Name: Syed Qadri
Date: 05/21/2024
Program: Essentials Directory (CPT-Class)
Class: ICU4U1-02
'''

# Import necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import customtkinter as ctk

# MP3 Class for managing playlists and cover images
class MP3:
    def __init__(self):
        # Define playlists and cover images for three sets
        self.__playlist1 = ['music/Trojan Horse.wav',
                            'music/Too Many Nights.wav',
                            'music/Stir Fry.wav',
                            'music/My Shit.wav',
                            'music/Mood Swings.wav',
                            'music/Lust.wav',
                            'music/In My Feelings.wav',
                            'music/FIEN.wav',
                            'music/Crazy Story, Pt3.wav',
                            'music/500lbs.wav',
                            ]

        self.__coverlist1 = [PhotoImage(file='objects/trojanhorse.png'),
                             PhotoImage(file='objects/toomanynights.png'),
                             PhotoImage(file='objects/stiryfry.png'),
                             PhotoImage(file='objects/myshit.png'),
                             PhotoImage(file='objects/moodswings.png'),
                             PhotoImage(file='objects/lust.png'),
                             PhotoImage(file='objects/inmyfeelings.png'),
                             PhotoImage(file='objects/fien.png'),
                             PhotoImage(file='objects/crazystory.png'),
                             PhotoImage(file='objects/500lbs.png'),
                             ]

        self.__playlist2 = ['music/The Color Violet.wav',
                            'music/Vampire.wav',
                            'music/STAY.wav',
                            'music/Electric Love.wav',
                            'music/Dark Red.wav',
                            'music/Backyard Boy.wav',
                            'music/falling in love.wav',
                            'music/Cold Heart.wav',
                            'music/Temperature.wav',
                            'music/Get You.wav'
                            ]

        self.__coverlist2 = [PhotoImage(file='objects/thecolorviolet.png'),
                             PhotoImage(file='objects/vampire.png'),
                             PhotoImage(file='objects/stay.png'),
                             PhotoImage(file='objects/electriclove.png'),
                             PhotoImage(file='objects/darkred.png'),
                             PhotoImage(file='objects/backyardboy.png'),
                             PhotoImage(file='objects/fallinginlove.png'),
                             PhotoImage(file='objects/coldheart.png'),
                             PhotoImage(file='objects/temperature.png'),
                             PhotoImage(file='objects/getyou.png'),
                             ]

        self.__playlist3 = ['music/Gata Only.wav',
                            'music/Come & Get it.wav',
                            'music/MALA.wav',
                            'music/Love Nwantiti.wav',
                            'music/Bella Ciao.wav',
                            'music/Ella Baila Sola.wav',
                            'music/Despacito.wav',
                            'music/Gente de Zona.wav',
                            'music/Pepas.wav',
                            'music/Jugaste y Sufri.wav'
                            ]

        self.__coverlist3 = [PhotoImage(file='objects/gataonly.png'),
                             PhotoImage(file='objects/comeandgetit.png'),
                             PhotoImage(file='objects/mala.png'),
                             PhotoImage(file='objects/lovenwantiti.png'),
                             PhotoImage(file='objects/bellaciao.png'),
                             PhotoImage(file='objects/ellabailasola.png'),
                             PhotoImage(file='objects/despacito.png'),
                             PhotoImage(file='objects/gente.png'),
                             PhotoImage(file='objects/pepas.png'),
                             PhotoImage(file='objects/jugaste.png'),
                             ]

    # Getter methods for playlists and cover images
    def get_playlist1(self):
        return self.__playlist1

    def get_coverlist1(self):
        return self.__coverlist1

    def get_playlist2(self):
        return self.__playlist2

    def get_coverlist2(self):
        return self.__coverlist2

    def get_playlist3(self):
        return self.__playlist3

    def get_coverlist3(self):
        return self.__coverlist3

# Whiteboard class for a drawing application
class Whiteboard:
    def __init__(self, app, light=True):
        self.app = app
        self.app.title('Whiteboard - essentials.')
        self.app.resizable(False, False)
        # Set window size and position
        self.app.geometry(f'1050x640+{self.app.winfo_screenwidth() // 2 - 1050 // 2}+{self.app.winfo_screenheight() // 2 - 640 // 2}')
        # Create canvas for drawing
        if light:
            self.canvas = tk.Canvas(self.app, width=1050, height=570, bg='white', cursor='hand2')
        else:
            self.canvas = tk.Canvas(self.app, width=1050, height=570, bg='black', cursor='hand2')
        self.canvas.pack()

        # Frame for buttons
        self.button_frame = ttk.Frame(self.app)
        self.button_frame.pack(side='top', pady=10)

        # Button configuration based on theme
        if light:
            button_config = {
                'black': ('dark.TButton', lambda: self.change_colour('black')),
                'red': ('danger.TButton', lambda: self.change_colour('red')),
                'blue': ('info.TButton', lambda: self.change_colour('blue')),
                'green': ('success.TButton', lambda: self.change_colour('green')),
                'eraser': ('success.TButton', lambda: self.change_colour('white')),
                'clear': ('light.TButton', self.clear_canvas)
            }
        else:
            button_config = {
                'golden': ('dark.TButton', lambda: self.change_colour('#B8860B')),
                'white': ('danger.TButton', lambda: self.change_colour('white')),
                'red': ('danger.TButton', lambda: self.change_colour('red')),
                'blue': ('info.TButton', lambda: self.change_colour('blue')),
                'green': ('success.TButton', lambda: self.change_colour('green')),
                'eraser': ('success.TButton', lambda: self.change_colour('black')),
                'clear': ('light.TButton', self.clear_canvas)
            }

        # Function to set line width
        def set_linewidth(linewidth):
            self.line_width = linewidth

        # Create buttons based on configuration
        for color, (style, command) in button_config.items():
            ttk.Button(self.button_frame, text=color.capitalize(), command=command, style=style).pack(side='left', padx=5, pady=5)

        # Slider for setting line width
        self.width_slider = ctk.CTkSlider(self.button_frame, from_=1, to=50, width=200, command=set_linewidth)
        self.width_slider.pack(side='left', padx=5, pady=5)

        # Initial drawing color and line width
        if light:
            self.draw_color = 'black'
        else:
            self.draw_color = '#B8860B'
        self.line_width = 5
        self.old_x, self.old_y = None, None

        # Bind mouse events to canvas for drawing
        self.canvas.bind('<Button-1>', self.start_line)
        self.canvas.bind('<B1-Motion>', self.draw_line)

    # Start drawing a line
    def start_line(self, event):
        self.old_x, self.old_y = event.x, event.y

    # Draw line based on mouse movement
    def draw_line(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=self.draw_color, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.old_x, self.old_y = event.x, event.y

    # Change drawing color
    def change_colour(self, new_color):
        self.draw_color = new_color

    # Clear the canvas
    def clear_canvas(self):
        self.canvas.delete('all')

# Stopwatch class for timing events
class Stopwatch:
    def __init__(self, app, light=True):
        self.app = app
        self.app.title('Stopwatch - essentials.')
        self.time = 0
        self.running = False
        # Set window title and initial time
        if light:
            self.bg = tk.Label(self.app, width=325, height=350, bg='white')
            self.frame = tk.Frame(self.app, width=325, height=350, bg='white')
            self.label = tk.Label(self.frame, text='0:00:00', pady=20, font=('Helvetica', 35), bg='white')
            self.btn_start = tk.Button(self.frame, text='Start', width=10, height=2, font=('Helvetica', 14), command=self.start, bg='white', fg='black', bd=1, activebackground='black', activeforeground='white')
            self.btn_stop = tk.Button(self.frame, text='Stop', width=10, height=2, font=('Helvetica', 14), command=self.stop, bg='white', fg='black', bd=1, activebackground='black', activeforeground='white')
            self.btn_reset = tk.Button(self.frame, text='Reset', width=10, height=2, font=('Helvetica', 14), command=self.reset, bg='white', fg='black', bd=1, activebackground='black', activeforeground='white')
        else:
            self.bg = tk.Label(self.app, width=325, height=350, bg='#212121')
            self.frame = tk.Frame(self.app, width=325, height=350, bg='#212121')
            self.label = tk.Label(self.frame, text='0:00:00', pady=20, font=('Helvetica', 35), bg='#212121', fg='#BB86FC')
            self.btn_start = tk.Button(self.frame, text='START', width=10, height=2, font=('Helvetica', 14), command=self.start, bg='#121212', fg='#BB86FC', bd=0, activebackground='#121212', activeforeground='#03DAC6')
            self.btn_stop = tk.Button(self.frame, text='Stop', width=10, height=2, font=('Helvetica', 14), command=self.stop, bg='#121212', fg='#BB86FC', bd=0, activebackground='#121212', activeforeground='#03DAC6')
            self.btn_reset = tk.Button(self.frame, text='Reset', width=10, height=2, font=('Helvetica', 14), command=self.reset, bg='#121212', fg='#03DAC6', bd=0, activebackground='#121212', activeforeground='#BB86FC')

        self.bg.place(x=0, y=0)
        self.frame.pack()
        self.label.grid(row=0, column=0, columnspan=3)
        self.btn_start.grid(row=1, column=1, pady=10)
        self.btn_stop.grid(row=2, column=1, pady=10)
        self.btn_reset.grid(row=3, column=1, pady=10)

    def start(self):
        # Start the stopwatch
        self.running = True
        self.btn_start.config(command=0)  # Disable the Start button during running
        self.count()  # Start counting time

    def stop(self):
        # Stop the stopwatch
        self.running = False
        self.btn_start.config(command=self.start)  # Re-enable the Start button

    def reset(self):
        # Reset the stopwatch
        self.running = False  # Stop running
        self.btn_start.config(command=self.start)  # Re-enable the Start button
        self.time = 0  # Reset the time counter
        self.label.config(text='0:00:00')  # Reset the displayed time

    def count(self):
        # Count and display the elapsed time
        if self.running:
            self.time += 1  # Increment time by 1 second
            minutes, seconds = divmod(self.time, 60)  # Calculate minutes and seconds
            hours, minutes = divmod(minutes, 60)  # Calculate hours and remaining minutes
            self.label.config(text='{:01d}:{:02d}:{:02d}'.format(hours, minutes, seconds))  # Update the displayed time
            self.app.after(1000, self.count)  # Schedule the next call to count() after 1000ms (1 second)

if __name__ == '__main__':
    root = tk.Tk()
    sw = Stopwatch(root)
    root.mainloop()
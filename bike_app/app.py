from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

def back():
    c = Canvas(window, bg="skyblue1", height=600, width=600)
    c.place(x=0, y=0)

    main_label = Label(c, text='BikeBuddy')
    main_label.config(font=('sans-serif', 40), bg='skyblue1', fg='white')
    main_label.place(x=160, y=50)

    start_button = Button(c, text='Begin Journey')
    start_button.config(font=('sans-serif', 20), bg='steelblue1', fg='white')
    start_button.place(x=180, y=170)

    select_device_button = Button(c, text='Select Device', command=lambda: select_device1())
    select_device_button.config(font=('sans-serif', 20), bg='steelblue1', fg='white')
    select_device_button.place(x=185, y=250)

    settings_button = Button(c, text='Settings', command=lambda: settings())
    settings_button.config(font=('sans-serif', 20), bg='steelblue1', fg='white')
    settings_button.place(x=210, y=330)

###### MAIN MENU ######
window = Tk()
window.geometry('828x1792')

def select_device1():
    clear = Canvas(window, bg="skyblue1", height=600, width=600)
    clear.place(x=0, y=0)

    select_device_menu = Label(text = 'Select a device')
    select_device_menu.config(font = ('sans-serif',40), bg = 'skyblue1', fg = 'white')
    select_device_menu.place(x=120,y=50)

    device_1 = Label(text = 'Jacks iPhone')
    device_1.config(font = ('sans-serif',20), bg = 'skyblue1', fg = 'white')
    device_1.place(x=120,y=170)

    device_1 = Label(text='Sadhbhs iPhone')
    device_1.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    device_1.place(x=120, y=230)

    device_1 = Label(text='Seans iPhone')
    device_1.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    device_1.place(x=120, y=290)

    device_1 = Label(text='Johns iPhone')
    device_1.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    device_1.place(x=120, y=350)

    device_1 = Label(text='Lukes iPhone')
    device_1.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    device_1.place(x=120, y=410)

    check1 = ttk.Checkbutton()
    check2 = ttk.Checkbutton()
    check3 = ttk.Checkbutton()
    check4 = ttk.Checkbutton()
    check5 = ttk.Checkbutton()
    check1.place(x=400,y=420)
    check2.place(x=400, y=360)
    check3.place(x=400, y=300)
    check4.place(x=400, y=240)
    check5.place(x=400, y=180)

    back_button = Button(text = 'Main Menu', command =lambda: back())
    back_button.config(font=('sans-serif', 10), bg='skyblue1', fg='white')
    back_button.place(x=20,y=20)

def audio_settings():
    clear = Canvas(window, bg="skyblue1", height=600, width=600)
    clear.place(x=0, y=0)

    audio_header = Label(text= 'Audio Settings')
    audio_header.config(font=('sans-serif', 40), bg='skyblue1', fg='white')
    audio_header.place(x=130,y=50)

    slider = ttk.Scale(
        from_=0,
        to=100,
        orient='horizontal')
    slider = Scale(from_=0, to=100, length=400,tickinterval=10, orient=HORIZONTAL)
    slider.place(x=90,y=250)

    lower_music = Label(text = 'Lower Music:')
    lower_music.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    lower_music.place(x=150,y=350)

    check1 = ttk.Checkbutton(text = 'Yes')
    check2 = ttk.Checkbutton(text = 'No')
    check1.place(x=350,y=350)
    check2.place(x=350,y=370)

    back_button = Button(text='Main Menu', command=lambda: back())
    back_button.config(font=('sans-serif', 10), bg='skyblue1', fg='white')
    back_button.place(x=20, y=20)

def settings():
    clear = Canvas(window, bg="skyblue1", height=600, width=600)
    clear.place(x=0, y=0)

    settings_header = Label(text = 'Settings')
    settings_header.config(font=('sans-serif', 40), bg='skyblue1', fg='white')
    settings_header.place(x=190, y=50)

    audio_button = Button(text = 'Audio', command=lambda: audio_settings())
    audio_button.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    audio_button.place(x=230,y = 170)

    LED_button = Button(text = "LEDs")
    LED_button.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    LED_button.place(x=230, y=250)

    Vib_button = Button(text = 'Vibrations')
    Vib_button.config(font=('sans-serif', 20), bg='skyblue1', fg='white')
    Vib_button.place(x=210, y=330)



    back_button = Button(text='Main Menu', command=lambda: back())
    back_button.config(font=('sans-serif', 10), bg='skyblue1', fg='white')
    back_button.place(x=20, y=20)


c = Canvas(window, bg="skyblue1", height=600, width=600)
c.place(x=0, y=0)


main_label = Label(c,text = 'BikeBuddy')
main_label.config(font = ('sans-serif',40), bg = 'skyblue1', fg = 'white')
main_label.place(x=160, y=50)



start_button = Button(c, text = 'Begin Journey')
start_button.config(font = ('sans-serif',20), bg = 'steelblue1', fg = 'white')
start_button.place(x=180, y=170)

select_device_button = Button(c,text = 'Select Device', command =lambda: select_device1())
select_device_button.config(font = ('sans-serif',20), bg = 'steelblue1', fg = 'white')
select_device_button.place(x=185, y=250)

settings_button = Button(c,text = 'Settings', command =lambda: settings())
settings_button.config(font = ('sans-serif',20), bg = 'steelblue1', fg = 'white')
settings_button.place(x=210, y=330)







window.mainloop()

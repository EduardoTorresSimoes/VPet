from tkinter import *
import random 
import time

from OOPet import VPET
img_Path = "Imagens/ryo-removebg-preview.png"

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
bg = "black"
meioX = screen_width / 2
meioY = screen_height / 2

pet = VPET("Ryo", meioX, meioY)

root.geometry(f'{screen_width}x{screen_height}')
root.wm_attributes('-transparentcolor', bg)
root.configure(bg=bg)
root.attributes('-topmost', True)
root.overrideredirect(True)

my_canvas = Canvas(root, width=screen_width, height=screen_height, bg=bg, bd=0)
my_canvas.config(highlightthickness=0)
my_canvas.pack()

img = PhotoImage(file=img_Path)
my_image = my_canvas.create_image(meioX, meioY, anchor=CENTER, image=img)
pet.posicao(meioX, meioY)

def clickOnIt(e):
    global img
    img = PhotoImage(file=img_Path)
    my_image = my_canvas.create_image(e.x, e.y, anchor=N, image=img)
    pet.posicao(e.x, e.y)
    print(f'Posição atual: X:{pet.xcoord} | Y:{pet.ycoord}')

def walking():
    global img, randomW, randomH
    img = PhotoImage(file=img_Path)
    my_image = my_canvas.create_image(pet.xcoord, pet.ycoord, anchor=NW, image=img)

    randomW = random.randrange(0, screen_width)
    randomH = random.randrange(0, screen_height)

    dx = randomW - pet.xcoord
    dy = randomH - pet.ycoord

    steps = 1000  # Number of steps for smooth movement
    for i in range(steps):
        x = pet.xcoord + (i * dx) / steps
        y = pet.ycoord + (i * dy) / steps
        my_canvas.coords(my_image, x, y)
        root.update()
        time.sleep(0.01)  # Delay for smoother animation

    pet.posicao(randomW, randomH)

root.bind('<B1-Motion>', clickOnIt)
root.bind('<Up>', lambda event: walking())  # Use lambda to pass the event argument
root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
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

def load_and_display_gif(gif_path):
    gif = Image.open(gif_path)
    gif = gif.resize((50, 50))  # Redimensione o GIF conforme necessário
    gif = ImageTk.PhotoImage(gif)
    return gif

idle_gif = load_and_display_gif("Imagens/idle.gif")  # Substitua pelo caminho real do seu GIF
sleeping_gif = load_and_display_gif("Imagens/sleeping.gif")
walking_gif = load_and_display_gif("Imagens/walking.gif")
carinho_gif = load_and_display_gif("Imagens/carinho.gif")  # Substitua pelo caminho real do seu GIF de carinho

# def carinho():
#     #Código para rodar um gif fazendo carinho
    

def randomAction():
    rAction = random.randrange(0,3)
    if rAction == 0:
        idle()
    elif rAction == 1:
        sleeping()
    else:
        walking

def clickOnIt(e):
    global img
    img = PhotoImage(file=img_Path)
    my_image = my_canvas.create_image(e.x, e.y, anchor=N, image=img)
    pet.posicao(e.x, e.y)
    print(f'Posição atual: X:{pet.xcoord} | Y:{pet.ycoord}')

def idle():
    global img
    # Gif Idle (Algumas variações)
        #-> Wait random time for Idle

def sleeping():
    global img
    # Gif Idle -> Dormir
    # Gif Dormir
        #-> Wait random time for sleep
    # Gif Dormir -> Idle

def walking():
    global img, randomW, randomH
    img = PhotoImage(file=img_Path)
    my_image = my_canvas.create_image(pet.xcoord, pet.ycoord, anchor=NW, image=img)

    randomW = random.randrange(0, (screen_width - 235)) # "- valor" é feito a mão para 
    randomH = random.randrange(0, (screen_height - 530))#  que a Ryo não suma da tela
    randomSpeed = random.randrange(0,3)
    print(randomSpeed)

    if randomSpeed == 0:   # Gif Rastejando (NF: gif cansada)
        steps = 1000
    elif randomSpeed == 1: # Gid Andando    (NF: gif normal)
        steps = 500
    else:                  # Gif Correndo   (NF: gif feliz)  
        steps = 100

    dx = randomW - pet.xcoord
    dy = randomH - pet.ycoord

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
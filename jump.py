# import tkinter
import tkinter

key = ""
# Program when a key is pressed
def key_down(e):
    global key
    key = e.keysym

# Program for when a key is no longer pressed
def key_up(e):
    global key
    key = ""

cx = 400
cy = 450
rakka = 0
jump = 0

# main loop
def main_proc():
    global cx, cy, rakka, jump
    cy = cy + rakka
    rakka = rakka + 1
    if rakka < 0:
        while cy > 449:
            cy = cy + 1
            rakka = 0
    else:
        while cy > 449:
            cy = cy - 1
            rakka = 0
            jump = 0
    if key == "Up":
        if jump == 0:
            jump = 1
            rakka = 0 - 20
    if key == "Left":
        cx = cx - 10
    if key == "Right":
        cx = cx + 10
    canvas.coords("MYCHR", cx, cy)
    root.after(30, main_proc)

# Window
root = tkinter.Tk()
root.title("移動")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="nico.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR")
main_proc()
root.mainloop()

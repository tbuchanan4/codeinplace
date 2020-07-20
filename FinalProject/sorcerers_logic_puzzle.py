"""
Sorcerer's Logic Puzzle:
This program will let the player reason their way through the potion logic puzzle that Harry & Hermione face and that
Hermione solves in Harry Potter and the Sorcerer's Stone (also known as the Philosopher's Stone for those of
differing geographies).

Some notes on future improvements:
-The code in general could certainly be structured better. It's very heavy in main() and should instead be broken out into other functions where possible
-Sound does not currently loop
-Would like reset button to also respond to a click of Button-1. Was having trouble with that click interfering with general operation when it was intially assigned as such so I changed to Button-3
-Rather than operating via independent if statements, I'd like getxy() to function via a branching decision tree that responds differently based on the object clicked.
"""
import tkinter
from PIL import ImageTk
from PIL import Image
import winsound

CANVAS_HEIGHT = 501
CANVAS_WIDTH = 1280

#The Sorcerer's Logic Puzzle begins by assigning locations and details to all images, text, and features. Then it records the players x and y coordinates of a left click and if they fall within an assigned region, outputs the results of their deductions.
def main():
    #Makes a canvas with the title of the program
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Sorcerer\'s Logic Puzzle')

    #Assigns the image and location of that image within the canvas
    image = ImageTk.PhotoImage(Image.open("images/potions.jpg"))
    canvas.create_image(0, 0, anchor = "nw", image = image)

    #Assigns the puzzle text, it's location, and properties
    canvas.create_text(640, 20, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Danger lies before you, two of us will help you, whichever you would find, one among us seven will let you move ahead, another will transport the drinker back instead,')
    canvas.create_text(640, 45, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Two among our number hold only nettle wine, three of us are killers, waiting hidden in line. Choose, unless you wish to stay here for evermore,')
    canvas.create_text(640, 75, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'To help you in your choice, we give you these clues four: ')
    canvas.create_text(640, 130, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'First, however slyly the poison tries to hide you will always find some on nettle wine’s left side; ')
    canvas.create_text(640, 155, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Second, different are those who stand at either end, but if you would move onwards, neither is your friend;')
    canvas.create_text(640, 180, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Third, as you see clearly, all are different size, neither dwarf nor giant holds death in their insides;')
    canvas.create_text(337, 180, anchor = 'n', fill = 'black', font = 'Helvetica 12', text = 'ird' )
    canvas.create_text(939, 180, anchor='n', fill='black', font='Helvetica 12', text='sid')
    canvas.create_text(640, 205, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Fourth, the second left and the second on the right are twins once you taste them, though different at first sight.')
    canvas.create_text(640, 460, anchor = 'n', fill = 'white', font = 'Helvetica 12', text = 'Please click your answer')

    #Plays creepy dungeon background music
    winsound.PlaySound('sounds/dungeon.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

    #This section shows the bounding hitboxes for each potion. Intentionally commented off for final test, can be deleted and still run fine. Also used as reference for the if statement conditions in getxy()
    #poison1 = canvas.create_rectangle(430,315,485,390, outline = 'white')
    #wine1 = canvas.create_rectangle(500,290,545,390, outline = 'red')
    #forward = canvas.create_rectangle(560,330,600,390, outline = 'blue')
    #poison2 = canvas.create_rectangle(610,270,655,390, outline = 'yellow')
    #poison3 = canvas.create_rectangle(660,320,710,390, outline = 'green')
    #wine2 = canvas.create_rectangle(720,255,770,390, outline = 'black')
    #back = canvas.create_rectangle(775,320,830,390, outline = 'purple')

    #getxy() takes the x and y coordinates of a left button click and if they fall within one of the potions, output a response accordingly
    def getxy(event):
        if 430 < event.x < 485 and 315 < event.y < 390:
            canvas.create_text(450, 422, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Poison', tags = 'poison')
        if 500 < event.x < 545 and 290 < event.y < 390:
            canvas.create_text(522, 422, anchor = "n", fill = "red", font = 'Helvetica 12', text = 'Wine', tags = 'wine')
        if 560 < event.x < 600 and 330 < event.y < 390:
            canvas.create_text(575, 422, anchor = "n", fill = "blue", font = 'Helvetica 12', text = 'Forward', tags = 'forward')
            canvas.create_text(990, 230, anchor = "n", fill = "white", font = 'Helvetica 16', text = 'Congratulations, you can move forward with you quest! --->', tags = 'forward')
        if 610 < event.x < 655 and 270 < event.y < 390:
            canvas.create_text(632, 422, anchor = "n", fill = "yellow", font = 'Helvetica 12', text = 'Poison', tags = 'poison')
        if 660 < event.x < 710 and 320 < event.y < 390:
            canvas.create_text(688, 422, anchor = "n", fill = "green", font = 'Helvetica 12', text = 'Poison', tags = 'poison')
        if 720 < event.x < 770 and 255 < event.y < 390:
            canvas.create_text(748, 422, anchor = "n", fill = "white", font = 'Helvetica 12', text = 'Wine', tags = 'wine')
        if 775 < event.x < 830 and 320 < event.y < 390:
            canvas.create_text(800, 422, anchor="n", fill="purple", font='Helvetica 12', text='Back', tags = 'back')
            canvas.create_text(320, 230, anchor = "n", fill = "white", font = 'Helvetica 16', text = '<--- Your quest is over but at least you can return to tell the tale.', tags = 'back')

    #Creates a button that resets the canvas and lets the player try again
    canvas.create_rectangle(1170,441,1270,491, fill = 'yellow', outline = 'black')
    canvas.create_text(1220,448, anchor = 'n', fill = 'black', font = 'Helvetica 12', text = 'Right click')
    canvas.create_text(1220,466, anchor = 'n', fill = 'black', font = 'Helvetica 12', text = 'to reset')

    def reset(event):
        if 1170 < event.x < 1270 and 441 < event.y < 491:
            canvas.delete('poison', 'wine', 'forward', 'back')

    #Binds the left click to the getxy() function
    canvas.bind('<Button-1>', getxy)
    canvas.bind('<Button-3>', reset)
    canvas.pack()
    canvas.mainloop()

def make_canvas(width, height, title=None):
    """
    This is a function provided by Code in Place that creates a canvas to be worked on.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
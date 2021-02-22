#Also note that `from <module> import *` is generally frowned upon
#since it can lead to namespace collisions. It's much better to only
#explicitly import the things you need.
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import audio as myaudiobtn
root = Tk()


root.counter = 0

root.geometry("500x500")
root.title('Sound Recorder Application')


def showName(fileName):
    print("file name entered :", fileName.get())
    return

def format():
    print ("value is:" + formatselection.get())

def thing():

    print("You clicked the record button!")
    root.counter += 1
    print(root.counter)
    print(root.counter % 2 == 1)
    if root.counter % 2 == 0:
        path = 'images/bulboff.png'
    else:
        path = 'images/bulbon.png'
    print(path)
    img = ImageTk.PhotoImage(Image.open(path))

    myaudiobtn.recButton(fileName.get(),formatselection.get())


    panel.config(image=img)
    panel.image=img
    print('GUI Recording stopped!')

record_btn = PhotoImage(file= 'COSC402/micbutton.png')

img_label = Label(image = record_btn)
#img_label.pack(pady=20)

OPTIONS = [
"mp3",
"flac",
"wav"
]

fileNameLabel = Label(root, text="File Name")#.grid(row=0, column=0)
fileNameLabel.pack(pady=20)
fileName = StringVar()
fileNameEntry = Entry(root, textvariable=fileName)#.grid(row=0, column=1)
fileNameEntry.pack(pady=20)

showName = partial(showName, fileName)

createButton = Button(root, text="Create File", command=showName)#.grid(row=4, column=0)
createButton.pack(pady=20)

formatLabel = Label(root, text="Select Format")#.grid(row=0, column=0)
formatLabel.pack(pady=20)

formatselection = StringVar(root)
formatselection.set(OPTIONS[0]) # default value

w = OptionMenu(root, formatselection, *OPTIONS)
w.pack()

button = Button(root, text="OK", command=format)
button.pack()

if root.counter % 2 == 0:
    path = 'images/bulboff.png'
else:
    path = 'images/bulbon.png'




#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = LEFT)


my_button = Button(root, image=record_btn, command= thing, borderwidth=0, height = 100, width = 100)
my_button.pack(pady=20, side=RIGHT)




#my_label = Label(root, text='')
#my_label.pack(pady=20)

root.mainloop()

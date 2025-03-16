from tkinter import *

root = Tk()

root.geometry("450x600")
root.title("cowculator")

def pressme():
    print("Git Works!")

button = Button(root, text="Press Me!", command=pressme)
button.pack()

root.mainloop()
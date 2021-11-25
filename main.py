from tkinter import *
import tkinter
from Todo import Todo

#Initialisation Todo
todoList = [Todo('Make user case'), Todo('Make the next one'), Todo('Get so bread')]
for i in todoList:
    i.print()

#Initialisation Fenetre
fenetre = tkinter.Tk()
fenetre.title("Todo App")
fenetre.geometry("150x200")


#Implication des todos dans la fenêtre
liste = Listbox(fenetre)
for i in range (len(todoList)):
    liste.insert(i, todoList[i].title)
liste.pack()

fenetre.mainloop()


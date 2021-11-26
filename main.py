from tkinter import *
import tkinter
from Todo import Todo
import function
#Initialisation Todo
function.todoList = [Todo('Make user case'), Todo('Make the next one'), Todo('Get so bread')]

#Sauvegarde dans un fichier
def save():
    fichier = open("todo.txt", "w")
    for i in function.todoList:
        
        fichier.write(i.title + "|" + str(i.state) + "|" + i.description + '\n')
    fichier.close()

#Remplace les todo par ceux dans le fichier
def load():
    for i in range(len(function.todoList)):
        liste.delete(0)
        function.todoList.pop(0)

    fichier = open("todo.txt", "r")
    ligne = "0|0"
    
    i = 0
    while (True):
        ligne = fichier.readline()
        if (len(ligne.split("|"))) > 1:
            title, state, description = ligne.split("|")
            function.todoList.append(Todo(title, int(state)))
            liste.insert(i, title)
            i += 1
            print(i)
        else:
            break

#Ajoute un todo dans la liste
def add():
    #Recuperer le titre
    title = var.get()
    if (len(title) > 1):
        function.todoList = [Todo(title)] + function.todoList
        liste.insert(0, title)



function.todoList[1].state = 1

#Initialisation Fenetre
fenetre = tkinter.Tk()
fenetre.title("Todo App")
fenetre.geometry("500x200")

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=50, pady=30)


#Implication des todos dans la fenêtre
liste = Listbox(Frame1)
for i in range (len(function.todoList)):
    #Met les todo fini à la fin
    if (function.todoList[i].state == 1):
        function.todoList.append(function.todoList.pop(i))
    liste.insert(i, function.todoList[i].title)
liste.pack()

var = StringVar()
name = Entry(fenetre, textvariable=var )
name.focus_set()
name.pack(side=RIGHT)

#Création des différents boutons
Button(fenetre, text ='Save', command=save).pack(side=RIGHT)
Button(fenetre, text ='Load', command=load).pack(side=RIGHT)
Button(fenetre, text ='Add', command=add).pack(side=RIGHT)

Label(Frame1).pack()








fenetre.mainloop()


        

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
    
    function.todoList = [Todo("title")] + function.todoList
    liste.insert(0, "title")



function.todoList[1].state = 1
print(function.todoList[1].state)
for i in function.todoList:
    i.print()

#Initialisation Fenetre
fenetre = tkinter.Tk()
fenetre.title("Todo App")
fenetre.geometry("400x200")

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



#Bouton mise à jour valeur state
#Button(fenetre, text ='Edit state', command=edit).pack(side=RIGHT, padx=5, pady=5)
Button(fenetre, text ='Save', command=save).pack(side=RIGHT, padx=5, pady=10)
Button(fenetre, text ='Load', command=load).pack(side=RIGHT, padx=5, pady=10)
Button(fenetre, text ='Add', command=add).pack(side=RIGHT, padx=5, pady=10)

Label(Frame1).pack(padx=10, pady=10)
#Label(Frame2).pack(padx=10, pady=10)








fenetre.mainloop()


        

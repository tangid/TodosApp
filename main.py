from tkinter import *
import tkinter
from Todo import Todo

#Initialisation Todo
todoList = [Todo('Make user case'), Todo('Make the next one'), Todo('Get so bread')]


"""
def edit():
    for i in range(len(todoList)):
        if listButtonValue[i].get():
            todoList[i].state = 1
        else:
            todoList[i].state = 0


    #Update position
    for i in range(len(todoList)):
        if todoList[i].state:

            #Update liste todo            
            for i in range(len(todoList)):
                if (todoList[i].state):
                    todoList.append(todoList.pop(i))
                liste.delete(i)
            for i in range (len(todoList)):
                pass
                liste.insert(i, todoList[i].title)

            #Update état bouton
            if (todoList[i].state):
                listButton[i].select()
            else:
                listButton[i].deselect()
"""
def save():
    fichier = open("todo.txt", "w")
    for i in todoList:
        
        fichier.write(i.title + "|" + str(i.state) + "|" + i.description + '\n')
    fichier.close()

def load():
    for i in range(len(todoList)):
        liste.delete(0)
        todoList.pop(0)

    fichier = open("todo.txt", "r")
    ligne = "0|0"
    
    i = 0
    while (True):
        ligne = fichier.readline()
        if (len(ligne.split("|"))) > 1:
            title, state, description = ligne.split("|")
            todoList.append(Todo(title, int(state)))
            liste.insert(i, title)
            i += 1
            print(i)
        else:
            break





todoList[1].state = 1
print(todoList[1].state)
for i in todoList:
    i.print()

#Initialisation Fenetre
fenetre = tkinter.Tk()
fenetre.title("Todo App")
fenetre.geometry("400x200")

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=50, pady=30)

"""
# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)
"""
#Implication des todos dans la fenêtre
liste = Listbox(Frame1)
for i in range (len(todoList)):
    #Met les todo fini à la fin
    if (todoList[i].state == 1):
        todoList.append(todoList.pop(i))
    liste.insert(i, todoList[i].title)
liste.pack()
"""
#Creation bouton State
listButton = []
listButtonValue = []
for i in range (len(todoList)):
    listButtonValue.append(IntVar())
    listButton.append(Checkbutton(Frame2, variable=listButtonValue[i], onvalue=1, offvalue=0))
    #Check the box if state is done
    if todoList[i].state == 1:
        listButton[i].select()
    listButton[i].pack()
"""


#Bouton mise à jour valeur state
#Button(fenetre, text ='Edit state', command=edit).pack(side=RIGHT, padx=5, pady=5)
Button(fenetre, text ='Save', command=save).pack(side=RIGHT, padx=5, pady=2)
Button(fenetre, text ='Load', command=load).pack(side=RIGHT, padx=5, pady=10)
#Button(fenetre, text ='Add', command=add).pack(side=RIGHT, padx=5, pady=10)

Label(Frame1).pack(padx=10, pady=10)
#Label(Frame2).pack(padx=10, pady=10)








fenetre.mainloop()


        

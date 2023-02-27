from tkinter import*

import random
root=Tk()
root.title("Ruleta")
root.geometry("500x500")
def numero():
    randomlist=random.sample(range(1 , 12),3)
    label_number["text"]="La lista aleatoria" + str(randomlist)
label_random_number=Label(root,text="Aqui se mostrara el resultado")
label_number=Label(root,text="")
button=Button(root,text="Dame click", command=numero)
label_random_number.place(relx=0.5,rely=0.5,anchor=CENTER)
label_number.place(relx=0.5,rely=0.6,anchor=CENTER)
button.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()


import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



import os

fasta=""
lista=""
window=Tk()
window.title("lector de fasta")

def callback1():
	
	file = filedialog.askopenfile(mode ='r', filetypes =[('Fasta Files', '*.fasta')])
	if file is not None:
		content = file.read()
		root = Tk()
		S = Scrollbar(root)
		T = Text(root, height=20, width=70)
		S.pack(side=RIGHT, fill=Y)
		T.pack(side=LEFT, fill=Y)
		S.config(command=T.yview)
		T.config(yscrollcommand=S.set)
		T.insert(END, content) 
		root.mainloop()
def callback2():
	lista=filedialog.askopenfilename()
	print (lista)
	return lista
def instruc():
   messagebox.showinfo( "instrucciones", "como usar el programa")

errmsg='error!'
but_fas=Button(pady=40,padx=200,bg='yellow',text='instrucciones de uso',command=instruc).pack(fill=X)
but_fas=Button(pady=40,padx=200,bg='green',text='abrir archivo Fasta',command=callback1).pack(fill=X)
but_lis=Button(pady=40,padx=200,bg='red',text='abrir archivo Lista',command=callback2).pack(fill=X)
window.mainloop()

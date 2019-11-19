import os
from os.path import basename
from glob import *
from Bio.Seq import translate, transcribe, back_transcribe

try:  # Python 2
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.ttk as ttk
    import tkinter.filedialog as filedialog

def clearSeq():
		input_text.delete('0.0', tk.END)
def setSequence(text):
    clearSeq()
    input_text.insert(tk.END, text)
def loadFasta():
    fileObj = filedialog.askopenfile( mode='rU',title='Choose a FASTA file')
    if fileObj:
        codon_list.insert(tk.END, fileObj.name)
        from Bio import SeqIO
        for entry in SeqIO.parse(fileObj, 'fasta'):
            setSequence(entry.seq)
            break
        fileObj.close()
def loadGenBank():
    fileObj = filedialog.askopenfile( mode='rU',title='Choose a FASTA file')
    if fileObj:
        codon_list.insert(tk.END, fileObj.name)
        from Bio import SeqIO
        for entry in SeqIO.parse(fileObj, 'gb'):
            setSequence(entry.seq)
            break
        fileObj.close()
a = []
def click1(x): 
    z = filedialog.askopenfilename(initialdir = "~",title = "Seleccionar archivo", filetypes = ( ("Fasta files", "*.fasta"), ("GenBank files", "*.gbk") ) )
    a[x].insert(tk.END, z)
def fdiag1():
    window1 = tk.Toplevel()
    window1.title('busqueda')
    text_z = ["archivo 1", "archivo 2"]
    for i in range(len(text_z)): 
    	frame = tk.Frame(window1)
    	frame.grid(row=i+2, column=0, sticky="nsew")
    	ttk.Label(frame, text=text_z[i], background="white").grid(row=0, column=0, columnspan=3, padx=10, pady=2, sticky="w")
    	a.append(ttk.Entry(frame, width=60, background="gray"))
    	a[i].grid(row=1, column=0, columnspan=3, padx=10, sticky="ew")
    	ttk.Button(frame, text="buscar", width=10, command=lambda x=i: click1(x)).grid(row=1, column=3, padx=5, sticky="w")
    ttk.Button(frame, text="ok", width=10, command=window1.destroy).grid(row=7, column=1, padx=1, sticky="w")
    ttk.Button(frame, text="cancel", width=10, command=window1.destroy).grid(row=7, column=2, padx=5, sticky="w")
    window1.mainloop()
b=[]
def click2(x): 
    z = filedialog.askopenfilename(initialdir = "~",title = "Seleccionar archivo", filetypes = ( ("Fasta files", "*.fasta"), ("GenBank files", "*.gbk") ) )
    b[x].insert(tk.END, z)
def fdiag2():
    window2 = tk.Toplevel()
    window2.title('busqueda blast')
    text_y = ["archivo"]
    for i in range(len(text_y)): 
    	frame = tk.Frame(window2)
    	frame.grid(row=i+2, column=0, sticky="nsew")
    	ttk.Label(frame, text=text_y[i], background="white").grid(row=0, column=0, columnspan=3, padx=10, pady=2, sticky="w")
    	b.append(ttk.Entry(frame, width=60, background="gray"))
    	b[i].grid(row=1, column=0, columnspan=3, padx=10, sticky="ew")
    	ttk.Button(frame, text="buscar", width=10, command=lambda x=i: click2(x)).grid(row=1, column=3, padx=5, sticky="w")
    ttk.Button(frame, text="ok", width=10, command=window2.destroy).grid(row=7, column=1, padx=1, sticky="w")
    ttk.Button(frame, text="cancel", width=10, command=window2.destroy).grid(row=7, column=2, padx=5, sticky="w")
    window2.mainloop()
c = []
def click3(x): 
    z = filedialog.askopenfilename(initialdir = "~",title = "Seleccionar archivo", filetypes = ( ("Fasta files", "*.fasta"), ("GenBank files", "*.gbk") ) )
    c[x].insert(tk.END, z)
def fdiag3():
    window3 = tk.Toplevel()
    window3.title('alineamiento local')
    text_x = ["archivo 1", "archivo 2"]
    for i in range(len(text_x)): 
    	frame = tk.Frame(window3)
    	frame.grid(row=i+2, column=0, sticky="nsew")
    	ttk.Label(frame, text=text_x[i], background="white").grid(row=0, column=0, columnspan=3, padx=10, pady=2, sticky="w")
    	c.append(ttk.Entry(frame, width=60, background="gray"))
    	c[i].grid(row=1, column=0, columnspan=3, padx=10, sticky="ew")
    	ttk.Button(frame, text="buscar", width=10, command=lambda x=i: click3(x)).grid(row=1, column=3, padx=5, sticky="w")
    ttk.Button(frame, text="ok", width=10, command=window3.destroy).grid(row=7, column=1, padx=1, sticky="w")
    ttk.Button(frame, text="cancel", width=10, command=window3.destroy).grid(row=7, column=2, padx=5, sticky="w")
    window3.mainloop()
d=[]
def click4(x): 
    z = filedialog.askopenfilename(initialdir = "~",title = "Seleccionar archivo", filetypes = ( ("Fasta files", "*.fasta"), ("GenBank files", "*.gbk") ) )
    d[x].insert(tk.END, z)
def fdiag4():
    window4 = tk.Toplevel()
    window4.title('alineamiento m secuencias')
    text_y = ["archivo"]
    for i in range(len(text_y)): 
    	frame = tk.Frame(window4)
    	frame.grid(row=i+2, column=0, sticky="nsew")
    	ttk.Label(frame, text=text_y[i], background="white").grid(row=0, column=0, columnspan=3, padx=10, pady=2, sticky="w")
    	d.append(ttk.Entry(frame, width=60, background="gray"))
    	d[i].grid(row=1, column=0, columnspan=3, padx=10, sticky="ew")
    	ttk.Button(frame, text="buscar", width=10, command=lambda x=i: click4(x)).grid(row=1, column=3, padx=5, sticky="w")
    ttk.Button(frame, text="ok", width=10, command=window4.destroy).grid(row=7, column=1, padx=1, sticky="w")
    ttk.Button(frame, text="cancel", width=10, command=window4.destroy).grid(row=7, column=2, padx=5, sticky="w")
    window4.mainloop()
e = []
def click5(x): 
    z = filedialog.askopenfilename(initialdir = "~",title = "Seleccionar archivo", filetypes = ( ("Fasta files", "*.fasta"), ("GenBank files", "*.gbk") ) )
    e[x].insert(tk.END, z)
def fdiag5():
    window5 = tk.Toplevel()
    window5.title('alineamiento global')
    text_z = ["archivo 1", "archivo 2"]
    for i in range(len(text_z)): 
    	frame = tk.Frame(window5)
    	frame.grid(row=i+2, column=0, sticky="nsew")
    	ttk.Label(frame, text=text_z[i], background="white").grid(row=0, column=0, columnspan=3, padx=10, pady=2, sticky="w")
    	e.append(ttk.Entry(frame, width=60, background="gray"))
    	e[i].grid(row=1, column=0, columnspan=3, padx=10, sticky="ew")
    	ttk.Button(frame, text="buscar", width=10, command=lambda x=i: click5(x)).grid(row=1, column=3, padx=5, sticky="w")
    ttk.Button(frame, text="ok", width=10, command=window5.destroy).grid(row=7, column=1, padx=1, sticky="w")
    ttk.Button(frame, text="cancel", width=10, command=window5.destroy).grid(row=7, column=2, padx=5, sticky="w")
    window5.mainloop()
f=[]
def click6(x): 
    z = filedialog.askopenfilename(initialdir = "~",title = "Seleccionar archivo", filetypes = ( ("Fasta files", "*.fasta"), ("GenBank files", "*.gbk") ) )
    f[x].insert(tk.END, z)
def fdiag6():
    window6 = tk.Toplevel()
    window6.title('analisis filogenetico')
    text_y = ["archivo"]
    for i in range(len(text_y)): 
    	frame = tk.Frame(window6)
    	frame.grid(row=i+2, column=0, sticky="nsew")
    	ttk.Label(frame, text=text_y[i], background="white").grid(row=0, column=0, columnspan=3, padx=10, pady=2, sticky="w")
    	f.append(ttk.Entry(frame, width=60, background="gray"))
    	f[i].grid(row=1, column=0, columnspan=3, padx=10, sticky="ew")
    	ttk.Button(frame, text="buscar", width=10, command=lambda x=i: click6(x)).grid(row=1, column=3, padx=5, sticky="w")
    ttk.Button(frame, text="ok", width=10, command=window6.destroy).grid(row=7, column=1, padx=1, sticky="w")
    ttk.Button(frame, text="cancel", width=10, command=window6.destroy).grid(row=7, column=2, padx=5, sticky="w")
    window6.mainloop()
    
main_window = tk.Tk()
main_window.title('Proyecto de biopython')
menue = tk.Menu(main_window)
menue_single = tk.Menu(menue, tearoff=0)
menue.add_cascade(menu=menue_single, label='Menu')
menue_single.add_command(label='Busqueda',command=fdiag1)
menue_single.add_command(label='Busqueda Blast',command=fdiag2)
menue_single.add_command(label='Alineamiento Local',command=fdiag3)
menue_single.add_command(label='Alineamiento Global',command=fdiag5)
menue_single.add_command(label='Alineamiento M Secuencias',command=fdiag4)
menue_single.add_command(label='Analisis filogenetico',command=fdiag6)
menue_single.add_separator()
menue_single.add_command(label='Exit', command=main_window.destroy)
menue_single1 = tk.Menu(menue, tearoff=0)
menue.add_cascade(menu=menue_single1, label='Instrucciones')
main_window.config(menu=menue)


param_panel = ttk.Frame(main_window, relief=tk.GROOVE, padding=5)

codon_panel = ttk.LabelFrame(param_panel, text='Archivos')
codon_scroller = ttk.Scrollbar(codon_panel, orient=tk.VERTICAL)
codon_list = tk.Listbox(codon_panel, height=5, width=25,yscrollcommand=codon_scroller.set)
codon_scroller.config(command=codon_list.yview)



seq_panel = ttk.Frame(main_window, relief=tk.GROOVE, padding=5)

input_panel = ttk.LabelFrame(seq_panel, text='Contenido de archivos')
input_scroller = ttk.Scrollbar(input_panel, orient=tk.VERTICAL)
input_text = tk.Text(input_panel, width=39, height=5,
                     yscrollcommand=input_scroller.set)
input_scroller.config(command=input_text.yview)

output_panel = ttk.LabelFrame(seq_panel, text='Resultados')
output_scroller = ttk.Scrollbar(output_panel, orient=tk.VERTICAL)
output_text = tk.Text(output_panel, width=39, height=5,
                      yscrollcommand=output_scroller.set)
output_scroller.config(command=output_text.yview)


apply_button = ttk.Button(seq_panel, text='Apply')
clear_button = ttk.Button(seq_panel, text='Clear')
close_button = ttk.Button(seq_panel, text='Close', command=main_window.destroy)


statustext = tk.StringVar()
statusbar = ttk.Label(main_window, textvariable=statustext, relief=tk.GROOVE,
                      padding=5)
statustext.set('barra de estado')
sizegrip = ttk.Sizegrip(statusbar)

def clear_output():
    input_text.delete(1.0, tk.END)
    output_text.delete(1.0, tk.END)
    return

statusbar.pack(side=tk.BOTTOM, padx=1, fill=tk.X)
sizegrip.pack(side=tk.RIGHT, padx=3, pady=4)

param_panel.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=10, fill=tk.Y)
codon_panel.pack(fill=tk.Y, expand=True)
codon_scroller.pack(side=tk.RIGHT, fill=tk.Y)
codon_list.pack(fill=tk.Y, expand=True)


seq_panel.pack(anchor=tk.N, padx=5, pady=10, fill=tk.BOTH, expand=True)
input_panel.pack(fill=tk.BOTH, expand=True)
input_scroller.pack(side=tk.RIGHT, fill=tk.Y)
input_text.pack(fill=tk.BOTH, expand=True)
output_panel.pack(pady=10, fill=tk.BOTH, expand=True)
output_scroller.pack(side=tk.RIGHT, fill=tk.Y)
output_text.pack(fill=tk.BOTH, expand=True)
apply_button.pack(side=tk.LEFT)
clear_button.pack(side=tk.LEFT, padx=10)
close_button.pack(side=tk.LEFT)

main_window.mainloop()

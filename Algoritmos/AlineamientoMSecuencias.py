
from Utilidades import juntar_secuencias
# Usaremos clustalw para el alineamiento multiple ya que es mas eficiente
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
import os

def clustal(archivo,tipo,matriz):

#utilidad de carpeta de secuencias fasta a un archivo fasta
    clustalw_exe = "Algoritmos/programs/clustalw2"
    clustalw_cline = ClustalwCommandline(clustalw_exe, matrix = matriz, type = tipo, infile=archivo)
    #assert os.path.isfile(clustalw_exe)#, "Clustal W executable missing"
    stdout, stderr = clustalw_cline()
    print(stderr)
    print(stdout)

#juntar_secuencias("/home/mentalist/Desktop/prueba","fasta","/home/mentalist/Desktop/prueba/juntar/resultado.fasta" )


def test():
    alin2 = AlignIO.read("/home/mentalist/Desktop/prueba/juntar/resultado.aln", "clustal")
    print("Size:", alin2. get_alignment_length())
    for record in alin2:
        print(record.id)
        print(record.seq)

#clustal("/home/mentalist/Desktop/prueba/juntar/resultado.fasta", "protein" , "BLOSUM")
test()
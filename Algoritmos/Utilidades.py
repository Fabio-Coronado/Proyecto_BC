from Bio import SeqIO
import os, fnmatch
#retornar secuencia de un archivo fasta
def obtener_secuencia(archivo):
    record = SeqIO.read(archivo,"fasta")
    secuencia= record.seq
    return secuencia

#utilidad de carpeta de secuencias fasta a un archivo fasta
def juntar_secuencias(carpeta,tipo,resultado):
    records = []
    for filename in os.listdir(carpeta):
        if fnmatch.fnmatch(filename,"*."+tipo):
            handle = open (carpeta+"/"+filename)
            record = SeqIO.read(handle, tipo)
            records.append(record)
    SeqIO.write(records,resultado,"fasta")
    




from Bio import SeqIO

#retornar secuencia de un archivo fasta
def obtener_secuencia(archivo):
    record = SeqIO.read(archivo,"fasta")
    secuencia= record.seq
    return secuencia

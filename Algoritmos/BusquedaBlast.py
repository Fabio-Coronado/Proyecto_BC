from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import re
#guarda un archivo xml
def Blast(archivofasta, direccion,nombrearchivo):
    
    record = SeqIO.read(open(archivofasta), format="fasta")
    #protein
    #Puedo incluir una herramienta que cambie de otro formato a fasta
    result_handle = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))

    save_file = open( direccion+"/"+nombrearchivo+".xml", "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()

# Info archivo xml
def InfoArchivoXml(archivoxml):
    result_handle = open(archivoxml)
    blast_record = NCBIXML.read(result_handle)
    print ("PARAMETROS:")
    print ("Base de datos: " + blast_record.database)
    print ("Matriz: " + blast_record.matrix)
    print ("Penalizacion por gaps: ", blast_record.gap_penalties)
    result_handle.close()

#alineamiento con el valor e mas bajo
def Numero_Alineamiento(archivoxml,numero):
    result_handle = open(archivoxml)
    blast_record = NCBIXML.read(result_handle)
    first_alignment = blast_record.alignments[numero]
    print ("Primer  alineamiento:")
    print ("Acceso: " + first_alignment.accession)
    print ("Hit id: " + first_alignment.hit_id)
    print ("Definicion: " + first_alignment.hit_def)
    print ("Longitud de alineamiento: ", str(first_alignment.length))
    print ("Numero de HSPs: ", str(len(first_alignment.hsps)))
    #obtengo mas detalles si tengo un unico HSP
    if len(first_alignment.hsps) == 1:
        hsp = first_alignment.hsps[0]
        print ("E-value: ", hsp.expect)
        print ("Score: ", hsp.score)
        print ("Longitud: ", hsp.align_length)
        print ("Identities: ", hsp.identities)
        print ("Alineamiento de HSP:")
        print (hsp.query)
        print (hsp.match)
        print (hsp.sbjct)
    result_handle.close()

#Mejores alineamientos
def Mejores_Alineamientos(archivoxml,cantidad):
    result_handle = open(archivoxml)
    blast_record = NCBIXML.read(result_handle)
    print ("Mejores "+str(cantidad) + " alineamientos:")
    for i in range (cantidad):
        alineamiento = blast_record.alignments[i]
        print ("Acceso: " + alineamiento.accession)
        print ("Definicion: " + alineamiento.hit_def)
        for hsp in alineamiento.hsps:
            print ("E-value: ", hsp.expect)
        print()
    result_handle.close()

#Organismos presentes en los mejores alineamientos
    
def Organismos(archivoxml,cantidad):
    result_handle = open(archivoxml)
    blast_record = NCBIXML.read(result_handle)
    especies = []
    for i in range (cantidad):
        alineamiento = blast_record.alignments[i]
        definicion = alineamiento.hit_def
        x = re.search("\[(.*?)\]", definicion).group(1)
        especies.append(x)
    result_handle.close()
    print ("Organismos:")
    i=1
    for s in especies: 
        print(str(i)+": "+s)
        i=i+1
    
Blast("/home/mentalist/Desktop/prueba/LASP1MM.fasta","/home/mentalist/Desktop/prueba","my_blast")
#InfoArchivoXml("/home/mentalist/Desktop/prueba/my_blast.xml")      
#Numero_Alineamiento("/home/mentalist/Desktop/prueba/my_blast.xml",0)
#Mejores_Alineamientos("/home/mentalist/Desktop/prueba/my_blast.xml",20)
#Organismos("/home/mentalist/Desktop/prueba/my_blast.xml",20)
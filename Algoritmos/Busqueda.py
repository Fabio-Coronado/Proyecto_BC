#Busquedas mediante Entrez
from Bio import Entrez 
from Bio import SeqIO

def inicializacion(correo):
    Entrez.email = "<"+correo+">"
    Entrez.tool = "Biopython"
#info = Entrez.einfo()
#record = Entrez.read(info)
#print(record['DbList']) #base de datos
# bases de datos nucleotide  protein

def BusquedaIds(listaid,archivo):
    
    x = len(listaid)
    #abrir archivo para escritura
    f = open(archivo,"w")
    for i in range (x):
        r = Entrez.esearch("protein",str(listaid[i]),retmax = 1)
        records = Entrez.read(r)
        ID = records['IdList']
        resultado = Entrez.efetch("protein",id = ID[0], rettype = "fasta")
        record = list(SeqIO.parse(resultado, "fasta")) 
        f.write(">"+record[0].description+"\n")
        f.write(str(record[0].seq)+"\n")
    f.close()


def Busqueda(basededatos, termino, tipo, maximo):
    resultados = Entrez.esearch(basededatos,termino,retmax = maximo)
    records = Entrez.read(resultados)
    IDs = records['IdList'] #ids de la buqueda
    n = records['RetMax'] #cantidad de resultados
    n= int(n)
    #ID de resultados

    print("-----------------------------------------------------------------------------")
    print("Resultados de la Busqueda:")
    lista = {} #diccionario de resultados
    for i in range(0,n):
        r= Entrez.efetch(basededatos,id = IDs[i], rettype = tipo)
        record = list(SeqIO.parse(r, tipo)) 
        lista[i]= [IDs[i], ">"+record[0].description, str(record[0].seq) ]
        r.close()
        print(i,lista[i][0]+ " "+lista[i][1])

    #print(lista)
 
    
    print("-----------------------------------------------------------------------------")
    print("Busqueda finalizada")
    print("Se encontraron " + str(i+1) +" resultados")
    return lista

def ObtenerSecuencia ( listado , posicion ,  guardar = "No" , nombrearchivo= None, direccion = None, tipo=None):
   descripcion= listado[posicion][1]
   secuencia = listado[posicion][2]

   if guardar == "Si":
       f = open(direccion+"/"+nombrearchivo+"."+tipo,"w")
       f.write(descripcion+"\n")       
       f.write(secuencia)
       print("-----------------------------------------------------------------------------")
       print("Se guardo el archivo en "+ direccion+"/"+nombrearchivo+"."+tipo)
   print("-----------------------------------------------------------------------------")
   print("Retornado la secuencia escogida")
   return f

#inicializacion
inicializacion("acoronadoh@uni.pe")
#Busqueda que retorna la descripcion fasta de los archivos
#resultados = Busqueda("protein","LASP Bactrocera latifrons", "fasta", 10)
#Bombyx mori

#Obtener secuencia o guardar en formato fasta
#secuencia = ObtenerSecuencia(resultados,5,"Si","LASPBL","/home/mentalist/Desktop/prueba","fasta")

#print(secuencia)

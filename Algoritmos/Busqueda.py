#Busquedas mediante Entrez
from Bio import Entrez 
from Bio import SeqIO
Entrez.email = "<acoronadoh@uni.pe>"
Entrez.tool = "Biopython"
info = Entrez.einfo()
record = Entrez.read(info)
#print(record['DbList']) #base de datos
# nucleotide genome protein

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
        print(i,lista[i])

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
       f.close()
       print("-----------------------------------------------------------------------------")
       print("Se guardo el archivo en "+ direccion+"/"+nombrearchivo+"."+tipo)
   print("-----------------------------------------------------------------------------")
   print("Retornado la secuencia escogida")
   return secuencia
    

#Busqueda que retorna la descripcion fasta de los archivos
resultados = Busqueda("protein","LASP1 Homo sapiens", "fasta", 10)


#Obtener secuencia o guardar en formato fasta windows
secuencia = ObtenerSecuencia(resultados,3,"Si","ejemplo","C:/Users/MenTaLisT/Desktop","fasta")
#Obtener secuencia o guardar en formato fasta linux
#secuencia = ObtenerSecuencia(resultados,3,"Si","ejemplo","direccion","fasta")
print(secuencia)

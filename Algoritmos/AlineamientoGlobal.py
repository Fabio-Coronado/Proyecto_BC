#Alineamiento Global
from Bio.SubsMat import MatrixInfo as matlist
import Utilidades
#leyendo la matriz de puntuaciones
def score_pos (c1, c2, sm, g):
    if c1 == "-" or c2=="-":
        return g
    else:
        if (c1,c2) in sm:
            return sm[c1,c2]
        else:
            return sm[c2,c1]




#matriz de ratreo: 1 para la diagonal, 2 se usa para vertical y 3 para horizontal
def max3t (v1, v2, v3):
    if v1 > v2:
        if v1 > v3: return 1
        else : return 3
    else:
        if v2 > v3: return 2
        else : return 3


def needleman_Wunsch (seq1, seq2, sm, g):
    S = [[0]]
    T = [[0]]
    ## inicializacion de filas gaps
    for j in range(1, len (seq2)+1):
        S[0].append(g * j)
        T[0].append(3)
        ## inicializacion de columnas gaps
    for i in range(1, len (seq1)+1):
        S.append([g * i])
        T.append([2])
    ## Llenando el resto de la matriz
    for i in range(0, len (seq1)):
        for j in range( len (seq2)):
            s1 = S[i][j] + score_pos(seq1[i], seq2[j], sm, g);
            s2 = S[i][j+1] + g
            s3 = S[i+1][j] + g
            S[i+1].append(max(s1, s2, s3))
            T[i+1].append(max3t(s1, s2, s3))
    return (S, T)


def recover_align (T, seq1, seq2):
    res = ["", ""]
    i = len (seq1)
    j = len (seq2)
    while i>0 or j>0:
        if T[i][j]==1:
            res[0] = seq1[i-1] + res[0]
            res[1] = seq2[j-1] + res[1]
            i -= 1
            j -= 1
        elif T[i][j] == 3:
            res[0] = "-" + res[0]
            res[1] = seq2[j-1] + res[1]
            j -= 1
        else:
            res[0] = seq1[i-1] + res[0]
            res[1] = "-" + res[1]
            i -= 1
    return res

def print_mat (mat):
    for i in range(0, len (mat)):
        print (mat[i])
    
def test_global_alig():
    #cargando matriz de puntuaciones
    sm = matlist.pam250 # read_submat_file("C:/Users/MenTaLisT/Desktop/blosum62.mat")
    #print(sm["W","F"])
    seq1 = Utilidades.obtener_secuencia("/home/mentalist/Desktop/prueba/LASP1HS.fasta")
    seq2 = Utilidades.obtener_secuencia("/home/mentalist/Desktop/prueba/LASP1MS.fasta")

    res = needleman_Wunsch(seq1, seq2, sm, -8)
    S = res[0]
    T = res[1]
    print("------------------------------------------------------------------------------")
    print ("Score optimo:", S[len (seq1)][ len (seq2)])
    print("------------------------------------------------------------------------------")
    print("Matriz de puntuaciones")
    print_mat(S)
    print("------------------------------------------------------------------------------")
    print("Matriz de rastreo")
    print_mat(T)
    alig = recover_align(T, seq1, seq2)
    print("------------------------------------------------------------------------------")
    print("Alineamiento:")
    print (alig[0])
    print (alig[1])

test_global_alig()
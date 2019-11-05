#Alineamiento Local
from Bio.SubsMat import MatrixInfo as matlist
import Utilidades
def max_mat(mat):
    maxval = mat[0][0]
    maxrow = 0
    maxcol = 0
    for i in range(0, len (mat)):
        for j in range(0, len (mat[i])):
            if mat[i][j] > maxval:
                maxval = mat[i][j]
                maxrow = i
                maxcol = j
    return (maxrow ,maxcol)

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

def smith_Waterman (seq1, seq2, sm, g):
    S = [[0]]
    T = [[0]]
    maxscore = 0
    for j in range(1, len (seq2)+1):
        S[0].append(0)
        T[0].append(0)
    for i in range(1, len (seq1)+1):
        S.append([0])
        T.append([0])
    for i in range(0, len (seq1)):
        for j in range( len (seq2)):
            s1 = S[i][j] + score_pos(seq1[i], seq2[j], sm, g);
            s2 = S[i][j+1] + g
            s3 = S[i+1][j] + g
            b = max(s1, s2, s3)
            if b <= 0:
                S[i+1].append(0)
                T[i+1].append(0)
            else:
                S[i+1].append(b)
                T[i+1].append(max3t(s1, s2, s3))
                if b > maxscore:
                    maxscore = b
    return (S, T, maxscore)

def recover_align_local (S, T, seq1, seq2):
    res = ["", ""]
    i, j = max_mat(S)
    while T[i][j]>0:
        if T[i][j]==1:
            res[0] = seq1[i-1] + res[0]
            res[1] = seq2[j-1] + res[1]
            i -= 1
            j -= 1
        elif T[i][j] == 3:
            res[0] = "−" + res[0];
            res[1] = seq2[j-1] + res[1]
            j -= 1
        elif T[i][j] == 2:
            res[0] = seq1[i-1] + res[0]
            res[1] = "−" + res[1]
            i -= 1
    return res

def print_mat (mat):
    for i in range(0, len (mat)):
        print (mat[i])


def test_local_alig():
    sm = matlist.blosum62
    #print(sm)
    seq1 = Utilidades.obtener_secuencia("/home/mentalist/Desktop/prueba/LASP1HS.fasta")
    seq2 = Utilidades.obtener_secuencia("/home/mentalist/Desktop/prueba/LASP1MS.fasta")
    res = smith_Waterman(seq1, seq2, sm, -8)
    S = res[0]
    T = res[1]
    print("------------------------------------------------------------------------------")
    print ("Score optimo:", res[2])
    print("------------------------------------------------------------------------------")
    print("Matriz de puntuaciones")
    print_mat(S)
    print("------------------------------------------------------------------------------")
    print("Matriz de rastreo")
    print_mat(T)
    alinL= recover_align_local(S, T, seq1, seq2)
    print("------------------------------------------------------------------------------")
    print("Alineamiento:")
    print (alinL[0])
    print (alinL[1])

test_local_alig()
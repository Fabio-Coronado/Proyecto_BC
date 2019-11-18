from Bio.Phylo.TreeConstruction import *
from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.Consensus import *
from Bio import Phylo

def arboles(archivo,formato):
    aln = AlignIO.read(archivo, formato)
    #print (aln)
    calculator = DistanceCalculator("blosum62")
    dm = calculator.get_distance(aln)
    constructor = DistanceTreeConstructor()
    tree_NJ = constructor.nj(dm)
    #print(tree_NJ)
    tree_UPGMA = constructor.upgma(dm)
    print("---------------------------------------------------")
    print("Metodo UPGMA (agrupamiento jerarquico)")
    print(tree_UPGMA)
    print("---------------------------------------------------")
    print("Metodo NJ (agrupamiento ascendente)")
    print(tree_NJ)
    return tree_NJ, tree_UPGMA

#Reconstruccion de arboles evolutivos 
#parsimonia
def arbol_parsimonia(archivo,formato):
    aln = AlignIO.read(archivo, formato)
    NJ,UPGMA = arboles(archivo,formato)
    starting_tree = NJ
    scorer = ParsimonyScorer()
    searcher = NNITreeSearcher(scorer)
    constructor = ParsimonyTreeConstructor(searcher, starting_tree)
    pars_tree = constructor.build_tree(aln)
    print("Arbol Parsimonia")
    Phylo.draw_ascii(pars_tree)
    #print(pars_tree)

#algoritmo de arbol de consenso con boopstrap
def arbol_consenso(archivo,formato):
    msa = AlignIO.read(archivo,formato)
    #msas = bootstrap(msa,10)
    calculator = DistanceCalculator("blosum62")
    constructor = DistanceTreeConstructor(calculator)
    trees = list(bootstrap_trees(msa,10,constructor)) #contruir arboles replicados pseudoreplicaciones
   # stric_tree = strict_consensus(trees)
    #print(stric_tree)
    majority_tree = majority_consensus (trees,0.5)
    
    print("Arbol de consenso con boopstrap")
    Phylo.draw_ascii(majority_tree)

    #adam_tree = adam_consensus(trees)
    #print(adam_tree)
    #trees[0]
    #support_tree = get_support(trees[0], trees)
    #print(support_tree)
   # consensus_tree = bootstrap_consensus(msa, 100, constructor,majority_consensus)
    #print(consensus_tree)
#tree1,tree2 = arboles("/home/mentalist/Desktop/prueba/probando.aln","clustal")
#Phylo.draw(tree2)#pylab.show()
#print("NJ")
#Phylo.draw_ascii(tree1)
#print("UPGMA")
#Phylo.draw_ascii(tree2)

arbol_parsimonia("/home/mentalist/Desktop/prueba/probando.aln", "clustal")
#arbol_consenso("/home/mentalist/Desktop/prueba/probando.aln", "clustal")
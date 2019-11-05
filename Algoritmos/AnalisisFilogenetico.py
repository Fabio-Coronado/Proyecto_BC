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
    
    print(tree_UPGMA)
    
    return tree_NJ, tree_UPGMA

def arbol_parsimonia(archivo,formato):
    aln = AlignIO.read(archivo, formato)
    NJ,UPGMA = arboles(archivo,formato)
    starting_tree = NJ
    scorer = ParsimonyScorer()
    searcher = NNITreeSearcher(scorer)
    constructor = ParsimonyTreeConstructor(searcher, starting_tree)
    pars_tree = constructor.build_tree(aln)
    print(pars_tree)

def arbol_consenso(archivo,formato):
    msa = AlignIO.read(archivo,formato)
    msas = bootstrap(msa,100)
    calculator = DistanceCalculator("blosum62")
    constructor = DistanceTreeConstructor(calculator)
    trees = list(bootstrap_trees(msa,100,constructor))
    stric_tree = strict_consensus(trees)
    print(stric_tree)
    majority_tree = majority_consensus (trees,0.5)
    print(majority_tree)
    adam_tree = adam_consensus(trees)
    print(adam_tree)
    trees[0]
    support_tree = get_support(trees[0], trees)
    print(support_tree)
   # consensus_tree = bootstrap_consensus(msa, 100, constructor,majority_consensus)
    #print(consensus_tree)
tree1,tree2 = arboles("/home/mentalist/Desktop/prueba/juntar/resultado.aln", "clustal")
Phylo.draw(tree2)#pylab.show()
Phylo.draw_ascii(tree2)

#arbol_parsimonia("/home/mentalist/Desktop/prueba/juntar/resultado.aln", "clustal")
#arbol_consenso("/home/mentalist/Desktop/prueba/juntar/resultado.aln", "clustal")
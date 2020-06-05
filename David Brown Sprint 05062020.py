import importlib

inputfile = 'dnaIn.txt'                 #saves contents of text file as a variable
f = open(inputfile, "r")                #opens file in read mode
seq = f.read()

seq = seq.replace('\n','')
seq = seq.replace('\r', '')

    
def translate(seq):                     #function to translate 
	
	table = { 
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				 
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
		'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
		'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
	} 
	protein ="" 
	if len(seq)%3 == 0: 
		for i in range(0, len(seq), 3): 
			codon = seq[i:i + 3] 
			protein+= table[codon] 
	return protein

def mutate(inputfile):
        with open(inputfile, "r") as f:
                seq = f.read()
        seq = seq.relace(r"\n", "")
        seq = seq.replace(r"\r", "")
        seqN = seq
        seqM = seq
        normal = open("normalDNA.txt", "a")
        normal.truncate(0)
        mutated = open("mutatedDNA.txt", "a")
        mutated.truncate(0)
        seqN.replace('a' , 'A')
        seqM.replace('a' , 'T')
        normal.write(seqN)
        mutated.write(seqM)
        normal.close()
        mutated.close()

def txtTranslate (dType , seq):
        print(dType + translate(seq)


inputfile = 'normalDNA.txt'                 
f = open(inputfile, "r")                
seq = f.read()
dType = "normal amino acids are"
txtTranslate(seq)

inputfile = 'mutatedDNA.txt'
f = open(inputfile, "r")
seq = f.read()
dType = "Mutated amino acids"
txtTranslate(seq)




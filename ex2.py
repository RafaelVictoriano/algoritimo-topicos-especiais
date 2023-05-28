def leArq(arquivo):
	dna = ""
	f = open(arquivo,"r")
	linhas = f.readlines()
	for linha in linhas:
		linha = linha.strip()
		dna += linha
	return dna

dna = leArq("rosalind_dna.txt")
dnaReplaced = dna.replace("T", "U")
print(dnaReplaced)
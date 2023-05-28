def leArq(arquivo):
	dna = ""
	f = open(arquivo,"r")
	linhas = f.readlines()
	for linha in linhas:
		linha = linha.strip()
		dna += linha
	return dna

# A C G T
contA = 0
contC = 0
contT = 0
contG = 0
dna = leArq('dna.txt')
for l in dna:
	if (l == 'A'):
		contA += 1
	if (l == 'T'):
		contT += 1
	if (l == 'C'):
		contC += 1
	if (l == 'G'):
		contG += 1
print ("{} {} {} {}".format(contA,contC,contG,contT))
def leArq(arquivo):
    dna = ""
    f = open(arquivo, "r")
    linhas = f.readlines()
    for linha in linhas:
        linha = linha.strip()
        dna += linha
    return dna


codigos = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
           "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
           "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
           "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
rna = leArq('rosalind_prot_7_dataset.txt')

proteinas = []
proteina = ''
inicio = False

for i in range(len(rna) - 2):
    codon = rna[i:i + 3]
    rna = rna[2:]

    if codon == '':
        if proteina != '':
            proteinas.append(proteina)
        break
    if codon == 'AUG':
        inicio = True
    if codigos[codon] == 'Stop':
        if proteina != '':
            proteinas.append(proteina)
        proteina = ''
    elif inicio:
        proteina += codigos[codon]

for pro in proteinas:
    print(pro)

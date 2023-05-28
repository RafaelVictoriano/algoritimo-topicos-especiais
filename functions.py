def reverse(string):
    return string[::-1]


def leArq(arquivo):
    dna = ""
    f = open(arquivo, "r")
    linhas = f.readlines()
    for linha in linhas:
        linha = linha.strip()
        dna += linha
    return dna

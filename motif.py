from functions import leArq

conteudo = leArq('motfi.fasta')
motfi = 'CCAGTGGCC'

tamanhoConteudo = len(conteudo)
tamanhoMotifi = len(motfi)

for indice in range(len(conteudo)):
    if len(conteudo) < tamanhoMotifi:
        break
    comparaMotifi = conteudo[:tamanhoMotifi]
    conteudo = conteudo[1:]

    if comparaMotifi == motfi:
        print(indice+1,  end=' ')


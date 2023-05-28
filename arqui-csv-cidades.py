import pandas as pd

url = 'https://raw.githubusercontent.com/geraldocantelli/source/main/data/cidades.csv'

col_names = ['Origem', 'Destino', 'Distancia']
col_names_new_file = ['Destino', 'Origem', 'Distancia']

conteudo = pd.read_csv(url, sep=',', header=None, names=col_names)
novo_conteudo = "Destino\tOrigem\tDistancia\n";
for index, row in conteudo.iterrows():
    print(index)
    print(row)
    destino = row.values[1]
    origem = row.values[0]
    distancia = row.values[2]
    novo_conteudo = novo_conteudo + str(destino) + "\t" + str(origem) + "\t" + str(distancia) + "\n"


file = open('gravando.csv', 'w')
file.write(novo_conteudo)
file.close()



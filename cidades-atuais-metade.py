import pandas as pd

url = 'cidades.csv'

colnames = ['Origem','Destino','Distancia']
df1 = pd.read_csv(url,sep=',',header=None, names=colnames)

df2 = pd.concat([df1['Destino'],df1['Origem'], df1['Distancia']], axis=1)
colnames = ['Destino','Origem','Distancia']
df2.columns = colnames

f = open('cidadesAtual.csv', "w")
f.write("{}\t{}\t{}\t{}\n".format('Destino','Origem','Distancia', 'Metade'))

for i, linha in df2.iterrows():
  metade = linha.Distancia/2
  f.write("{}\t{}\t{}\t{}\n".format(linha.Destino,linha.Origem,linha.Distancia, metade))
f.close()
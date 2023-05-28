from functions import *

dna = leArq('dna3.fasta')
dnaReverse = reverse(dna)
response = ''

for letra in dnaReverse:
    if letra == 'A':
        response += 'T'
    elif letra == 'T':
        response += 'A'
    elif letra == 'C':
        response += 'G'
    elif letra == 'G':
        response += 'C'

print(response)




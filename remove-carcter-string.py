texto = input("Digite uma string: ")
novo_texto = texto
repeticoes_removidas = int(input("Digite uma um numero: "))

if len(texto) >= repeticoes_removidas:
    for caractere in novo_texto:
        contador = 0
        for caractere_atual in novo_texto:
            if caractere == caractere_atual:
                contador += 1

        if contador == repeticoes_removidas:
            novo_texto = novo_texto.replace(caractere, "")

    print("Texto antigo: ", texto)
    print("NOvo texto: ", novo_texto)
else:
    print("O programa não pode ser executado, por que o tamanho da string deve ser menor ou igual do que os número informados")

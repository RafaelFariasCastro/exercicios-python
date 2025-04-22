def cifra_cesar(k, palavra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho_alfabeto = len(alfabeto)
    palavra_criptografada = []
    for letra in palavra:
        indice = alfabeto.index(letra)
        novo_indice = (indice + k) % tamanho_alfabeto
        nova_letra = alfabeto[novo_indice]
        palavra_criptografada.append(nova_letra)
    return ''.join(palavra_criptografada)

k = int(input())
palavra = input().strip()
print(cifra_cesar(k, palavra))






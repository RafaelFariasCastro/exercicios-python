# Lê as três alturas
A, B, C = map(int, input().split())

# Determina a maior altura
maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C

# Imprime o resultado
print(maior)
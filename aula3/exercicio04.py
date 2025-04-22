N = int(input())

# Verifica se N é uma potência de 2
if (N & (N - 1)) == 0:
    print("Dattebayo")
else:
    print("Tururuuu")
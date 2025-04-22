# Inicializa as variáveis para armazenar as somas totais
total_lucas = 0
total_pedro = 0

# Lê as três partidas
for _ in range(3):
    L, P = map(int, input().split())
    total_lucas += L
    total_pedro += P

# Determina o resultado
if total_lucas > total_pedro:
    print("Lucas")
elif total_pedro > total_lucas:
    print("Pedro")
else:
    print("Empate")
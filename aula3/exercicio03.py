# Lê o número de dias
D = int(input())

# Lê as refeições por dia
refeicoes_por_dia = list(map(int, input().split()))

# Lê a quantidade total de ração e a média ideal
X, M = map(float, input().split())

# Calcula o total de refeições
total_refeicoes = sum(refeicoes_por_dia)

# Calcula a média de ração por refeição
Q = X / total_refeicoes

# Formata Q para uma casa decimal
Q_formatado = round(Q, 1)

# Verifica se a média é suficiente
if Q >= M:
    print(f"{Q_formatado:.1f} OK")
else:
    print(f"{Q_formatado:.1f} FOME")
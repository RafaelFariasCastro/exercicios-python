# Lendo as entradas
media_exigida = float(input())
nota1 = float(input())
nota2 = float(input())

# Calculando a média
media = (nota1 + nota2) / 2

# Verificando se o aluno foi aprovado
if media >= media_exigida:
    print(f"Aluno aprovado na disciplina! Parabens! A sua media foi: {media:.2f}")
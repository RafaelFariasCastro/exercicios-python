A, B = input().split()
B = int(B)

if A == 'N':
    print("Acesso permitido!")
else:
    if B >= 30:
        print("Imune! Siga para um local seguro")
    elif B >= 7:
        print("Acesso negado! Fique em observacao")
    else:
        print("Acesso negado! Isolamento urgente")
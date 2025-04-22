# Lê as duas entradas
 A,B = str(input()).split()

# Verifica as condições

if A == 'direita' and B == "esquerda" : 
    print('Achou')
elif A == 'direita' and B == 'direita' :
    print('Tente novamente')
elif A == 'esquerda' and B == 'esquerda' :
    print('Morreu')
elif A == 'esquerda' and B == 'direita' :
    print('Tente novamente')
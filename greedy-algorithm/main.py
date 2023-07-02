def capturar_galinhas(arranjo, k):
    raposas = []
    galinhas = []
    n = len(arranjo)

    for i in range(n):
        if arranjo[i] == 'R':
            raposas.append(i)
        else:
            galinhas.append(i)

    pares = []
    i = 0
    j = 0

    while i < len(raposas) and j < len(galinhas):
        if abs(raposas[i] - galinhas[j]) <= k:
            pares.append((raposas[i] + 1, galinhas[j] + 1))
            i += 1
            j += 1
        elif raposas[i] < galinhas[j]:
            i += 1
        else:
            j += 1

    return pares


# Exemplo de uso
arranjo_1 = ['R', 'G', 'G', 'G', 'R']
k1 = 1
pares_1 = capturar_galinhas(arranjo_1, k1)
print(f'B[] = {pares_1}\nSize = {len(pares_1)}\n')

arranjo_2 = ['G', 'G', 'R', 'R', 'G', 'R']
k2 = 2
pares_2 = capturar_galinhas(arranjo_2, k2)

print(f'B[] = {pares_2}\nSize = {len(pares_2)}')

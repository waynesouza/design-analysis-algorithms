def to_capture_chickens(A, k):
    captures = []  # Lista de capturas

    for i in range(len(A)):
        if A[i] == 'R':
            j = i - k  # Inicializa o índice da galinha no limite inferior do intervalo permitido

            while j <= i + k:
                if 0 <= j < len(A) and A[j] == 'G':
                    captures.append((i + 1, j + 1))  # Adiciona o par (i, j) à lista de capturas
                    break
                j += 1

    return captures, len(captures)


A = ['G', 'G', 'R', 'R', 'G', 'R']
k = 2
B, size = to_capture_chickens(A, k)
print(f'A[] = {A}\nB[] = {B}\nSize = {size}')

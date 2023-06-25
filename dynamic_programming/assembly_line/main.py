import sys


def min_production_time(N, e1, e2, a1, a2, t1, t2, x1, x2):
    # Inicialização das listas de tempo mínimo
    T1 = [0] * N
    T2 = [0] * N

    # Calculando o tempo mínimo para a primeira estação
    T1[0] = e1 + a1[0]
    T2[0] = e2 + a2[0]

    # Calculando os tempos mínimos para cada etapa subsequente
    for i in range(1, N):
        T1[i] = min(T1[i - 1] + a1[i], T2[i - 1] + t2[i - 1] + a1[i])
        T2[i] = min(T2[i - 1] + a2[i], T1[i - 1] + t1[i - 1] + a2[i])

    # Calculando o tempo mínimo de saída
    min_time = min(T1[N - 1] + x1, T2[N - 1] + x2)

    return min_time


def main():
    for line in sys.stdin:
        N = int(line)
        e1, e2 = [int(x) for x in input().split()]
        a1 = [int(x) for x in input().split()]
        a2 = [int(x) for x in input().split()]
        if N != 1:
            t1 = [int(x) for x in input().split()]
            t2 = [int(x) for x in input().split()]
        x1, x2 = [int(x) for x in input().split()]

        min_time = min_production_time(N, e1, e2, a1, a2, t1, t2, x1, x2)
        print(min_time)


if __name__ == "__main__":
    main()

import sys


def solve_shopping_session(M, N, jones_list):
    # Inicializar a tabela de custos mínimos
    # O valor inicial será infinito (representado por sys.float_info.max)
    dp = [[sys.float_info.max] * (N + 1) for _ in range(M + 1)]

    # Preencher a primeira linha com zeros, pois é possível comprar zero itens
    supermarket_list = []
    for j in range(N + 1):
        dp[0][j] = 0
        if j != N:
            K, P = map(float, input().split())
            supermarket_list.append((int(K), float(P)))

    # Preencher a tabela de custos mínimos
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # Verificar se o produto está disponível no supermercado
            if jones_list[i - 1] == supermarket_list[j - 1][0]:
                # Caso o produto esteja disponível, calcular o custo mínimo
                # entre comprar o produto e não comprar o produto
                dp[i][j] = min(dp[i - 1][j - 1] + supermarket_list[j - 1][1], dp[i][j - 1])
            else:
                # Caso o produto não esteja disponível, copiar o custo mínimo
                # da linha anterior
                dp[i][j] = dp[i][j - 1]

    # Verificar se é possível comprar todos os itens da sessão
    if dp[M][N] == sys.float_info.max:
        return "Impossible"
    else:
        return "{:.2f}".format(dp[M][N])


# Função principal
def main():
    while True:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break

        jones_list = list(map(int, input().split()))

        result = solve_shopping_session(M, N, jones_list)
        print(result)


# Executar a função principal
if __name__ == "__main__":
    main()

import sys


def solve_problem(M, N, jones_list):
    dp = [[sys.float_info.max] * (N + 1) for _ in range(M + 1)]

    supermarket_list = []
    for j in range(N + 1):
        dp[0][j] = 0
        if j != N:
            K, P = map(float, input().split())
            supermarket_list.append((int(K), float(P)))

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if jones_list[i - 1] == supermarket_list[j - 1][0]:
                dp[i][j] = min(dp[i - 1][j - 1] + supermarket_list[j - 1][1], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]

    if dp[M][N] == sys.float_info.max:
        return "Impossible"
    else:
        return "{:.2f}".format(dp[M][N])


def main():
    while True:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break

        jones_list = list(map(int, input().split()))

        result = solve_problem(M, N, jones_list)
        print(result)


if __name__ == "__main__":
    main()
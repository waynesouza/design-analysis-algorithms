while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    Xi = list(map(int, input().split()))

    dp = [float('inf')] * (N * M)
    dp[0] = 0

    for _ in range(N):
        K, P = map(float, input().split())
        for j in range(1, M + 1):
            if K == Xi[j - 1] and dp[j - 1] != float('inf') and (dp[j - 1] + P) < dp[j]:
                dp[j] = dp[j - 1] + P
                break

    if dp[M] == float('inf'):
        print("Impossible")
    else:
        print(f"{dp[M]:.2f}")

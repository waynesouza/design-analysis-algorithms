while True:
    try:
        N = int(input())
        e1, e2 = map(int, input().split())
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        t1 = list(map(int, input().split()))
        t2 = list(map(int, input().split()))
        x1, x2 = map(int, input().split())

        dp1 = [0] * (N + 2)
        dp2 = [0] * (N + 2)

        dp1[1] = e1 + a1[0]
        dp2[1] = e2 + a2[0]

        for i in range(2, N + 1):
            dp1[i] = min(dp1[i - 1] + a1[i - 1], dp2[i - 1] + t2[i - 2] + a1[i - 1])
            dp2[i] = min(dp2[i - 1] + a2[i - 1], dp1[i - 1] + t1[i - 2] + a2[i - 1])

        dp1[N + 1] = dp1[N] + x1
        dp2[N + 1] = dp2[N] + x2

        print(min(dp1[N + 1], dp2[N + 1]))

    except (EOFError, ValueError):
        break

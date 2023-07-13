def solve_problem(input_list, k):
    foxes = []
    chickens = []
    n = len(input_list)

    for i in range(n):
        if input_list[i] == 'R':
            foxes.append(i)
        else:
            chickens.append(i)

    pairs = []
    i = 0
    j = 0

    while i < len(foxes) and j < len(chickens):
        if abs(foxes[i] - chickens[j]) <= k:
            pairs.append((foxes[i] + 1, chickens[j] + 1))
            i += 1
            j += 1
        elif foxes[i] < chickens[j]:
            i += 1
        else:
            j += 1

    return pairs


first_list = ['R', 'G', 'G', 'G', 'R']
first_k = 1
first_pairs = solve_problem(first_list, first_k)
print(f'B[] = {first_pairs}\nSize = {len(first_pairs)}\n')

second_list = ['G', 'G', 'R', 'R', 'G', 'R']
second_k = 2
second_pairs = solve_problem(second_list, second_k)
print(f'B[] = {second_pairs}\nSize = {len(second_pairs)}')

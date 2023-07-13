def merge(skyline1, skyline2):
    merged = []
    i = j = 0
    h1 = h2 = 0
    x = h = 0

    while i < len(skyline1) and j < len(skyline2):
        if skyline1[i] < skyline2[j]:
            h1 = skyline1[i+1]
            x = skyline1[i]
            i += 2
        elif skyline2[j] < skyline1[i]:
            h2 = skyline2[j+1]
            x = skyline2[j]
            j += 2
        else:
            h1 = skyline1[i+1]
            h2 = skyline2[j+1]
            x = skyline1[i]
            i += 2
            j += 2

        h = max(h1, h2)
        if len(merged) == 0 or h != merged[-1]:
            merged.append(x)
            merged.append(h)

    merged.extend(skyline1[i:])
    merged.extend(skyline2[j:])

    return merged


def get_skyline(buildings):
    if len(buildings) == 0:
        return []
    elif len(buildings) == 1:
        x, h, d = buildings[0]
        return [x, h, d, 0]

    mid = len(buildings) // 2
    left = get_skyline(buildings[:mid])
    right = get_skyline(buildings[mid:])

    return merge(left, right)


input_skylines = [(0, 8, 5), (2, 10, 9), (1, 4, 7), (11, 5, 15), (17, 11, 20), (19, 17, 22), (14, 3, 28), (25, 13, 30), (8, 6, 23)]
print(get_skyline(input_skylines))


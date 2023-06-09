import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(points):
    n = len(points)
    if n <= 1:
        return None, None, float('inf')
    elif n == 2:
        return points[0], points[1], distance(points[0], points[1])
    else:
        mid = n // 2
        left = points[:mid]
        right = points[mid:]
        lmin, lmax, ldist = closest_pair(left)
        rmin, rmax, rdist = closest_pair(right)

        if ldist <= rdist:
            dmin = ldist
            dmin_pair = (lmin, lmax)
        else:
            dmin = rdist
            dmin_pair = (rmin, rmax)
        midx = (left[-1][0] + right[0][0]) / 2
        strip = []

        for point in points:
            if abs(point[0] - midx) < dmin:
                strip.append(point)
        strip.sort(key=lambda x: x[1])
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= dmin:
                    break
                elif distance(strip[i], strip[j]) < dmin:
                    dmin = distance(strip[i], strip[j])
                    dmin_pair = (strip[i], strip[j])
        return dmin_pair[0], dmin_pair[1], dmin


print(closest_pair([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))

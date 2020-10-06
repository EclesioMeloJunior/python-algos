def read():
    first_line = input().strip().split()

    n = int(first_line[0])
    m = int(first_line[1])

    arr = []

    for _ in range(n):
        cols = list(int(num) for num in input().strip().split())[:m]
        arr.append(cols)

    return n, m, arr


# O(r*log c)
def solve(mtx, n, m):
    mid = int(m / 2)

    max_global = 0

    for r in range(1, n):
        if mtx[r][mid] > mtx[max_global][mid]:
            max_global = r

    if (mid == 0 or mtx[max_global][mid - 1] <= mtx[max_global][mid]) and (mid == m-1 or mtx[max_global][mid + 1] <= mtx[max_global][mid]):
        return mtx[max_global][mid]

    if mid > 0 and mtx[max_global][mid - 1] > mtx[max_global][mid]:
        return solve(mtx, n, mid - 1)

    return solve(mtx, n, mid+1)


def main():
    n, m, arr = read()

    print(solve(arr, m, n))


if __name__ == "__main__":
    main()

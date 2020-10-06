def read():
    first_line = input().strip().split()

    n = int(first_line[0])
    m = int(first_line[1])

    arr = []

    for r in range(n):
        cols = list(int(num) for num in input().strip().split())[:m]
        arr.append(cols)

    return n, m, arr


# O(n*m)
def brute_force_solve(n, m, arr):
    for r in range(n):
        for c in range(m):
            curr = arr[r][c]

            is_peak = (c == 0 or arr[r][c-1] <= curr) and (c == m - 1 or arr[r][c+1] <= curr) and (
                r == 0 or arr[r-1][c] <= curr) and (r == n - 1 or arr[r+1][c] <= curr)

            if is_peak:
                return curr


def main():
    n, m, arr = read()

    print(brute_force_solve(n, m, arr))


if __name__ == "__main__":
    main()

def readN():
    n = int(input())
    return list(int(num) for num in input().strip().split())[:n]


def solve(arr, low, high, n):
    mid = int(low + (high-low)/2)

    if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]

    if mid > 0 and arr[mid-1] > arr[mid]:
        return solve(arr, low, (mid-1), n)

    return solve(arr, (mid+1), high, n)


def main():
    n = readN()
    aws = solve(n, 0, len(n) - 1, len(n))
    print(aws)


if __name__ == "__main__":
    main()

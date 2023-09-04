def selection_sort():
    count = 0
    for last in range(a-1, 0, -1):
        big = max(arr[:last+1])
        i = arr.index(big)
        if i != last:
            arr[last], arr[i] = arr[i], arr[last]
            count += 1
        if count == k:
            return arr
    return [-1]


a, k = map(int, input().split())
arr = list(map(int, input().split()))

result = selection_sort()
for num in result:
    print(num, end=' ')
def binary_search(array, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid+1
        else:
            end = mid-1
    return -1


n = int(input())
data = list(map(int, input().split()))
print(binary_search(data, 0, n-1))

# from bisect import bisect_left, bisect_right
#
# n, x = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# left = bisect_right(data, x-1)
# right = bisect_left(data, x+1)
# if right-left == 0:
#     print(-1)
# else:
#     print(right-left)


n, x = map(int, input().split())
data = list(map(int, input().split()))


# x 원소가 위치한 가장 왼쪽 인덱스를 찾는 함수
def find_left(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        # 가장 왼쪽에 있는 target 인덱스 반환
        if array[mid] == target and (mid == 0 or array[mid-1] < target):
            return mid
        elif array[mid] >= target:
            end = mid-1
        else:
            start = mid+1
    return -1


# x 원소가 위치한 가장 오른쪽 인덱스를 찾는 함수
def find_right(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        # 가장 오른쪽에 있는 target 인덱스 반환
        if array[mid] == target and (mid == n-1 or array[mid+1] > target):
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1


left = find_left(data, x, 0, n-1)
if left == -1:
    print(-1)
else:
    right = find_right(data, x, 0, n-1)
    print(right-left+1)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0
start = 0
end = max(trees)

while start<=end:
    total = 0
    mid = (start+end)//2
    for tree in trees:
        if tree > mid:
            total += tree-mid

    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)

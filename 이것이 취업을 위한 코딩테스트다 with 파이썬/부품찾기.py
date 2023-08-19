n = int(input())
data = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))
for x in request:
    if x in data:
        print("yes", end=' ')
    else:
        print("no", end=' ')
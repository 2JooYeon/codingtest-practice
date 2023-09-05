def back(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        result.append(i)
        back(i)
        result.pop()


n, m = map(int, input().split())
result = []
back(1)
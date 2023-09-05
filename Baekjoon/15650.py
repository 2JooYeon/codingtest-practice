def back(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            back(i+1)
            result.pop()


n, m = map(int, input().split())
result = []
back(1)

import sys
input = sys.stdin.readline

data = list(input().rstrip())
n = len(data)
cursor = n
m = int(input())
for _ in range(m):
    query = input().split()
    c = query[0]
    if c == 'P':
        # insert의 시간복잡도 o(n)
        data.insert(cursor, query[1])
        cursor += 1
        n += 1

    else:
        if c == 'L' and cursor != 0:
            cursor -= 1
        if c == 'D' and cursor != n:
            cursor += 1
        if c == 'B' and cursor != 0:
            # pop 시간복잡도 o(n)
            data.pop(cursor-1)
            cursor -= 1
            n -= 1
print(''.join(data))

from collections import defaultdict

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
money = list(map(int, input().split()))
parent = [x for x in range(n+1)]

for _ in range(m):
    v, w = map(int, input().split())
    union_parent(parent, v, w)

friend_money = defaultdict(lambda : int(1e9))
for i in range(1, n+1):
    friend_money[find_parent(parent, i)] = min(friend_money[find_parent(parent, i)], money[i-1])

need = sum(friend_money.values())

if need>k:
    print('Oh no')
else:
    print(need)

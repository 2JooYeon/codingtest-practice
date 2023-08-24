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


n, m = map(int, input().split())
parent = [x for x in range(n+1)]
for a in range(1, n+1):
    data = list(map(int, input().split()))
    for b in range(1, n+1):
        if data[b-1] == 1:
            union_parent(parent, a, b)

plan = list(map(int, input().split()))
target = parent[plan[0]]
flag = 1
for t in plan[1:]:
    if find_parent(parent, t) != target:
        print('NO')
        flag = 0
if flag:
    print('YES')
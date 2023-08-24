def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [x for x in range(n+1)]
edges = []
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()
answer = 0
original = 0

for z, x, y in edges:
    original += z
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        answer += z

print(original - answer)

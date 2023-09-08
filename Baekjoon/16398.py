def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
edges = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(i, n):
        if data[j] != 0:
            edges.append((data[j], i, j))

edges.sort()
parent = [x for x in range(n+1)]
answer = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c

print(answer)

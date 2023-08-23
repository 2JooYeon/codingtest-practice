import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


answer = []
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
# 유지비가 작은 간선 순으로 정렬
edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer.append(c)

print(sum(answer[:-1]))
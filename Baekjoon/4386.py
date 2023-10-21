import sys
import math
input = sys.stdin.readline

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
parent = list(range(n))
stars = []
for _ in range(n):
    a, b = map(float, input().split())
    stars.append((a, b))

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        edges.append(((math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2)), i, j))

edges.sort()

answer = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c

print(round(answer, 2))

n = int(input())

def get_cost(a, b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

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

planet = []
for _ in range(n):
    planet.append(list(map(int, input().split())))

edges = []
for i in range(n):
    for j in range(i+1, n):
        cost = get_cost(planet[i], planet[j])
        edges.append((cost, i, j))

edges.sort()

parent = [x for x in range(n)]
answer = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c

print(answer)
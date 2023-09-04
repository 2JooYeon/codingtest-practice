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


n = int(input())
m = int(input())
parent = [x for x in range(n+1)]

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 연결 정보 중복을 피하기 위해 대각선 위 정보만 확인
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if city[i-1][j-1]:
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

plan_root = []
for c in plan:
    plan_root.append(find_parent(parent, c))

# 여행 계획에 있는 도시들의 부모 노드가 모두 같다면 yes, 그렇지 않으면 no
plan_root = set(plan_root)
if len(plan_root) == 1:
    print("YES")
else:
    print("NO")
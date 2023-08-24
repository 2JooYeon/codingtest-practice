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

g = int(input())
parent = [x for x in range(g+1)]
p = int(input())
answer = 0
for _ in range(p):
    x = int(input())
    # 현재 비행기 탑승구 확인
    data = find_parent(parent, x)
    # 현재 탑승구가 0이라면 종료
    if data == 0:
        break
    # 현재 탑승구가 0이 아니면 왼쪽 집합과 합치기
    union_parent(parent, data, data-1)
    answer += 1
print(answer)

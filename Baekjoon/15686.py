from itertools import combinations

n, m = map(int, input().split())
home = []
chicken = []
chicken_distance = []
city_distance = []

# 0은 빈칸, 1은 집, 2는 치킨집
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 일반 집 좌표 저장
        if data[j] == 1:
            home.append([i, j])
        # 치킨 집 좌표 저장
        if data[j] == 2:
            chicken.append([i, j])

chicken_num = len(chicken)

# 각 집마다 치킨 거리 구하기
for x, y in home:
    distance = {}
    for i in range(len(chicken)):
        a, b = chicken[i]
        distance[i] = abs(x - a) + abs(y - b)
    chicken_distance.append(distance)

# M개의 치킨집 조합
combi = combinations(range(0, chicken_num), m)
for c in combi:
    temp_city_distance = 0
    # 모든 집의 치킨거리에서
    for distance in chicken_distance:
        temp = 99999
        # M개의 치킨거리 중 최소값 찾기
        for i in c:
            temp = min(temp, distance[i])
        temp_city_distance += temp
    city_distance.append(temp_city_distance)

print(min(city_distance))
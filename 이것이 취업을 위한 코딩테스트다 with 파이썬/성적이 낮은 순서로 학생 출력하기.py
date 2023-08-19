n = int(input())
name_score = []
for _ in range(n):
    data = input().split()
    name_score.append((data[0], int(data[1])))
name_score.sort(key=lambda x: x[1])
for name, score in name_score:
    print(name, end=' ')

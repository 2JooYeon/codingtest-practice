str1 = input()
str2 = input()
len_a = len(str1)
len_b = len(str2)
d = [[0 for _ in range(len_b+1)] for _ in range(len_a+1)]

for i in range(1, len_a+1):
    d[i][0] = i
for i in range(1, len_b+1):
    d[0][i] = i

for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        # 두 문자가 같으면, 왼쪽 위의 값과 동일
        if str1[i-1] == str2[j-1]:
            d[i][j] = d[i-1][j-1]
        # 두 문자가 다르다면, 왼쪽(삽입), 왼쪽 위(교체), 위(삭제) 중 최소 비용으로
        else:
            d[i][j] = min(d[i][j-1], d[i-1][j-1], d[i-1][j]) + 1
print(d[len_a][len_b])

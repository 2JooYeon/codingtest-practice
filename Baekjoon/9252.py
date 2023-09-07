word1 = input()
word2 = input()

len1, len2 = len(word1), len(word2)
dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
# 최장 공통 부분 수열을 구하기 위한 역추적
answer = []
x, y = len1, len2
while x>0 and y>0:
    if dp[x-1][y] == dp[x][y]:
        x -= 1
    elif dp[x][y-1] == dp[x][y]:
        y -= 1
    else:
        answer.append(word1[x-1])
        x -= 1
        y -= 1

print(''.join(map(str, answer[::-1])))
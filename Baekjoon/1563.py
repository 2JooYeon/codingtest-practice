'''해설 블로그: https://lighter.tistory.com/182'''

n = int(input())
# dp[n][i][j] -> n일 동안 지각을 총 i번 하고, 연속 결석 횟수가 j번인 경우의 수
dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
dp[1][0][0], dp[1][0][1], dp[1][1][0] = 1, 1, 1
div = 1000000
for i in range(1, n):
    dp[i+1][0][0] = (dp[i][0][0] + dp[i][0][1] + dp[i][0][2]) % div
    dp[i+1][0][1] = dp[i][0][0]
    dp[i+1][0][2] = dp[i][0][1]
    dp[i+1][1][0] = (dp[i][1][0] + dp[i][1][1] + dp[i][1][2]
                     + dp[i][0][0] + dp[i][0][1] + dp[i][0][2]) % div
    dp[i+1][1][1] = dp[i][1][0]
    dp[i+1][1][2] = dp[i][1][1]

print((dp[n][0][0] + dp[n][0][1] + dp[n][0][2]
       + dp[n][1][0] + dp[n][1][1] + dp[n][1][2]) % div)
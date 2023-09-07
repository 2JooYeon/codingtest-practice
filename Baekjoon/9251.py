'''2차원 버전'''
# word1 = input()
# word2 = input()
# len1, len2 = len(word1), len(word2)
# dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
#
# for i in range(1, len1+1):
#     for j in range(1, len2+1):
#         # 문자가 같으면 이전 LCS값에 +1
#         if word1[i-1] == word2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         # 문자가 다르면 이전에 비교한 값들 중 최댓값 선택
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# print(dp[-1][-1])

'''1차원 버전'''
word1 = input()
word2 = input()
len1, len2 = len(word1), len(word2)
dp = [0 for _ in range(len2)]
for i in range(len1):
    # count에 이전 위치까지의 최대 길이를 저장
    count = 0
    for j in range(len2):
        if count < dp[j]:
            count = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = count + 1
print(max(dp))
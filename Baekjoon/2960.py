def solution():
    count = 0
    for i in range(2, n+1):
        # i가 소수라면 이것을 P라고 함
        if arr[i]:
            j = 2
            # P를 지우고
            arr[i] = False
            count += 1
            if count == k:
                return i
            # 아직 지우지 않은 P의 배수를 순서대로 지우기
            while i*j <= n:
                if arr[i*j]:
                    arr[i * j] = False
                    count += 1
                    if count == k:
                        return i * j
                j += 1


n, k = map(int, input().split())
# 처음에 모든 수가 소수라고 가정(0, 1제외)
arr = [True for _ in range(n+1)]
print(solution())

'''이분탐색(파라메트릭 서치)을 이용한 풀이'''
def solution(stones, k):
    answer = 0
    # 징검다리를 건널 수 있는지 확인할 인원 수
    start = min(stones)
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2
        # mid 번째 사람이 밟을 수 없는 돌의 개수
        cnt = 0
        for stone in stones:
            if stone <= mid:
                cnt += 1
            # 밟을 수 있는 돌을 만나면 cnt 리셋
            else:
                cnt = 0
            # 밟을 수 없는 돌이 연속으로 k 개 있으면 break
            if cnt == k:
                break
        if cnt < k:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid

    return answer

from collections import deque

def solution(gems):
    answer = []
    # 보석 구매 구간의 길이
    distance = int(1e9)
    # 보석의 종류 확인
    gem_type = set(gems)
    # gem_shop[i] = j -> 보석 i를 j개 구매
    gem_shop = dict(zip(gem_type, [0] * len(gem_type)))
    # 구매한 보석 종류의 개수
    cnt = 0
    # 보석 구매 장바구니
    queue = deque()
    for i in range(len(gems)):
        gem = gems[i]
        # 아직 구매하지 않은 보석인 경우
        if gem_shop[gem] == 0:
            queue.append(i)
            gem_shop[gem] += 1
            cnt += 1
            # 모든 종류의 보석을 구매했고, 기존 구매 구간의 길이보다 더 짧은 구간인 경우 업데이트
            if cnt == len(gem_type) and len(queue) < distance:
                distance = len(queue)
                answer = [queue[0] + 1, queue[-1] + 1]
        # 이전에 구매했던 보석인 경우
        else:
            queue.append(i)
            gem_shop[gem] += 1
            # queue의 앞에서부터 장바구니에 2개 이상 있는 보석 제거, 1개만 구매한 보석을 만나면 종료
            while gem_shop[gems[queue[0]]] > 1:
                gem_shop[gems[queue.popleft()]] -= 1
            # 모든 종류의 보석을 구매했고, 기존 구매 구간의 길이보다 더 짧은 구간인 경우 업데이트
            if cnt == len(gem_type) and len(queue) < distance:
                distance = len(queue)
                answer = [queue[0] + 1, queue[-1] + 1]

    return answer

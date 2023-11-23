'''순열과 set을 이용한 풀이'''
from itertools import permutations

def solution(user_id, banned_id):

    # source가 target에 매핑되면 true 반환 / source: user_id 원소, target: banned_id 원소
    def check(source, target):
        if len(source) != len(target):
            return False
        for i in range(len(target)):
            if target[i] == '*': continue
            if source[i] != target[i]: return False
        return True

    n = len(banned_id)
    permutation = permutations(user_id, n)
    # 중복을 피하기 위해 set 사용
    result = set()
    for permu in permutation:
        # 선택된 아이디 목록(permu)이 불량 사용자 목록으로 모두 매핑될 수 있다면 True
        mapping = True
        user = []
        for i in range(n):
            if not check(permu[i], banned_id[i]):
                mapping = False
                break
            else:
                user.append(permu[i])
        # 모두 매핑된 경우
        if mapping:
            # 중복을 피하기 위해 정렬한 후에 set(result)에 추가
            user.sort()
            result.add(tuple(user))

    answer = len(result)

    return answer

'''list의 count함수를 이용한 풀이'''
def solution(s):
    answer = []
    s = s.replace('{', '').replace('}', '').split(',')
    # 중복되는 원소가 없는 튜플
    set_s = set(s)
    # num_elem[i] = j -> 원소 j가 s에서 i번 등장
    num_elem = {}
    for n in set_s:
        num_elem[s.count(n)] = int(n)
    # 가장 많이 등장한 원소부터 answer에 추가
    for i in range(len(set_s), 0, -1):
        answer.append(num_elem[i])

    return answer

'''풀이1: list의 count함수를 이용한 풀이'''
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

'''풀이2: set을 이용한 풀이 (풀이1 보다 시간효율적)'''
def solution(s):
    answer = []
    tuple_group = s[2:-2].split('},{')
    tuple_arr = []
    for group in tuple_group:
        tuple_arr.append(set(group.split(',')))
    tuple_arr.sort(key=lambda x: len(x))

    target = set()
    for arr in tuple_arr:
        answer.append(int(list(arr - target)[0]))
        target = arr

    return answer

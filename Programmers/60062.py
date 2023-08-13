from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    num_weak = len(weak)
    # 원형 외벽 길이 2배로
    for i in range(num_weak):
        weak.append(weak[i] + n)

    for friends in permutations(dist, len(dist)):
        for start in range(num_weak):
            # 투입된 친구의 수
            count = 1
            now = weak[start] + friends[0]
            for i in range(start, start + num_weak):
                if now < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    now = weak[i] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

    return answer

def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        clear_player = len([x for x in stages if x>=i])
        if clear_player == 0:
            answer.append([i, 0])
            continue
        player = stages.count(i)
        answer.append([i, player/clear_player])
    answer.sort(key=lambda x:(-x[1], x[0]))
    answer = [x[0] for x in answer]
    return answer
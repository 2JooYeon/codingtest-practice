def solution(survey, choices):
    answer = ''
    ptype = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    ptype_score = dict(zip(ptype, [0] * 8))
    n = len(survey)
    for i in range(n):
        choice = choices[i]
        if choice == 4:
            continue
        if choice < 4:
            ptype_score[survey[i][0]] += (4 - choice)
        else:
            ptype_score[survey[i][1]] += (choice - 4)
    ptype_score = list(ptype_score.items())

    for i in range(0, 8, 2):
        if ptype_score[i][1] >= ptype_score[i + 1][1]:
            answer += ptype_score[i][0]
        else:
            answer += ptype_score[i + 1][0]

    return answer
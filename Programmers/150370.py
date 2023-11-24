'''풀이 1: YYYY.MM.DD 형태로 비교 '''
def solution(today, terms, privacies):
    answer = []
    # 약관 별 유효기간 저장
    term_month = {}
    for term in terms:
        c, m = term.split()
        term_month[c] = int(m)
    # 날짜를 숫자 리스트로 변환
    today = list(map(int, today.split('.')))

    n = len(privacies)
    for i in range(n):
        privacy = privacies[i]
        # 개인정보 수집 날짜 숫자 리스트로 변환
        day = list(map(int, privacy[:-2].split('.')))
        # 약관 종류에 해당 하는 유효기간 설정
        month = term_month[privacy[-1]]
        if (day[1]+month) % 12 == 0:
            day[1] = 12
            if (day[1]+month)//12 > 1:
                day[0] = day[0]+((day[1]+month)//12) -1
        else:
            day[0] = day[0]+((day[1]+month)//12)
            day[1] = (day[1]+month)%12

        if day[0] > today[0]: continue
        elif day[0] == today[0] and day[1] > today[1]: continue
        elif day[0] == today[0] and day[1] == today[1] and day[2] > today[2]: continue

        answer.append(i+1)

    return answer


'''풀이 2: 2000년 1월 1일부터 경과된 일 수를 계산하여 비교'''
def solution(today, terms, privacies):
    answer = []
    # 약관 별 유효기간 저장
    term_period = {}
    for term in terms:
        c, m = term.split()
        term_period[c] = int(m)

    # 날짜를 숫자 리스트로 변환
    year, month, day = map(int, today.split('.'))
    # 2000년 1월 1일 기준으로 오늘까지 며칠이 흘렀는지 계산
    # 문제에서 한 달은 28일이라고 했으므로 1년은 336일, 1달은 28일
    today = (year - 2000) * 336 + (month - 1) * 28 + (day - 1)

    n = len(privacies)
    for i in range(n):
        privacy = privacies[i]
        year, month, day = map(int, privacy[:-2].split('.'))
        # 약관 종류에 해당 하는 유효기간 설정
        period = term_period[privacy[-1]]
        # 2000년 1월 1일 기준으로 유효기간까지 며칠이 흘렀는지 계산
        exday = (year - 2000) * 336 + (month + period - 1) * 28 + (day - 1)
        if exday <= today:
            answer.append(i + 1)

    return answer

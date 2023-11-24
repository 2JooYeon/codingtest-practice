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
        answer.sort()

    return answer

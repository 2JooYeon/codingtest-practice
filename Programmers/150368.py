'''중복 순열을 이용해서 모든 경우의 수를 확인하는 풀이'''
from itertools import product
from collections import defaultdict

def solution(users, emoticons):
    answer = [0, 0]

    user_percent = {}
    user_limit = {}
    num_user = len(users)
    for user in range(num_user):
        user_percent[user] = users[user][0]
        user_limit[user] = users[user][1]

    discount = [10, 20, 30, 40]
    num_emoti = len(emoticons)
    cases = list(product(discount, repeat=num_emoti))

    for case in cases:
        # 이모티콘 플러스 가입자 수
        emoti_plus = 0
        # 이모티콘 판매액
        cost = 0
        # user_basket[user] = money -> user의 이모티콘 총 구매 비용 money
        user_basket = defaultdict(int)
        # 현재 이모티콘 할인율에 대해 user의 총 구매 비용 계산
        for user in range(num_user):
            for i in range(num_emoti):
                # i번째 이모티콘 할인율이 user가 원하는 할인율 이상인 경우 구매
                if case[i] >= user_percent[user]:
                    user_basket[user] += int(emoticons[i] * (100 - case[i]) * 0.01)
            # user의 이모티콘 총 구매 비용이 user의 기준 가격 이상이 된다면 이모티콘 플러스에 가입
            if user_basket[user] >= user_limit[user]:
                emoti_plus += 1
            # 이모티콘 플러스 가입 안하면 판매액 증가
            else:
                cost += user_basket[user]

        if answer[0] < emoti_plus or (answer[0] == emoti_plus and answer[1] < cost):
            answer = [emoti_plus, cost]

    return answer

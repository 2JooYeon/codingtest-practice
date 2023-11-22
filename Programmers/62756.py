def solution(numbers, hand):
    answer = ''
    hand_rule = {1:'L', 4:'L', 7:'L', 3:'R', 6:'R', 9:'R'}
    num_xy = {2:(0,1), 5:(1, 1), 8:(2, 1), 0:(3, 1)}
    left = (3, 0)
    right = (3, 2)
    for num in numbers:
        if num in hand_rule:
            answer += hand_rule[num]
            # 1,4,7 중 하나면 왼손 이동
            if num%3:
                left = ((num-1)//3, (num-1)%3)
            # 3,6,9 중 하나면 왼손 이동
            else:
                right = ((num-1)//3, (num-1)%3)
        else:
            x, y = num_xy[num]
            # 거리 계산
            left_dist = abs(left[0]-x) + abs(left[1]-y)
            right_dist = abs(right[0]-x) + abs(right[1]-y)
            # 왼손 엄지와 오른손 엄지 중에 가까운 엄지 찾기
            if left_dist<right_dist:
                answer += 'L'
                left = (x, y)
            elif right_dist<left_dist:
                answer += 'R'
                right = (x, y)
            # 거리가 같은 경우 hand에 따라 엄지 선택
            else:
                answer += hand[0].upper()
                if answer[-1] == 'L':
                    left = (x, y)
                else:
                    right = (x, y)

    return answer

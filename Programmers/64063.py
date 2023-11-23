def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        if num not in room:
            answer.append(num)
            room[num] = 1
        else:
            while num in room:
                num += 1
            room[num] = 1
            answer.append(num)

    return answer

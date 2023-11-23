def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        # 빈 방인 경우
        if num not in room:
            answer.append(num)
            # 방을 배정하고 +1을 부모 방으로 설정
            room[num] = num + 1

        # 이미 배정된 방인 경우
        else:
            # 빈 방을 찾는 동안 방문한 방을 기록
            visit = [num]
            # 빈 방이 나올 때까지 확인
            while num in room:
                # 부모 방 방문
                num = room[num]
                # 부모 방이 비어있다면 방 배정
                if num not in room:
                    answer.append(num)
                    # 배정 받은 방의 +1을 부모 방으로 설정
                    room[num] = num + 1
                    # 이전에 방문했던 방들도 부모 방 설정
                    for node in visit:
                        room[node] = num + 1
                    break
                visit.append(num)

    return answer

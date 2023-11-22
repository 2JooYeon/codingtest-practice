'''다익스트라와 비트마스킹을 이용한 풀이'''
from collections import defaultdict
from heapq import heappush, heappop

def solution(n, start, end, roads, traps):
    # trap_index[i] = j -> 트랩 i의 인덱스 j
    trap_index = {}
    for i in range(len(traps)):
        trap_index[traps[i]] = i
    # 도착한 방이 트랩인지 빠르게 찾기 위해 set 이용
    set_trap = set(traps)
    # graph[now] = [(next, weight, is_reverse)] -> now 방에서 next 방으로 갈때 weight의 시간이 걸림. is_reverse는 길의 방향이 반대로 변했는지 여부
    graph = defaultdict(list)
    for p, q, s in roads:
        # 순방향
        graph[p].append((q, s, 0))
        # 역방향(길의 방향이 반대로 변한 경우)
        if p in set_trap or q in set_trap:
            graph[q].append((p, s, 1))

    INF = int(1e9)
    answer = INF
    num_trap = len(traps)
    distance = defaultdict(dict)
    # start 방까지 특정 trap의 상태일때 걸린 시간
    distance[start]['0' * num_trap] = 0

    q = []
    # (총 걸린 시간, 방의 번호, trap의 상태)
    heappush(q, (0, start, '0' * num_trap))

    while q:
        # 현재 누적 시간, 현재 방, 현재 trap의 상태
        total_time, cur_room, trap_status = heappop(q)
        # 현재 방이 함정으로 인해 활성화 되었는지 확인, 0:비활성 / 1:활성
        cur_status = 0
        if cur_room in set_trap:
            cur_status = int(trap_status[trap_index[cur_room]])

        for next_room, weight, is_reverse in graph[cur_room]:
            # 다음 방이 함정으로 인해 활성화 되었는지 확인, 0:비활성 / 1:활성
            next_status = 0
            # 다음 방이 함정인 경우 전체 trap의 상태를 업데이트 해야함
            new_trap_status = trap_status
            if next_room in set_trap:
                next_status = int(trap_status[trap_index[next_room]])
                new_trap_status = trap_status[:trap_index[next_room]] + str((next_status + 1) % 2) + trap_status[
                                                                                                     trap_index[
                                                                                                         next_room] + 1:]
            # 만약 현재 방과 다음 방이 활성화 상태가 달라서 역방향 길이어야 하는데 순방향 길인 경우 패스
            if cur_status ^ next_status and not is_reverse: continue
            # 만약 현재 방과 다음에 도착할 방이 활성화 상태가 같아서 순방향 길이어야 하는데 역방향 길인 경우 패스
            if not cur_status ^ next_status and is_reverse: continue

            # 다음 방에 도착하는데 걸리는 총 시간
            cost = total_time + weight
            # 현재 답보다 클 경우 더 이상 탐색할 필요 없음
            if cost >= answer:
                continue
            # 이동한 후의 트랩 상태로 다음 방에 간적이 없거나, 더 적은 시간으로 갈 수 있을 경우 distance 업데이트
            if (new_trap_status not in distance[next_room]) or (distance[next_room][new_trap_status] > cost):
                distance[next_room][new_trap_status] = cost
                # end에 도착한 경우 answer 업데이트
                if next_room == end:
                    answer = min(answer, cost)
                else:
                    heappush(q, (cost, next_room, new_trap_status))

    return answer
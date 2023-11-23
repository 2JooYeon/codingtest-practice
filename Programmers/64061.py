'''stack을 이용한 풀이'''
def solution(board, moves):
    answer = 0
    # 바구니
    basket = []
    graph = []
    n = len(board)
    # board를 열 단위로 스택으로 재생성
    for j in range(n):
        stack = []
        for i in range(n - 1, -1, -1):
            doll = board[i][j]
            if doll == 0:
                break
            stack.append(doll)
        graph.append(stack)

    for move in moves:
        move -= 1
        # 크레인이 집을 인형이 있다면
        if graph[move]:
            doll = graph[move].pop()
            # 집은 인형과 바구니의 맨 위에 있는 인형이 같으면 인형을 터트린다.
            if basket and basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)

    return answer

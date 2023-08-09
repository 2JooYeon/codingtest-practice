def solution(key, lock):
    # 시계 방향으로 90도 회전하는 함수
    def rotate90(arr):
        rot_arr = []
        m = len(arr)
        for i in range(m):
            row = []
            for j in range(m - 1, -1, -1):
                row.append(arr[j][i])
            rot_arr.append(row)
        return rot_arr

    # 자물쇠가 열렸는지 확인하는 함수
    def is_unlock(ex_lock, m, n):
        for i in range(n):
            if 0 in ex_lock[m - 1 + i][m - 1:m - 1 + n]:
                return False
        return True

    # 모든 경우의 수를 탐색하기 위해 자물쇠 배열을 확장하는 함수
    def make_ex_lock(lock, m, n):
        ex_lock = [[0 for _ in range(n + 2 * (m - 1))] for _ in range(n + 2 * (m - 1))]
        for i in range(n):
            for j in range(n):
                ex_lock[m - 1 + i][m - 1 + j] = lock[i][j]
        return ex_lock

    m = len(key)
    n = len(lock)

    for _ in range(4):
        key = rotate90(key)
        # 확장된 자물쇠의 왼쪽 위부터 오른쪽 아래까지 반복
        for i in range((n + 2 * (m - 1)) - m + 1):
            for j in range((n + 2 * (m - 1)) - m + 1):
                ex_lock = make_ex_lock(lock, m, n)
                # 자물쇠와 열쇠 XOR 연산 진행
                for k in range(m):
                    for h in range(m):
                        ex_lock[i + k][j + h] ^= key[k][h]
                if is_unlock(ex_lock, m, n):
                    return True

    return False

'''로그와 이분탐색을 이용한 풀이'''
import math

def solution(numbers):
    answer = []
    # 이분 탐색하는 함수, 부모 노드가 0인데 자식 노드가 1인 경우 0을 반환
    def check(start, end):
        if start == end:
            return 1
        mid = (start + end) // 2
        # 부모 노드가 0인 경우
        if bin_num[mid] == '0':
            # 왼쪽 자식 노드에 1이 있으면 0 반환
            for i in range(start, mid):
                if bin_num[i] == '1':
                    return 0
            # 오른쪽 자식 노드에 1이 있으면 0 반환
            for i in range(start + 1, end + 1):
                if bin_num[i] == '1':
                    return 0

        left = check(start, mid - 1)
        right = check(mid + 1, end)
        return left and right

    for num in numbers:
        bin_num = bin(num)[2:]
        # 로그를 이용해서 포화 이진트리의 높이를 구한다.
        h = int(math.log(len(bin_num), 2) + 1)
        bin_num = '0' * ((2 ** h - 1) - len(bin_num)) + bin_num
        answer.append(check(0, len(bin_num) - 1))

    return answer

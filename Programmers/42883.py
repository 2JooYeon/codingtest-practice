def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        # stack[-1]의 값보다 현재 넣으려는 수가 더 크면 교체
        while len(stack) > 0 and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    # k 만큼 제거되지 않았다면 슬라이싱 처리
    if k > 0:
        stack = stack[:len(number) - k]
    return ''.join(stack)

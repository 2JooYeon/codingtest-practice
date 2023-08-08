def solution(s):
    answer = 0
    len_s = len(s)
    if len_s == 1: return 1

    len_str = []
    # 문자열의 절반 길이까지만을 반복단위로 확인
    for unit in range(1, (len_s//2)+1):
        count = 0
        temp = ''
        cur = 0
        while cur + unit <= len_s+1:
            prev = s[cur:cur+unit]
            cur += unit
            # 이전 문자(prev) 기준으로 다음 단위 문자가 같다면
            while cur + unit <= len_s+1 and prev == s[cur:cur+unit]:
                count += 1
                prev = s[cur:cur+unit]
                cur += unit
            if count > 0:
                temp += str(count+1)
                count = 0
            temp += prev
            if cur + unit > len_s+1:
                temp += s[cur:]
        # 가능한 모든 경우를 확인한 후
        len_str.append(len(temp))
    # 길이가 가장 짧은 압축 문자열의 길이만을 반환
    answer = min(len_str)
    return answer

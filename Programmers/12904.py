def solution(s):
    answer = 1
    len_s = len(s)
    for i in range(len_s):
        for j in range(i+2, len_s+1):
            word = s[i:j]
            if len(word) < answer:
                continue
            if word == word[::-1]:
                answer = max(answer, j-i)


    return answer

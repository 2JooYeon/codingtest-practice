from itertools import combinations


def check(data):
    a = set(['a', 'e', 'i', 'o', 'u'])
    temp = set(data) - a
    # 모음이 없는 경우
    if len(temp) == len(data):
        return False
    # 자음이 2개 미만인 경우
    if len(temp) < 2:
        return False
    return True


n, c = map(int, input().split())
words = input().split()
words.sort()
combi = combinations(words, n)
for word in combi:
    if check(word):
        word = list(word)
        print(''.join(word))

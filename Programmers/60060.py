from collections import defaultdict
from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    len_word = defaultdict(list)
    len_reversed_word = defaultdict(list)
    words.sort()

    # 단어를 뒤집어서 저장
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    reversed_words.sort()

    # {단어 길이: 단어}
    for word, reversed_word in zip(words, reversed_words):
        len_word[len(word)].append(word)
        len_reversed_word[len(reversed_word)].append(reversed_word)

    for query in queries:
        len_query = len(query)
        left, right = 0, 0
        # '?'가 접두사인 경우
        if query[0] == '?' and len_query in len_reversed_word:
            query = query[::-1]
            a_query = query.replace('?', 'a')
            z_query = query.replace('?', 'z')
            left = bisect_left(len_reversed_word[len_query], a_query)
            right = bisect_right(len_reversed_word[len_query], z_query)
        # '?'가 접미사인 경우
        elif len_query in len_word:
            a_query = query.replace('?', 'a')
            z_query = query.replace('?', 'z')
            left = bisect_left(len_word[len_query], a_query)
            right = bisect_right(len_word[len_query], z_query)
        answer.append(right - left)

    return answer

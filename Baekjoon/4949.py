import sys
input = sys.stdin.readline

def check_str():
    stack = []
    for c in sentence:
        if c == '(':
            stack.append(c)
        if c == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if c == '[':
            stack.append(c)
        if c == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True


while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    sentence = list(sentence)
    if check_str():
        print('yes')
    else:
        print('no')
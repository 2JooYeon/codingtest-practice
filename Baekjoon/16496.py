from functools import cmp_to_key

# 정렬 key로 넣어줄 함수
def cmp(x, y):
    # 큰 수가 앞으로 오기 위해 -1
    if int(x+y) > int(y+x):
        return -1
    else:
        return 1

n = int(input())
arr = input().split()
arr.sort(key=cmp_to_key(cmp))
if sum(map(int, arr)) == 0:
    print(0)
else:
    print(''.join(map(str, arr)))
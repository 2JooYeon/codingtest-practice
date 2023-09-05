def check_palindrome(i, j, status):
    while i<=j:
        if word[i] == word[j]:
            i+=1
            j-=1
        else:
            # 아직 한 문자도 삭제하지 않았다면
            if status == 0:
                left = check_palindrome(i+1, j, status+1)
                right = check_palindrome(i, j-1, status+1)
                return min(left, right)
            # 한 문자를 삭제했는데도 문자가 서로 다르다면 일반 문자열
            else:
                return 2
    return status


t = int(input())
for _ in range(t):
    word = input()
    print(check_palindrome(0, len(word)-1, 0))
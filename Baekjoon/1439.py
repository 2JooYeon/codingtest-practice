s = input().rstrip()
change = 0
target = s[0]
for c in s:
    if target != c:
        target = c
        change += 1
print((change+1)//2)

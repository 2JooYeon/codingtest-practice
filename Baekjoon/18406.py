n = list(map(int, input()))
i = len(n)//2
if sum(n[:i]) == sum(n[i:]):
    print("LUCKY")
else:
    print("READY")

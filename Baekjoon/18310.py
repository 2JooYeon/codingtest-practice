n = int(input())
home = list(map(int, input().split()))
home.sort()
if n % 2 == 0:
    x1 = n//2
    x2 = x1-1
    x1_distance = [abs(x-home[x1]) for x in home]
    x2_distance = [abs(x-home[x2]) for x in home]

    if x1_distance <= x2_distance:
        print(home[x1])
    else:
        print(home[x2])
else:
    print(home[n//2])

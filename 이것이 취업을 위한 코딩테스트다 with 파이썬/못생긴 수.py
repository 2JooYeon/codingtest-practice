n = int(input())
ugly_num = [0] * n
ugly_num[0] = 1
i2, i3, i5 = 0, 0, 0
two, three, five = 2, 3, 5
for i in range(1, n):
    ugly_num[i] = min(two, three, five)
    if ugly_num[i] == two:
        i2 += 1
        two = ugly_num[i2] * 2
    if ugly_num[i] == three:
        i3 += 1
        three = ugly_num[i3] * 3
    if ugly_num[i] == five:
        i5 += 1
        five = ugly_num[i5] * 5
print(ugly_num[n-1])
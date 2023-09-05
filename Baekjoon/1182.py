def back(i, interval_sum):
    if i >= n:
        return

    interval_sum += arr[i]

    if interval_sum == s:
        global count
        count += 1

    back(i+1, interval_sum)
    back(i+1, interval_sum-arr[i])


n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
back(0,0)
print(count)
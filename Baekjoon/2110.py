n, c = map(int, input().split())
home = []
answer = 0
for _ in range(n):
    home.append(int(input()))
home.sort()
# 공유기가 2개인 경우
if n==2:
    print(home[1]-home[0])

else:
    # start와 end는 공유기 사이의 거리 최소, 최대값을 의미
    start = 1
    end = home[-1] - home[0]

    while start<=end:
        # mid: 현재 공유기 사이의 거리값
        mid = (start+end)//2
        now = home[0]
        # 설치할 수 있는 공유기 개수
        router = 1
        for i in range(1, n):
            if home[i] >= now + mid:
                router += 1
                now = home[i]
        # 설치한 공유기 수가 c보다 크거나 같다면, 공유기 사이의 거리값을 증가
        if router >= c:
            start = mid+1
            answer = mid
        # 설치한 공유기 수가 c보다 작다면, 공유기 사이의 거리값을 감소
        else:
            end = mid-1

    print(answer)
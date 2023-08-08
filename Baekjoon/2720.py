t = int(input())
coins = [25, 10, 5, 1]
c = []
answers = []
for _ in range(t):
    c.append(int(input()))

for money in c:
    temp = []
    for i in range(4):
        temp.append(str(money // coins[i]))
        money %= coins[i]
    answers.append(temp)

for answer in answers:
    print(" ".join(answer))

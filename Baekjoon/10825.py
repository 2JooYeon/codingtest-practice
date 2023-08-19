n = int(input())
student = []
for _ in range(n):
    data = input().split()
    student.append([data[0], int(data[1]), int(data[2]), int(data[3])])

student.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(student[i][0])
# a가 97, h가 104
location = input()
col, row = ord(location[0])-97, int(location[1])-1
answer = 0

dl = [(-1, -2), (1, -2), (-1, 2), (1, 2),
      (-2, -1), (-2, 1), (2, -1), (2, 1)]

for dx, dy in dl:
    if row + dx < 0 or row + dx >= 8 or col + dy < 0 or col + dy >=8:
        continue
    answer += 1

print(answer)
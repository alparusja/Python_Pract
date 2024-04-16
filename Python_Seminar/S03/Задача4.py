list = [0, -1, 5, 2, 3]

count = 0
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        count += 1
print(count)    
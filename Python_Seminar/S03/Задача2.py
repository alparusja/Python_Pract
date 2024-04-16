list = [5, 4, 6, 7, -10]
k = int(input())
k = k % len(list)

list_res = []

for i in range(k):
    list_res.append(list[len(list) - 1 - i])
print(list_res)

for i in range(len(list) - k):
    list_res.append(list[i])
print(list_res)
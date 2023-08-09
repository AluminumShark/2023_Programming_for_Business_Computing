n = int(input())
x = list(map(int, input().split(",")))
y = list(map(int, input().split(",")))

dis_m = 9999999999999
min = 0
list_1 = list()
output_str = str()

for i in range(1, n + 1) :
    dis = (x[0] - x[i]) ** 2 + (y[0] - y[i]) ** 2
    if dis < dis_m :
        dis_m = dis

for j in range(1, n + 1) :
    dis_2 = (x[0] - x[j]) ** 2 + (y[0] - y[j]) ** 2
    if dis_2 == dis_m :
        list_1.append(j)

for k in range(len(list_1)) :
    if k == len(list_1) - 1 :
        output_str += str(list_1[k])
    else :
        output_str += str(list_1[k]) + ","

print(output_str)
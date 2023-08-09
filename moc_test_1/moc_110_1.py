x_0 = int(input())
y_0 = int(input())
x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

dis_01 = (x_0 - x_1) ** 2 + (y_0 - y_1) ** 2
dis_02 = (x_0 - x_2) ** 2 + (y_0 - y_2) ** 2
output = int()

if dis_01 == dis_02 :
    output = 0
elif dis_01 < dis_02 :
    output = 1
elif dis_01 > dis_02 :
    output = 2


print(output)
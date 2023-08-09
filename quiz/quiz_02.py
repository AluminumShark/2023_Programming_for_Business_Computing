n = int(input())
list_xn = list(map(int, input().split(",")))
x0 = list_xn[0]
output = 0

for i in range(len(list_xn)) :
    if list_xn[i] == x0 :
        continue
    elif (list_xn[i] % x0) == 0 :
        break
    else :
        output = 1

for j in range(len(list_xn)) :
    if list_xn[j] == x0 :
        continue
    if (list_xn[i] % x0) == 0 :
        output = 2

if output == 2 :
    for k in range(len(list_xn)) :
        if (list_xn[k] % x0) == 0 :
            output = 3
        else :
            output = 2
            break

r = 0
if output == 2 :
    for l in range(len(list_xn)) :
        if list_xn[l] == x0 :
            continue
        if (list_xn[l] % x0) == 0 :
            r += 1
        if r > 1 :
            output = 4
            break



print(output)
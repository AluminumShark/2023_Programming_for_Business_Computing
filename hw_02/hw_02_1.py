days = int(input())
red_t = 0
for i in range(1, (days + 1)) :
    red_m = int(input())
    red_t += red_m
    if red_t < 0 :
        print(i)
        break
    else :
        continue
if red_t >= 0 :
    print(red_t)
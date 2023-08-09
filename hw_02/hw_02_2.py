com = int(input())
pine_t = 0
egg_t = 0

for i in range(1, (com + 1)) :
    box = int(input())
    pine = (i + 2) * box
    egg = i * box
    pine_t += pine
    egg_t += egg

pine_s = int(input())
egg_s = int(input())

s_1 = (pine_t // pine_s) + int(bool(pine_t % pine_s))
s_2 = (egg_t // egg_s) + int(bool(egg_t % egg_s))

print(pine_t, egg_t, s_1, s_2 ,sep = ",")
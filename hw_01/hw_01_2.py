bird = int(input())
trad = int(input())
#兩種禮盒的數量
egg_s1 = int(input())
pine_s1 = int(input())
#第一類員工可以做幾個蛋黃酥跟鳳梨酥
p_1 = int(input())
p_2 = int(input())
#兩類員工的薪水

egg = bird * 2 + trad * 3
pine = bird * 4 + trad * 3
#蛋黃酥跟鳳梨酥的數量

sta_1_e = egg // egg_s1
sta_1_p = pine // pine_s1
#第一類員工做兩種糕點的人數

sta_2 = 0
if ((egg % egg_s1) != 0) and ((pine % pine_s1) != 0) :
    if ((egg % egg_s1) * pine_s1 + (pine % pine_s1) * egg_s1) <= egg_s1 * pine_s1 :
        sta_2 = 1
    else :
        sta_1_e += 1
        sta_1_p += 1
elif (egg % egg_s1) != 0 :
    sta_1_e += 1
elif (pine % pine_s1) != 0 :
    sta_1_p += 1
#第二類員工的人數

p_t = (p_1 * (sta_1_e + sta_1_p)) + (p_2 * sta_2)
#總薪水

print(egg, pine, sta_1_e, sta_1_p, sta_2, p_t , sep = ",")
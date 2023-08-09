days = int(input())
#未來有幾天
box_plus = int(input())
#每天增加幾盒
bird = int(input())
trad = int(input())
#第一天兩種禮盒數量
pine_s = int(input())
egg_s = int(input())
#每位員工能做幾個鳳梨酥、蛋黃酥

for i in range(1, (days + 1)) :
    bird_t = bird + (i - 1) * box_plus
    trad_t = trad + (i - 1) * box_plus
    #每天兩種禮盒的數量
    pine = (4 * bird_t) + (3 * trad_t)
    egg = (2 * bird_t) + (3 * trad_t)
    #每天兩種糕點的數量
    staff_p = (pine // pine_s) + int(bool(pine % pine_s))
    staff_e = (egg // egg_s) + int(bool(egg % egg_s))
    #每天聘請做兩種糕點的員工數

    print(staff_p, staff_e, sep = ",")
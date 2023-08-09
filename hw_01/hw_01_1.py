bird = int(input())
trad = int(input())
#兩種禮盒的數量

egg = bird * 2 + trad * 3
pine = bird * 4 + trad * 3
#蛋黃酥跟鳳梨酥的數量

egg_s = int(input())
pine_s = int(input())
#一個員工可以做幾個蛋黃酥跟鳳梨酥

if (egg / egg_s) > (egg // egg_s) :
    sta_e = (egg // egg_s) + 1
else :
    sta_e = egg // egg_s
#蛋黃酥的人力

if (pine / pine_s) > (pine // pine_s) :
    sta_p = (pine // pine_s) + 1
else :
    sta_p = pine // pine_s
#鳳梨酥的人力

print(egg, pine, sta_e, sta_p, sep = ",")
x_1 = int(input())
x_2 = int(input())
y_1 = int(input())
y_2 = int(input())
p_1 = int(input())
p_2 = int(input())
r_1 = int(input())
r_2 = int(input())

egg = (2 * x_1) + (3 * x_2)
pine = (4 * x_1) + (3 * x_2)
#製作兩種糕點的個數

staf_1e = egg // y_1
staf_1p = pine // y_2
#聘請第一類員工製作兩種糕點的人數

egg_re = egg % y_1
pine_re = pine % y_2
#扣除第一類員工能整除之糕點剩餘個數

staf_2 = 0
staf_3e = 0
staf_3p = 0
min_salary = 2147483647
egg_rm = int(egg_re > 0)
pine_rm = int(pine_re > 0)
#first class & neightbor
first_class = p_1 * (egg_rm + pine_rm)
if first_class < min_salary:
    min_salary = 
neightbor1 = p_1 * egg_rm  + r_2 * pine_re
min_salary = min(neightbor1, min_salary)
neight

#第二類員工人數及鄰居代工數量
if egg_re != 0 and pine_re == 0 :
    #被第一類員工整除過後蛋黃酥有剩的情況
    if (egg_re * r_1) < p_1 :
        staf_3e += egg_re
    else :
        staf_1e += 1
elif egg_re == 0 and pine_re != 0 :
    #被第一類員工整除過後鳳梨酥有剩的情況
    if (pine_re * r_2) < p_1 :
        staf_3p += pine_re
    else :
        staf_1p += 1
elif egg_re != 0 and pine_re != 0 :
    if (egg_re * y_2) + (pine_re * y_1) <= y_1 * y_2 :
        #第二類員工做的完的情況
        if (p_2 < (p_1 + (r_1 * egg_re))) and (p_2 < (p_1 + (r_2 * pine_re))) and (p_2 < ((r_1 * egg_re) + (r_2 * pine_re))) :
            #第二類員工做比較便宜
            staf_2 += 1
        elif (p_2 > (p_1 + (r_1 * egg_re))) and ((r_1 * egg_re) + (r_2 * pine_re)) > (p_1 + (r_1 * egg_re)) and (p_1 + (r_2 * pine_re)) > (p_1 + (r_1 * egg_re)) :
            #鄰居做蛋黃酥，第一類員工做鳳梨酥比較便宜
            staf_3e += egg_re
            staf_1p += 1
        elif (p_2 > (p_1 + (r_2 * pine_re))) and ((r_1 *egg_re) + (r_2 * pine_re)) > (p_1 + (r_2 * pine_re)) and (p_1 + (r_1 * egg_re)) > (p_1 + (r_2 * pine_re)) :
            #鄰居做鳳梨酥，第一類員工做蛋黃酥比較便宜
            staf_3p += pine_re
            staf_1p += 1
        else :
            #都鄰居做比較便宜
            staf_3e += egg_re
            staf_3p += pine_re
    else :
        #第二類員工做不完的情況
        if ((egg_re * r_1) < p_1) and ((pine_re * r_2) > p_1) :
            #鄰居做蛋黃酥，第一類員工做鳳梨酥比較便宜
            staf_3e += egg_re
            staf_1p += 1
        elif ((egg_re * r_1) > p_2) and ((pine_re * r_2) < p_1) :
            #鄰居做鳳梨酥，第一類員工做蛋黃酥比較便宜
            staf_3p += pine_re
            staf_1e += 1
        elif ((egg_re * r_1) > p_1) and ((pine_re * r_2) > p_1) :
            #都第一類員工做比較便宜
            staf_1e += 1
            staf_1p += 1
        else :
            #都鄰居做比較便宜
            staf_3e += egg_re
            staf_3p += pine_re
 
p_t = (p_1 * (staf_1e + staf_1p)) + (p_2 * staf_2) + ((r_1 * staf_3e) + (r_2 * staf_3p))
#薪水總額

print(egg, pine, p_t, sep = ",")
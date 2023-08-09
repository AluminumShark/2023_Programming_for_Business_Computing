box_days_work1_work2 = input().split(",") #禮盒數、天數、相同的時間每位員工可做之鳳梨酥與蛋黃酥
pine_box = input().split(",") #每種禮盒有幾個鳳梨酥
egg_box = input().split(",") #每種禮盒有幾個蛋黃酥
pine_day = list() #每天個別要做幾個鳳梨酥
egg_day = list() #每天個別要做幾個蛋黃酥
employ = list() #每天個別要請幾個員工
output_str = str() #把list轉成輸出格式

for i in range(len(box_days_work1_work2)) :
    box_days_work1_work2[i] = int(box_days_work1_work2[i])
for j in range(len(pine_box)) :
    pine_box[j] = int(pine_box[j])
    egg_box[j] = int(egg_box[j]) #將各個list內的element轉成interger

box = box_days_work1_work2[0]
days = box_days_work1_work2[1]
work_1 = box_days_work1_work2[2]
work_2 = box_days_work1_work2[3] #將禮盒數、天數、員工可做蛋黃酥鳳梨酥之變數簡化

for l in range(0, box) : #在每一盒的情況
    demand = input().split(",") #輸入一種禮盒對應每天的需求量
    for m in range(0, days) :
        demand[m] = int(demand[m]) #將list內的element轉成interger
    pine_list = list()
    egg_list = list()
    for n in range(len(demand)) : #對於一種禮盒每一天會有幾個鳳梨酥、鳳梨酥
        pine_list.append(demand[n] * pine_box[l])
        egg_list.append(demand[n] * egg_box[l])
    if l == 0 : #將第一輪結果assign給pine_day、egg_day
        pine_day = pine_list 
        egg_day = egg_list
    else : #將其他輪結果加上pine_day、egg_day
        for o in range(0, days) :
            pine_day[o] += pine_list[o]
            egg_day[o] += egg_list[o]

for p in range(0, days) : #算出員工數
    employ_t = (pine_day[p] // work_1) + (egg_day[p] // work_2) + bool(pine_day[p] % work_1) + bool(egg_day[p] % work_2)
    employ.append(employ_t)

for q in range(len(employ)) : #將員工數轉為輸出格式
    if (q + 1) == len(employ) :
        output_str += str(employ[q])
    else :
        output_str += (str(employ[q]) + ",")

print(output_str)
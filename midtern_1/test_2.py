clas, rate = map(int, input().split(","))
member = list(map(int, input().split(",")))
tien = list(map(int, input().split(",")))

pas = list()

for i in range(clas) :
    score = list(map(int, input().split(",")))
    if (tien[i] / member[i]) * 100 >= rate :
        score_n = 0
        for j in range(len(score)) :
            score_n += score[j]
        pas.append([i , member[i] , score_n])

out_list = [[0, 0, 0]]
socre_e = 0
out_str = str()

for k in range(len(pas)) :
    if pas[k][2] / tien[pas[k][0]] > socre_e :
        socre_e = pas[k][2] / tien[pas[k][0]]
        out_list.pop(0)
        out_list.append(pas[k])

out_list[0][0] += 1

for l in range(len(out_list[0])) :
    if out_list[0][l] == out_list[0][-1] :
        out_str += str(out_list[0][l])
    else :
        out_str += str(out_list[0][l]) + ","

if out_list[0][0] == 0 :
    print(-1)
else :
    print(out_str)
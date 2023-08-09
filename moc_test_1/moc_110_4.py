job = int(input())
pt = list(map(int, input().split(",")))
dl = list(map(int, input().split(",")))

list_1 = list()

for i in range(job) :
    list_1.append([pt[i], dl[i]])

sor_list = sorted(list_1, key = lambda x : x[1])

per_list = list()
rem_list = list()
sum = 0

for i in range(job) :
    if sum + sor_list[i][0] > sor_list[i][1] :
        rem_list.append(dl.index(sor_list[i][1]))
    else :
        per_list.append(dl.index(sor_list[i][1]))
        sum += sor_list[i][0]


output_list = per_list + rem_list 
output_str = str()

for j in range(len(output_list)) :
    if output_list[j] == output_list[-1] :
        output_str += str(output_list[j] + 1)
    else :    
        output_str += str(output_list[j] + 1) + ","

#output_str += ";" + str(len(rem_list))

#print(output_str)

print(f"{output_str};{len(rem_list)}")
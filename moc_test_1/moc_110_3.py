cata_n, obj, c0 = map(int, input().split(","))
posi = list(map(int, input().split(",")))
cata_i = list(map(int, input().split(",")))
list_c0 = list()

for i in range(obj) :
    if cata_i[i] == c0 :
        list_c0.append(posi[i])

list_c0.sort(reverse = True)
output_list = list_c0[0:3]

if len(output_list) == 1 :
    output_list.append(-1)
    output_list.append(-1)
elif len(output_list) == 2 :
    output_list.append(-1)

output_str = str()

for j in range(len(output_list)) :
    if j == len(output_list) - 1 :
        output_str += str(output_list[j])
    else :
        output_str += str(output_list[j]) + ","

print(output_str)
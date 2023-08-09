stat = int(input())
capa = int(input())
member = list(map(int, input().split(",")))

out_list = list()

while True :
    capa_n = capa
    bus_n = list()
    for i in range(len(member)) :
        if member[i] == 0 :
            continue
        elif member[i] >= capa_n :
            bus_n.append([i + 1, capa_n])
            member[i] -= capa_n
            capa_n = 0
            break
        elif member[i] < capa_n :
            bus_n.append([i + 1, member[i]])
            capa_n -= member[i]
            member[i] = 0
    out_list.append(bus_n)
    if member == [0] * len(member) :
        break

for j in range(len(out_list)) :
    out_str = str()
    for k in range(len(out_list[j])) :
        if out_list[j][k] == out_list[j][-1] :
            out_str += str(out_list[j][k][0]) + "," + str(out_list[j][k][1])
        else :
            out_str += str(out_list[j][k][0]) + "," + str(out_list[j][k][1]) + ";"
    print(out_str)
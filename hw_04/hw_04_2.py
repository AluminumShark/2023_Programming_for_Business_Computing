num = int(input())
asse = list(map(int, input().split(",")))
pac = list(map(int, input().split(",")))
t_list = list()

for i in range(num) :
    t_list.append([i + 1 ,asse[i], pac[i]])

t_list.sort(key = lambda x: (x[2] + x[1], x[1], x[0]) )

mac_a = 0
mac_p = 0
rest = 0

for j in range(num + 1) :
    if j == 0 :
        mac_a += t_list[j][1]
        mac_p += t_list[j][1]
        rest += t_list[j][1]
    elif j == num :
        mac_p += t_list[j - 1][2]
        t_list[j - 1].append(mac_p)
    elif (mac_a + t_list[j][1]) >= (mac_p + t_list[j - 1][2]) :
        mac_a += t_list[j][1]
        mac_p += t_list[j - 1][2]
        rest += mac_a - mac_p
        t_list[j - 1].append(mac_p)
        mac_p += mac_a - mac_p
    else :
        mac_a += t_list[j][1]
        mac_p += t_list[j - 1][2]
        t_list[j - 1].append(mac_p)

t_list.sort(key = lambda x : x[0])

out_str = str()

for k in range(len(t_list)) :
    out_str += str(t_list[k][3]) + ","

print(f"{out_str}{rest}")
num = int(input())
asse = list(map(int, input().split(",")))
pac = list(map(int, input().split(",")))

mac_a = 0
mac_p = 0
rest = 0
out_list = list()
asse.append(0)

for i in range(num + 1) :
    if i == 0 :
        mac_a += asse[i]
        mac_p += asse[i]
        rest += asse[i]
    elif i == num :
        mac_a += asse[i]
        mac_p += pac[i - 1]
        out_list.append(mac_p)
    elif mac_a + asse[i] >= mac_p + pac[i - 1] :
        mac_a += asse[i]
        mac_p += pac[i - 1]
        rest += mac_a - mac_p
        out_list.append(mac_p)
        mac_p +=  mac_a - mac_p
    elif mac_a + asse[i] < mac_p + pac[i - 1] :
        mac_a += asse[i]
        mac_p += pac[i - 1]
        out_list.append(mac_p)

out_str = str()
for j in range(len(out_list)) :
    out_str += str(out_list[j]) + ","

print(f"{out_str}{rest}")
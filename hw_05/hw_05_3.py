n_node = int(input())
a_list = []

while True :
    app = input()
    if app == "STOP" :
        break
    else :
        app = list(map(int, app.split(",")))
        a_list.append(app)

def mat(a, n) :
    a_mat = []
    test = 0
    for i in range(len(a)) :
        maxi = max(a[i])
        if maxi > test :
            test = maxi
    if n == 0 :
        n = test + 1
    else :
        if n < test + 1 :
            return
    for j in range(n) :
        a_mat.append([0] * n)
    for k in range(len(a)) :
        x = a[k][0]
        y = a[k][1]
        a_mat[x][y] = 1
        a_mat[y][x] = 1
    return a_mat

out_list = mat(a_list, n_node)

if out_list == None :
    print(out_list)
else :
    for l in range(len(out_list)) :
        out_str = str()
        for m in range(len(out_list[l])) :
            if m == len(out_list[l]) - 1 :
                out_str += str(out_list[l][m])
            else :
                out_str += str(out_list[l][m]) + ","
        print(out_str)
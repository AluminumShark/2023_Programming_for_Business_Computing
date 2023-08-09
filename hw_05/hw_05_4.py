n_node = int(input())
kk = int(input())
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
    if n <= kk :
        return
    for j in range(n) :
        a_mat.append([0] * n)
    for k in range(len(a)) :
        x = a[k][0]
        y = a[k][1]
        a_mat[x][y] = 1
        a_mat[y][x] = 1

    out_list = [0] * 2
    for l in range(len(a_mat)) :
        if l == kk :
            continue
        else :
            count = 0
            for m in range(len(a_mat)) :
                if a_mat[l][m] == a_mat[l][l] :
                    continue
                elif a_mat[l][m] == a_mat[kk][m] :
                    count += 1
            if count > out_list[1] :
                out_list = [l, count]
    return out_list

xxx = mat(a_list, n_node)

if xxx == None :
    print(xxx)
else :
    print(xxx[0])
    print(xxx[1])

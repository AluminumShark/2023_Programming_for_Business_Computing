n, m = map(int,input().split(',')) # 有多少種玩具，有幾條生產線
times = [] # 每條生產線上每個玩具需要多少時間
for i in range(m):
    time = input().split(',')
    for i in range(n):
        time[i] = int(time[i])
    times.append(time) # 一條為一單位，裡面有n種玩具
    
totals = [] # 每個玩具總製作時間 (一維)
for i in range(n):
    total = 0
    for j in range(m):
        total += times[j][i]
    totals.append(total) 


order = [] # 為玩具排製作順序
unorder = list(range(n))
for i in range(n): 
    opt = unorder[0]
    for j in unorder:
        if totals[j] < totals[opt]:
            opt = j
        elif totals[j] == totals[opt]:
            for x in range(m): # 依序比較各生產線上的時間
                if times[x][j] < times[x][opt]:
                    opt = j
                    continue
                if x == m-1 and j < opt:
                    opt = j                
    order.append(opt)
    unorder.remove(opt)

 
line = [] # 每條生產線上每個玩具的完成時間
for i in range(m):
    line.append([])
    for j in range(n):
        line[i].append(0)

total_idletime = 0

for j in range(m):
    if j == 0:
        for i in range(n):
            if i == 0:
                line[j][order[i]] = times[j][order[i]]
            else:
                line[j][order[i]] = line[j][order[i-1]] + times[j][order[i]]
    else: 
        for i in range(n):
            line[j][order[i]] = max(line[j-1][order[i]], line[j][order[i-1]]) + times[j][order[i]]
            idletime = line[j-1][order[i]] - line[j][order[i-1]]
            if idletime > 0: 
                total_idletime += idletime


for i in range(n):
    print(line[m-1][i], end = ',')
print(total_idletime)
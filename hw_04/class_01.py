station_capacity = list(map(int, input().split(",")))
man = list(map(int, input().split(",")))
output = man.copy

for i in range(len(man)) :
    man[i] = int(man[i])

while any(element != 0 for element in man) :
    on_board = station_capacity[1]
    for j in range(len(man)) :
        if (on_board - man[j]) > 0:
            on_board -= man[j]
            man[j] = 0
        elif (on_board - man[j]) == 0 :
            man[j] = 0
            print(man)
            break
        else :
            man[j] = man[j] - on_board
            print(man)
            break
print(man)
point, capa = map(int, input().split(","))
member = list(map(int, input().split(",")))

car = 0
dist_t = 0
while True :
    car += 1
    capa_n = capa
    for i in range(point) :
        dist = list(map(int, input().split(",")))
        if capa_n >= member[i] :
            dist_t += dist[i]
            member[i] = 0
            capa_n -= member[i]
            continue
        else :
            dist_t += dist[0]
            break
    if member == [0] * point :
        break


print(f"{car},{dist_t}")
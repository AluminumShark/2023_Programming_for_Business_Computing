cata, ding, q, d = map(int, input().split(","))
price = list(map(int, input().split(",")))

money = 0

for i in range(ding) :
    quanti = list(map(int, input().split(",")))
    money_c = 0
    for j in range(len(price)) :
        money_c += price[j] * quanti[j]
    if money_c > q :
        if money_c - d >= q :
                money_c -= d
        else :
            money_c = q
    money += money_c

print(money)
        
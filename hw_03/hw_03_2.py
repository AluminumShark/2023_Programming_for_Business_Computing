day_m_dollar = input().split(",")
lower = input().split(",")
upper = input().split(",")
price = input().split(",")

for i in range(len(day_m_dollar)):
    day_m_dollar[i] = int(day_m_dollar[i])
for j in range(len(lower)) :
    lower[j] = int(lower[j])
for k in range(len(upper)) :
    upper[k] = int(upper[k])
for l in range(len(price)) :
    price[l] = int(price[l])

money_after = 0

for m in range(len(lower)) :
    money = day_m_dollar[-1]
    stock = 0
    for n in range(len(price)) :
        if (n + 1) == day_m_dollar[0] :
            money += stock * price[-1]
        elif price[n] <= lower[m] :
            spend_m = int(0.5 * money)
            money -= spend_m
            stock += spend_m // price[n]
            money += spend_m % price[n]
        elif price[n] >= upper[m] :
            spend_s = int(0.5 * stock)
            stock -= spend_s
            money += spend_s * price[n]
    if money > money_after :
        money_after = money

print(money_after)
days_dollar = input().split(",")
stock_price = input().split(",")
lower_upper = input().split(",")
stocks = 0

for i in range(len(days_dollar)) :
    days_dollar[i] = int(days_dollar[i])
for j in range(len(stock_price)) :
    stock_price[j] = int(stock_price[j])
for k in range(len(lower_upper)) :
    lower_upper[k] = int(lower_upper[k])

for l in range(len(stock_price)) :
    if (l + 1) == days_dollar[0] :
        days_dollar[-1] += (stocks * stock_price[-1])
        stocks = 0
    elif stock_price[l] <= lower_upper[0] :
        spend_m = int(0.5 * days_dollar[-1])
        stocks += spend_m // stock_price[l]
        days_dollar[-1] -= spend_m
        days_dollar[-1] += spend_m % stock_price[l]
    elif stock_price[l] >= lower_upper[-1] :
        spend_s = int(0.5 * stocks)
        days_dollar[-1] += spend_s * stock_price[l]
        stocks -= spend_s


print(days_dollar[-1])
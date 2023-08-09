goods = []
while True :
    goods_row = input()
    if goods_row == "RECORDSTOP" :
        break
    else :
        goods.append(goods_row)

out_put = []
for i in range(len(goods)) :
    if "折扣" not in goods[i] and "點數" not in goods[i] :
        goods_row = goods[i].split("_")
        if float(goods_row[2]) > 0 :
            price = float(goods_row[2]) / float(goods_row[1])
            price = round(price, 1)
            goods_row = [goods_row[0], price]
            out_put.append(goods_row)

out_put.sort(key=lambda x : x[1], reverse=True)

for i in range(len(out_put)) :
    out_put[i][1] = format(out_put[i][1], ".2f")
    print(" ".join(out_put[i]))
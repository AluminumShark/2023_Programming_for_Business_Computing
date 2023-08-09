test_data = list(map(float, input().split(",")))

def autocor_2(ds) :
    alist = ds[ : len(ds) - 2]
    blist = ds[2 : ]
    mean_a = sum(alist) / len(alist)
    mean_b = sum(blist) / len(blist)
    var_a = 0
    var_b = 0
    cov_ab = 0
    for i in range(len(alist)) :
        var_a += (alist[i] - mean_a) ** 2
        var_b += (blist[i] - mean_b) ** 2
        cov_ab += (alist[i] - mean_a) * (blist[i] - mean_b)
    for j in [var_a, var_b, cov_ab] :
        j /= (len(alist) - 1 )
    cor_gx = cov_ab / ((var_a * var_b) ** 0.5)
    if abs(cor_gx) < 0.000001 :
        return 0
    else :
        cor_gx = round(cor_gx, 4)
        cor_gx = format(cor_gx, ".4f")
        return cor_gx
    
out_put = autocor_2(test_data)

print(out_put)
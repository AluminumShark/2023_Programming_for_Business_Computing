a = list(map(float, input().split(",")))
b = int(input())

def troughs(inlist, k = 2) :
    if k < 1 :
        k = 2
    num = list()
    for i in range(k, len(inlist) - k) :
        if inlist[i - k : i + 1] == sorted(inlist[i - k : i + 1], reverse = True) \
                and inlist[i : i + k + 1] == sorted(inlist[i : i + k + 1])\
                    and inlist[i - k] > inlist[i - k - 1]\
                        and inlist[i + k] > inlist[i + k + 1]:
                num.append(i)
    return num

if troughs(a, b) != [] :
    for j in range(len(troughs(a, b))) :
        print(troughs(a, b)[j])
else :
    print("NA")
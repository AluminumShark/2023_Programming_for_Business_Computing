a = list(map(float, input().split(",")))
b = int(input())

def dupl(alist) :
    return len(alist) != len(set(alist))

def troughs(inlist, k = 2) :
    num = list()
    for i in range(k, len(inlist) - k) :
        if dupl(inlist[i - k : i + 1]) == True or dupl(inlist[i : i + k + 1]) == True :
             continue
        elif inlist[i - k : i + 1] == sorted(inlist[i - k : i + 1], reverse = True) \
                and inlist[i : i + k + 1] == sorted(inlist[i : i + k + 1]):
                num.append(i)
    return num

if b < 1 :
     c = troughs(a)
else :
    c = troughs(a, b)


if c != [] :
    for j in range(len(c)) :
        print(c[j])
else :
    print("NA")
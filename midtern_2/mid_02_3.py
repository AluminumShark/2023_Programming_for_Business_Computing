fraction = input()

fraction = fraction.replace("+", "X")
fraction = fraction.replace("/", "X")
fraction = fraction.split("X")

def simp_change(num) :
    num = num.replace("0", "零")
    num = num.replace("1", "一")
    num = num.replace("2", "二")
    num = num.replace("3", "三")
    num = num.replace("4", "四")
    num = num.replace("5", "五")
    num = num.replace("6", "六")
    num = num.replace("7", "七")
    num = num.replace("8", "八")
    num = num.replace("9", "九")
    return num

def comp_change(num) :
    ten_dg = num[0]
    dg = num[1]
    ten_dg = simp_change(ten_dg)
    dg = simp_change(dg)
    if ten_dg == "一" :
        ten_dg = "十"
        num = f"{ten_dg}{dg}"
    else :
        num = f"{ten_dg}十{dg}"
    return num

def dg(num) :
    if len(num) == 2 :
        num = comp_change(num)
        return num
    elif len(num) == 1 :
        num = simp_change(num)
        return num

out_str = str()
if len(fraction) == 3 :
    a = dg(fraction[0])
    b = dg(fraction[1])
    c = dg(fraction[2])
    out_str = f"{a}又{c}分之{b}"
elif len(fraction) == 2 :
    b = dg(fraction[0])
    c = dg(fraction[1])
    out_str = f"{c}分之{b}"

print(out_str)

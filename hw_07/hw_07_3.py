import datetime as dt

finding = input()

formats = [
    "%Y-%m-%d",
    "%Y-%m-%dT%H",
    "%Y-%m-%dT%H:%M",
    "%Y-%m-%dT%H:%M:%S",
    "T%H",
    "T%H:%M",
    "T%H:%M:%S",
    ]

for i in formats :
    try :
        finding_dt = dt.datetime.strptime(finding, i)
        final_format = i
        finding_dt = finding_dt.strftime(i)
        break
    except ValueError :
        pass

finding_dt = finding_dt.replace("-", ",")
finding_dt = finding_dt.replace("T", ",")
finding_dt = finding_dt.replace(":", ",")
finding_list = finding_dt.split(",")


while "" in finding_list :
    index = finding_list.index("")
    finding_list.pop(index)

for i in range(len(finding_list)) :
    if len(finding_list[i]) != 4 :
        finding_list[i] = str(int(finding_list[i]))

def simple_change(num) :
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
    if len(num) == 2 :
        if num[0] == "1" :
            num = f"十{num[1]}"
        elif num[0] == "2" :
            num = f"二十{num[1]}"
        elif num[0] == "3" :
            num = f"三十{num[1]}"
        elif num[0] == "4" :
            num = f"四十{num[1]}"
        elif num[0] == "5" :
            num = f"五十{num[1]}"
        if "0" in num :
            num = num.replace("0", "")
    num = simple_change(num)
    return num

def year(yyyy) :
    if len(yyyy) == 1 :
        yyyy = f"000{yyyy}"
    elif len(yyyy) == 2 :
        yyyy = f"00{yyyy}"
    elif len(yyyy) == 3 :
        yyyy = f"0{yyyy}"
    yyyy = f"西元{simple_change(yyyy)}年"
    return yyyy

def month(mm) :
    mm = f"{comp_change(mm)}月"
    return mm

def day(dd) :
    dd = f"{comp_change(dd)}日"
    return dd

def hour(hh) :
    hh = int(hh)
    if hh > 12 :
        hh -= 12
        hh = str(hh)
        hh = f"下午{comp_change(hh)}點"
    elif hh < 12 :
        hh = str(hh)
        hh = f"上午{comp_change(hh)}點"
    elif hh == 12 :
        hh = str(hh)
        hh = f"下午{comp_change(hh)}點"
    if hh == "上午二點" or hh == "下午二點" :
        hh = hh.replace("二", "兩")
    return hh

def minute(mm) :
    mm = f"{comp_change(mm)}分"
    return mm

def second(ss) :
    ss = f"{comp_change(ss)}秒"
    return ss

if final_format == "%Y-%m-%d" :
    for i in range(len(finding_list)) :
        if i == 0 :
            finding_list[i] = year(finding_list[i])
        elif i == 1 :
            finding_list[i] = month(finding_list[i])
        elif i == 2 :
            finding_list[i] = day(finding_list[i])
elif final_format == "%Y-%m-%dT%H" :
    for i in range(len(finding_list)) :
        if i == 0 :
            finding_list[i] = year(finding_list[i])
        elif i == 1 :
            finding_list[i] = month(finding_list[i])
        elif i == 2 :
            finding_list[i] = day(finding_list[i])
        elif i == 3 :
            finding_list[i] = hour(finding_list[i])
elif final_format == "%Y-%m-%dT%H:%M" :
    for i in range(len(finding_list)) :
        if i == 0 :
            finding_list[i] = year(finding_list[i])
        elif i == 1 :
            finding_list[i] = month(finding_list[i])
        elif i == 2 :
            finding_list[i] = day(finding_list[i])
        elif i == 3 :
            finding_list[i] = hour(finding_list[i])
        elif i == 4 :
            finding_list[i] = minute(finding_list[i])
elif final_format == "%Y-%m-%dT%H:%M:%S" :
    for i in range(len(finding_list)) :
        if i == 0 :
            finding_list[i] = year(finding_list[i])
        elif i == 1 :
            finding_list[i] = month(finding_list[i])
        elif i == 2 :
            finding_list[i] = day(finding_list[i])
        elif i == 3 :
            finding_list[i] = hour(finding_list[i])
        elif i == 4 :
            finding_list[i] = minute(finding_list[i])
        elif i == 5 :
            finding_list[i] = second(finding_list[i])
elif final_format == "T%H" :
    finding_list[0] = hour(finding_list[0])
elif final_format == "T%H:%M" :
    for i in range(len(finding_list)) :
        if i == 0 :
            finding_list[i] = hour(finding_list[i])
        elif i == 1 :
            finding_list[i] = minute(finding_list[i])
elif final_format == "T%H:%M:%S" :
    for i in range(len(finding_list)) :
        if i == 0 :
            finding_list[i] = hour(finding_list[i])
        elif i == 1 :
            finding_list[i] = minute(finding_list[i])
        elif i == 2 :
            finding_list[i] = second(finding_list[i])


out_str = "".join(finding_list)

print(out_str)
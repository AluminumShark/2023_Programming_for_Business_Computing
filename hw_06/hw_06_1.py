str_1 = input()
str_2 = input()
dist = int(input())
docx = input()

def finding(former, later, dist, doc) :
    doc = doc.replace(former, "％")
    doc = doc.replace(later, "＃")
    flist = list()
    out_list = list()
    for i in range(len(doc)) :
        if doc[i] == "％" or doc[i] == "＃":
            flist.append(i)
    for j in range(len(flist)) :
        for k in range(len(flist)) :
            if j >= k or doc[flist[j]] == doc[flist[k]] :
                continue
            elif flist[k] - flist[j] <= dist :
                app = doc[flist[j] : flist[k] + 1]
                app = app.replace("％", former)
                app = app.replace("＃", later)
                out_list.append(app)
    return out_list

fin = finding(str_1, str_2, dist, docx)

if dist <= 0 or len(docx) > 10000 or dist > 10000 :
    print("ILLEGAL_INPUT")
elif fin == [] :
    print("^^NOT_FOUND^^")
else :
    for m in range(len(fin)) :
        print(fin[m])
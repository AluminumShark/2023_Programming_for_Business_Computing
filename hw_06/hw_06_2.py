docx = input()

def naruto(doc) :
    mark = "。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !\"#$%&'()*+,-./:;<=>?@[\]^_`{¦}~"
    index = list()
    doc_sep = list()
    for i in range(len(doc)) :
        if doc[i] in mark :
            index.append(i)
    start = 0
    for j in range(len(index)) :
        for k in range(len(doc)) :
            if index[j] == k :
                doc_sep.append(doc[start : index[j] + 1])
                start = index[j] + 1
                break
    doc = doc[start : ]
    if len(doc) != 0 :
        doc_sep.append(doc)
    doc_str = str()
    for k in range(len(doc_sep)) :
        if "大" in doc_sep[k] or "蛇" in doc_sep[k] or "丸" in doc_sep[k] :
            doc_str += "!".join(doc_sep[k][ : -1]) + doc_sep[k][-1]
#            for l in range(len(doc_sep[k])) :
#                if doc_sep[k][l] in mark :
#                    doc_str += doc_sep[k][l]
#                elif l < len(doc_sep[k]) - 1  and doc_sep[k][l + 1] in mark :
#                    doc_str += doc_sep[k][l]
#                else :
#                    doc_str += doc_sep[k][l] + "!"
#                    print(doc_str)
        else :
            doc_str += doc_sep[k]

    return doc_str

fin = naruto(docx)

print(fin)
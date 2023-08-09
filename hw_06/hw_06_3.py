docx = input()

def findnum(doc) :
    target = "0123456789.,%"
    #找出數字的index
    index = []
    for i in range(len(doc)):
        if doc[i] in target:
            index.append(i)
    #找出連號數字
    index_sor = []
    sor = []
    for j in range(len(index)):
        if j < len(index) - 1 and index[j] + 1 == index[j + 1]:
            sor.append(index[j])
        else:
            if sor == []:
                index_sor.append([index[j]])
            else:
                sor.append(index[j])
                index_sor.append(sor)
                sor = []
    #將數字和文字分開處理並做成字串
    out_str = ''
    for k in range(len(doc)) :
        #取出數字的index
        if k in index :
            for l in range(len(index_sor)):
                if k in index_sor[l]:
                    #處理單一數字
                    if len(index_sor[l]) == 1:
                        out_str += f'<<{doc[k]}>>'
                    #處理連號數字
                    else:
                        if k == index_sor[l][0]:
                            out_str += f'<<{doc[k]}'
                        elif k == index_sor[l][-1]:
                            out_str += f'{doc[k]}>>'
                        else:
                            out_str += doc[k]
        else:
            out_str += doc[k]
    return out_str

fin = findnum(docx)
print(fin)
docx = input()

find = "。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !\"#$%&'()*+,-./:;<=>?@[]^_`{¦}~"

line_list = []
with open(docx, "r", encoding = "UTF-8") as doc :
    while True :
        line = doc.readline()
        if not line :
            break
        else :
            line = line.strip("\n")
            line_list.append(line)
    doc.close()

line_list_len = []
for i in range(len(line_list)) :
    clean_str = str()
    for j in range(len(line_list[i])) :
        if line_list[i][j] not in find :
            clean_str += line_list[i][j]
    line_list_len.append(len(clean_str))


for i in range(len(line_list)) :
    line_list[i] = [line_list_len[i], line_list[i]]

line_list.sort(key=lambda x : x[0], reverse=True)

out_list = []
length = 0
count = 0
for i in range(len(line_list)) :
    if i == 0 :
        length = line_list[i][0]
        out_list.append(line_list[i])
    elif len(out_list) < 3 :
        if line_list[i][0] == length :
            out_list.append(line_list[i])
        elif line_list[i][0] < length :
            count += 1
            length = line_list[i][0]
            out_list.append(line_list[i])
    elif len(out_list) >= 3 and (line_list[i][0] == length) :
        out_list.append(line_list[i])
    else :
        break

for i in range(len(out_list)) :
    out_list[i] = f"{out_list[i][0]} {out_list[i][1]}"
    print(out_list[i])
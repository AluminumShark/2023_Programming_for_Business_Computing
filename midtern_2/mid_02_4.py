finding = input()
docx = input()

replacing = finding.count("?")
finding_list = finding.split("?")
finding_list = [x for x in finding_list if x != ""]

docx_list = []
for i in range(len(docx)) :
    if i + replacing - 1 <= len(docx) - 1 :
        docx_list.append(docx[i : i + replacing])

out_list = []
for i in range(len(docx_list)) :
    key_word = f"{finding_list[0]}{docx_list[i]}{finding_list[1]}"
    print(key_word)
    while key_word in docx :
        out_list.append(key_word)
        index = docx.find(key_word)
        docx = docx[index + 1 : ]

if out_list == [] :
    print("^^^NOT_FOUND^^^")
else :
    for i in range(len(out_list)) :
        print("out",out_list[i])

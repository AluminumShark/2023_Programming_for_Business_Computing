mapping_table = input()
finding = input()

mapping_table_list = []
with open(mapping_table, "r") as mapping_file :
    while True :
        line = mapping_file.readline()
        line = line.strip("\n")
        if not line :
            break
        else :
            mapping_table_list.append(line)
    mapping_file.close()

mapping_table_list = list(set(mapping_table_list))
for i in range(len(mapping_table_list)) :
    mapping_table_list[i] = mapping_table_list[i].split()

def mapping_function(data, find) :
    num = len(data)
    if "CNS" in find :
        mapping_dict = dict()
        find = find[4 : ]
        cns = []
        for j in range(len(data)) :
            cns.append(data[j][0])
        if len(set(cns)) != num :
            return ["MAPPING_TABLE_ERROR"]
        for k in range(len(data)) :
            mapping_dict[f"{data[k][0]}"] = f"0x{data[k][1]}"
        if find in mapping_dict :
            unicode = mapping_dict[find]
            unicode = chr(int(unicode, 16))
            return [num, unicode]
        else :
            return [num ,"NO_DATA_FOUND"]
    elif "CHAR" in find :
        find = find[5]
        mapping_list = []
        for l in range(len(data)) :
            data[l][1] = f"0x{data[l][1]}"
            data[l][1] = chr(int(data[l][1], 16))
        for m in range(len(data)) :
            if data[m][1] == find :
                mapping_list.append(data[m][0])
        mapping_list.sort()
        if mapping_list == [] :
            return [num, "NO_DATA_FOUND"]
        else :
            mapping_list.insert(0, num)
            return mapping_list
    
output = mapping_function(mapping_table_list, finding)

for n in range(len(output)) :
    print(output[n])
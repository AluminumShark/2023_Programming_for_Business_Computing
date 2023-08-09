mapping_allinone = input()
mapping_phonetic = input()
finding = input()

mapping_allinone_list = []
with open(mapping_allinone, "r") as allinone :
    while True :
        line = allinone.readline()
        line = line.strip("\n")
        if not line :
            break
        else :
            mapping_allinone_list.append(line)
    allinone.close()
mapping_allinone_list = list(set(mapping_allinone_list))
for i in range(len(mapping_allinone_list)) :
    mapping_allinone_list[i] = mapping_allinone_list[i].split()
for j in range(len(mapping_allinone_list)) :
    mapping_allinone_list[j][1] = f"0x{mapping_allinone_list[j][1]}"
    mapping_allinone_list[j][1] = chr(int(mapping_allinone_list[j][1], 16))

mapping_phonetic_list = []
with open(mapping_phonetic, "r") as phonetic :
    while True :
        line = phonetic.readline()
        line = line.strip()
        if not line :
            break
        else :
            mapping_phonetic_list.append(line)
    phonetic.close()
mapping_phonetic_list = list(set(mapping_phonetic_list))
for k in range(len(mapping_phonetic_list)) :
    mapping_phonetic_list[k] = mapping_phonetic_list[k].split()
mapping_phonetic_list.sort(key=lambda x : x[0])


def mapping(allinone, phonetic, find) :
    allinone_cns_count = []
    for l in range(len(allinone)) :
        allinone_cns_count.append(allinone[l][0])
    if len(allinone_cns_count) > len(set(allinone_cns_count)) :
        return ["MAPPING_TABLE_ERROR"]
    
    allinone_cns_list = []
    for m in range(len(allinone)) :
        if find == allinone[m][1] :
            allinone_cns_list.append(allinone[m][0])
    allinone_cns_list.sort()
    
    phonetic_num = []
    for n in range(len(phonetic)) :
        phonetic_num.append(phonetic[n][0])
    phonetic_num = len(set(phonetic_num))
    phonetic_list = []
    for o in range(len(allinone_cns_list)) :
        for p in range(len(phonetic)) :
            if allinone_cns_list[o] == phonetic[p][0] :
                if phonetic[p][1] not in phonetic_list :
                    phonetic_list.append(phonetic[p][1])
    phonetic_list.sort()
    
    if allinone_cns_list == [] :
        return [phonetic_num, "NO_CNS_DATA"]
    elif phonetic_list == [] :
        return [phonetic_num, "NO_PHONETIC_DATA"]
    else :
        phonetic_list.insert(0, phonetic_num)
        return phonetic_list

output = mapping(mapping_allinone_list, mapping_phonetic_list, finding)
for q in range(len(output)) :
    print(output[q])
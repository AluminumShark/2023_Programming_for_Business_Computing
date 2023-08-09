word = input()

last_name = "陳林黃張李王吳劉蔡楊許鄭謝郭洪曾邱廖賴周徐蘇葉莊呂\
    江何蕭羅高簡朱鍾施游詹沈彭胡余盧潘顏梁趙柯翁魏方孫戴范\
        宋鄧杜侯曹薛傅丁溫紀蔣歐藍連唐馬董石卓程姚康馮古姜湯\
            汪白田涂鄒巫尤鐘龔嚴韓黎阮袁童陸金錢邵"

name_list = []
for i in range(len(last_name)) :
    count = word.count(f"{last_name[i]}小姐")\
    + word.count(f"{last_name[i]}先生")\
    + word.count(f"{last_name[i]}姓")\
    + word.count(f"姓{last_name[i]}")
    if count != 0 :
        name_list.append([last_name[i], count])

name_list.sort(key=lambda x : (-x[1]))

for i in range(len(name_list)) :
    print(f"{name_list[i][0]}:{name_list[i][1]}")
import numpy as np
import pandas as pd
import pyreadstat
from sklearn.preprocessing import LabelEncoder

df_1, meta = pyreadstat.read_sav("fakedata.sav", encoding="big5",\
                            apply_value_formats = True)

df_1.to_csv("fakedata.csv", index = False, encoding="utf-8")

df_2 = pd.read_csv("fakedata.csv", encoding="utf-8")

def hav_havn(col):
    if col == "有":
        col = 1
    elif col == "沒有":
        col = 0
    else :
        col = None
    return col


df_2["fakenews1"] = df_2["fakenews1"].apply(hav_havn)

def freqency(col):
    if col == "從未" or col == "從未製造" or col == "從未散播":
        col = 0
    elif col == "偶而":
        col = 1
    elif col == "經常":
        col = 2
    elif col == "每天":
        col = 3
    else:
        col = None
    return col

df_2["fakenews2"] = df_2["fakenews2"].apply(freqency)


def serious(col) :
    if col == "一點也不嚴重":
        col = 0
    elif col == "不嚴重":
        col = 1
    elif col == "嚴重" :
        col = 2
    elif col == "非常嚴重":
        col = 3
    else :
        col = None
    return col

df_2["fakenews3"] = df_2["fakenews3"].apply(serious)

varlist1 = ["fnsce_press", "fnsce_politician",
            "fnsce_citizen", "fnsce_enemy", "fnsce_ngo",
            "fnsce_mag", "fnsce_tv", "fnsce_internet",
            "fnsce_mobile", "fnsce_nbr"]

for i in varlist1 :
    df_2[i] = df_2[i].apply(freqency)

def add(col) :
    if col == "減少":
        col = 0
    elif col == "沒有改變":
        col = 1
    elif col == "增加":
        col = 2
    else : 
        col = None
    return col

varlist2 = ["fndt_gov", "fndt_con", "fndt_dem", "fndt_pln", "fndt_press"]

for i in varlist2:
    df_2[i] = df_2[i].apply(add)

def yes_no(col):
    if col == "一點也不會":
        col = 0
    elif col == "不會":
        col = 1
    elif col == "會":
        col = 2
    elif col == "絕對會":
        col = 3
    else:
        col = None
    return col

varlist3 = ["fn_self", "fn_other"]

for i in varlist3 :
    df_2[i] = df_2[i].apply(yes_no)

varlist4 = ["fncheck_friend", "fncheck_book", "fncheck_expert",
            "fncheck_factcheck", "fnrespond1", "fnrespond_2",
            "fnrespond_3", "fnrespond_4"]

for i in varlist4:
    df_2[i] = df_2[i].apply(hav_havn)

def need(col):
    if col == "一點都不需要":
        col = 0
    elif col == "不太需要":
        col = 1
    elif col == "有點需要":
        col = 2
    elif col == "非常需要":
        col = 3
    else :
        col = None
    return col

df_2["fn_edu"] = df_2["fn_edu"].apply(need)

def truth(col):
    if col == "事實陳述":
        col = 1
    elif col == "意見陳述":
        col = 0
    else:
        col = None
    return col

varlist5 = ["v_o_1", "v_o_2", "v_o_3", "v_o_4", "v_o_5", "v_o_6"]

for i in varlist5:
    df_2[i] = df_2[i].apply(truth)

def know(col):
    if col == "知道" or col == "知道 (回答Q16a)":
        col = 1
    elif col == "不知道" or col == "不知道 (進入Q17)":
        col = 0
    else:
        col = None
    return col

df_2["fc"] = df_2["fc"].apply(know)

df_2["fc_usage"] = df_2["fc_usage"].apply(freqency)

def trust(col):
    if col == "一點也沒公信力":
        col = 0
    elif col == "沒公信力":
        col = 1
    elif col == "有公信力":
        col = 2
    else:
        col = None
    return col

varlist6 = ["fc_power", "tfc_power"]

df_2["tfc"] = df_2["tfc"].apply(know)

for i in varlist6:
    df_2[i] = df_2[i].apply(trust)

def responsibility(col):
    if col == "一點也沒責任":
        col = 0
    elif col == "沒有責任":
        col = 1
    elif col == "有責任":
        col = 2
    elif col =="非常有責任":
        col = 3
    else:
        col = None
    return col

varlist7 = ["fnresponsibility_src", "fnresponsibility_press", "fnresponsibility_official",
            "fnresponsibility_platform", "fnresponsibility_citizen"]

for i in varlist7:
    df_2[i] = df_2[i].apply(responsibility)

def should(col):
    if col == "非常不應該":
        col = 0
    elif col == "不應該":
        col = 1
    elif col == "應該":
        col = 2
    elif col == "非常應該":
        col = 3
    else:
        col = None
    return col

df_2["fnlaws"] = df_2["fnlaws"].apply(should)

varlist8 = ["fn_gov", "fn_tech"]

def freedom_of_speech(col):
    if col == "即使在網路散播假消息，人民在網路上的言論自由也應該獲得保障。":
        col = 1
    elif col == "即使損害人民的言論自由，政府也應該限制假消息在網路傳播。"\
    or col == "即使損害人民的言論自由，科技公司（臉書、Line等）也應該限制假消息在網路傳播。":
        col = 0
    else:
        col = None
    return col

for i in varlist8:
    df_2[i] = df_2[i].apply(freedom_of_speech)

def party(col):
    if col == "中國國民黨":
        col = 0
    elif col == "台灣基進":
        col = 1
    elif col == "台灣民眾黨":
        col = 2
    elif col == "新黨":
        col = 3
    elif col == "時代力量":
        col = 4
    elif col == "民主進步黨":
        col = 5
    elif col == "沒有政黨偏好":
        col = 6
    else:
        col = None
    return col

df_2["party"] = df_2["party"].apply(party)

def blue_green(col):
    if col == "非常接近泛藍":
        col = 0
    elif col == "接近泛藍":
        col = 1
    elif col == "接近泛綠":
        col = 2
    elif col == "非常接近泛綠":
        col = 3
    else:
        col = None
    return col

df_2["pan"] = df_2["pan"].apply(blue_green)

varlist9 = ["city", "sex", "age", "edu", "job", "job_other", "monthincome_self", "monthincome_family",
            "father", "father_other", "mother", "mother_other", "partner", "partner_other", "carlis",
            "motorlis", "CDC", "vaccines"]

label = LabelEncoder()

for i in varlist9:
    df_2[i] = label.fit_transform(df_2[i])

def president(col):
    if col == "林佳龍":
        col = 0
    elif col == "柯文哲":
        col = 1
    elif col == "侯友宜":
        col = 2
    elif col == "郭台銘":
        col = 3
    elif col == "賴清德":
        col = 4
    elif col == "朱立倫":
        col = 5
    elif col == "江啓臣":
        col = 6
    elif col == "陳其邁":
        col = 7
    elif col == "鄭文燦":
        col = 8
    elif col == "韓國瑜":
        col = 9
    else:
        col = None
    return col

df_2["@2024president"] = df_2["@2024president"].apply(president)

varlist10 = ["taiwanese", "chinese"]

def deep(col):
    if col == "非常不深":
        col = 0
    elif col == "不深":
        col = 1
    elif col == "深":
        col = 2
    elif col == "非常深":
        col = 3
    return col

for i in varlist10:
    df_2[i] = df_2[i].apply(deep)

varlist11 = ["ethic", "sovereignty"]

for i in varlist11:
    df_2[i] = label.fit_transform(df_2[i])

def like(col):
    if col == "非常不喜歡":
        col = 0
    elif col == "不喜歡":
        col = 1
    elif col == "喜歡":
        col = 2
    elif col == "非常喜歡":
        col = 3
    return col

df_2["cultrue"] = df_2["cultrue"].apply(like)

df_2["fakenews_indicator"] = 0

varlist12 = ["fncheck_friend", "fncheck_book", "fncheck_expert", "fncheck_factcheck", "fnrespond1",
             "fnrespond_2", "fnrespond_3", "fnrespond_4", "fc", "fc_usage", "tfc"]

for i in varlist12:
    df_2["fakenews_indicator"] += df_2[i]

varlist13 = ["partyhate", "@2024partyhate", "@2024presidenthate"]

df_2 = df_2.drop(varlist13, axis=1)

df_2.to_csv("fakedata_tidy.csv", index=False, encoding="utf-8")
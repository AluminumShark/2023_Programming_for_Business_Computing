import numpy as np
import pandas as pd
import statsmodels.api as sm
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import HTML

df = pd.read_csv("fakedata_tidy.csv")

df = df.dropna()

y1 = df["fakenews_indicator"]

varlist1 = ["fakenews1", "fakenews2", "fakenews3", "city", "sex", "age", "edu", "job", "job_other",
            "incomelevel", "classlevel", "monthincome_self", "monthincome_family", "father",
            "father_other", "mother", "mother_other", "partner", "partner_other", "carlis", "motorlis"
            ]

varlist2 = ["fnsce_press", "fnsce_politician", "fnsce_citizen","fnsce_enemy", "fnsce_ngo",
            "fnsce_mag","fnsce_tv", "fnsce_internet", "fnsce_mobile", "fnsce_nbr","city", "sex",
            "age", "edu", "job", "job_other",
            "incomelevel", "classlevel", "monthincome_self", "monthincome_family", "father",
            "father_other", "mother", "mother_other", "partner", "partner_other", "carlis", "motorlis"
            ]

varlist3 = ["fakenews1", "fakenews2", "fakenews3", "fnsce_press", "fnsce_politician", "fnsce_citizen","fnsce_enemy", "fnsce_ngo",
            "fnsce_mag","fnsce_tv", "fnsce_internet", "fnsce_mobile", "fnsce_nbr","city", "sex",
            "age", "edu", "job", "job_other",
            "incomelevel", "classlevel", "monthincome_self", "monthincome_family", "father",
            "father_other", "mother", "mother_other", "partner", "partner_other", "carlis", "motorlis"
            ]
            

x1 = df[varlist1]

x2 = df[varlist2]

model1 = sm.OLS(y1, x1)

model2 = sm.OLS(y1, x2)

result1 = model1.fit(cov_type="HC3")

result2 = model2.fit(cov_type="HC3")

with open("models.tex", "w", encoding= "utf-8") as models:
    models.write(result1.summary().as_text())
    models.write(result2.summary().as_text())
    models.close()

jitter = 0.1


df["jittered_fakenews1"] = df["fakenews1"] + np.random.uniform(-jitter, jitter, size=len(df))
df["jittered_fakenews2"] = df["fakenews2"] + np.random.uniform(-jitter, jitter, size=len(df))
df["jittered_fnsce_nbr"] = df["fnsce_nbr"] + np.random.uniform(-jitter, jitter, size=len(df))
df["jittered_fakenews_indicator"] = df["fakenews_indicator"] + np.random.uniform(-jitter, jitter, size=len(df))


fig_fakenews1 = go.Figure()
scatter_fakenews1 = px.scatter(df, x="jittered_fakenews1", y="jittered_fakenews_indicator")
boxplot_fnsce_mobile = px.box(df, x="fakenews1", y="fakenews_indicator")

for i in fig_fakenews1.data:
    fig_fakenews1.add_trace(i)
for i in boxplot_fnsce_mobile.data:
    fig_fakenews1.add_trace(i)

fig_fakenews1.update_layout(xaxis_title = "您最近一年內有沒有收到過假消息", yaxis_title = "進行事實查核的程度")

pio.write_image(fig_fakenews1, "fakenews1.png")


fig_fakenews2 = go.Figure()
scatter_fakenews2 = px.scatter(df, x="jittered_fakenews2", y="jittered_fakenews_indicator")
boxplot_fakenews2 = px.box(df, x="fakenews2", y="fakenews_indicator")

for i in scatter_fakenews2.data:
    fig_fakenews2.add_trace(i)

for i in boxplot_fakenews2.data:
    fig_fakenews2.add_trace(i)

fig_fakenews2.update_layout(xaxis_title = "感覺生活中出現假訊息的頻率", yaxis_title = "進行事實查核的程度")

pio.write_image(fig_fakenews2, "fakenews2.png")


fig_fnsce_nbr = go.Figure()
scatter_fnsce_nbr = px.scatter(df, x="jittered_fnsce_nbr", y="jittered_fakenews_indicator")
boxplot_fnsce_nbr = px.box(df, x="fnsce_nbr", y="fakenews_indicator")

for i in scatter_fnsce_nbr.data:
    fig_fnsce_nbr.add_trace(i)
for i in boxplot_fnsce_nbr.data:
    fig_fnsce_nbr.add_trace(i)

fig_fnsce_nbr.update_layout(xaxis_title = "認為社區鄰里散播假訊息的程度", yaxis_title = "進行事實查核的程度")

pio.write_image(fig_fnsce_nbr, "fnsce_nbr.png")

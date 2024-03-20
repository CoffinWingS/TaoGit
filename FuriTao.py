import streamlit as st
import pandas as pd

df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")

# เลือกปีล่าสุด
year = df["year"].max()

# เลือกเพศ
sex = "male"

# กรองข้อมูล
df = df[(df["year"] == year) & (df["sex"] == sex)]

# นับจำนวนผู้ฆ่าตัวตายในแต่ละประเทศ
counts = df.groupby("country").size()

# วาดกราฟแท่ง
plt.bar(counts.index, counts)
plt.xlabel("ประเทศ")
plt.ylabel("จำนวนผู้ฆ่าตัวตาย")

# แสดงกราฟบน Streamlit
st.pyplot(plt)





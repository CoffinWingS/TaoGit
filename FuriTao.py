import streamlit as st
import pandas as pd

df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")

import numpy as np

df = pd.read_csv('/content/master.csv')

# แปลงคอลัมน์ "country" เป็น float
df["country"] = pd.to_numeric(df["country"], errors="coerce").astype(np.float64)

# บันทึกข้อมูลกลับไปยังไฟล์ CSV
df.to_csv('/content/master.csv', index=False)

# นับจำนวนผู้ฆ่าตัวตายในแต่ละประเทศ
counts = df.groupby("country").size()

# วาดกราฟแท่ง
plt.bar(counts.index, counts)
plt.xlabel("ประเทศ")
plt.ylabel("จำนวนผู้ฆ่าตัวตาย")

# แสดงกราฟบน Streamlit
st.pyplot(plt)





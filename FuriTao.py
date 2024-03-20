import streamlit as st
import pandas as pd

df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")

countries = ["Albania", "Antigua and Barbuda", "Argentina", "Aruba", "Australia", "Australia"]

# กรองข้อมูล
df = df[df["country"].isin(countries)]

# นับจำนวนผู้ติดเชื้อในแต่ละประเทศ
counts = df.groupby("country").size()

# วาดกราฟแท่ง
plt.bar(counts.index, counts)
plt.xlabel("ประเทศ")
plt.ylabel("จำนวนผู้ติดเชื้อ")





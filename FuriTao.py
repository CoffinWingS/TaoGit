import streamlit as st
import pandas as pd

df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")


import matplotlib.pyplot as plt

# เลือกเฉพาะประเทศที่ต้องการ
countries = ["Albania", "Antigua and Barbuda", "Argentina", "Aruba", "Australia", "Australia"]
df = df[df["Country"].isin(countries)]

# กรุ๊ปข้อมูลตามประเทศและนับจำนวนผู้ติดเชื้อ
df = df.groupby("country").size().reset_index(name="จำนวนผู้ติดเชื้อ")

# เรียงลำดับจำนวนผู้ติดเชื้อจากมากไปน้อย
df = df.sort_values("จำนวนผู้ติดเชื้อ", ascending=False)

# วาดกราฟแท่ง
plt.bar(df["Country"], df["จำนวนผู้ติดเชื้อ"])
plt.xlabel("ประเทศ")
plt.ylabel("จำนวนผู้ติดเชื้อ")
plt.title("จำนวนผู้ติดเชื้อโควิดในแต่ละประเทศ")
plt.show()


import streamlit as st
import pandas as pd

df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")
import matplotlib.pyplot as plt

# เลือกประเทศที่ต้องการ
c = ["Albania", "Antigua and Barbuda", "Argentina", "Aruba", "Australia", "Australia"]

# กรองข้อมูลเฉพาะประเทศที่เลือก
df = dt[dt["Country"].isin(c)]

# แสดงกราฟแท่ง
plt.bar(df["Country"], df["Confirmed"])
plt.xlabel("ประเทศ")
plt.ylabel("จำนวนผู้ติดเชื้อ")
plt.title("จำนวนผู้ติดเชื้อโควิด-19")
plt.show()


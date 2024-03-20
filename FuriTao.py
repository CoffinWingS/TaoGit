import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")


# นับจำนวนผู้ฆ่าตัวตายในแต่ละประเทศ
counts = df.groupby('country').size()

# วาดกราฟแท่ง
fig, ax = plt.subplots(figsize=(10, 6))
plt.barplot(counts.index, counts)
plt.xlabel("Furina For Like")
plt.ylabel("HuTao for Love")

# แสดงกราฟบน Streamlit
st.pyplot(plt)





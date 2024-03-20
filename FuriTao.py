import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")


# นับจำนวนการฆ่าตัวตายในแต่ละประเทศ
df_country = df.groupby('country').size()

# เรียงลำดับประเทศตามจำนวนการฆ่าตัวตาย
df_country = df_country.sort_values(ascending=False)

# ปรับขนาดกราฟ
plt.figure(figsize=(22, 50))

# เพิ่มเครื่องหมายบอกค่าบนแท่ง
for i, v in enumerate(df_country):
    plt.text(v, i, f'{v:,}', ha='right', va='center')

# เพิ่มกริด
plt.grid(axis='x')

# แสดงข้อมูลเพิ่มเติมบนกราฟ
for i, v in enumerate(df_country):
    plt.text(v + 3, i, f'{v:,}')
    plt.annotate(f'{df_country.index[i]}', (v, i), xytext=(0, 5), textcoords='offset points')

# แสดงกราฟแท่งแนวนอน
#plt.barh(df_country.index, df_country, linewidth=3)
plt.barh(df_country.index, df_country, color='#ff5722')
plt.xlabel('Furina For Like', fontsize=40)
plt.ylabel('HuTao for Love', fontsize=40)
plt.show()


# แสดงกราฟบน Streamlit
st.pyplot(plt)





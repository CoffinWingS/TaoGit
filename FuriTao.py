import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")


# นับจำนวนการฆ่าตัวตายในแต่ละประเทศ
df_country = df.groupby('country').size(30)

# เรียงลำดับประเทศตามจำนวนการฆ่าตัวตาย
df_country = df_country.sort_values(ascending=False)

# ปรับขนาดกราฟ
plt.figure(figsize=(22, 50))

# แสดงกราฟแท่งแนวนอน
plt.barh(df_country.index, df_country)
plt.xlabel('Furina For Like', fontsize=40)
plt.ylabel('HuTao for Love', fontsize=40)
plt.show()


# แสดงกราฟบน Streamlit
st.pyplot(plt)





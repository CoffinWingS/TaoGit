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

# แสดงกราฟแท่งแนวนอน
plt.barh(df_country.index, df_country)
plt.xlabel('Furina For Like')
plt.ylabel('HuTao for Love')
plt.show()

# แสดงกราฟบน Streamlit
st.pyplot(plt)





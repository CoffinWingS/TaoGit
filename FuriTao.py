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
#plt.barh(df_country.index, df_country)
#plt.xlabel('Furina For Like')
#plt.ylabel('HuTao for Love')
#plt.show()


# ปรับขนาดตัวอักษร
plt.rcParams['font.size'] = 10
plt.xlabel('Furina For Like', fontsize=10)
plt.ylabel('HuTao for Love', fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# แสดงกราฟแท่งแนวนอน
plt.barh(df_country.index, df_country)

# แสดงชื่อประเทศ
for i in range(len(df_country)):
    plt.text(df_country[i], i, df_country.index[i], ha='right', fontsize=8)

plt.show()
st.pyplot()

# แสดงกราฟบน Streamlit
#st.pyplot(plt)





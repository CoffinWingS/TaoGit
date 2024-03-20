import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")


# นับจำนวนผู้ฆ่าตัวตายในแต่ละประเทศ
counts = df.groupby('country').size()

# วาดกราฟแท่ง
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=country_counts.index, y=country_counts, ax=ax)
ax.set_xlabel("Country")
ax.set_ylabel("Number of Suicides")
#st.pyplot(fig)

# แสดงกราฟบน Streamlit
st.pyplot(plt)





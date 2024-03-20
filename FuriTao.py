import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))


#***************************************************************************************************
st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")

if(st.button("แสดงกราฟแท่ง")):
 # นับจำนวนการฆ่าตัวตายในแต่ละประเทศ
 df_country = df.groupby('country').size()

 # เรียงลำดับประเทศตามจำนวนการฆ่าตัวตาย
 df_country = df_country.sort_values(ascending=False)

 # ปรับขนาดกราฟ
 plt.figure(figsize=(22, 50))

 # เพิ่มกริด
 plt.grid(axis='x')

 # เพิ่มเครื่องหมายบอกค่าบนแท่ง
 for i, v in enumerate(df_country):
    plt.text(v, i, f'{v:,}', ha='right', va='center')


 # แสดงกราฟแท่งแนวนอน
 #plt.barh(df_country.index, df_country, linewidth=3)
 plt.barh(df_country.index, df_country, color='#ff5722')
 plt.xlabel('Furina For Like', fontsize=40)
 plt.ylabel('HuTao for Love', fontsize=40)
 plt.show()


 # แสดงกราฟบน Streamlit
 st.pyplot(plt)
 st.button("ปิดข้อมูล")
else:
    st.button("ปิดไปเลย")

#***************************************************************************************************
# เลือกข้อมูลปี 1987 ถึง 2014
df = df[df['year'] >= 1987]
df = df[df['year'] <= 2014]

# กรองข้อมูลเฉพาะประเทศไทย
#df = df[df['country'] == 'Thailand']

# สร้างกราฟเส้น
plt.plot(df['suicides_no'],df['year'])
plt.xlabel('Year')
plt.ylabel('Suicide Rate')
plt.show()
st.pyplot()





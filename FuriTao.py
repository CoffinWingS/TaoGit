import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('./data/masteerrp.csv')

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
st.subheader("โนมโน้มการฆ่าตัวตายในช่วงปี")


if(st.button("แสดงโนมโน้มการฆ่าตัวตายในช่วงปี")):
 # นับจำนวนการฆ่าตัวตายในแต่ละปี
 df_year = df.groupby('year').size()

 # แสดงกราฟเส้น
 plt.bar(df_year.index, df_year,color='#607d8b')
 #plt.plot(df_year.index, df_year)
 plt.xlabel('Year')
 plt.ylabel('Number of Suicides')
 plt.show()

 st.pyplot(plt)
 st.button("ปิดข้อมูล")
else:
   st.button("ปิดดิ")
#***************************************************************************************************
if(st.button("แบบกราฟเส้น")):
 
 df_year = df.groupby('year').size()


 x = [10,20,30,40,50]
 y1 = [40,8,60,30,0]
 plt.plot(x,y1,ls='-',c='r',label = 'Product 1')
 y2 = [20,30,35,40,42]
 plt.plot(x,y2,ls='--',c='g', label = 'Product 2')
 y3 = [55,52,51,42,40]
 plt.plot(x,y3,ls=':',c='b', label = 'Product 3')
 # แสดงกราฟเส้น
 plt.plot(df_year.index, df_year)
 plt.xlabel('Year')
 plt.ylabel('Number of Suicides')
 plt.show()

 st.pyplot(plt)
 st.button("ปิดข้อมูล")
else:
  st.button("Exit!")
#***************************************************************************************************

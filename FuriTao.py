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

 plt.style.use('seaborn-v0_8-whitegrid')

 plt.title('Trend of Suicide Rates from 1987 to 2014', fontsize=16)



 # แสดงกราฟเส้น
 plt.plot(df_year.index, df_year, label='Line 1')
 plt.legend(loc='best')
 plt.xlabel('Year')
 plt.ylabel('Number of Suicides')
 plt.show()

 st.pyplot(plt)
 st.button("ปิดข้อมูล")
else:
  st.button("Exit!")
#***************************************************************************************************
 gender_counts = dt['sex'].size()

  # Plotting
  plt.figure(figsize=(8, 5))
  plt.plot(gender_counts.index, gender_counts.values, marker='o', linestyle='-')
  plt.title('Counts of Genders')
  plt.xlabel('Gender')
  plt.ylabel('Count')
  plt.grid(True)
  plt.xticks(rotation=45)
  st.pyplot()




import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('./data/Taohu.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))


#***************************************************************************************************
st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")

#if(st.button("แสดงกราฟแท่ง")):

  # เลือกประเทศ
 selected_country = st.selectbox("เลือกประเทศ", df['country'].unique())

 # กรองข้อมูลตามประเทศที่เลือก
 filtered_df = df[df['country'] == selected_country]
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
 #st.button("ปิดข้อมูล")
#else:
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
sex_counts = df['sex'].value_counts()
 # แสดงข้อมูลด้วย Streamlit
st.title('Counts of Gender in Suicide Dataset')
st.write('Counts of Male and Female in Suicide Dataset')
st.bar_chart(sex_counts)

 # เพิ่มกราฟเส้นเพื่อแสดงการแยกตามเพศ
male_data = df[df['sex'] == 'male']
female_data = df[df['sex'] == 'female']

male_counts = male_data['year'].value_counts().sort_index()
female_counts = female_data['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.plot(male_counts.index, male_counts.values, label='Male')
ax.plot(female_counts.index, female_counts.values, label='Female')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Suicide Counts by Gender over Time')
ax.legend()

st.pyplot(fig)
#***************************************************************************************************



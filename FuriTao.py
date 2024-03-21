import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df=pd.read_csv('./data/FuriTao.csv')

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
 plt.xlabel('body', fontsize=40)
 plt.ylabel('country', fontsize=40)
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
st.subheader("อัตราการฆ่าตัวตายของเพศชายและเพศหญิง")

# นับจำนวนการฆ่าตัวตายของแต่ละเพศ
sex_counts = df['sex'].value_counts()

# แสดงข้อมูลในรูปแบบของวงกลม
plt.figure(figsize=(6, 6))
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Suicide rates for males and females')
st.pyplot(plt)

#***************************************************************************************************


sex_counts = df['sex'].value_counts()
 # แสดงข้อมูลด้วย Streamlit
st.title('Counts of Gender in Suicide Dataset')
st.write('Counts of Male and Female in Suicide Dataset')
#st.bar_chart(sex_counts)

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

st.subheader("อัตราการฆ่าตัวตายในแต่ละประเทศ")

# ฟังก์ชันสำหรับแสดงกราฟตามประเทศที่เลือก
def show_country_stats(country_name):
    plt.figure(figsize=(12, 6))

    # กรองข้อมูลตามประเทศที่เลือก
    df_selected_country = df[df['country'] == country_name]

    # นับจำนวนการฆ่าตัวตายในแต่ละปี
    death_counts = df_selected_country.groupby('year').size()


    # แสดงกราฟเส้น
    plt.plot(death_counts.index, death_counts.values, marker='o')
    plt.title(f"Suicide rate in the country!!! {country_name}")
    plt.xlabel('YEAR')
    plt.ylabel('Number Of Suicides')
    plt.grid(True)
    st.pyplot(plt)

# เลือกประเทศจาก dropdown
selected_country = st.selectbox("เลือกประเทศ", df['country'].unique())

# เรียกใช้ฟังก์ชันเมื่อมีการเลือกประเทศ
show_country_stats(selected_country)

#***************************************************************************************************
# ฟังก์ชันสำหรับแสดงกราฟตามช่วงอายุที่เลือก
def show_age_stats(age_group):
    plt.figure(figsize=(12, 6))

    # กรองข้อมูลตามช่วงอายุที่เลือก
    df_selected_age = df[df['age'] == age_group]

    # นับจำนวนการฆ่าตัวตายในแต่ละประเทศ
    death_counts = df_selected_age.groupby('country').size().sort_values(ascending=False)


    # ปรับขนาดกราฟ
    plt.figure(figsize=(22, 50))

    # เพิ่มกริด
    plt.grid(axis='x')
 
    # แสดงกราฟแท่ง
    death_counts.plot(kind='barh')
    plt.title(f"Suicide rates during age {age_group}", fontsize=65)
    plt.xlabel('Country', fontsize=40)
    plt.ylabel('Number of suicides', fontsize=40)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    st.pyplot(plt)

# เลือกช่วงอายุจาก dropdown
selected_age_group = st.selectbox("เลือกช่วงอายุ", df['age'].unique())

# เรียกใช้ฟังก์ชันเมื่อมีการเลือกช่วงอายุ
show_age_stats(selected_age_group)
#***************************************************************************************************
#st.subheader("ค่าต่ำสุดและค่าสูงสุดของอัตราการฆ่าตัวตายของเพศชายและเพศหญิง")

# นับจำนวนการฆ่าตัวตายของแต่ละเพศ
#sex_counts = df.groupby('sex').size()

# แสดงค่าต่ำสุดและค่าสูงสุด
#min_count = sex_counts.min()
#max_count = sex_counts.max()

#st.write(f"ค่าต่ำสุด: {min_count}")
#st.write(f"ค่าสูงสุด: {max_count}")

#st.subheader("การเปรียบเทียบแปรปรวนของอัตราการฆ่าตัวตายในแต่ละปีด้วย Box Plot")

# สร้าง Box Plot เพื่อเปรียบเทียบแปรปรวนของอัตราการฆ่าตัวตายในแต่ละปี
#plt.figure(figsize=(12, 6))
#sns.boxplot(x='year', y='suicides_no', hue='sex', data=df)
#plt.title('การเปรียบเทียบแปรปรวนของอัตราการฆ่าตัวตายในแต่ละปี')
#plt.xlabel('ปี')
#plt.ylabel('จำนวนการฆ่าตัวตาย')
#plt.xticks(rotation=45, ha='right')
#st.pyplot()
#***************************************************************************************************

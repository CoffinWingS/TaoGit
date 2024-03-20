import streamlit as st
import pandas as pd

df=pd.read_csv('./data/master.csv')

st.header("สถิติการฆ่าตัวต่ายในปี 1987 - 2014")

st.write(df.head(10))

st.subheader("จำนวนผู้เสียชีวิต")
df['year'].hist(bins=[1987,1990,1995,2000,2005,2010,2014])

import streamlit as st
import pandas


st.set_page_config(layout="wide")

col3,col4=st.columns(2)

with col3:
    st.image("images/"+"photo.png")


with col4:
    st.header("Ayushman Page")
    content = """This is my Instructor for Python ,who is helping me build application for real world
     now i have gained a little knowledge to check for errors and data sensitivity as was into some problems rercently.
      Good to see me coding as i always feared it, but now on i will be building 20 apps from the course chosen 
      on Udemy and showcase my talent for developer as one of my cousin.May God help me further in this course and 
      guide me to completion of mega building by me of applications. """
    st.info(content)

st.subheader("Here are some apps i will be building in near future as my own wish.")



col1,empty_col,col2=st.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=";")

with col1:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")


with col2:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
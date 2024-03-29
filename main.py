import streamlit as st
import pandas
# st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Home")
    content = """
    Hi my name is Avazbek. I am from Uzbbekistan and now i learning 
    Pyhton with Ardit Sulce my teacher for Python!
    """
    st.info(content)

st.write("Below you can find some of apps i have built in Python. Feel free contact me")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f'[Source code]({row["url"]})')


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f'[Source code]({row["url"]})')


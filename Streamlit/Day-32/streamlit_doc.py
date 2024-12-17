import streamlit as st
import pandas as pd

st.title("Startup Dashboard")

st.header("this is header")
st.subheader("and this is subheader")

st.write("this is a normal text like a paragraph")

st.markdown(
    """
    ### This is example of markdown
    #### This is 4 star
    ### This is 3 star
    ## This is 2 star
    # This is 1 star
"""
)

st.markdown(
    """
    List of programming language
    - Java
    - Python
    - Javascript
    - C / C++
"""
)


st.code(
    """
def foo(input):
    return input ** 2

x = foo(2)
"""
)

st.latex("x^2 + y^2 + 5 = 0")

df = pd.DataFrame(
    {"name": ["aa", "bb", "cc"], "marks": [70, 50, 60], "package": [15, 12, 18]}
)

st.dataframe(df)

st.metric("Revenue", "Rs 3 lac", "3%")
st.metric("Revenue", "Rs 3 lac", "-3%")

st.json({"name": ["aa", "bb", "cc"], "marks": [70, 50, 60], "package": [15, 12, 18]})

st.image("./OIG.jpeg")
st.video("./ads.mp4")
# st.audio("")

# --------------- Creating Layouts
st.sidebar.title("Side bar of title")

col1, col2 = st.columns(2)
with col1:
    st.image("OIG.jpeg")
with col2:
    st.image("OIG.jpeg")

# --------------- Showing Status
st.error("login failed")
st.success("login successful")
st.info("info msg")
st.warning("this is warning")

import time

bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.01)
    bar.progress(i)

# ----------------- Taking user input
email = st.text_input("Enter your mail: ")
number = st.number_input("Enter number: ")
date = st.date_input("Enter reg date: ")

st.button("Nice")

email = st.text_input("Enter email")
password = st.text_input("Enter password: ")
gender = st.selectbox("select gender", ["male", "female", "other"])

btn = st.button("Login")

if btn:
    if email == "hi@gmail.com" and password == "1234":
        st.success("Login successful")
        st.balloons()
        st.write(gender)
    else:
        st.error("Wrong password/email")

file = st.file_uploader("Upload a csv file")
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.dataframe(df.describe())

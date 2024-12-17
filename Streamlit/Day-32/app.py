import streamlit as st
import pandas as pd


df = pd.read_csv("./startup_funding.csv")
# st.dataframe(df)
df["Investors Name"] = df["Investors Name"].fillna("Undisclosed")


st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox(
    "Select one of them", ["Overall Analysis", "Startup", "Investor"]
)

if option == "Overall Analysis":
    st.title("Overall analysis")

elif option == "Startup":
    # st.sidebar.selectbox("Select startup", ["Byjus", "Ola", "Flipkart"])
    # startup_name = df['Startup Name'].unique().tolist()
    st.sidebar.selectbox("Select startup", sorted(df["Startup Name"].unique().tolist()))
    st.sidebar.button("Find Details")
    st.title("Startup analysis")

elif option == "Investor":
    # st.sidebar.selectbox("Select investor", ["Rich kid 1", "Rich kid 2", "Rich kid 3"])
    st.sidebar.selectbox(
        "Select investor", sorted(df["Investors Name"].unique().tolist())
    )
    st.sidebar.button("Find Details")
    st.title("Investor analysis")

# pass

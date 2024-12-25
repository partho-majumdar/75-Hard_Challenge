import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("./india.csv")
list_of_state = list(df["State"].unique())
list_of_state.insert(0, "Overall India")

# sorted(df.columns[6:])

st.set_page_config(page_title="Map Visualization", layout="wide")


st.sidebar.title("Data viz of india")
selected_state = st.sidebar.selectbox("Select a state", list_of_state)
primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[6:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[6:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represent primary parameter")
    st.text("Color represent secondary parameter")
    if selected_state == "Overall India":
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=4,
            # mapbox_style="carto-positron",
            mapbox_style="open-street-map",
            size_max=35,
            width=1500,
            height=700,
            color_continuous_scale=px.colors.cyclical.IceFire,
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df["State"] == selected_state]
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=4,
            mapbox_style="open-street-map",
            size_max=35,
            width=1500,
            height=700,
            color_continuous_scale=px.colors.cyclical.IceFire,
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)

import streamlit as st

import pandas as pd
import plotly.express as px
from Utils.data import load_data
from Utils.config import ORDERS,COLORS

df = load_data()


st.title("Titanic app")
st.image("Utils/titanic.jpg")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total passengers",len(df))
with c2:
    st.metric("survival_rate", df["survival"].mean() * 100)
with c3:
    st.metric("Median age", df['age'].median())
with c4:
    st.metric("Median fare",df['fare'].median())
show_data = st.checkbox("Show data")
if show_data:
    st.dataframe(df.head(10), hide_index=True)

classes = st.multiselect("Select classes", df["class"].unique(), default=df["class"].unique())
gender = st.radio("Select gender", ["male", "female"], horizontal=True)

data = df[(df["class"].isin(classes)) & (df["sex"] == gender)]


c1, c2 = st.columns(2)

with c1:
    fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                   title="How big were the families on board?")
    fig.update_layout(bargap=0.1, yaxis_title="Passengers")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    outcome = data["survival"].value_counts().reset_index()

    fig = px.pie(outcome, names="survival", values="count", hole=0.5, color="survival",
                color_discrete_map=COLORS, title="Died vs survived")
    st.plotly_chart(fig, use_container_width=True)
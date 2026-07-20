import streamlit as st
import plotly.express as pl


st.title("weather forcast for the next day")

place = st.text_input("place: ")
days = st.slider("forcast days:", min_value=1, max_value=5, help="select days")
temp = st.selectbox("select data to vew: ", ("temperature", "sky"))
st.subheader(f"{temp} for the next {days} days in {place} ")


def get_days(days):
    dates = ["20-07-2026", "19-07-2026", "18-07-2026", "17-07-2026", "16-07-2026"]

    temperature = [14, 10, 12, 21, 18]
    temperature = [days * i for i in temperature]
    return dates, temperature

d, t = get_days(days)


figure = pl.line(x=d, y=t, labels={"x": "dates", "y": "temperature"} )
st.plotly_chart(figure)
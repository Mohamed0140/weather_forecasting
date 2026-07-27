import streamlit as st
import plotly.express as pl
from function import get_api

st.title("weather forcast for the next day")

place = st.text_input("place: ")
days = st.slider("forcast days:", min_value=1, max_value=5, help="select days")
temp = st.selectbox("select data to vew: ", ("temperature", "sky"))
st.subheader(f"{temp} for the next {days} days in {place} ")



if place:
    try:
        filtered_data = get_api(place, days)
        if temp == "temperature":
            temperature = [i["main"]["temp"] for i in filtered_data]
            temperature_cel = [i - 273.15 for i in temperature]
            date = [j["dt_txt"] for j in filtered_data]
            figure = pl.line(x=date, y=temperature_cel, labels={"x": "dates", "y": "temperature"} )
            st.plotly_chart(figure)

        if temp == "sky":
            img_list = ["images/clear.png", "images/cloud.png", "images/rain.png", "images/snow.png"]
            weather_conditions = [i["weather"][0]["main"] for i in filtered_data]
            sky_conditions = {"clear": img_list[0], "Clouds": img_list[1], "Rain": img_list[2], "snow": img_list[3]}
            img_condition = [sky_conditions[condition] for condition in weather_conditions]
            dates = [i["dt_txt"] for i in filtered_data]
            for i in range(0, len(img_condition), 8):
                cols = st.columns(8)
                for j in range(8):
                    if i + j < len(img_condition):
                        with cols[j]:
                            st.image(img_condition[i + j])
                            st.write(dates[i + j])

    except KeyError:
        st.write("this place does not exist")


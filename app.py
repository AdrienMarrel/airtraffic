import streamlit as st
import pandas as pd


HOME_AIRPORTS = ('LGW', 'LIS', 'LYS')
PAIRED_AIRPORTS = ('FUE', 'AMS', 'ORY')

#df = pd.read_parquet("traffic_10lines.parquet")

st.title('Traffic Forecaster')


with st.sidebar:
    home_airport = st.selectbox(
        'Home Airport', HOME_AIRPORTS)
    paired_airport = st.selectbox(
        'Paired Airport', PAIRED_AIRPORTS)
    forecast_date = st.date_input('Forecast Start Date')
    nb_days = st.slider('Days of forecast', 7, 30, 1)

    run_forecast = st.button('Forecast')


st.write('Home Airport selected:', home_airport)
st.write('Paired Airport selected:', home_airport)
st.write('Days of forecast:', nb_days)
st.write('Date selected:', forecast_date)



#A partir du df il applique le query et au niveau du format: affiche le .widget
#st.write(df.query('home_airpot = "{}"'.format(home_airport)).shape[0])


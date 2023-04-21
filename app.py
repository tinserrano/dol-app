import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=6)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public"])
df = df.set_index("TipoDolar")
df = df.fillna("")

st.title("Dol-APP")
st.write("Algunas cotizaciones de los diferentes tipos de cambio de dólar. DYOR")
# Print results.
#for row in df.itertuples():
#    st.write(f"{row.TipoDolar} has a :{row.Cotizacion}:")


st.dataframe(df)
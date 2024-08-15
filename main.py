__author__ = "Ejelonu Benedict O."

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="test assessment",
    page_icon="📊",
    layout="wide",
)

st.title("TICKER Announcement Filter")

# cache data retrieval
@st.cache_resource(ttl=1800, show_spinner="Fetching data ...")
def get_data(path_to_dataset):
    return pd.read_csv(path_to_dataset)

# import data
data = get_data('./data/test_data.csv')

tickers = ["AEE","REZ","1AE","1MC","NRZ"]

# Sidebar filters
st.sidebar.header("Filters")

# Sidebar filter for tickers
selected_ticker = st.sidebar.selectbox("Select Ticker", options=["All"] + tickers)

# filter for 'Trading Halt'
apply_filter_button = st.sidebar.button("Click for announcements with 'Trading Halt'")

# I implemented text search filter for other announcement keywords
#search_text = st.sidebar.text_input("Search for text in header")

if apply_filter_button:
    # Filter data to include rows with 'trading halt' in the 'header' column
    filtered_data = data[data["header"].str.contains("trading halt", case=False, na=False)]

    # Display filtered data
    st.write("Tickers having 'Trading Halt' in their announcements")
    st.dataframe(filtered_data[['issuer_code', 'issuer_full_name']])
else:
    # Apply ticker filter
    if selected_ticker != "All":
        filtered_data = data[data["ticker"] == selected_ticker]
    else:
        filtered_data = data

    # Display filtered data
    st.write(f"Showing announcements for ticker: '{selected_ticker}'")
    st.dataframe(filtered_data)

# if search_text:
#     filtered_data = data[data["header"].str.contains(search_text, case=False, na=False)]
#     st.write(f"Containing text: '{search_text}'")
# else:
#     st.write(f"Showing announcements for ticker: '{selected_ticker}'")
#     st.write(f"Containing text: '{search_text}'")


# # Display filtered DataFrame
# st.dataframe(filtered_data)
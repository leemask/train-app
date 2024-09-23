import streamlit as st
from datetime import datetime, timedelta

# Input boxes for ID and Password
user_id = st.text_input("ID")
password = st.text_input("Password", type="password")

# Create two columns
col1, col2 = st.columns(2)

# Select boxes for sources and destinations
locations = ["수서", "동대구", "부산", "대전", "동탄"]

with col1:
    source = st.selectbox("Source", locations)

# Set default destination value
default_destination = "동대구" if source != "동대구" else "수서"

with col2:
    destination = st.selectbox("Destination", locations, index=locations.index(default_destination))

# Adjust destination if source is "동대구"
if source == "동대구":
    destination = "수서"

# Time select boxes for start time range of train
start_time = st.time_input("Start Time")

# Calculate end time as one hour later
if start_time:
    start_datetime = datetime.combine(datetime.today(), start_time)
    end_datetime = start_datetime + timedelta(hours=1)
    end_time = end_datetime.time()
else:
    end_time = None

end_time = st.time_input("End Time", value=end_time)

# Check boxes for options
show_browser = st.checkbox("Show Browser")
continue_after_reserve = st.checkbox("Continue after one reserve")
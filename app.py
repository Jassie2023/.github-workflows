import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

def main():
    st.title("World Clock")

    # Define a list of time zones that you want to display
    all_timezones = {
        'Los Angeles': 'America/Los_Angeles',
        'New York': 'America/New_York',
        'London': 'Europe/London',
        'Amsterdam': 'Europe/Amsterdam',
        'Tokyo': 'Asia/Tokyo',
        'Sydney': 'Australia/Sydney'
    }

    # Create a multiselect dropdown to select locations
    selected_cities = st.multiselect('Select up to 4 locations:', 
                                     options=list(all_timezones.keys()), 
                                     default=['New York', 'London'],
                                     help='You can select up to 4 locations.')

    # Ensure only up to 4 locations can be selected
    if len(selected_cities) > 4:
        st.error('Please select no more than 4 locations.')
        return

    # Create placeholders for each selected timezone
    placeholders = {city: st.empty() for city in selected_cities}
    
    # Function to update time
    def update_time():
        for city in selected_cities:
            timezone = all_timezones[city]
            now = datetime.now(tz=ZoneInfo(timezone))
            placeholders[city].markdown(f"**{city}**: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Update the time every second
    while True:
        update_time()
        time.sleep(1)

if __name__ == "__main__":
    main()

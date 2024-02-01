## Overview
Jassie
A Streamlit-based web app showcasing real-time updates of current time across multiple global time zones, with user-selectable locations.

## How to run
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```

## Lessons learned
1. Create a world clock that displays time in different locations around the world
2. Create a GitHub Action that runs a script periodically (every 15 min)
3. Create a PostgreSQL server on Azure (for free)

# Features
1. A drop down menu for selecting locations
2. Can select up to 4 locations
3. Must update the time every second


## Questions/Future improvements
How can Python fetch real-time data like stock and weather updates periodically?
What are key considerations for maintaining data integrity when storing this data in a PostgreSQL database?

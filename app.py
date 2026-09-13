import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(page_title="AgroSphere Dashboard", page_icon="🌾", layout="wide")

st.title("🌾 AgroSphere Sustainable IoT Dashboard")
st.caption("Project ID: e035800e | EcoLogic 1.0 Hackathon Prototype")

# Sidebar Controls
st.sidebar.header("⚙️ Simulation Settings")
moisture_threshold = st.sidebar.slider("Smart Irrigation Trigger Threshold (%)", 15, 50, 30)

# Live Metrics Placeholders
m1, m2, m3, m4 = st.columns(4)
with m1:
    moisture_place = st.empty()
with m2:
    temp_place = st.empty()
with m3:
    battery_place = st.empty()
with m4:
    pump_place = st.empty()

# Graph Placeholder
chart_place = st.empty()
data_history = []

# Live Loop Simulation
for i in range(20):
    soil_moisture = random.randint(15, 85)
    soil_temp = round(random.uniform(22.0, 38.0), 1)
    battery_level = random.randint(40, 100)
    
    irrigation_status = "🔴 ON (Watering)" if soil_moisture < moisture_threshold else "🟢 OFF (Sufficient)"
    
    # Update visual metrics
    moisture_place.metric("💧 Soil Moisture", f"{soil_moisture}%")
    temp_place.metric("🌡️ Soil Temp", f"{soil_temp}°C")
    battery_place.metric("🔋 Solar Battery", f"{battery_level}%")
    pump_place.metric("⚙️ Pump Status", irrigation_status)
    
    # Store history for graphing
    data_history.append({"Time Tracking": i, "Moisture %": soil_moisture, "Battery %": battery_level})
    chart_place.line_chart(pd.DataFrame(data_history).set_index("Time Tracking"))
    
    time.sleep(1)


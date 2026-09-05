import time
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AgroSphere e035800e", page_icon="🌾", layout="wide")

st.title("🌾 AgroSphere Precision Farming Dashboard")
st.markdown("### Powered by Team AgriVarshini | System ID: **e035800e**")
st.write("---")

# Navigation Menu
menu = st.sidebar.radio(
    "Go To Dashboard Insights",
    ["Live Tracking", "Fertilizer Optimization", "Solar Power Analytics"],
)

if menu == "Live Tracking":
    st.subheader("💧 Real-Time Soil & Irrigation Tracker")

    col1, col2, col3 = st.columns(3)
    with col1:
        moisture = st.slider("Live Soil Moisture (%)", 0, 100, 28)
    with col2:
        temp = st.number_input("Soil Temperature (°C)", value=29.2)
    with col3:
        ph_level = st.slider("Soil pH Level", 0.0, 14.0, 6.5)

    st.write("---")
    if moisture < 30:
        st.error(
            f"🚨 CRITICAL ALERT: Moisture level is low ({moisture}%). Smart Irrigation Pump status: [RUNNING]"
        )
    else:
        st.success(
            f"✅ SYSTEM NORMAL: Soil status stable ({moisture}%). Smart Irrigation Pump status: [STANDBY]"
        )

elif menu == "Fertilizer Optimization":
    st.subheader("🧪 Precision NPK Compound Advisor")
    st.markdown("Target values calculated dynamically for EcoLogic Smart Agriculture framework.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Nitrogen (N)", "42 mg/kg", "-8 mg/kg (Deficit)")
    col2.metric("Phosphorus (P)", "24 mg/kg", "Normal")
    col3.metric("Potassium (K)", "55 mg/kg", "Optimal")

    st.info(
        "💡 Smart Advice: Apply 4.5kg of Nitrogen-enriched organic manure per acre to stabilize yield metrics."
    )

elif menu == "Solar Power Analytics":
    st.subheader("☀️ Farm Clean Energy Node Monitoring")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Solar Array Grid Input", value="13.4 V", delta="0.8 V")
    with col2:
        st.write("🔋 Battery System Charge State:")
        st.progress(89)

    st.success(
        "⚡ Eco-Energy Status: Autonomous Node operational. 0% grid dependencies recorded."
    )

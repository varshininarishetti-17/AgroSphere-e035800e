import random
import streamlit as st

# Set up the web page title and icon
st.set_page_config(page_title="AgroSphere e035800e", page_icon="🌾", layout="wide")

st.title("🌾 AgroSphere Precision Farming Dashboard")
st.markdown("### Powered by Team AgriVarshini | System ID: **e035800e**")
st.write("---")

# Create two columns on the web page layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("💧 Live Soil Metrics")
    # Generate interactive mockup metrics
    moisture = st.slider("Simulated Soil Moisture (%)", 0, 100, 35)
    temp = st.number_input("Soil Temperature (°C)", value=28.5)

    # Automated decision alert logic
    if moisture < 30:
        st.error("🚨 ALERT: Soil is too dry! Smart Irrigation Pump is ON.")
    elif moisture > 70:
        st.warning("⚠️ ALERT: Soil is saturated. Turning Pump OFF.")
    else:
        st.success("✅ Soil moisture levels are optimal.")

with col2:
    st.subheader("☀️ Clean Energy Status")
    battery = st.progress(82)
    st.write("🔋 Solar Battery Charge: 82%")
    st.metric(label="Solar Panel Output", value="12.6 V", delta="0.4 V (Optimal)")

st.write("---")
st.subheader("🧪 Automated Fertilizer Recommendations (NPK)")
st.info("📊 Current Profile: Nitrogen (Low) | Phosphorus (Medium) | Potassium (High)")
st.success("💡 Recommendation: Apply 15% more organic Nitrogen-based compost for this crop cycle.")

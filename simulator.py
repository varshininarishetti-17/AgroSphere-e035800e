import random
import time


def generate_farm_data():
    # 1. Simulate Agricultural Sensors
    soil_moisture = random.randint(15, 85)  # Percentage (%)
    soil_temp = round(random.uniform(22.0, 38.0), 1)  # Celsius (°C)

    # 2. Simulate Fertilizer NPK Levels (mg/kg)
    nitrogen = random.randint(20, 50)
    phosphorus = random.randint(10, 30)
    potassium = random.randint(30, 60)

    # 3. Simulate Solar Power & Energy Monitoring
    solar_voltage = round(random.uniform(10.5, 14.8), 2)  # Volts (V)
    battery_level = random.randint(40, 100)  # Percentage (%)

    # 4. Smart Irrigation Logic (Decision Making)
    if soil_moisture < 30:
        irrigation_status = "ON (Soil is dry! Watering crops...)"
    else:
        irrigation_status = "OFF (Soil moisture is sufficient)"

    # Print data nicely to the screen
    print("\n--- 🌾 AGROSPHERE LIVE SENSOR STREAM [e035800e] ---")
    print(f"💧 Soil Moisture: {soil_moisture}% | Temp: {soil_temp}°C")
    print(f"🧪 Soil Nutrients -> N: {nitrogen} | P: {phosphorus} | K: {potassium}")
    print(f"☀️ Solar Panel: {solar_voltage}V | 🔋 Battery: {battery_level}%")
    print(f"⚙️ Smart Irrigation Pump: {irrigation_status}")


# Run the simulator 5 times to show data flowing
for i in range(5):
    generate_farm_data()
    time.sleep(2)  # Wait 2 seconds between updates


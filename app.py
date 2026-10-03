import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home Energy Optimizer",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Home Energy Consumption Optimizer")
st.write("AI-based system for analyzing and reducing home energy consumption.")

st.sidebar.header("🔌 Appliance Details")

name = st.sidebar.text_input("Appliance Name", "AC")
power = st.sidebar.number_input("Power Rating (Watts)", 1, 5000, 1500)
hours = st.sidebar.number_input("Daily Usage (Hours)", 0.0, 24.0, 6.0)

if "data" not in st.session_state:
    st.session_state.data = []

if st.sidebar.button("➕ Add Appliance"):

    energy = (power * hours) / 1000

    st.session_state.data.append({
        "Appliance": name,
        "Power (W)": power,
        "Hours/Day": hours,
        "Energy (kWh/day)": energy
    })

    st.sidebar.success("Appliance added!")

if st.sidebar.button("🗑️ Clear All"):
    st.session_state.data = []
    st.rerun()

if len(st.session_state.data) == 0:

    st.info("👈 Enter appliance details in the sidebar and click Add Appliance.")

else:

    df = pd.DataFrame(st.session_state.data)

    total_daily = df["Energy (kWh/day)"].sum()
    total_monthly = total_daily * 30

    col1, col2, col3 = st.columns(3)

    col1.metric("⚡ Daily Consumption",
                f"{total_daily:.2f} kWh")

    col2.metric("📅 Monthly Consumption",
                f"{total_monthly:.2f} kWh")

    col3.metric("🔌 Appliances",
                len(df))

    st.divider()

    st.subheader("📊 Appliance Energy Details")

    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Energy Consumption Chart")

    chart = df.set_index("Appliance")["Energy (kWh/day)"]

    st.bar_chart(chart)

    st.subheader("🤖 AI Recommendations")

    for _, row in df.iterrows():

        appliance = row["Appliance"]
        energy = row["Energy (kWh/day)"]
        hours_used = row["Hours/Day"]
        power_used = row["Power (W)"]

        if hours_used > 10:
            recommendation = (
                f"Reduce {appliance} usage time."
            )

        elif power_used > 1500:
            recommendation = (
                f"{appliance} is a high-power appliance. "
                f"Use it carefully."
            )

        elif energy > 5:
            recommendation = (
                f"{appliance} consumes high energy. "
                f"Try reducing its usage."
            )

        elif energy > 2:
            recommendation = (
                f"Monitor the usage of {appliance}."
            )

        else:
            recommendation = (
                f"{appliance} usage is efficient."
            )

        st.write("🔹", recommendation)

    st.divider()

    if total_daily > 15:
        st.error(
            "⚠️ High Energy Consumption - "
            "Try reducing high-power appliance usage."
        )

    elif total_daily > 8:
        st.warning(
            "⚠️ Moderate Energy Consumption - "
            "Monitor your appliance usage."
        )

    else:
        st.success(
            "✅ Energy consumption is relatively low."
        )
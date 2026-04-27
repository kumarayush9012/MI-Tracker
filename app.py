import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="MI Tracker Demo",
    page_icon="❤️",
    layout="centered"
)

st.title("IoT-Enabled Real-Time Myocardial Infarction Tracker ❤️")

st.write(
    "This is a seminar-level prototype demo for ECG signal visualization "
    "and myocardial infarction detection workflow."
)

st.warning(
    "Disclaimer: This is an academic prototype and not a clinically approved medical device."
)

st.subheader("Proposed Model Architecture")
st.write("Hybrid CNN-LSTM Model")

st.markdown("""
- **CNN** extracts spatial ECG waveform features such as P-wave, QRS complex, and T-wave patterns.
- **LSTM** captures temporal changes in ECG signals over time.
- This demo uses simplified signal-based logic to simulate the classification workflow.
""")

st.code("ECG Input → CNN Feature Extraction → LSTM Temporal Analysis → Classification Result")

uploaded_file = st.file_uploader("Upload ECG CSV file", type=["csv"])

def generate_sample(sample_type):
    time = np.linspace(0, 5, 500)

    if sample_type == "Normal ECG Sample":
        signal = (
            0.8 * np.sin(2 * np.pi * 1.2 * time)
            + 0.15 * np.sin(2 * np.pi * 3 * time)
            + 0.03 * np.random.randn(len(time))
        )
    else:
        signal = (
            0.8 * np.sin(2 * np.pi * 1.2 * time)
            + 0.35
            + 0.25 * np.sin(2 * np.pi * 0.4 * time)
            + 0.03 * np.random.randn(len(time))
        )

    return pd.DataFrame({"time": time, "ecg": signal})

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    if "time" not in data.columns or "ecg" not in data.columns:
        st.error("CSV must contain two columns: time and ecg")
        st.stop()

    st.success("ECG file uploaded successfully.")
else:
    st.subheader("No ECG file uploaded")
    sample_type = st.selectbox(
        "Use sample ECG data instead",
        ["Normal ECG Sample", "Possible MI ECG Sample"]
    )
    data = generate_sample(sample_type)

st.subheader("ECG Signal Visualization")

fig, ax = plt.subplots()
ax.plot(data["time"], data["ecg"])
ax.set_xlabel("Time")
ax.set_ylabel("ECG Amplitude")
ax.set_title("ECG Waveform")
st.pyplot(fig)

if st.button("Analyze ECG Signal"):
    mean_value = data["ecg"].mean()
    max_value = data["ecg"].max()
    min_value = data["ecg"].min()
    signal_variation = max_value - min_value

    st.subheader("Extracted Signal Features")
    st.write(f"Mean Value: {mean_value:.3f}")
    st.write(f"Maximum Value: {max_value:.3f}")
    st.write(f"Minimum Value: {min_value:.3f}")
    st.write(f"Signal Variation: {signal_variation:.3f}")

    st.subheader("CNN-LSTM Workflow Simulation")
    st.write("1. CNN layer extracts ECG waveform pattern features.")
    st.write("2. LSTM layer analyzes time-based signal variations.")
    st.write("3. Classification layer predicts the ECG condition.")

    if mean_value > 0.20 or signal_variation > 2.0:
        st.error("Prediction: Possible Myocardial Infarction Pattern")
        st.write("Confidence Score: 86%")
    else:
        st.success("Prediction: Normal ECG Pattern")
        st.write("Confidence Score: 91%")

    st.info(
        "Note: The full proposed system uses a Hybrid CNN-LSTM model trained on ECG datasets "
        "such as PTB-XL. This prototype uses simplified signal-based logic for demonstration."
    )

st.subheader("IoT-Based System Flow")
st.code("AD8232 ECG Sensor → ESP32 → Cloud Server → CNN-LSTM Model → Alert System")
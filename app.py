import streamlit as st
import pandas as pd
import numpy as np
import openai
import datetime

# -------- CONFIG --------
st.set_page_config(page_title="Burnout Radar", layout="centered")

st.title("🧠 Burnout Radar")
st.subheader("Predict burnout before it hits")

# -------- SIDEBAR INPUTS --------
st.sidebar.header("Daily Inputs")

sleep = st.sidebar.slider("Sleep (hours)", 0.0, 12.0, 7.0)
screen = st.sidebar.slider("Screen Time (hours)", 0.0, 16.0, 6.0)
tasks = st.sidebar.slider("Number of tasks today", 0, 10, 3)
mood = st.sidebar.slider("Mood (1 = terrible, 5 = great)", 1, 5, 3)

# Demo chaos button
if st.sidebar.button("😈 Simulate Bad Day"):
    sleep = 4.0
    screen = 10.0
    tasks = 7
    mood = 2

# -------- BURNOUT LOGIC --------

# Normalize inputs to 0–1 scale
sleep_score = max(0, (8 - sleep) / 8)        # less sleep → higher burnout
screen_score = min(screen / 10, 1)           # more screen → higher burnout
task_score = min(tasks / 8, 1)               # more tasks → higher burnout
mood_score = (5 - mood) / 4                  # worse mood → higher burnout

# Weighted sum (tune weights if you want)
burnout_raw = (
    0.35 * sleep_score +
    0.25 * screen_score +
    0.25 * task_score +
    0.15 * mood_score
)

# Convert to 0–100 scale
burnout_score = int(burnout_raw * 100)


# -------- STATUS --------

if burnout_score < 35:
    status = "Low"
    color = "🟢"
    message = "You're doing well! Keep maintaining your balance."
elif burnout_score < 70:
    status = "Moderate"
    color = "🟡"
    message = "You're starting to feel the pressure. Take small breaks."
else:
    status = "High"
    color = "🔴"
    message = "High risk of burnout. You should slow down and recharge."


st.markdown(f"## Burnout Status: {color} **{status}**")
st.info(message)







# -------- SAVE HISTORY --------
today = datetime.date.today()

new_entry = {
    "date": today,
    "burnout": burnout_score
}

# Load existing data
try:
    history = pd.read_csv("burnout_history.csv")
except FileNotFoundError:
    history = pd.DataFrame(columns=["date", "burnout"])

# Add today’s entry
history = pd.concat([history, pd.DataFrame([new_entry])], ignore_index=True)

# Save back
history.to_csv("burnout_history.csv", index=False)






# -------- GRAPH --------
# -------- PIE CHART --------
# -------- PIE CHART (FIXED) --------
import matplotlib.pyplot as plt

st.subheader("🥧 Burnout Risk Breakdown")

healthy = max(0, 100 - burnout_score)
risk = burnout_score
stress = min(risk, 70)
burnout = max(0, risk - 70)

labels = ["Healthy Zone", "Stress Zone", "Burnout Zone"]
sizes = [healthy, stress, burnout]

# Remove zero-value parts
filtered = [(l, s) for l, s in zip(labels, sizes) if s > 0]
labels, sizes = zip(*filtered)

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")

st.pyplot(fig)



# -------- LINE CHART --------
st.subheader("📈 Burnout Trend Over Time")

if not history.empty:
    history["date"] = pd.to_datetime(history["date"])

    st.line_chart(
        history.set_index("date")["burnout"]
    )
else:
    st.write("No data yet. Start tracking today!")


# -------- AI EXPLANATION --------
st.subheader("Why is your burnout like this?")

if st.button("Get AI Explanation"):
    prompt = f"""
    A student has:
    Sleep: {sleep} hours
    Screen time: {screen} hours
    Tasks: {tasks}
    Mood: {mood}/5
    Burnout score: {burnout_score}/100

    Explain why burnout is high or low and give 3 actionable tips.
    """

    # --- OPENAI INTEGRATION ----

    

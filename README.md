🧠 Burnout Radar
Burnout Radar is a student-focused wellness and workload monitoring system designed to identify early burnout signals, explain contributing factors, and visualize academic pressure in a calm, non-judgmental interface.
The project combines:

a Streamlit-based student dashboard (calendar-aware, privacy-first UI)
a logic-heavy burnout analysis engine (scoring, explanations, simulations)


🎯 Project Goal
Burnout Radar is not a motivation app.
It is a warning and awareness system for college students.
The goal is to help students:

see workload pressure clearly
understand burnout contributors
regain control early — before performance and mental health drop


🚀 Key Features
🖥️ Student Dashboard (UI-Focused Module)

Clean, card-based interface 
Profile panel with calendar + tasks in one view
Google Calendar read-only integration
Daily workload visibility
Privacy-respecting design
Mobile + desktop friendly

📅 Calendar-Aware Workload

Reads upcoming events (classes, exams, deadlines)
Displays workload density
No event editing or modification
Calendar access can be disabled anytime

📊 Burnout Analysis Engine (Logic Module)

Burnout Risk Score (0–100)
Trend analysis from historical data
Burnout factor breakdown
“What-if” simulation (e.g., effect of extra sleep)
Manual save control (no accidental writes)

🤖 AI-Powered Explanation (Optional / Advanced Module)

Uses Google Gemini
Explains:

why burnout level is high/low
main contributing factors
realistic suggestions


🔐 Demo Login Credentials
For demonstration and evaluation purposes:
Username: Simi
Password: 1234


🧩 Tech Stack
Frontend / UI

HTML,CSS,JavaScript

Backend / Logic

Python
Streamlit app architecture

Calendar Integration

Google Calendar API (read-only)

Storage

Firebase Firestore (cloud persistence)
Local per-user JSON files (fast demo updates)

AI 

Google Gemini (gemini-1.5-flash)


📁 Project Structure
Burnout-Radar/
│
├── app.py                     # Streamlit entry point
├── styles.py                  # Global UI styling
├── profile.png                # User profile image
├── google_calendar.py          # Google Calendar integration
│
├── pages/
│   ├── Dashboard.py            # Main student dashboard (UI)
│   ├── Daily_Checkin.py        # Mood / sleep input (UI)
│   ├── Insights.py             # Read-only trends & patterns
│   └── Settings.py             # Privacy & permissions
│
├── index.html                  # Advanced dashboard UI (logic demo)
├── style.css                   # Styling for HTML dashboard
├── script.js                  # UI helpers
│
├── users_data/
│   ├── simi.json
│   ├── nauman.json
│   └── rohit.json
│
├── firebase_key.json           # Firebase service key
└── README.md


🔐 User Data Handling 

Each user has a separate local JSON file
Data is written only when “Save” is clicked
No background auto-saving
No cross-user overwrites
Firebase is used for:

persistence
analytics
demo credibility




🧠 Burnout Score Logic (High-Level)
Burnout scoring is based on weighted, non-linear factors:

Sleep debt
Screen overload
Task / deadline pressure
Mood decline

Extreme behavior is penalized more heavily than small fluctuations.

🤖 AI Explanation Flow 


User inputs:

Sleep
Screen time
Tasks
Mood
Optional stress context



Data is sent to Gemini


AI returns:

Reason for burnout level
Key contributors
Actionable, realistic suggestions


▶️ How to Run the Project
1️⃣ Install Dependencies
pip install streamlit firebase-admin google-api-python-client google-auth google-auth-oauthlib google-generativeai


2️⃣ Set Environment Variables (for AI module)
Windows (PowerShell):
setx GEMINI_API_KEY "your_gemini_key"


3️⃣ Run Streamlit App
streamlit run app.py


4️⃣ (Optional) Run HTML Dashboard
python -m http.server 8000

Open:
http://localhost:8000/index.html?user=simi


⚠️ Design Decisions (Why This Architecture)
❌ No auto-saving → prevents noisy data
❌ No iframe messaging → avoids browser security issues
❌ No cross-origin hacks → avoids CORS failures
✅ Manual save → user control
✅ Local JSON → instant UI updates
✅ Firebase → persistence + credibility
Built to work under pressure, not to look clever and fail.

📌 Future Improvements

Proper authentication (OAuth / Firebase Auth)
Multi-day history per user
Burnout prediction (next-day / next-week)
AI response caching
Export reports (PDF)
Mobile app wrapper


👥 Team
Team Name: Chicklers
Event: Innovate 3.0
Project Domain: AI + Mental Health + Student Technology

Just tell me what you need.

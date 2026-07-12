import streamlit as st
from pathlib import Path
import base64
import random
import time
import plotly.graph_objects as go
import pandas as pd

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Smart Elevator Systems",
    page_icon="🛗",
    layout="wide",
    initial_sidebar_state="expanded",
)

IMG_DIR = Path(__file__).parent / "images"


def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


HERO_B64 = img_to_base64(IMG_DIR / "hero_city.png")
TECH_B64 = img_to_base64(IMG_DIR / "tech_cabin.png")
MARKET_B64 = img_to_base64(IMG_DIR / "market_network.png")
EFF_B64 = img_to_base64(IMG_DIR / "efficiency_panel.png")
CONC_B64 = img_to_base64(IMG_DIR / "conclusion_panel.png")

# ----------------------------------------------------------------------------
# GLOBAL CSS — bright, clean, high-contrast theme
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;900&family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #f4faff 0%, #eef6fc 40%, #e8f4fb 100%);
        color: #142433;
    }

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #d9ecf7;
    }
    section[data-testid="stSidebar"] * { color: #16324a !important; }
    section[data-testid="stSidebar"] label { font-weight: 500; }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #0a3d62;
        letter-spacing: 0.3px;
    }

    p, li, span, div { color: #1c3a52; }

    .accent-text {
        color: #0091d5;
        font-weight: 700;
    }

    .subtitle {
        color: #3d6b87;
        font-size: 1.15rem;
        font-weight: 400;
    }

    .hero-wrap {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 1.4rem;
        border: 1px solid #cdeaf9;
        box-shadow: 0 8px 30px rgba(0, 145, 213, 0.18);
    }
    .hero-wrap img { width: 100%; display: block; filter: brightness(0.68) saturate(1.1); }
    .hero-overlay {
        position: absolute; inset: 0;
        display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
        padding: 3rem 4rem;
        background: linear-gradient(90deg, rgba(3,20,35,0.82) 25%, rgba(3,20,35,0.05) 80%);
    }
    .hero-overlay h1 { font-size: 2.6rem; margin-bottom: 0.4rem; max-width: 700px; color: #ffffff; }
    .hero-overlay h1 .glow-text { color: #4fd1ff; }
    .hero-overlay p { font-size: 1.2rem; color: #d9f1ff; max-width: 560px; }
    .tagline {
        margin-top: 1rem; font-style: italic; color: #7fe0ff; font-size: 0.95rem;
    }

    .card {
        background: #ffffff;
        border: 1px solid #d9ecf7;
        border-left: 5px solid #00a3e0;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        height: 100%;
        box-shadow: 0 3px 14px rgba(10, 61, 98, 0.06);
        transition: 0.25s ease;
    }
    .card:hover {
        border-left-color: #ff8a3d;
        box-shadow: 0 8px 22px rgba(10, 61, 98, 0.14);
        transform: translateY(-3px);
    }
    .card h4 { color: #0a3d62; margin-top:0; font-family:'Orbitron',sans-serif; font-size:1.05rem; }
    .card p, .card li { color: #2a4a63; font-size: 0.94rem; line-height: 1.55; }

    .section-img {
        width: 100%;
        border-radius: 16px;
        border: 1px solid #cdeaf9;
        box-shadow: 0 6px 22px rgba(10, 61, 98, 0.15);
    }

    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00a3e0 40%, #ff8a3d 60%, transparent);
        margin: 2.5rem 0;
        border: none;
        opacity: 0.5;
    }

    .stat-box {
        text-align: center;
        padding: 1.1rem;
        border-radius: 14px;
        background: #ffffff;
        border: 1px solid #cdeaf9;
        box-shadow: 0 3px 14px rgba(10, 61, 98, 0.07);
    }
    .stat-box .num { font-family:'Orbitron',sans-serif; font-size: 2.1rem; color:#0091d5; font-weight:700; }
    .stat-box .label { font-size: 0.85rem; color:#3d6b87; margin-top:0.2rem; }

    .footer {
        text-align: center; color: #6d93ab; font-size: 0.85rem; padding: 2rem 0 1rem 0;
    }

    .quote-box {
        border-left: 4px solid #ff8a3d;
        padding: 0.9rem 1.4rem;
        background: #fff6ef;
        border-radius: 0 12px 12px 0;
        font-style: italic;
        color: #6b3a12;
        margin: 1.5rem 0;
    }

    .status-ok { color: #12a150; font-weight: 700; }
    .status-warn { color: #e08900; font-weight: 700; }
    .status-alert { color: #e0362e; font-weight: 700; }

    .monitor-panel {
        background: #ffffff;
        border: 1px solid #d9ecf7;
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        box-shadow: 0 3px 14px rgba(10, 61, 98, 0.07);
    }

    .floor-track {
        background: #0a3d62;
        border-radius: 12px;
        padding: 0.8rem;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }

    .stButton>button {
        background: linear-gradient(135deg, #00a3e0, #0072c6);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1.3rem;
        box-shadow: 0 3px 10px rgba(0, 145, 213, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ff9a4d, #ff7a1a);
        box-shadow: 0 3px 12px rgba(255, 138, 61, 0.4);
    }

    .stTabs [data-baseweb="tab"] { font-weight: 600; color: #0a3d62; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# SIDEBAR NAV
# ----------------------------------------------------------------------------
st.sidebar.markdown("## 🛗 Smart Elevator AI")
section = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "⚠️ The Problem",
        "🤖 AI Solution & Tech",
        "🏢 Market Segments",
        "⚙️ How It Works — Live Model",
        "🌱 Efficiency & Safety",
        "🚀 Future Outlook",
    ],
    label_visibility="collapsed",
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<span style='font-size:0.8rem;color:#4a7793;'>Academic project prototype — "
    "AI-powered smart elevator systems for high-rise residential, commercial "
    "and industrial applications.</span>",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# HOME
# ----------------------------------------------------------------------------
if section == "🏠 Home":
    st.markdown(
        f"""
        <div class="hero-wrap">
            <img src="data:image/png;base64,{HERO_B64}">
            <div class="hero-overlay">
                <h1>Next-Gen Vertical Mobility<br><span class="glow-text">AI-Powered Smart Elevator Systems</span></h1>
                <p>Intelligent destination control for modern high-rises, commercial hubs, and industrial facilities.</p>
                <div class="tagline">"Moving people smarter, not just faster."</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("30%", "Avg. Wait Time Reduction"),
        ("24/7", "Predictive Health Monitoring"),
        ("3", "Core Deployment Segments"),
        ("0", "Target Unplanned Downtime"),
    ]
    for col, (num, label) in zip([c1, c2, c3, c4], stats):
        col.markdown(
            f"<div class='stat-box'><div class='num'>{num}</div>"
            f"<div class='label'>{label}</div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("### What This Project Covers")
    c1, c2, c3 = st.columns(3)
    cards = [
        ("⚠️ The Problem", "Long waits, ghost stops, rush-hour bottlenecks, energy waste, and industrial safety risks in traditional elevator systems."),
        ("🤖 The AI Solution", "Destination dispatch, predictive maintenance via IoT, and computer vision for safety — the technology stack driving smart vertical transit."),
        ("🏢 Market Fit", "Tailored deployments for high-rise residential towers, commercial hubs with badge integration, and heavy-duty industrial zones."),
    ]
    for col, (title, desc) in zip([c1, c2, c3], cards):
        col.markdown(
            f"<div class='card'><h4>{title}</h4><p>{desc}</p></div>",
            unsafe_allow_html=True,
        )

    st.info("👉 Check the **⚙️ How It Works — Live Model** tab in the sidebar for an interactive dispatch simulator and live monitoring dashboard.")

# ----------------------------------------------------------------------------
# THE PROBLEM
# ----------------------------------------------------------------------------
elif section == "⚠️ The Problem":
    st.markdown("## ⚠️ The Core Problem")
    st.markdown(
        "<p class='subtitle'>Why traditional elevator systems can't keep up with modern buildings.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="card">
            <h4>🏙️ Traditional System Flaws</h4>
            <ul>
                <li>Long wait times during peak hours</li>
                <li>"Ghost stops" — empty calls that waste cycle time</li>
                <li>Rush-hour bottlenecks in high-occupancy buildings</li>
                <li>High energy waste from idle or inefficient operation</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="card">
            <h4>🏭 Industrial Pain Points</h4>
            <ul>
                <li>Slow cargo and freight transit between floors</li>
                <li>Unpredictable mechanical breakdowns halting operations</li>
                <li>Safety risks in hazardous zones (chemical plants, warehouses)</li>
                <li>Lack of integration with automated material handling</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="quote-box">
        A single elevator breakdown in a 40-story tower can strand thousands of
        occupants — smart systems aim to predict failure before it happens.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# AI SOLUTION & TECH
# ----------------------------------------------------------------------------
elif section == "🤖 AI Solution & Tech":
    st.markdown("## 🤖 The AI Solution & Core Technology")
    st.markdown(
        "<p class='subtitle'>Three pillars of intelligence power the modern smart elevator.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.1])
    with c1:
        st.markdown(
            f"<img class='section-img' src='data:image/png;base64,{TECH_B64}'>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="card">
            <h4>🎯 Destination Dispatch</h4>
            <p>Groups passengers heading to the same or nearby floors before they even board,
            cutting the number of stops and reducing total trip time significantly compared
            to conventional call-button systems.</p>
            </div>
            <br>
            <div class="card">
            <h4>🔧 Predictive Maintenance</h4>
            <p>IoT sensors continuously track vibration, motor temperature, door cycle speed,
            and cable tension. Machine learning models flag anomalies days before a component
            actually fails, enabling proactive servicing.</p>
            </div>
            <br>
            <div class="card">
            <h4>📷 Computer Vision</h4>
            <p>In-cabin cameras detect overcrowding, falls or medical emergencies, and
            unattended baggage — triggering automatic alerts to building security or
            emergency services in real time.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<div class='card' style='margin-top:1.5rem;'><h4>⚡ Edge AI Processing</h4>"
        "<p>Decisions are made locally in the elevator controller for near-zero latency "
        "response, rather than depending entirely on a remote cloud round-trip.</p></div>",
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# MARKET SEGMENTS
# ----------------------------------------------------------------------------
elif section == "🏢 Market Segments":
    st.markdown("## 🏢 Market Segments & Customization")
    st.markdown(
        "<p class='subtitle'>One core AI engine, tuned differently for every environment.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown(
        f"<img class='section-img' src='data:image/png;base64,{MARKET_B64}' style='margin-bottom:1.5rem;'>",
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3 = st.tabs(["🏘️ High-Rise Residential", "🏢 Commercial Hubs", "🏭 Industrial Areas"])
    with tab1:
        st.markdown(
            """
            <div class="card">
            <h4>High-Rise Residential</h4>
            <p>Learns daily rhythms such as the morning school and work rush, then
            pre-positions cabs at predicted demand floors ahead of time — reducing
            wait times exactly when residents need it most.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with tab2:
        st.markdown(
            """
            <div class="card">
            <h4>Commercial Hubs</h4>
            <p>Integrates directly with security turnstiles and ID badge systems.
            A single badge scan automatically assigns the nearest optimal elevator,
            cutting lobby congestion during business hours.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with tab3:
        st.markdown(
            """
            <div class="card">
            <h4>Industrial Areas</h4>
            <p>Heavy-load optimization, explosion-proof and hazard-rated cabins for
            dangerous environments, plus native integration with AGVs (Automated
            Guided Vehicles) for seamless material handling between floors.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------------------------
# HOW IT WORKS — LIVE MODEL (interactive simulator + monitoring dashboard)
# ----------------------------------------------------------------------------
elif section == "⚙️ How It Works — Live Model":
    st.markdown("## ⚙️ How It Works — Interactive Model")
    st.markdown(
        "<p class='subtitle'>Simulate the AI dispatch logic, then step into the live "
        "monitoring dashboard used to check elevator health in real time.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    demo_tab1, demo_tab2 = st.tabs(["🎯 Destination Dispatch Simulator", "📡 Live Health Monitor"])

    # ---------------- DISPATCH SIMULATOR ----------------
    with demo_tab1:
        st.markdown("#### Configure the Building")
        c1, c2, c3 = st.columns(3)
        num_floors = c1.slider("Number of Floors", 5, 20, 10)
        num_cars = c2.slider("Number of Elevator Cars", 1, 5, 3)
        num_requests = c3.slider("Passengers Requesting a Ride", 1, 12, 6)

        if st.button("🚦 Run Dispatch Simulation"):
            random.seed()
            requests = [random.randint(1, num_floors) for _ in range(num_requests)]
            cars = {i: [] for i in range(1, num_cars + 1)}

            # simple destination-dispatch style grouping: sort requests, then
            # round-robin assign contiguous blocks of nearby floors to cars
            sorted_reqs = sorted(requests)
            chunk_size = max(1, len(sorted_reqs) // num_cars + 1)
            chunks = [sorted_reqs[i:i + chunk_size] for i in range(0, len(sorted_reqs), chunk_size)]
            for idx, chunk in enumerate(chunks):
                car_id = (idx % num_cars) + 1
                cars[car_id].extend(chunk)

            st.session_state["dispatch_result"] = cars
            st.session_state["dispatch_requests"] = requests

        if "dispatch_result" in st.session_state:
            cars = st.session_state["dispatch_result"]
            requests = st.session_state["dispatch_requests"]

            st.markdown(f"**Incoming requests (floors):** {sorted(requests)}")
            st.markdown("#### Assignment Result")

            colors = ["#00a3e0", "#ff8a3d", "#12a150", "#a24ee0", "#e0362e"]
            cols = st.columns(len(cars))
            total_stops_smart = sum(len(set(v)) for v in cars.values())
            total_stops_naive = len(requests)

            for i, (car_id, floors) in enumerate(cars.items()):
                with cols[i]:
                    color = colors[(car_id - 1) % len(colors)]
                    floor_list = sorted(set(floors)) if floors else []
                    st.markdown(
                        f"<div class='floor-track' style='border-top:6px solid {color};'>"
                        f"<b>Car {car_id}</b><br>"
                        f"Stops: {floor_list if floor_list else '—'}<br>"
                        f"Passengers: {len(floors)}"
                        f"</div>",
                        unsafe_allow_html=True,
                    )

            st.markdown("<br>", unsafe_allow_html=True)
            saved_pct = round((1 - total_stops_smart / total_stops_naive) * 100) if total_stops_naive else 0
            st.success(
                f"✅ Smart grouping needs **{total_stops_smart} unique stops** across all cars "
                f"vs **{total_stops_naive} stops** a first-come-first-served system would make "
                f"— roughly **{max(saved_pct, 0)}% fewer stops**."
            )
        else:
            st.caption("Set your building parameters above and click **Run Dispatch Simulation** to see how the AI groups passengers.")

    # ---------------- LIVE MONITORING DASHBOARD ----------------
    with demo_tab2:
        st.markdown("#### Real-Time Sensor & Health Dashboard")
        st.caption("This simulates the data an IoT-connected elevator would stream to a facility manager's dashboard.")

        if "sensor_data" not in st.session_state:
            st.session_state.sensor_data = {
                "vibration": 2.1,
                "temperature": 38.0,
                "door_cycle": 1.4,
                "energy_saved": 0.0,
                "history": pd.DataFrame({"tick": [], "health": []}),
            }

        refresh = st.button("🔄 Simulate New Live Reading")

        if refresh:
            sd = st.session_state.sensor_data
            sd["vibration"] = round(max(0.5, sd["vibration"] + random.uniform(-0.4, 0.6)), 2)
            sd["temperature"] = round(max(25, sd["temperature"] + random.uniform(-1.5, 2.0)), 1)
            sd["door_cycle"] = round(max(0.8, sd["door_cycle"] + random.uniform(-0.15, 0.2)), 2)
            sd["energy_saved"] = round(sd["energy_saved"] + random.uniform(0.3, 1.2), 2)

            health = 100 - (sd["vibration"] * 6 + max(0, sd["temperature"] - 40) * 2 + max(0, sd["door_cycle"] - 1.5) * 15)
            health = max(0, min(100, round(health)))
            new_row = pd.DataFrame({"tick": [len(sd["history"]) + 1], "health": [health]})
            sd["history"] = pd.concat([sd["history"], new_row], ignore_index=True)

        sd = st.session_state.sensor_data

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Vibration (mm/s)", sd["vibration"], delta=None)
        m2.metric("Motor Temp (°C)", sd["temperature"])
        m3.metric("Door Cycle Time (s)", sd["door_cycle"])
        m4.metric("Energy Regenerated (kWh)", sd["energy_saved"])

        current_health = int(sd["history"]["health"].iloc[-1]) if len(sd["history"]) else 92

        gc1, gc2 = st.columns([1, 1.4])
        with gc1:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=current_health,
                title={"text": "Predicted System Health"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#00a3e0"},
                    "steps": [
                        {"range": [0, 50], "color": "#ffd9d3"},
                        {"range": [50, 80], "color": "#ffe9c7"},
                        {"range": [80, 100], "color": "#d3f5e0"},
                    ],
                },
            ))
            fig.update_layout(height=280, margin=dict(l=20, r=20, t=50, b=10),
                               paper_bgcolor="rgba(0,0,0,0)", font={"color": "#0a3d62"})
            st.plotly_chart(fig, use_container_width=True)

        with gc2:
            if len(sd["history"]) > 1:
                st.line_chart(sd["history"].set_index("tick")["health"], height=280)
            else:
                st.info("Click **Simulate New Live Reading** a few times to build up a health trend chart.")

        if current_health < 50:
            st.error("🚨 **Predictive Maintenance Alert** — component health critical. Technician dispatch recommended immediately.")
        elif current_health < 80:
            st.warning("⚠️ **Attention** — sensor readings trending outside normal range. Schedule an inspection soon.")
        else:
            st.success("✅ **All systems nominal** — no maintenance action required.")

        st.caption("In production, these readings stream from onboard IoT sensors → gateway → cloud analytics → facility manager dashboard (see the architecture diagram concept used in this project).")

# ----------------------------------------------------------------------------
# EFFICIENCY, SAFETY & SUSTAINABILITY
# ----------------------------------------------------------------------------
elif section == "🌱 Efficiency & Safety":
    st.markdown("## 🌱 Efficiency, Safety & Sustainability")
    st.markdown(
        "<p class='subtitle'>Smart elevators don't just move people — they give energy back.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.1])
    with c1:
        st.markdown(
            f"<img class='section-img' src='data:image/png;base64,{EFF_B64}'>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="card">
            <h4>🔋 Energy Savings</h4>
            <p>Regenerative drives capture braking energy and feed it back into the
            building grid, meaningfully cutting overall elevator energy consumption.</p>
            </div>
            <br>
            <div class="card">
            <h4>🖐️ Touchless Controls</h4>
            <p>Voice commands, mobile app calling, and facial recognition access reduce
            surface contact and speed up boarding.</p>
            </div>
            <br>
            <div class="card">
            <h4>🛡️ Safety Layer</h4>
            <p>Real-time anomaly detection paired with automatic emergency dispatch —
            directly alerting building security or medical response teams.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<div class='card' style='margin-top:1.5rem;'><h4>🌍 Sustainability Angle</h4>"
        "<p>These energy and efficiency gains tie directly into green building "
        "certification goals, positioning smart elevators as core infrastructure "
        "for sustainable, future-ready construction.</p></div>",
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# FUTURE OUTLOOK
# ----------------------------------------------------------------------------
elif section == "🚀 Future Outlook":
    st.markdown("## 🚀 Conclusion & Future Outlook")
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 1])
    with c1:
        st.markdown(
            """
            <div class="card">
            <h4>Summary</h4>
            <p>Scaling urban density requires intelligent vertical transit. Elevators
            are becoming a core part of "smart building" infrastructure — not just a
            mechanical utility, but a connected, predictive system.</p>
            </div>
            <br>
            <div class="card">
            <h4>Vision</h4>
            <p>Seamless, zero-wait, self-healing buildings where vertical transit is
            invisible and instant — the elevator disappears into the experience.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"<img class='section-img' src='data:image/png;base64,{CONC_B64}'>",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="quote-box">
        "The elevator of the future doesn't just move you — it knows where you're going before you do."
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    "<div class='footer'>Next-Gen Vertical Mobility &nbsp;|&nbsp; AI-Powered Smart Elevator Systems &nbsp;|&nbsp; Academic Project</div>",
    unsafe_allow_html=True,
)

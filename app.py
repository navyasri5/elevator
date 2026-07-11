import streamlit as st
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def show_image(filename, caption=None, use_container_width=True):
    """Show an image from /assets if it exists, otherwise a subtle placeholder."""
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=use_container_width)
    else:
        st.markdown(f"""
        <div style="
            width:100%; aspect-ratio:16/9; border-radius:16px;
            background: repeating-linear-gradient(45deg, rgba(127,216,255,0.06), rgba(127,216,255,0.06) 10px, rgba(127,255,212,0.04) 10px, rgba(127,255,212,0.04) 20px);
            border: 1px dashed rgba(127,216,255,0.35);
            display:flex; align-items:center; justify-content:center;
            color:#7fd8ff; font-size:0.85rem; text-align:center; padding:1rem;">
            📷 Add image: <code>assets/{filename}</code>
        </div>
        """, unsafe_allow_html=True)

st.set_page_config(
    page_title="AscendAI | Smart Elevator Systems",
    page_icon="🛗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# GLOBAL STYLE
# ---------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3, h4 {
        font-family: 'Space Grotesk', sans-serif !important;
        letter-spacing: -0.02em;
    }

    .stApp {
        background: linear-gradient(180deg, #05070c 0%, #0a0e17 40%, #05070c 100%);
        color: #e8ecf3;
    }

    section[data-testid="stSidebar"] {
        background: #070a10;
        border-right: 1px solid rgba(120,150,255,0.12);
    }

    /* Hero */
    .hero-wrap {
        padding: 3.2rem 2rem 2.6rem 2rem;
        border-radius: 22px;
        background: radial-gradient(circle at 20% 20%, rgba(80,130,255,0.18), transparent 55%),
                    radial-gradient(circle at 80% 0%, rgba(0,220,200,0.12), transparent 50%),
                    linear-gradient(135deg, #0b0f1a 0%, #0d1424 100%);
        border: 1px solid rgba(120,150,255,0.15);
        margin-bottom: 2rem;
    }
    .eyebrow {
        display:inline-block;
        font-size: 0.75rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #7fd8ff;
        background: rgba(127,216,255,0.08);
        border: 1px solid rgba(127,216,255,0.25);
        padding: 0.3rem 0.8rem;
        border-radius: 999px;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        line-height: 1.08;
        background: linear-gradient(90deg, #ffffff 20%, #9fd8ff 60%, #7fffd4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .hero-sub {
        font-size: 1.12rem;
        color: #aab4c8;
        max-width: 720px;
        line-height: 1.6;
        font-weight: 300;
    }

    /* Stat strip */
    .stat-box {
        background: rgba(127,216,255,0.05);
        border: 1px solid rgba(127,216,255,0.15);
        border-radius: 14px;
        padding: 1.1rem 0.6rem;
        text-align: center;
    }
    .stat-num {
        font-family:'Space Grotesk', sans-serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: #7fffd4;
    }
    .stat-label {
        font-size: 0.78rem;
        color: #8b93a7;
        margin-top: 0.2rem;
    }

    /* Generic card */
    .card {
        background: linear-gradient(160deg, rgba(255,255,255,0.035), rgba(255,255,255,0.01));
        border: 1px solid rgba(120,150,255,0.14);
        border-radius: 18px;
        padding: 1.5rem 1.5rem 1.3rem 1.5rem;
        height: 100%;
        margin-bottom: 1rem;
    }
    .card h4 {
        margin-top: 0;
        color: #ffffff;
        font-size: 1.08rem;
    }
    .card p {
        color: #a4adc0;
        font-size: 0.92rem;
        line-height: 1.55;
        font-weight: 300;
    }
    .card .icon {
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
        display:block;
    }

    .sector-tag-res { color:#7fd8ff; font-weight:600; font-size:0.78rem; letter-spacing:0.08em; text-transform:uppercase;}
    .sector-tag-ind { color:#ffb37f; font-weight:600; font-size:0.78rem; letter-spacing:0.08em; text-transform:uppercase;}

    .cert-pill {
        display:inline-block;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.14);
        color: #cbd3e1;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        font-size: 0.8rem;
        margin: 0.2rem 0.35rem 0.2rem 0;
    }

    .quote-card {
        background: rgba(255,255,255,0.02);
        border-left: 3px solid #7fffd4;
        border-radius: 10px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
    }
    .quote-text { color:#d3d9e6; font-style: italic; font-size:0.95rem; }
    .quote-author { color:#7fffd4; font-size:0.82rem; margin-top:0.5rem; font-weight:600;}

    hr { border-color: rgba(120,150,255,0.12); }

    .stButton>button {
        border-radius: 10px;
        border: 1px solid rgba(127,216,255,0.4);
        background: linear-gradient(90deg, rgba(127,216,255,0.15), rgba(127,255,212,0.10));
        color: #eaf6ff;
        font-weight: 500;
        padding: 0.5rem 1.1rem;
    }
    .stButton>button:hover {
        border-color: #7fffd4;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# SESSION STATE / NAV
# ---------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

with st.sidebar:
    st.markdown("### 🛗 AscendAI")
    st.caption("Smart, Safe, Adaptive Vertical Mobility")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["Home", "Core Technology", "Residential", "Industrial", "Compare Sectors", "FAQ", "Request a Demo"],
        index=["Home", "Core Technology", "Residential", "Industrial", "Compare Sectors", "FAQ", "Request a Demo"].index(st.session_state.page),
        label_visibility="collapsed",
    )
    st.session_state.page = page
    st.markdown("---")
    st.caption("© 2026 AscendAI Systems · Concept Website")

def go(p):
    st.session_state.page = p
    st.rerun()

# ---------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------
if st.session_state.page == "Home":
    st.markdown("""
    <div class="hero-wrap">
        <div class="eyebrow">AI-NATIVE ELEVATOR INTELLIGENCE</div>
        <div class="hero-title">The Future of Vertical<br>Mobility: Smart, Safe,<br>and Adaptive.</div>
        <div class="hero-sub">AI-powered elevator systems engineered for the comfort of high-rise luxury
        living and the extreme safety demands of industrial oil refineries — one intelligent core,
        two mission-critical worlds.</div>
    </div>
    """, unsafe_allow_html=True)

    show_image("hero.png", caption="AI-powered elevator systems for luxury towers and industrial facilities")
    st.write("")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🏙️ Explore Residential Solutions", use_container_width=True):
            go("Residential")
    with c2:
        if st.button("🏭 Explore Industrial Solutions", use_container_width=True):
            go("Industrial")
    with c3:
        if st.button("📅 Request a Demo", use_container_width=True):
            go("Request a Demo")

    st.write("")
    stats = [
        ("99.9%", "System Uptime"),
        ("40%", "Faster Dispatch"),
        ("Class 1, Div 1", "Hazard Certified"),
        ("24/7", "AI Monitoring"),
    ]
    cols = st.columns(4)
    for col, (num, label) in zip(cols, stats):
        with col:
            st.markdown(f"""<div class="stat-box"><div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("## How It Works")
    st.caption("One AI core. Three stages. Adapted for every environment.")
    steps = [
        ("🔍", "Sense", "A dense mesh of vibration, thermal, acoustic, and occupancy sensors continuously reads the health of every car and shaft in real time."),
        ("🧠", "Predict", "Onboard AI models forecast wear, traffic surges, and hazard risk minutes to weeks in advance — before a human ever notices."),
        ("⚡", "Act", "The system self-corrects: rerouting cars, scheduling maintenance, adjusting ride dynamics, or triggering evacuation protocols autonomously."),
    ]
    cols = st.columns(3)
    for col, (icon, title, desc) in zip(cols, steps):
        with col:
            st.markdown(f"""<div class="card"><span class="icon">{icon}</span>
            <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("## Trusted Across Both Worlds")
    q1, q2 = st.columns(2)
    with q1:
        st.markdown("""<div class="quote-card">
        <div class="quote-text">"Wait times in our tower dropped almost by half. Residents genuinely
        notice the difference — it feels like the elevator knows where you're headed."</div>
        <div class="quote-author">— Facilities Director, Marina Heights Tower (concept)</div></div>""", unsafe_allow_html=True)
    with q2:
        st.markdown("""<div class="quote-card">
        <div class="quote-text">"The predictive alerts caught a bearing fault three weeks before it
        would have caused unplanned downtime in a hazardous zone."</div>
        <div class="quote-author">— Plant Safety Engineer, Gulf Coast Refinery Complex (concept)</div></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("#### Certifications & Standards")
    certs = ["ASME A17.1 / CSA B44", "ATEX Directive", "IECEx Certified", "Class 1, Division 1", "ISO 25745 Energy", "NFPA 70 Compliant"]
    st.markdown("".join([f'<span class="cert-pill">{c}</span>' for c in certs]), unsafe_allow_html=True)

# ---------------------------------------------------------------------
# CORE TECHNOLOGY
# ---------------------------------------------------------------------
elif st.session_state.page == "Core Technology":
    st.markdown("## Core Technology")
    st.caption("How the AI actually works, under the hood.")

    techs = [
        ("🔧", "Predictive Maintenance", "tech_predictive.png",
         "AI sensors continuously analyze vibration, temperature, and motor sound signatures. "
         "Machine learning models detect anomaly patterns and schedule repairs before a breakdown "
         "happens — achieving 99.9% uptime and cutting emergency callouts dramatically."),
        ("📈", "Traffic Optimization", "tech_traffic.png",
         "The system learns building or facility occupancy patterns over time. It pre-positions "
         "elevators on high-demand floors before a button is even pressed, reducing average wait "
         "times by up to 40%."),
        ("🔐", "Biometric & Touchless Integration", "tech_biometric.png",
         "Voice activation, facial recognition, and smartphone pairing combine to deliver seamless, "
         "touchless, and secure access — ideal for both high-end residences and restricted "
         "industrial zones."),
    ]
    for icon, title, img, desc in techs:
        col_img, col_text = st.columns([1, 2])
        with col_img:
            show_image(img)
        with col_text:
            st.markdown(f"""<div class="card"><span class="icon">{icon}</span>
            <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("### Under the Hood")
    with st.expander("🧠 What kind of AI models are running?"):
        st.write("""
        - **Anomaly detection** on time-series sensor data (vibration, temperature, current draw)
        - **Demand forecasting** models trained on historical + real-time traffic patterns
        - **Computer vision** for occupancy counting, biometric access, and thermal hazard mapping
        - **Reinforcement learning** dispatch logic that continuously improves car allocation
        """)
    with st.expander("🔗 How does it integrate with existing building systems?"):
        st.write("""
        AscendAI connects via secure APIs to Building Management Systems (BMS), fire & life-safety
        panels, smart home hubs, and industrial SCADA/DCS systems — allowing it to both read
        real-time context and push safety-critical overrides when required.
        """)
    with st.expander("🛰️ Where does the data live?"):
        st.write("""
        Time-critical inference (safety overrides, evacuation logic) runs **on-edge**, inside the
        elevator controller, so it works even if connectivity drops. Non-critical analytics
        (long-term maintenance forecasting, traffic trend learning) sync to the cloud.
        """)

# ---------------------------------------------------------------------
# RESIDENTIAL
# ---------------------------------------------------------------------
elif st.session_state.page == "Residential":
    st.markdown('<div class="sector-tag-res">SECTOR A</div>', unsafe_allow_html=True)
    st.markdown("## High-Rise Luxury Apartments")
    st.caption("Focus: Comfort, Speed, and Exclusivity.")

    show_image("residential_hero.png", caption="Luxury elevator interior in a high-rise residential tower")
    st.write("")

    feats = [
        ("🌀", "Smooth Glide Technology",
         "AI actively adjusts magnetic brakes and counterweights in real time to eliminate ear-popping "
         "pressure changes and cabin sway — even at high speed."),
        ("👑", "VIP Dispatch",
         "Automatically prioritizes penthouse residents or emergency services based on real-time "
         "traffic data, without disrupting the flow for other residents."),
        ("🏠", "Smart Home Sync",
         "The elevator integrates with smart home hubs, calling a cab to your floor the moment you "
         "unlock your apartment door — arriving before you reach the lobby."),
    ]
    cols = st.columns(3)
    for col, (icon, title, desc) in zip(cols, feats):
        with col:
            st.markdown(f"""<div class="card"><span class="icon">{icon}</span>
            <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("### Why It Matters for Residents")
    st.write(
        "In luxury towers, the elevator ride is part of the living experience. Sub-second dispatch, "
        "whisper-quiet cabins, and personalized access mean residents rarely think about the elevator "
        "at all — it simply anticipates them."
    )
    if st.button("📅 Book a Residential Demo"):
        go("Request a Demo")

# ---------------------------------------------------------------------
# INDUSTRIAL
# ---------------------------------------------------------------------
elif st.session_state.page == "Industrial":
    st.markdown('<div class="sector-tag-ind">SECTOR B</div>', unsafe_allow_html=True)
    st.markdown("## Oil Refineries & Hazardous Zones")
    st.caption("Focus: Explosion Proofing, Life Safety, and Durability.")

    show_image("industrial_hero.png", caption="Industrial-grade elevator system at an oil refinery / hazardous facility")
    st.write("")

    feats = [
        ("💥", "Explosion-Proof Engineering",
         "Class 1, Division 1 certified spark-free electronics and pressurized cabs keep combustible "
         "gases out of critical components, meeting ATEX and IECEx standards."),
        ("🚨", "Emergency Evacuation Mode",
         "In a crisis, the AI overrides standard traffic logic entirely. It uses thermal imaging to "
         "identify and bypass smoke-filled floors, safely routing and evacuating workers first."),
        ("🧪", "Corrosion Resistance",
         "Built with marine-grade materials engineered to withstand harsh chemical exposure and "
         "coastal salt air over decades of continuous operation."),
    ]
    cols = st.columns(3)
    for col, (icon, title, desc) in zip(cols, feats):
        with col:
            st.markdown(f"""<div class="card"><span class="icon">{icon}</span>
            <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("### Why It Matters for Plant Safety")
    st.write(
        "In a refinery, an elevator failure isn't an inconvenience — it's a life-safety event. "
        "AscendAI's industrial line is built first for survivability and predictable behavior under "
        "extreme conditions, with comfort features stripped down to what keeps operators safe and alert."
    )
    st.markdown("#### Relevant Certifications")
    certs = ["ATEX Zone 1/2", "IECEx", "Class 1, Division 1", "NEC 500/505", "NFPA 496 Purged Enclosures"]
    st.markdown("".join([f'<span class="cert-pill">{c}</span>' for c in certs]), unsafe_allow_html=True)
    if st.button("📅 Book an Industrial Consultation"):
        go("Request a Demo")

# ---------------------------------------------------------------------
# COMPARE SECTORS
# ---------------------------------------------------------------------
elif st.session_state.page == "Compare Sectors":
    st.markdown("## Residential vs. Industrial")
    st.caption("Same AI core. Two very different mission profiles.")

    import pandas as pd
    data = {
        "Dimension": [
            "Primary Goal", "Ride Priority", "Access Control", "Emergency Behavior",
            "Materials", "Key Certification", "AI Emphasis"
        ],
        "🏙️ Luxury Residential": [
            "Comfort & exclusivity", "Speed + smoothness", "Biometric + smart home sync",
            "VIP / priority rerouting", "Premium interior finishes",
            "ASME A17.1 / CSA B44", "Traffic prediction & personalization"
        ],
        "🏭 Oil Refinery / Hazardous": [
            "Life safety & durability", "Predictable, fail-safe operation", "Restricted biometric access",
            "Thermal-guided evacuation override", "Marine-grade, corrosion-resistant",
            "ATEX / IECEx / Class 1 Div 1", "Hazard detection & evacuation routing"
        ],
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.info("💡 Both product lines share the same predictive-maintenance and sensor-fusion core — "
            "only the decision logic and hardware hardening differ.")

# ---------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------
elif st.session_state.page == "FAQ":
    st.markdown("## Frequently Asked Questions")

    faqs = [
        ("Can AscendAI be retrofitted into an existing elevator, or only new installs?",
         "Both. The sensor and AI control layer is designed to retrofit onto most modern traction "
         "and hydraulic systems, though full explosion-proof hardening for hazardous zones typically "
         "requires a new or heavily modified cab."),
        ("How is safety-critical decision-making validated?",
         "All safety-override logic (evacuation mode, hazard rerouting) is tested against relevant "
         "codes (ASME A17.1, ATEX, IECEx) and validated through simulation and third-party audit "
         "before certification."),
        ("What happens if connectivity is lost?",
         "Safety-critical inference runs on-edge inside the controller, so core life-safety functions "
         "continue to operate without cloud connectivity."),
        ("What's the typical maintenance model?",
         "Predictive maintenance shifts most work from scheduled/reactive visits to condition-based "
         "servicing — technicians are dispatched only when the AI detects a developing issue."),
        ("Is the system compatible with existing Building Management / SCADA systems?",
         "Yes, via secure API integration with common BMS and industrial SCADA/DCS platforms."),
    ]
    for q, a in faqs:
        with st.expander(q):
            st.write(a)

# ---------------------------------------------------------------------
# REQUEST A DEMO
# ---------------------------------------------------------------------
elif st.session_state.page == "Request a Demo":
    st.markdown("## Request a Demo")
    st.caption("Tell us about your project and our team will follow up.")

    with st.form("demo_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name")
            email = st.text_input("Work Email")
        with c2:
            company = st.text_input("Company / Organization")
            sector = st.selectbox("Sector", ["High-Rise Residential", "Oil Refinery / Industrial", "Other"])
        message = st.text_area("Project Details", placeholder="Number of units, building height, timeline, etc.")
        submitted = st.form_submit_button("Submit Request")

    if submitted:
        if name and email:
            st.success(f"Thanks, {name}! Your request for {sector} has been recorded. Our team will reach out to {email} shortly.")
        else:
            st.error("Please fill in at least your name and email.")

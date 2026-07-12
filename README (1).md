# AI-Powered Smart Elevator Systems — Streamlit Site

A single-page project site built with Streamlit, covering:
- Home / Hero
- The Problem
- AI Solution & Core Technology
- Market Segments (Residential / Commercial / Industrial)
- **How It Works — Live Model**: an interactive destination-dispatch simulator (set floors/cars/passengers and watch the AI group them) plus a live IoT health-monitoring dashboard (gauge chart, health trend, simulated alerts)
- Efficiency, Safety & Sustainability
- Future Outlook

Theme: bright, high-contrast light UI (white/light-blue background, navy text, cyan/orange accents) for clear readability on screen and projector.

## How to run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app from this folder (keep the `images/` folder alongside `app.py`):
   ```bash
   streamlit run app.py
   ```

3. It will open automatically in your browser at `http://localhost:8501`.

## Folder structure
```
smart_elevator_site/
├── app.py
├── requirements.txt
├── README.md
└── images/
    ├── hero_city.png
    ├── tech_cabin.png
    ├── market_network.png
    ├── efficiency_panel.png
    └── conclusion_panel.png
```

## Notes
- Navigation is via the sidebar on the left.
- All images are embedded via base64 at runtime, so the app works fully offline once installed.
- To deploy publicly, push this folder to a GitHub repo and deploy free via [Streamlit Community Cloud](https://streamlit.io/cloud).

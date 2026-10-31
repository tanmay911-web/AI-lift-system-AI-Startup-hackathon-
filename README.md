# LiftMind 🛗🧠
### The AI-Powered Retrofit Kit for Smart Elevators

> *We do not replace elevators — we give them a brain.*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-0071e3?style=for-the-badge)](https://app-lime-mu-42.vercel.app/)
[![Source Code](https://img.shields.io/badge/💻_Source_Code-Browse-24292f?style=for-the-badge)](#-source-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Built for the HackIndia AI-First Startup Hackathon · Team 429 hui hui**

---

## 📌 Quick Links

| Deliverable | Link |
|---|---|
| 🌐 **Live deployed app** | **[https://app-lime-mu-42.vercel.app/](https://app-lime-mu-42.vercel.app/)** |
| 💻 **Web app code** (`index.html`) | [`index.html`](index.html) |
| 🖐️ **Python palm detector code** | [`palm_detector.py`](palm_detector.py) |
| 🤖 **AI usage report** | [`ai-usage-report.md`](ai-usage-report.md) |

---

## 🚨 The Problem

Legacy elevators are **blind to passenger context**.

- **Wasted energy:** cars stop at floors where the passenger has already walked away (*phantom calls*) or where the cabin is already packed.
- **No emergency awareness:** a hospital stretcher is treated like any other hall call, and a collapsed passenger inside the cabin goes unnoticed.
- **Prohibitive upgrade costs:** replacing a controller costs ₹3–8 Lakh in India, and a new commercial lift costs $75K–$350K globally.
- **Vendor lock-in:** smart dispatch from Otis, KONE and Schindler only comes with expensive new OEM installations.

## 💡 Our Solution

LiftMind is **not** an elevator manufacturer. It is a **low-cost, brand-agnostic Edge AI + Computer Vision retrofit kit** that gives existing elevators passenger-context awareness at a fraction of the cost of mechanical modernization.

**Hardware stack:** hallway landing camera · overhead cabin camera · local edge AI compute box · relay controller interface board

| Principle | What it means |
|---|---|
| 🔒 **100% on-device privacy** | Video inference (YOLOv8 + MediaPipe) runs locally. No cloud video streaming. |
| 🔌 **Zero mechanical tampering** | Connects through standard button-call relays, not safety-brake wiring, which avoids multi-year recertification. |
| 🏢 **Brand-agnostic** | Works on hydraulic, traction and MRL elevators from any vendor. |

---

## ✨ 8 Core Features (all in the prototype)

| # | Feature | What it does |
|---|---|---|
| 1 | **Dynamic Load Balancing** | When a car hits ≥ 85% weight or ≥ 90% space, hall calls are handed to an idle car. |
| 2 | **CV Stretcher Priority** | Detects medical stretchers and overrides routine queues for a non-stop emergency run. |
| 3 | **Phantom Call Cancellation** | If the waiting passenger leaves, a 3-second check cancels the stop and saves energy. |
| 4 | **Predictive Peak Staging** | Pre-parks idle cars based on the daily traffic schedule (morning rush, lunch, evening exit). |
| 5 | **Dual-Modal Full-Capacity Bypass** | Combines load-cell weight with CV floor-space tracking so bulky luggage is also counted. |
| 6 | **In-Cabin SOS Siren** | Detects a collapsed passenger, halts the car, locks the doors open, sounds a siren and alerts security. |
| 7 | **Multi-Tap Headcount Forecasting** | Pressing a floor button several times logs several riders, so the system can predict free space. |
| 8 | **Palm-Gesture Door Hold** | An open palm shown to the hallway camera (21-point MediaPipe landmarks) holds the doors open. |

---

## 💻 Source Code

Click a file to open it:

| Component | File | Tech |
|---|---|---|
| 🌐 **Digital Twin web app** | [`index.html`](index.html) | HTML · CSS · JavaScript (single file) |
| 🖐️ **Palm-gesture detector** (feature 8) | [`palm_detector.py`](palm_detector.py) | Python · OpenCV · MediaPipe Tasks API |
| 🧩 **Hand landmark model** | `hand_landmarker.task` | MediaPipe model used by the detector |

### Run the web app

**Option 1:** use the live version: **[app-lime-mu-42.vercel.app](https://app-lime-mu-42.vercel.app/)**

**Option 2:** run locally. Clone the repo and open `index.html` in any modern browser. No build step is needed.

```bash
git clone https://github.com/HackIndiaXYZ/ai-first-startup-hackathon-build-a-startup-using-ai-only-429-hui-hui.git
cd ai-first-startup-hackathon-build-a-startup-using-ai-only-429-hui-hui
# then open index.html in your browser
```

### Run the Python palm detector

Requires Python 3.9+ and a webcam.

```bash
python -m pip install opencv-python mediapipe
python palm_detector.py
```

- Keep `hand_landmarker.task` (~8 MB, included in this repo) in the same folder as `palm_detector.py`.
- Hold an **open palm facing the camera** for a few frames and the screen shows **"palm is open"** and **"lift+stop"**, which is the door-hold trigger.
- Press **`q`** to quit.
- If palm and back of hand are detected the wrong way round, set `FLIP_HANDEDNESS = False` at the top of the script.

**How the detector works:** MediaPipe returns 21 hand landmarks. The script checks that all five fingers are extended (tip-to-wrist distance versus the joint below it), then checks palm orientation with a cross-product of the wrist→index and wrist→pinky vectors. The gesture must persist for `HOLD_FRAMES` (5) frames before it fires, which removes flicker.

---

## 💰 Business Model

| | |
|---|---|
| **One-time kit** | $2,000 per shaft (edge compute, dual camera pods, relay modules) |
| **Annual SaaS** | $300 per shaft per year (dashboard, predictive health alerts, OTA model updates) |
| **Distribution** | Existing AMC elevator-maintenance partners sell, install and service the kit |
| **Market** | Global TAM $30B–$35B · India retrofit beachhead (SAM) $1.45B · Phase 1 pilot: 5 hospitals, 25 shafts |

**Go-to-market:** 5 hospital pilots → commercial tech parks → national scale through AMC networks.

---

## 🗂️ Repository Structure

```
├── index.html             # Digital Twin web app
├── palm_detector.py       # OpenCV + MediaPipe palm-gesture detector
├── hand_landmarker.task   # MediaPipe hand landmark model
├── ai-usage-report.md     # AI tools + prompts used
├── LICENSE                # MIT License
└── README.md
```

## 🤖 AI Usage

This project was built under the "AI-only" rules of the hackathon. Tools, prompts and a breakdown of what AI produced versus what the team did are documented in [`ai-usage-report.md`](ai-usage-report.md).

## 📄 License

Released under the [MIT License](LICENSE).

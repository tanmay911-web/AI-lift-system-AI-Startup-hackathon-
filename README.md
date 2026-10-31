[README (1).md](https://github.com/user-attachments/files/34226755/README.1.md)
# LiftMind 🛗🧠
### The AI-Powered Retrofit Kit for Smart Elevators

> *We do not replace elevators — we give them a brain.*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-0071e3?style=for-the-badge)](https://app-lime-mu-42.vercel.app/)
[![Pitch Deck](https://img.shields.io/badge/📊_Pitch_Deck-View_Slides-7c3aed?style=for-the-badge)](#pitch-deck)
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
| 📊 **Pitch deck** (10 slides, PNG) | [Jump to deck ↓](#pitch-deck) |
| 🎬 **Demo video** | _Add link here_ |
| 🤖 **AI usage report** | [`ai-usage-report.md`](ai-usage-report.md) |

---

## 🚨 The Problem

Legacy elevators are **blind to passenger context**.

- **Wasted energy:** cars stop at floors where the passenger has already walked away (*phantom calls*) or where the cabin is already packed.
- **No emergency awareness:** a hospital stretcher is treated like any other hall call, and a collapsed passenger inside the cabin goes unnoticed.
- **Prohibitive upgrade costs:** replacing a controller costs ₹3–8 Lakh in India (≈ $50K–$70K globally), and a new commercial lift costs $75K–$350K globally.
- **Vendor lock-in:** smart dispatch from Otis, KONE and Schindler only comes with expensive new OEM installations.

## 💡 Our Solution

LiftMind is **not** an elevator manufacturer. It is a **low-cost, brand-agnostic Edge AI + Computer Vision retrofit kit** that gives existing elevators passenger-context awareness at roughly **1/10th the cost** of mechanical modernization.

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

- The hand model (`hand_landmarker.task`, ~8 MB) downloads automatically on first run.
- Hold an **open palm facing the camera** for a few frames and the screen shows **"palm is open"** and **"lift+stop"**, which is the door-hold trigger.
- Press **`q`** to quit.
- If palm and back of hand are detected the wrong way round, set `FLIP_HANDEDNESS = False` at the top of the script.

**How the detector works:** MediaPipe returns 21 hand landmarks. The script checks that all five fingers are extended (tip-to-wrist distance versus the joint below it), then checks palm orientation with a cross-product of the wrist→index and wrist→pinky vectors. The gesture must persist for `HOLD_FRAMES` (5) frames before it fires, which removes flicker.

---

<a id="pitch-deck"></a>

## 📊 Pitch Deck

Click any slide to view it full size.

<table>
<tr>
<td width="50%"><a href="slide-01.png"><img src="slide-01.png" alt="Slide 1 – Title"></a><br><sub><b>1. Title</b></sub></td>
<td width="50%"><a href="slide-02.png"><img src="slide-02.png" alt="Slide 2 – The Problem"></a><br><sub><b>2. The Problem</b></sub></td>
</tr>
<tr>
<td width="50%"><a href="slide-03.png"><img src="slide-03.png" alt="Slide 3 – The Solution"></a><br><sub><b>3. The Solution</b></sub></td>
<td width="50%"><a href="slide-04.png"><img src="slide-04.png" alt="Slide 4 – Live Demo"></a><br><sub><b>4. Live Demo</b></sub></td>
</tr>
<tr>
<td width="50%"><a href="slide-05.png"><img src="slide-05.png" alt="Slide 5 – Features 1–4"></a><br><sub><b>5. Features 1–4</b></sub></td>
<td width="50%"><a href="slide-06.png"><img src="slide-06.png" alt="Slide 6 – Features 5–8"></a><br><sub><b>6. Features 5–8</b></sub></td>
</tr>
<tr>
<td width="50%"><a href="slide-07.png"><img src="slide-07.png" alt="Slide 7 – Market"></a><br><sub><b>7. Market</b></sub></td>
<td width="50%"><a href="slide-08.png"><img src="slide-08.png" alt="Slide 8 – Revenue Model"></a><br><sub><b>8. Revenue Model</b></sub></td>
</tr>
<tr>
<td width="50%"><a href="slide-09.png"><img src="slide-09.png" alt="Slide 9 – Go-To-Market"></a><br><sub><b>9. Go-To-Market</b></sub></td>
<td width="50%"><a href="slide-10.png"><img src="slide-10.png" alt="Slide 10 – Team"></a><br><sub><b>10. Team</b></sub></td>
</tr>
</table>

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
├── index.html            # Digital Twin web app
├── palm_detector.py      # OpenCV + MediaPipe palm-gesture detector
├── slide-01.png … slide-10.png   # Pitch deck as PNG images
├── ai-usage-report.md    # AI tools + prompts used
├── LICENSE
└── README.md
```

## 🤖 AI Usage

This project was built under the "AI-only" rules of the hackathon. Tools, prompts and a breakdown of what AI produced versus what the team did are documented in [`ai-usage-report.md`](ai-usage-report.md).

## 📄 License

Released under the [MIT License](LICENSE).

# LiftMind: AI Usage & Major Prompts Log

*Report generated: November 1, 2026*

---

# Part 1: Google Gemini Prompt Log

This document serves as a record of the major prompts used during the hackathon to generate ideas, conduct market research, write code, and build the final submission materials for the LiftMind Smart Elevator project. Minor troubleshooting and navigational prompts have been excluded.

## Phase 1: Project Kickoff & Planning
* **Prompt 1 (Project Initiation):** "Lets get started on a new project, Integrating AI in lift"
* **Prompt 2 (Hackathon Strategy):** "Participants are challenged to build a fully functional startup using AI for everything: Idea generation, Market research, UI/UX design, Coding, Testing, Deployment, Pitch creation. Apart from idea generation, we have to do all this. make a rough plan to follow."

## Phase 2: Feature Definition & Architecture
* **Prompt 3 (Core Features 1-3):** "Lets get started on market research, i have choosen perplexity. before we start let me give you a brief overview of what exactly we are targerting. 1-If there are two lifts and one of them is full, and that lift is called, the second lift if empty is sent automatically to the floor where the lift was called. 2-There will be a camera at every floor and the camera will use ai to assign priority to special targets, if there is a stretcher with a patient on it, then lift will ignore others and go there first. If a person presses a button on a floor, and then goes away, or gets into another lift, then the ai camera will ignore that call. Keep this in memory, i will give more features. Wait for the next prompt"
* **Prompt 4 (Core Features 4-7):** "4-automatically Moves to Top, Ground or the floor with more traffic according to the office hours or college hours to avoid last minute hassles. 5-If lift is full AI will automatically skip the next floors calls, not only on weight, but using camera inside to check space. 6-Emergency Siren in case the passenger is pass out or not in condition. 7-if 5 people get inside the lift to go on 6th floor, 6th button will be pressed 5 times for the lift to be more accurate on which floor to go. Keep this in memory, i will give more features. Wait for the next prompt"
* **Prompt 5 (Core Feature 8):** "8- if there is a person in the hallway rushing to the lift, they can show out their palm and the lift will stop automatically using camera outside"

## Phase 3: Market Research
* **Prompt 6 (Generating the Perplexity Prompt):** "The features are done now, lets get started on the market research. Give a prompt to put into perplexity to get the fitting market research, it should contain the necessary info along with cost of different types of list, their maintainance cost etc. also give the exact setting that perplexity should be used to get the best free results"
* **Prompt 7 (Analyzing the Research Data):** "[Anlayze this, convert the numbers into inr and write full form or simple meaning in brackets in front of abbreviations." *(Note: This was pasted alongside the raw output from Perplexity).*

## Phase 4: Prototyping & Development
* **Prompt 8 (Simulation Planning):** "Lets get started on making a prototype, since we do not have a lift, we would have to simulate everything. Make a plan for creating it"
* **Prompt 9 (Application Generation):** "Make the whole application, complete with tests for all 8 features. do not make any mistakes. Double check everything."
* **Prompt 10 (Edge AI / Computer Vision Script):** "make a seperate program using open cv that detects when my hand is open and palm is facing forward, it shows palm is open and lift+stop"

## Phase 5: Go-To-Market & Submission Packaging
* **Prompt 11 (Next Steps):** "i am satisfies with With the simulation what are the next steps"
* **Prompt 12 (GitHub Structuring):** "make a new plan everything is going to be uploaded on github"
* **Prompt 13 (Pitch Deck Generation):** "the previous prompt for gamma ppt making was bit bad it added its own features by himself make a master perfect prompt for it and make sure the features and data related to our project only"

---

# Part 2: Perplexity Market Research Report

## Major Substantive Prompts

| # | Phase | Prompt | Outcome |
|---|---|---|---|
| 1 | Business Strategy & Market Research | Act as an expert PropTech Market Research Analyst and Smart Building Consultant for a startup integrating AI and Computer Vision into elevator systems. Define an 8-capability product profile: dynamic load balancing, CV priority preemption for stretchers/emergencies, phantom call cancellation, predictive floor staging, dual-modal capacity bypass, in-cabin distress/collapse detection, destination headcount tracking, and hallway gesture recognition. Generate a startup-pitch market research report covering global and India-specific TAM/SAM/SOM, competitor capabilities and gaps for Otis, KONE, Schindler, and TK Elevator, installation costs for traction, hydraulic, and MRL elevators, standard versus smart/IoT AMC costs, and a go-to-market recommendation comparing a retrofit AI kit versus building new AI elevators. | Produced a comprehensive market research and GTM report with market sizing, India opportunity, competitor gap analysis, cost benchmarks, differentiation mapping for all 8 capabilities, and a recommendation to prioritize a retrofit AI/CV kit over manufacturing new elevators. |

## Phase Breakdown

### Ideation & Product Definition
- Defined the startup's AI/Computer Vision elevator product concept.
- Established eight core capabilities across traffic optimization, safety, accessibility, and passenger behavior detection.

### Market Research & Business Strategy
- Requested global and India-specific market sizing for smart elevators, elevator modernization, and elevator control systems.
- Requested competitor benchmarking against major elevator OEMs to identify product whitespace.
- Requested hardware installation and annual maintenance cost benchmarks.

### Go-to-Market Strategy
- Requested a financial comparison between building new AI elevators and selling a retrofit AI kit.
- Established a retrofit-first strategy targeting legacy commercial and institutional elevators through hardware, installation, and recurring SaaS revenue.

## Key Decisions Driven
- Position the startup as a brand-agnostic AI/CV retrofit layer, not an elevator OEM.
- Prioritize a Retrofit AI Kit with cameras, edge devices, relay controllers, and SaaS analytics.
- Target hospitals, colleges, IT parks, offices, hotels, and residential societies.
- Differentiate through passenger-context awareness: emergency preemption, phantom-call cancellation, distress detection, gesture recognition, and occupancy-aware dispatch.
- Use a hardware-plus-recurring-SaaS business model priced below full modernization or controls-replacement costs.

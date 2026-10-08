# Mechatronics Systems Design: MATLAB & LabVIEW Simulations
### Powertrain Dynamic Modeling, Actuator Feedback Control & LabVIEW State Machine Access Systems

**Course:** ME561 / ME0562 – Mechatronics Systems Design and Interfacing  
**Instructor:** Dr. Ghaith Al-refai / Eng. Ghaith Alshishani  
**Department:** Department of Mechatronics & Artificial Intelligence Engineering  
**Institution:** German Jordanian University (GJU)

---

## Overview

This repository contains the simulation projects and virtual instrument models completed for **Mechatronics Systems Design and Interfacing**. It focuses strictly on computational and virtual engineering environments:

1. **MATLAB / Simulink:** Longitudinal electric vehicle powertrain dynamics, motor look-up tables, and closed-loop electromechanical actuator stability.
2. **National Instruments LabVIEW:** Event-driven finite state machine (FSM) simulating a digital password lock and electronic door access security system.

---

## 1. MATLAB & Simulink Simulations (`simulink/`)

### Electric Vehicle (EV) Powertrain Dynamics (`EV_HW.slx`, `Acceleration.slx`, `Torque_Function.mat`)
* **Physical Road Load Model:** Computes longitudinal vehicle forces including aerodynamic drag ($F_{\text{aero}} = \frac{1}{2}\rho C_d A v^2$), rolling resistance ($F_{\text{roll}} = C_{rr} m g \cos\theta$), and road grade resistance.
* **Electric Motor Characteristic:** Integrates a realistic motor torque-speed curve via MATLAB LUT (`Torque_Function.mat`) modeling constant-torque and field-weakening constant-power envelopes.
* **Transient Acceleration:** Simulates 0–100 km/h acceleration times, final-drive wheel torque delivery, and drive-cycle energy consumption.

### Electromechanical Dynamics & Feedback Stability (`HW2.slx`, `HW3.slx`, `MSD_HW.slx`)
* **Time-Domain Response:** Step and impulse responses of electromechanical actuators (DC motor drive, mechanical inertia, viscous damping).
* **Feedback Control Loop:** Closed-loop position/speed regulation, H-bridge driver PWM interfacing, and system settling time analysis.

---

## 2. LabVIEW Password Lock & Access Control (`labview/`)

### Architecture & Finite State Machine (FSM)
Implemented in LabVIEW as an event-driven state machine managing digital security, credential comparison, and actuator output signals:

```
 [ Initialization ] ──── Reset password registers, set default locked state
         │
 [ Wait for Input ] ──── Event-driven polling of keypad digits
         │
 [ Validate Code  ] ──── Dynamic array comparison against programmed access code
       ├── Correct? ──> [ Open Door (Access Granted) ] ──> Timed unlock pulse
       └── Incorrect? ─> [ Alarm / Lockout ] ───────────> Error state & attempt lockout
         │
 [ Save & Display ] ──── Updates user interface status indicators and event logs
```

### Files & Virtual Instruments
* **`My_Method_Password_Lock.vi`:** Custom LabVIEW implementation of the password entry and state-transition evaluation logic.
* **`Door_Access_System.vi`:** Complete interactive door security simulation including user keypad front panel, digital indicators, and timed unlock triggers.
* **`State_Machine_Architecture.pdf`:** State transition diagram outlining the operational states.
* **`Door_Access_System_Solved.exe`:** Standalone compiled executable allowing direct testing on Windows without requiring full LabVIEW runtime installation.

---

## Repository Structure

```text
├── simulink/
│   ├── EV_HW.slx                 # Electric vehicle longitudinal dynamic model
│   ├── Acceleration.slx          # Powertrain acceleration simulation
│   ├── Torque_Function.mat       # Motor torque curve LUT
│   ├── HW2.slx                   # Dynamic response simulation
│   ├── HW3.slx                   # Feedback loop simulation
│   └── MSD_HW.slx                # Electromechanical system model
├── labview/
│   ├── My_Method_Password_Lock.vi     # Custom LabVIEW password lock logic
│   ├── Door_Access_System.vi          # Interactive door access front panel & diagram
│   ├── State_Machine_Architecture.pdf # State machine specification diagram
│   └── Door_Access_System_Solved.exe  # Standalone compiled executable
├── .gitignore
└── README.md
```

---

## How to Run

* **Simulink Models:** Open in MATLAB (R2021a or newer). Ensure `Torque_Function.mat` is loaded into the MATLAB workspace before executing `Acceleration.slx`.
* **LabVIEW Simulations:** Open `.vi` files using NI LabVIEW (2020 or newer). Alternatively, launch `Door_Access_System_Solved.exe` directly on Windows for standalone evaluation.
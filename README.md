# Mechatronics Systems Design: Coursework, Dynamic Modeling & Case Studies
### MATLAB/Simulink Powertrain Simulations, IMU Sensor Fusion & V-Model System Design

**Course:** ME561 - Mechatronics Systems Design and Interfacing  
**Instructor:** Dr. Ghaith Al-refai  
**Department:** Department of Mechatronics & Artificial Intelligence Engineering  
**Institution:** German Jordanian University (GJU)

---

## Overview

This repository contains the advanced coursework assignments, dynamic system simulations, and engineering case studies completed for **ME561: Mechatronics Systems Design and Interfacing**. The curriculum focuses on cyber-physical systems engineering, multidisciplinary MATLAB/Simulink modeling, sensor interfacing, and formal requirements-driven engineering.

---

## Key Modules & Projects

### 1. Electric Vehicle (EV) Longitudinal Powertrain Dynamics (`simulink/EV_HW.slx`, `Acceleration.slx`, `Torque_Function.mat`)
- **Physics Modeling:** Implements longitudinal vehicle dynamics incorporating aerodynamic drag ($F_{aero} = \frac{1}{2}\rho C_d A v^2$), rolling resistance ($F_{roll} = C_{rr} m g \cos\theta$), gradient resistance ($F_{grade} = m g \sin\theta$), and rotational inertia coefficients.
- **Electric Motor Modeling:** Integrates a realistic electric motor torque-speed envelope using look-up tables (`Torque_Function.mat`) reflecting constant-torque and field-weakening constant-power operational regions.
- **Acceleration Simulation:** Computes 0–100 km/h acceleration trajectories, torque delivery at the drive wheels through final drive gearing, and energy consumption under dynamic driving profiles.

### 2. Multi-Domain Dynamic Simulations (`simulink/HW2.slx`, `HW3.slx`, `MSD_HW.slx`)
- Time-domain transient response analysis (rise time, peak overshoot, settling time) of mixed electromechanical actuators.
- Control loop design, motor drive interfacing (PWM, H-Bridge drivers), and feedback stability analysis.

### 3. IMU Calibration & Sensor Fusion Case Study (`case-studies/IMU_Case_Study.pdf`)
- In-depth investigation of 6-DOF Inertial Measurement Units (accelerometers and MEMS gyroscopes).
- Evaluates sensor error characteristics: bias instability, random walk noise, temperature drift, and g-sensitivity.
- Analyzes orientation tracking algorithms (complementary filter vs. Kalman filter) to compensate for integration drift and dynamic motion artifacts.

### 4. Smart Automated Trash Bin V-Model Design (`case-studies/Smart_Trash_Bin_V-Model.pdf`)
- Complete systems engineering design following the **V-Model development process**.
- Decomposes stakeholder operational needs into functional subsystem requirements, finite state machines (idle $\to$ approach detection $\to$ lid opening $\to$ fill-level monitoring $\to$ latch/lock), and verification test matrices.

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
├── case-studies/
│   ├── IMU_Case_Study.pdf        # IMU calibration and error compensation study
│   └── Smart_Trash_Bin_V-Model.pdf # Systems engineering V-model design report
└── README.md
```
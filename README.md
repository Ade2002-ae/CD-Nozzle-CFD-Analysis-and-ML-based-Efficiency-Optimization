CD Nozzle Design, CFD Analysis & AI-Based Performance Optimization

Overview
This project demonstrates a complete end-to-end propulsion engineering workflow, combining classical gas dynamics, CFD analysis, and data-driven optimization to determine the most efficient operating altitude for a convergent–divergent (CD) nozzle.
The goal was not to design a space-grade nozzle, but to:
Strengthen fundamentals
Validate theory with CFD
Use AI/ML tools responsibly for optimization
Show how engineering decisions are actually made in practice

1. Problem Definition

A CD nozzle was designed to operate at a target exit Mach number of 3, and its performance was evaluated across different altitudes.
Key questions addressed:
How does thrust and efficiency vary with altitude?
Is there an optimal altitude where the nozzle performs best?
Can data-driven methods identify this operating point more precisely than visual estimation?

2. Theoretical Foundation (Gas Dynamics)

Assumptions:
Compressible, isentropic flow
Perfect gas 
Axisymmetric nozzle
No shocks inside the nozzle (design intent)
Design Inputs
Target exit Mach number: Mₑ = 3
Isentropic relations used:
Area ratio (Aₑ / A*)
Pressure ratio (P / P₀)
Temperature ratio (T / T₀)
These values were obtained from isentropic flow tables for perfect gases.

3. Nozzle Geometry Design

Using the isentropic relations:
Throat diameter and area (A*)
Exit area and diameter (Aₑ)
Area ratio consistent with Mach 3
A straight-walled CD nozzle was selected initially to:
Reduce geometric complexity
Focus on flow physics and performance trends
Keep results interpretable and reproducible
The geometry was created in ANSYS DesignModeler.

4. CFD Setup (ANSYS Fluent)

Solver & Model

Density-based solver
Compressible flow
Ideal gas model
2D axisymmetric setup
Boundary Conditions
Pressure Inlet
Gauge total pressure based on chamber pressure
Total temperature specified
Supersonic/initial gauge pressure provided for numerical stability
Pressure Outlet
Gauge pressure set according to atmospheric pressure at each altitude
Walls
No-slip, adiabatic
Altitude Modeling
Atmospheric pressure was varied to simulate:
Sea level
1–7 km (primary operating range)
Higher altitudes included only for trend observation

5. Data Extraction from CFD

For each altitude, the following quantities were extracted at the nozzle exit:
Static pressure (Pₑ)
Mach number (Mₑ)
Velocity magnitude (Vₑ)
Density (ρₑ)
Static temperature (Tₑ)
Mass flow rate (ṁ)
Net thrust (F)
Thrust was obtained using force reports on nozzle walls.

6. Performance Metrics

Specific Thrust (Efficiency Metric)
To evaluate efficiency independent of mass flow: F/ṁ

This metric was chosen because:
It reflects propulsion efficiency
It is directly comparable across altitudes
It aligns with real propulsion performance analysis

7. Data Processing & Visualization (Python)

The CFD results were exported to CSV and analyzed using Python.

Plots generated:
Thrust vs Altitude
Mass Flow Rate vs Altitude
Exit Mach vs Altitude
Exit Velocity vs Altitude
Exit Temperature vs Altitude
Specific Thrust vs Altitude

These plots revealed:
Rapid efficiency improvement from sea level
Gradual saturation at mid-altitudes
Degradation beyond the nozzle’s design envelope

8. AI / ML-Based Optimization

Why ML was used
Visual inspection often leads to conclusions like:
“Efficiency looks highest somewhere between X and Y.”
Instead, regression was used to:
Fit a smooth curve through CFD data
Identify the exact optimal altitude
Avoid guesswork

Method
Polynomial feature transformation (degree = 3)
Linear regression on transformed data
Optimization performed on Specific Thrust vs Altitude
Physical Constraints Applied

To prevent non-physical solutions:
Optimization constrained to 0–7 km
This range matches the nozzle’s pressure-expansion capability

9. Final Result

Optimal altitude for maximum efficiency:
≈ 6.9–7.0 km
This result:
Matches physical expectations
Respects nozzle geometry limitations
Demonstrates correct pressure-expansion behavior

10. Key Engineering Takeaways

CFD must be interpreted with physics, not blindly trusted
ML is a tool, not a replacement for engineering judgment
Optimization without constraints leads to misleading results
Even simple geometries can yield meaningful insights when analyzed correctly

11. Scope & Limitations

Straight-wall nozzle (no bell contour optimization)
No shock analysis beyond nozzle exit
No combustion modeling
Focused on fundamentals and methodology
These choices were intentional to keep the project clear, educational, and reproducible.

12. Tools Used

ANSYS Fluent – CFD simulation
Python – Data analysis & visualization
scikit-learn – Polynomial regression
Matplotlib / Pandas / NumPy – Plotting & processing

13. Why This Project Matters

This project demonstrates:
Strong understanding of propulsion fundamentals
Ability to bridge theory, simulation, and data science
Engineering decision-making with physical reasoning
Practical use of AI for optimization, not hype

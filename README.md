# 🚖 RideMate: AI-Powered Sustainable Mobility Support

> **Final Submission – Nasscom Tech Developer Hackathon 2025**  
> Team: *TechEase* | Date: September 2025  

RideMate is an AI-powered agent built on **Inya.ai** that automates customer support for urban mobility platforms.  
It handles bookings, payments, app issues, and promotes **eco-friendly ride options** — cutting support costs by **40%** while boosting sustainability.

---

## 🌟 Features
- **24/7 Voice & Text Support** – Handles ride bookings, payments, and troubleshooting.  
- **Eco-Route Integration** – Suggests green routes & calculates CO2 savings.  
- **SMS Confirmations** – Uses Twilio (or equivalent) for instant ride confirmations.  
- **Multi-Agent Orchestration** – Modular flow with decision, eco-handler, and SMS nodes.  
- **Scalable & Cost-Efficient** – Reduces cost per query from ₹50 ➝ ₹0.10.

---

## 🏗️ Architecture
The agent uses a **multi-node decision flow**:

```mermaid
flowchart TD
    A[Start Node] --> B[User Input]
    B --> C{Decision: Eco or Standard?}
    C -->|BOOK_GREEN| D[Eco_Route_Handler]
    C -->|BOOK_STANDARD| E[Standard_Booking_Agent]
    D --> F[Ride_Confirmer]
    E --> F[Ride_Confirmer]
    F --> G[SMS_Confirmer]
    G --> H[End Node (EOC)]


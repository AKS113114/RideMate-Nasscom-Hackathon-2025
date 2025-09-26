# 🏗️ RideMate Architecture

**Flow name:** `Eco_Route_Handler.json`  
**Project:** RideMate — AI-Powered Sustainable Mobility Support

---

## 🔹 High-level flow (Mermaid)
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





\# 🏗️ RideMate Architecture



This document explains the agent-chain architecture used in the \*\*Eco\_Route\_Handler\*\* flow.



---



\## 🔹 Flow (Mermaid Diagram)



```mermaid

flowchart TD

&nbsp;   A\[Start Node] --> B\[User Input]

&nbsp;   B --> C{Decision: Eco or Standard?}

&nbsp;   C -->|BOOK\_GREEN| D\[Eco\_Route\_Handler]

&nbsp;   C -->|BOOK\_STANDARD| E\[Standard\_Booking\_Agent]

&nbsp;   D --> F\[Ride\_Confirmer]

&nbsp;   E --> F\[Ride\_Confirmer]

&nbsp;   F --> G\[SMS\_Confirmer]

&nbsp;   G --> H\[End Node (EOC)]




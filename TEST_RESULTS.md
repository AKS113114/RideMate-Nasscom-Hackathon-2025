\# ✅ RideMate Test Results



This document contains test cases and outcomes for `flows/Eco\_Route\_Handler.json`.



---



\## 🔹 Functional Tests



| Test Case ID | Input Query                | Expected Behavior                                                                 | Actual Result                     | Status |

|--------------|----------------------------|-----------------------------------------------------------------------------------|-----------------------------------|--------|

| T1           | "Book a green ride"        | Routes to \*\*Eco\_Route\_Handler\*\*, returns eco-route + CO2 savings, SMS sent        | Ride confirmed with CO2 savings   | ✅ Pass |

| T2           | "I need a sustainable cab" | Detected as eco → \*\*Eco\_Route\_Handler\*\*, returns JSON with `eco\_route\_details`    | Eco route booked, SMS confirmed   | ✅ Pass |

| T3           | "Book a cab"               | Routes to \*\*Standard\_Booking\_Agent\*\*, booking confirmed, SMS sent                 | Standard booking confirmed, SMS   | ✅ Pass |

| T4           | "I need a taxi"            | Standard booking flow triggered, no CO2 savings shown                             | Standard booking confirmed, SMS   | ✅ Pass |

| T5           | "Sing a song"              | Not recognized → fallback / end or escalate                                       | Fallback/End node triggered       | ✅ Pass |



---



\## 🔹 Validation Script Output



Executed using:

```bash

python scripts/test\_agent.py




























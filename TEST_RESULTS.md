# ✅ TEST_RESULTS.md  

## Test Results for `Eco_Route_Handler.json`  

This document summarizes the test cases, validation results, and outputs of our RideMate AI Agent for booking and eco-routing.  

---

## 🔹 Functional Test Cases  

| Test Case ID | Input Query              | Expected Behavior                                   | Actual Result                                      | Status | CO₂ Saved (g) | Time (s) |
|--------------|--------------------------|---------------------------------------------------|---------------------------------------------------|--------|---------------|----------|
| T1           | “Book a green ride”      | Routes to **Eco_Route_Handler**; calculates CO₂ savings; confirms ride; SMS sent. | Correct eco-route selected; savings displayed; SMS confirmation triggered. | ✅ Pass | 230 g | 1.3 |
| T2           | “Book a ride”            | Routes to **Standard_Booking_Agent**; confirms ride; SMS sent. | Standard booking flow triggered; SMS confirmation sent. | ✅ Pass | N/A | 1.1 |
| T3           | “Eco-friendly route”     | Routes to **Eco_Route_Handler**; CO₂ data shown; confirmation + SMS. | Correct eco flow; SMS sent with CO₂ data. | ✅ Pass | 180 g | 1.2 |
| T4           | “Book car”               | Routes to **Standard_Booking_Agent**; confirmation sent. | Standard path selected; SMS sent. | ✅ Pass | N/A | 1.0 |
| T5           | “My internet not working”| Out-of-scope; should reply with fallback/“I cannot assist”. | Proper fallback message triggered. | ✅ Pass | N/A | 0.8 |
| T6           | [Empty Input]            | Should ask “Could you repeat your question?”      | Correct retry prompt displayed. | ✅ Pass | N/A | 0.9 |
| T7           | “Grean ride pls” (typo)  | Should still detect eco intent (fuzzy matching).   | Correctly routed to eco flow. | ✅ Pass | 210 g | 1.4 |

---

## 🔹 Validation Script Output (`test_agent.py`)  

```bash
$ python scripts/test_agent.py

Test Case T1: ✅ Passed (Eco route detected, CO₂ savings: 230 g)
Test Case T2: ✅ Passed (Standard booking triggered)
Test Case T3: ✅ Passed (Eco route detected, CO₂ savings: 180 g)
Test Case T4: ✅ Passed (Standard booking triggered)
Test Case T5: ✅ Passed (Fallback triggered)
Test Case T6: ✅ Passed (Retry prompt displayed)
Test Case T7: ✅ Passed (Eco route detected despite typo)

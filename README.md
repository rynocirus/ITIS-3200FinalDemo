# ITIS-3200FinalDemo
# BOLA Attack & Defense Simulation

## Overview

This project demonstrates a **Broken Object Level Authorization (BOLA)** vulnerability using a simulated API. It shows how a system can allow unauthorized access to data and how proper authorization checks can prevent it.

The demo is inspired by real-world incidents such as the 2023 breach involving T-Mobile.

---

## Purpose

The goal is to show the difference between:

* **Authentication** (verifying who a user is through login)
* **Authorization** (verifying what a user is allowed to access)

A BOLA vulnerability occurs when a system authenticates a user but fails to verify whether they are authorized to access specific data.

---

## Demo Explanation

### Failure Case (Vulnerable API)

* The system allows access to any user’s data using an ID
* No authorization check is performed

Example:

```
GET /api/user/2 → 200 OK
Returns another user’s data
```

---

### Successful Case (Secure API)

* The system checks if the user is authorized to access the data
* Unauthorized requests are blocked

Example:

```
GET /api/user/2 → 403 Forbidden
Access denied
```

---

## How to Run

1. Save the code as `BOLA2.py`
2. Run in a terminal:

```
python BOLA2.py
```

---

## Demo Login

```
Username: Alice   Password: alice123
Username: Bob     Password: bob123
```

---

## How to Demonstrate

1. Log in as Alice
2. Request user ID 2
3. Compare results:

   * Vulnerable system shows Bob’s data
   * Secure system blocks access

---

## Key Takeaway

BOLA vulnerabilities occur when systems fail to enforce authorization checks. Even if a user is authenticated, they should only be able to access their own data.

---

## Note

This project is for educational purposes only.

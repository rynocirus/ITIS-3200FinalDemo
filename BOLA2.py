# ===============================
# BOLA Attack & Defense Simulation
# ===============================

# Fake database
users = {
    "Alice": {"id": 1, "grade": "A", "password": "alice123"},
    "Bob": {"id": 2, "grade": "B", "password": "bob123"}
}


# ===============================
# LOGIN SYSTEM
# ===============================
def login():
    print("=== SECURE SYSTEM LOGIN ===")

    for attempt in range(3):
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            print(f"\n[✔] Login successful. Welcome, {username}!\n")
            return username
        else:
            print("[✘] Invalid credentials. Try again.\n")

    print("Too many failed attempts. Exiting.")
    return None


# ===============================
# FAILURE CASE (BOLA VULNERABLE)
# ===============================
def vulnerable_api(logged_in_user, requested_id):
    print("\n--- VULNERABLE API (BOLA) ---")

    print(f"\nLogged in as: {logged_in_user}")
    print(f"Sending request: GET /api/user/{requested_id}")

    # ❌ No authorization check
    for name, data in users.items():
        if data["id"] == requested_id:
            print("\nResponse: 200 OK ❌")
            print("{")
            print(f'  "name": "{name}",')
            print(f'  "grade": "{data["grade"]}"')
            print("}")
            print(f"\nLOG: {logged_in_user} accessed {name}'s data WITHOUT authorization ❌")
            return

    print("\nResponse: 404 Not Found")


# ===============================
# SECURE CASE (PROTECTED API)
# ===============================
def secure_api(logged_in_user, requested_id):
    print("\n--- SECURE API (PROTECTED) ---")

    print(f"\nLogged in as: {logged_in_user}")
    print(f"Sending request: GET /api/user/{requested_id}")

    # ✅ Authorization check
    for name, data in users.items():
        if data["id"] == requested_id:

            if name == logged_in_user:
                print("\nResponse: 200 OK ✅")
                print("{")
                print(f'  "name": "{name}",')
                print(f'  "grade": "{data["grade"]}"')
                print("}")
                print("\nLOG: Authorized access ✅")
            else:
                print("\nResponse: 403 Forbidden 🚫")
                print('{ "error": "Access denied" }')
                print("\nLOG: Unauthorized access attempt BLOCKED ✅")
            return

    print("\nResponse: 404 Not Found")


# ===============================
# MAIN DEMO
# ===============================
def run_demo():
    user = login()

    if not user:
        return

    print("=== ATTACK SIMULATION ===")
    print("Try accessing another user's data by changing the ID.\n")

    try:
        requested_id = int(input("Enter user ID to request (1 or 2): "))
    except ValueError:
        print("Invalid input.")
        return

    print("\n==============================")
    print(" SAME REQUEST → DIFFERENT RESULTS ")
    print("==============================")

    # Run both versions with SAME request
    vulnerable_api(user, requested_id)
    secure_api(user, requested_id)


# Run program
run_demo()
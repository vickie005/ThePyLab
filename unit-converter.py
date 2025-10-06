# ----- Conversion Functions -----
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def km_to_miles(km): return km * 0.621371
def miles_to_km(mi): return mi / 0.621371
def kg_to_pounds(kg): return kg * 2.20462
def pounds_to_kg(lb): return lb / 2.20462

# ---- Load History from File ----
history = []
try:
    with open("history.txt", "r") as file:
        history = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    # File does not exist yet
    pass

# ---- Main Loop ----
while True:
    print("\n--- Unit Converter ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Kilometers → Miles")
    print("4. Miles → Kilometers")
    print("5. Kilograms → Pounds")
    print("6. Pounds → Kilograms")
    print("7. View conversion history")
    print("8. Exit")

    try:
        choice = int(input("Choose conversion (1-8): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number (1-8)")
        continue

    if choice == 8:
        print("👋🏼 Exiting unit converter... Goodbye!")
        break

    elif choice == 7:
        if history:
            print("\n--- Conversion History ---")
            for record in history:
                print(record)
        else:
            print("\nNo conversions yet.")
        continue

    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    # ---- Perform Conversion ----
    if choice == 1:
        result = f"{value}°C = {c_to_f(value):.2f}°F"
    elif choice == 2:
        result = f"{value}°F = {f_to_c(value):.2f}°C"
    elif choice == 3:
        result = f"{value} km = {km_to_miles(value):.2f} miles"
    elif choice == 4:
        result = f"{value} miles = {miles_to_km(value):.2f} km"
    elif choice == 5:
        result = f"{value} kg = {kg_to_pounds(value):.2f} lbs"
    elif choice == 6:
        result = f"{value} lbs = {pounds_to_kg(value):.2f} kg"
    else:
        print("❌ Invalid choice!")
        continue

    # ---- Display & Save ----
    print("✅", result)
    history.append(result)

    # Save to file
    with open("history.txt", "a") as file:
        file.write(result + "\n")

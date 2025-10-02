def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def km_to_miles(km): return km * 0.621371
def miles_to_km(mi): return mi / 0.621371
def kg_to_pounds(kg): return kg * 2.20462
def pounds_to_kg(lb): return lb / 2.20462

print("Unit Converter")
print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")
print("3. Kilometers → Miles")
print("4. Miles → Kilometers")
print("5. Kilograms → Pounds")
print("6. Pounds → Kilograms")

choice = int(input("Choose conversion (1-6): "))
value = float(input("Enter value: "))

if choice == 1: print(f"{value}°C = {c_to_f(value):.2f}°F")
elif choice == 2: print(f"{value}°F = {f_to_c(value):.2f}°C")
elif choice == 3: print(f"{value} km = {km_to_miles(value):.2f} miles")
elif choice == 4: print(f"{value} miles = {miles_to_km(value):.2f} km")
elif choice == 5: print(f"{value} kg = {kg_to_pounds(value):.2f} lbs")
elif choice == 6: print(f"{value} lbs = {pounds_to_kg(value):.2f} kg")
else: print("Invalid choice!")


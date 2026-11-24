
# 1. Speed Calculation
distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))
speed = distance / time
print("Speed =", speed, "m/s")


# 2. Force Calculation (Newton's Second Law)
mass = float(input("\nEnter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s²): "))
force = mass * acceleration
print("Force =", force, "N")


# 3. Work Done
force = float(input("\nEnter force (N): "))
distance = float(input("Enter distance (m): "))
work = force * distance
print("Work Done =", work, "J")


# 4. Density Calculation
mass = float(input("\nEnter mass (kg): "))
volume = float(input("Enter volume (m³): "))
density = mass / volume
print("Density =", density, "kg/m³")


# 5. Kinetic Energy
mass = float(input("\nEnter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
kinetic_energy = 0.5 * mass * velocity**2
print("Kinetic Energy =", kinetic_energy, "J")


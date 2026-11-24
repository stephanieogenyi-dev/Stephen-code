
# Function to calculate velocity
def calculate_velocity(distance, time):
    velocity = distance / time
    print("Velocity is:", velocity)


# Function to calculate area of a circle
def calculate_area(radius):
    area = 3.14 * radius * radius
    print("Area of circle is:", area)


# Ask user to choose
choice = input("Enter 'v' to calculate velocity or 'a' to calculate area: ")

if choice == 'v':
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))

    calculate_velocity(distance, time)

elif choice == 'a':
    radius = float(input("Enter radius: "))

    calculate_area(radius)

else:
    print("Invalid choice!")

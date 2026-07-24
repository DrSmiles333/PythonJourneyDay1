Max = 0
Min = 135
Count = 0
Total = 0
while True:
    knee_flexion = input("Enter knee flexion in degrees: ")
    if knee_flexion.lower() == "done":
        break
    degrees = int(knee_flexion)
    if degrees < 0 or degrees > 135:
        print("Invalid input. Please enter a value between 0 and 135 degrees.")
    else:
        print(f"Knee flexion is {degrees} degrees.")
        if degrees >= Max:
            Max = degrees
        if degrees <= Min:
            Min = degrees
        Count += 1
        Total += degrees
if Count > 0:
    print(f"Maximum knee flexion recorded: {Max} degrees.")
    print(f"Minimum knee flexion recorded: {Min} degrees.")
    print(f"Average knee flexion recorded: {Total / Count} degrees.")
    print(f"Total number of knee flexion measurements: {Count}.")
else:
    print("No valid knee flexion measurements recorded.")
total = 0
sets = 0
while True:
    entry = input("Enter reps completed this set (or 'done' to finish): ")
    if entry == 'done':
        break
    reps = int(entry)
    if reps < 0:
        print("Please enter a non-negative number of reps.")
    else:
        total = total + reps
        sets = sets + 1
        if sets == 1:
            label = "set"
        else:
            label = "sets"
        print(f"You have completed {total} reps in {sets} {label} so far.")

print(f"You completed {total} reps in {sets} sets.")


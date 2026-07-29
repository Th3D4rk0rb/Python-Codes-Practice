passed_count = 0

for i in range(1, 6):
    score = float(input(f"What was your score #{i}? "))
    if score >= 75:
        passed_count += 1

print(f"You passed {passed_count} classes")

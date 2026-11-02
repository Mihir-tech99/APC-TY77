with open("attendance.txt", "r") as file:
    for line in file:
        roll, name, present, total = line.strip().split(",")

        present = int(present)
        total = int(total)

        percentage = (present / total) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print("Below 75%")
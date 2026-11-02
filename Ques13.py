word = input("Enter the word to search: ")
count = 0
line_numbers = []
with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        words = line.split()
        for w in words:
            if w.lower() == word.lower():
                count += 1
                line_numbers.append(line_no)
print("Number of occurrences:", count)
print("Line numbers:", line_numbers)
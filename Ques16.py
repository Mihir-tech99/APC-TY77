with open("student.txt", "r") as file:
    content = file.read()
content = content.upper()
with open("uppercase.txt", "w") as file:
    file.write(content)
print("Uppercase text saved in uppercase.txt")
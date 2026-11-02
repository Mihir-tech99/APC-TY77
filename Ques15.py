with open("program.py", "r") as file:
    lines = file.readlines()
with open("program_without_comments.py", "w") as file:
    for line in lines:
        if "#" in line:
            line = line.split("#")[0]
        file.write(line)
print("Comments removed successfully.")
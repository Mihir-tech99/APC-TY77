with open("file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("file2.txt", "r") as file2:
    lines2 = file2.readlines()


if lines1 == lines2:
    print("Both files have identical contents.")

else:
    print("Files are different.")

    minimum = min(len(lines1), len(lines2))

    found = False

    for i in range(minimum):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i], end="")
            print("File 2:", lines2[i], end="")
            found = True
            break

    if not found:
        print("One file has extra lines.")
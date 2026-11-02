with open("student.txt", "r") as file:
    content = file.read()
words = content.split()
longest = max(words, key=len)
print("Longest word:", longest)
print("Length:", len(longest))
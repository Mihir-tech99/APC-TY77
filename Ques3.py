info=input("Enter additional info:")
with open("student.txt","a")as file:
    file.write(info)

    print("Additional info added successfully!!")
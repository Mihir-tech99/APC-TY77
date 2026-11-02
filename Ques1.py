name=input("Enter your name:")
roll_no=input("Enter your roll no:")
branch=input("Enter Branch:")
Sem=input("Enter Semester:")

with open ("student.txt","w")as file:
    file.write("Student name:"+name+"\n")
    file.write("Student rollno:"+roll_no+"\n")
    file.write("Branch:"+branch+"\n")
    file.write("Current Semester:"+Sem+"\n")

    print("Students details added to student.txt successfully!!")



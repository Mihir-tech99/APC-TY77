count=0
with open("student.txt","r")as file:
    for line in file:
        count=count+1
    print(count)     
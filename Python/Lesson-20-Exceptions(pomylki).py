import sys

filename = "Lesson_List.txt" ### Lesson/Lessons (add "s" in end)

while True:
    try:
        print("Inside TRY")
        myfile=open(filename, mode='r', encoding='utf_8')
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        filename=input("Enter correct file name! :")

    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
print("===================EOF===============")
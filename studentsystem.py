import re
import os
filename = "students.txt"


def menu():
    # Output menu
    print("""
    -------------- Welcome to Student Information Management Sytem -----------------
              ========================= Menu =========================
                        1. Enter new student information
                        2. Search student information
                        3. Delete student information
                        4. Modify student information
                        5. Sort
                        6. Total number of students
                        7. Show all student information
                        0. Exit
            =========== Enter number to select functionality ===========
                """)


def save(student):
    try:
        students_txt = open(filename, "a")
    except Exception as e:
        students_txt = open(filename, "w")
    for info in student:
        students_txt.write(str(info)+"\n")
    students_txt.close()


def insert():
    studentList = []
    mark = True
    while mark:
        id = input("Enter Student ID: ")
        if not id:
            break
        name = input("Enter Student Name: ")
        if not name:
            break
        try:
            english = int(input("Enter English Grade: "))
            math = int(input("Enter Math Grade: "))
            history = int(input("Enter History Grade: "))
            art = int(input("Enter Art Grade: "))
        except:
            print("Value Invalid. Not Integer. Please Enter Again.")
            continue
        student = {"id": id, "name": name, "english": english,
                   "math": math, "history": history, "art": art}
        studentList.append(student)
        inputMark = input("Input another student info? (Y/N): ")
        if inputMark.lower() == "y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("Student Information Recorded!")


def delete():
    mark = True
    while mark:
        studentId = input("Enter ID of student you want to delete: ")
        if studentId != "":
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d["id"] != studentId:
                            wfile.write(str(d)+'\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID Student {} is deleted".format(studentId))
                    else:
                        print("ID Student {} is not found".format(studentId))
            else:
                print("No student information reocorded")
                break
            show()
            inputMark = input("Continue deleting? (Y/N): ")
            if inputMark.lower() == "y":
                mark = True
            else:
                mark = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    studentId = input("Enter ID of student you want to modify: ")
    with open(filename, 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d["id"] == studentId:
                print("ID Student {} found".format(studentId))
                while True:
                    try:
                        d["name"] = input("Enter name: ")
                        d["english"] = int(input("Enter English Grade: "))
                        d["math"] = int(input("Enter Math Grade: "))
                        d["history"] = int(input("Enter History Grade: "))
                        d["art"] = int(input("Enter Art Grade: "))
                    except:
                        print("Error, please enter again....")
                    else:
                        break
                student = str(d)
                wfile.write(student+'\n')
                print("Modification succeed!")
            else:
                wfile.write(student)
    mark = input("Continue modifying? (Y/N): ")
    if mark.lower() == "y":
        modify()

def show_student(studentList):
    if not studentList:
        print("No Student Information Found!")
        return
    else:
        format_title="{:^6}{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}"
        print(format_title.format("ID", "Name", "English", "Math", "History", "Art", "Total Grade"))
        
        format_data="{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
        for info in studentList:
            print(format_data.format(info.get("id"), info.get("name"), info.get("english"), info.get("math"),
            info.get("history"), info.get("art"), 
            str(info.get("english")+info.get("math")+info.get("history")+info.get("art")).center(12)))

def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode=int(input("Enter 1 for searching based on name, enter 2 for search based on ID: "))
            if mode==1:
                name=input("Enter Student Name: ")
            elif mode==2:
                id=input("Enter Student ID: ")
            else:
                print("Error input, please enter again!")

            with open(filename, 'r') as rfile:
                students= rfile.readlines()
                for list1 in students:
                    d = dict(eval(list1))
                    if mode==1:
                        if d["name"]==name:
                            student_query.append(d)
                    else:
                        if d["id"]==id:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark=input("Continue searching? (Y/N): ")
                if inputMark.lower()=="y":
                    mark=True
                else:
                    mark=False
        else:
            print("No Student Information is Stored!")
            return

def show():
    student_new=[]
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old= rfile.readlines()
        for list1 in student_old:
            d = dict(eval(list1))
            student_new.append(d)
        if student_new:
            show_student(student_new)
        else:
            print("No Student Information is Stored!")
    else:
        print("No Student Information is Stored!")

def total():
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
                student_old= rfile.readlines()
        if student_old:
            print("Total {} Student Recorded".format(len(student_old)))
        else:
            print("No Student Information is Stored!")
    else:
        print("No Student Information is Stored!")

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
                student_old= rfile.readlines()
                student_new=[]
                for list1 in student_old:
                    student_new.append(dict(eval(list1)))
    else:
        return

    ascORdesc=int(input("Enter 0 for ascending order, enter 1 for descending order: "))
    if ascORdesc==0:
        ascORdescBool=True
    elif ascORdesc==1:
        ascORdescBool=False
    else:
        print("Invalid input, please enter again!")
        sort()
    mode=int(input("""
    Enter 1 for sorting based on English Grade,
    Enter 2 for sorting based on Math Grade, 
    Enter 3 for sorting based on Hisotry Grade,
    Enter 4 for sorting based on Art Grade, 
    Enter 0 for sorting based on Total Grade: """))
    if mode==1:
        student_new.sort(key=lambda x:x["english"], reverse=ascORdescBool)
    elif mode==2:
        student_new.sort(key=lambda x:x["math"], reverse=ascORdescBool)
    elif mode==3:
        student_new.sort(key=lambda x:x["history"], reverse=ascORdescBool)
    elif mode==4:
        student_new.sort(key=lambda x:x["art"], reverse=ascORdescBool)
    elif mode==0:
        student_new.sort(key=lambda x:x["english"]+x["math"]+x["history"]+x["art"], reverse=ascORdescBool)
    else:
        print("Invalid input, please enter again!")
        sort()
    show_student(student_new)

def main():
    ctrl = True
    while (True):
        menu()
        option = input("Please choose: ")
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print("You existed the Student Information Management Sytem! ")
                ctrl = False
                break
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()
        else:
            print("Invalid input, please enter again!")
            main()

main()
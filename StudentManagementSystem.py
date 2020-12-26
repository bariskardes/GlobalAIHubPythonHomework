#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Bu kodu Burhan ÖK isimli kullanıcının GitHub hesabından aldım. Kendisi sağ olsun açıktan paylaşmış. 
Kodu kendim yazamadığım için inceleme maksadıyla repository'me ekliyorum, bilginize..."""

#@title Student Managment System
print("Wellcome to student managment system\n    \n    Choice 1: Create a new student\n    Choice 2: Login to student managment system\n    Choice 3: Take your courses, also you should take minimum 3 and maximun 5 courses\n    Choice 4: Choose a course from the courses you take for the exam\n    Choice 5: Show your exam results\n    Choice 6: Show your grade\n    Choice 7: Delete student\n    Choice 8: Shootdown the student manegment system\n")
print("*************************************")
while True:
    choice = int(input("Select your choice : "))
    if choice == 1:
        name = input("Enter your name : ")
        lastname = input("Enter your lastname : ")
        student = SMS(name,lastname)

        print("*************************************")

    elif choice == 2:
        try:
            student.login()
            print("*************************************")
        except Exception as inst:
            print("Oops! You should create a new student account")
            print("*************************************")
    elif choice == 3:
        try:
            if student.check_login == False:
                print("Please create an account or login")
                print("*************************************")
            else:
                if len(student.courses) != 0:
                    print("You allready take courses!!!")
                    print("*************************************")
                else:
                    student.takeCourses()
                    print("*************************************")
        except Exception as inst:
            print("Oops! You should create a new student account")
            print("*************************************")
    
    elif choice == 4:
        try:
            if student.check_login == False:
                print("Please create an account or login")
                print("*************************************")
            else:
                if len(student.courses) == 0:
                    print("Please take your courses")
                    print("*************************************")
                else:
                    student.selectCourse()
                    print("*************************************")
        except Exception as inst:
            print(inst)
            print("*************************************")
    elif choice == 5:
        try:
            if student.check_login == False:
                print("Please create an account or login")
                print("*************************************")
            else:
                if len(student.courses) == 0:
                    print("Please take your courses")
                    print("*************************************")
                elif len(student.grades) == 0:
                    print("Please make your exam")
                    print("*************************************")
                else:
                    for i in student.grades.keys():
                        print(f" {i} : {student.grades[i]} ")
                    print("*************************************")

        except Exception as inst:
            print(inst)
            print("*************************************")

    elif choice == 6:
        try:
            if student.check_login == False:
                print("Please create an account or login")
                print("*************************************")
            else:
                if len(student.courses) == 0:
                    print("Please take your courses")
                    print("*************************************")
                elif len(student.grades) == 0:
                    print("Please make your exam")
                    print("*************************************")
                else:
                    print(f"Your {student.course} grade :  {student.grade} ")
                    print("*************************************")

        except Exception as inst:
            print(inst)
            print("*************************************")
      
    elif choice == 7:
        del student
        print("Your student account is deleted")
        print("*************************************")
    
    elif choice == 8:
        print("Student Managment System Shooting Down")
        print("*************************************")
        break


# In[1]:


#@title Create Student Managment System Class
import random
class SMS(object):
    def __init__(self, name, lastname):
        self.name = name.lower()
        self.lastname = lastname.lower()
        self.courses_list = ["Deep Learning","Python","Machine Learning","Computer Vision","Reinforcement Learning"]
        self.courses = []
        self.grades = {}
        self.grade = 0
        self.course = ""
        self.check_login = False
        print("Registration completed successfully!!!")
    
    def login(self):
        for i in range(3):
            name  = input("Enter your name : ")
            lastname  = input("Enter your lastname : ")
            
            if name.lower() == self.name and lastname.lower() == self.lastname:
                print("Wellcome...")
                self.check_login = True
                break
            else:
                if i == 2:
                    print("Please try again later")
                else:
                    print("Your informations incorrect\n\ Please try again")
    def takeCourses(self):
        print("Courses List : ")

        for i in range(len(self.courses_list)):
            print(f"{i+1}. {self.courses_list[i]}")

        course_num = int(input("How many courses will you take? : "))
        if course_num < 3 or course_num > 5:
            return "You failed in class"
        else:
            for i in range(course_num):
                course = input(f"Write your {i+1}. course name : ")
                self.courses.append(course.title())
        print("You took following courses")
        for i in range(course_num):
            print(f"{i+1}. {self.courses[i]}")
    
    def selectCourse(self):
        print("Your courses : ")

        for i in range(len(self.courses)):
            print(f"{i}. {self.courses[i]}")
        
        while True:
            self.course = (input("Enter a course name for exam : ")).title()
            if self.course in self.courses:
                midterm = random.randint(0,100)
                final = random.randint(0,100)
                project = random.randint(0,100)

                self.grades["midterm"] = midterm
                self.grades["final"] = final
                self.grades["project"] = project

                self.grade = midterm*0.3 + final*0.5 + project*0.2

                if self.grade > 90:
                    print("Your grade AA - passed")
                elif 70 < self.grade < 90:
                    print("Your grade BB - passed")
                elif 50 < self.grade < 70:
                    print("Your grade CC - passed")
                elif 30 < self.grade < 50:
                    print("Your grade DD - passed")
                elif self.grade < 30:
                    print("Your grade FF - failure")
                
                break
            else:
                print(f"There isn't a course named {self.course} in your courses.")


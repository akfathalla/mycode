#!/usr/bin/env python3
""" CLASSES WERE OBTAINED FROM UH.EDU WEBSITE"""
# All classes are contained into separate dictionaries, based on class level (core, CS, and electives).
# Notice here, on each dictionary, there is multiple keys (classes), 
# with their values being strings to define class name, and number of credits

core_classes = {'MATH-2413':['Calculus-I', 4], 'MATH-2414':['Calculus-II', 4], 'MATH-3339':['Statistics', 3]}
cs_classes = {'COSC-1336': ['Computer Science and Programming', 3],
              'COSC 1437':['Introduction to Programming', 4],
              'COSC 2436':['Programming and Data Structures', 4],
              'COSC 2425':['Computer Organization and Architecture', 4],
              'COSC 3320':['Algorithms and Data Structures', 4],
              'COSC 3340':['Introduction to Automata and Computability', 3],
              'COSC 3360':['Fundamentals of Operating Systems', 3], 'COSC 3380':['Database Systems', 3] }

core_electives = {'MATH 2318':['Linear Algebra', 3],
                  'MATH 3321':['Engineering Mathematics', 3]}

cs_electives = {'COSC 2305':['Computing Structures', 3], 'MATH 2305':['Discrete Mathematics', 3]}
sde_electives = {'COSC 4351':['Fundamentals of Software Engineering', 4], 'COSC 4353':['Software Design', 3]}

# Enrollment function
def enroll():
 enrolled = []
 print("====== Class Levels =======\n1: Core Classes\n2: Computer Science Classes (CS)\n3: Electives\n")
 level = input("Please type class level : ")
 if level == '1':
    enroll_core()
 elif level == '2':
    enroll_cs()
 elif level == '3':
    enroll_elective()
 else: 
  print("Incorrect option")
  
  enrolled.append("test1")
    print(enrolled)
    

 print("Please select classes to enroll to.", "\n", "Min cridits=6, Max credits=12")
 
def main():
    print("+++++++ CORE CLASSES +++++++\n")
    for key, values in core_classes.items():
        print("\n" , key, "   ", end='')
        for i in values:
            print(i, "   ", end='')
    
enroll()
main()

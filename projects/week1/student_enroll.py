#!/usr/bin/env python3
""" CLASSES WERE OBTAINED FROM UH.EDU WEBSITE"""
# All classes are contained into separate dictionaries, based on class level (core, CS, and electives).
# Notice here, on each dictionary, there is multiple keys (classes), 
# with their values being strings to define class name, and number of credits
# Print function

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


# This function will be used to print out classes and allow a student to enroll in classes for the semester

def enroll_classes(class_level):
    enrolled_classes = {} # An empty dictionary to add classes to
    j = 1
    for key, values in class_level.items():
      print("\n", j , ":", key, "   ", end='')
      for i in values:
       print(i, end='')
      j += 1
    class_option = input("\nPlease select class from the menu: ")
    enrolled_classes.update(class_level)
    print(enrolled_classes)
    return None


# This function will help the student move throughout the menu

def class_menu():
  print("====== Class Levels =======\n1: Core Classes\n2: Computer Science Classes (CS)\n3: Electives\n")
  level = input("Please type class level : ")
  if level == '1':
    print("+++++++ CORE CLASSES +++++++\n")
    enroll_classes(core_classes)
    
  elif level == '2':
    enroll_classes(cs_classes)
    print("+++++++ Computer Science CLASSES +++++++\n")
  elif level == '3':
    print("+++++++ Core Electives +++++++\n")
    enroll_classes(core_electives)
  elif level == '4':
    print("+++++++ CS Electives +++++++\n")
    enroll_classes(cs_electives)
  elif level == '5':
    print("+++++++SDE Electives +++++++\n")
    enroll_classes(sde_electives)
  else: 
   print("Incorrect option, please try again!"), enroll()

  return None  

# The main function brings up the main menu and calls other functions accordingly.

def main():
  print("\n########## MAIN Menu ###########\n1: Enroll in classes\n2: Update grades \n3: Check GPA")
  action = input("\nPlease enter your main option: ")
  if action == '1':
   class_menu()
  elif action == '2':
    update_grades()
  elif action == '3':
   calculate_gpa() 
  else:
    print("Incorrect choice, please try again!"), main()

if __name__ == '__main__':
 main()


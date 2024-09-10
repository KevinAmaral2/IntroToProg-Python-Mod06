# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   KAmaral,9/3/24,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = "" # Hold the choice made by the user

#Define File Processing Class and Associated Functions

class FileProcessor:
    """A class for similar functions that relate to file processing
    ChangeLog: (Kevin, 9/3, Created Class)
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from the JSON file
        ChangeLog: (Kevin, 9/3, Created Function)
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: Unable to read the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to the JSON file
        ChangeLog: (Kevin, 9/3, Created Function)
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: could not write to file\n"
            message += "Please check that the file is not open by a different program"
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


#Define Input/Output Class and Associated Functions

class IO:
    """A class for similar functions that relate to input and output
    ChangeLog: (Kevin, 9/3, Created Class)
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function outputs error messages
        ChangeLog: (Kevin, 9/3, Created Function)
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function outputs the menu for the user
        ChangeLog: (Kevin, 9/3, Created Function)
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """This function prompts for user input based on the menu
        ChangeLog: (Kevin, 9/3, Created Function)
        """
        choice = "0"

        try:
            choice = input("Please select your choice: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please select a valid option")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """This function outputs student info based on input
        ChangeLog: (Kevin, 9/3, Created Function)
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the Student's first and last name, with course name
        ChangeLog: (Kevin, 9/3, Created Function)
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Please only use letters")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Please only use letters")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was an issue with the data entered", error=e)
        return student_data


#Outlining the Main Program

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while (True):

#Present the menu of choices

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break
    else:
         print("Please select a valid option")

print("Program Ended")
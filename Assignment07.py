# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Bani Bedi,03/10/2024,Created Homework Assignment
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
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# TODO Create a Person Class
# TODO Add first_name and last_name properties to the constructor (Done)
# TODO Create a getter and setter for the first_name property (Done)
# TODO Create a getter and setter for the last_name property (Done)
# TODO Override the __str__() method to return Person data (Done)

# TODO Create a Student class the inherits from the Person class (Done)
# TODO call to the Person constructor and pass it the first_name and last_name data (Done)
# TODO add a assignment to the course_name property using the course_name parameter (Done)
# TODO add the getter for course_name (Done)
# TODO add the setter for course_name (Done)
# TODO Override the __str__() method to return the Student data (Done)


class Person:
    """
    A collection of functions and variables for people

    ChangeLog: (Who, When, What)
    BaniBedi,3.10.2024,Created Class
    """
    def __init__(self, first_name: str, last_name: str):
        """ This constructor creates a person

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param first_name: string with the first name of the person
        :param last_name: string with the last name of the person
        """

        self.first_name = first_name
        self.last_name = last_name

    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        """ getter for first_name

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function
        """
        return self.__first_name.title()  # Optional formatting code

    @first_name.setter
    def first_name(self, value: str):
        """ setter for first_name

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param value: string with the first name of the person
        """
        if value.isalpha() or value == "":  # Optional validation code
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """ getter for last_name

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function
        """
        return self.__last_name.title()  # Optional formatting code

    @last_name.setter
    def last_name(self, value: str):
        """ setter for last_name

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param value: string with the last name of the person
        """
        if value.isalpha() or value == "":  # Optional validation code
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f'Person {self.first_name} {self.last_name}'


class Student(Person):
    """
    A collection of functions and variables for students

    ChangeLog: (Who, When, What)
    BaniBedi,3.10.2024,Created Class
    """
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        """ This constructor creates a student

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param first_name: string with the first name of the student
        :param last_name: string with the last name of the student
        :param course_name: string with the course of the student
        """
        super().__init__(first_name=first_name, last_name=last_name)

        self.course_name = course_name

    @property  # (Use this decorator for the getter or accessor)
    def course_name(self):
        """ getter for course

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function
        """
        return self.__course_name.title()  # Optional formatting code

    @course_name.setter
    def course_name(self, value: str):
        """ setter for first_name

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param value: string with the first name of the person
        """
        self.__course_name = value

    def __str__(self):
        return f'Student {self.first_name} {self.last_name} is enrolled in {self.course_name}'


class FileProcessor:
    """
    A collection of functions to save and read file data

    ChangeLog: (Who, When, What)
    BaniBedi,3.10.2024,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

        Notes:
        - Data sent to the student_data parameter will be overwritten.

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param file_name: string with the name of the file we are reading
        :param student_data: list of dictionary rows we are adding data to
        :return: list of dictionary rows filled with data
        """
        try:
            file = open(file_name, "r")

            # JSON Answer
            json_data = json.load(file)
            for student in json_data:
                student_data.append(Student(student['FirstName'], student['LastName'], student['CourseName']))

            file.close()
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data into a json file from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param file_name: string with the name of the file we are writing
        :param student_data: list of dictionary rows we are saving to file
        """
        try:
            file = open(file_name, "w")

            json_data = []
            for student in student_data:
                json_data.append({
                    'FirstName': student.first_name,
                    'LastName': student.last_name,
                    'CourseName': student.course_name
                })

            # # JSON answer
            json.dump(json_data, file)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(student)
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)


class IO:
    """
    A collection of functions for input and ouput

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays an error message

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param message: string of the error message
        :param error: error message to display
        """
        print(error)  # Prints the custom message
        print(message)
        print(error.__doc__)
        print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu message

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param menu: string of the menu message
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function inputs a menu option and chooses different functions depending on input

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function
        """
        menu_choice = input("What would you like to do: ")

        # Input user data
        if menu_choice == "1":  # This will not work if it is an integer!
            IO.input_student_data(students)
            return True

        # Present the current data
        elif menu_choice == "2":
            IO.output_student_courses(students)
            return True

        # Save the data to a file
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
            return True

        # Stop the loop
        elif menu_choice == "4":
            return False  # out of the loop
        else:
            print("Please only choose option 1, 2, or 3")
            return True

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays student courses

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param student_data: list of students to output
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(student)
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function inputs a new student course

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param student_data: list of students to append new student data to
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            sd = Student(first_name=student_first_name, last_name=student_last_name, course_name=course_name)
            student_data.append(sd)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("-- Technical Error Message -- ", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(MENU)
    if IO.input_menu_choice() == False:
        break

print("Program Ended")

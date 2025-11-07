# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title
    def get_name(self):
        return self.__name
    def get_ID_number(self):
        return self.__ID_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title
    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'ID number: {self.__ID_number}\n'
                f'Department: {self.__department}\n'
                f'Job title: {self.__job_title}')

emp1 = Employee('Susan Meyers', 4789, 'Accounting', 'Vice President' )
emp2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
emp3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

print(emp1)
print()
print(emp2)
print()
print(emp3)
# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
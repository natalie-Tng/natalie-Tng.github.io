# Employee class definition
class Employee:
    def __init__(self, eid, name):
        """
        Initialize an Employee object with an ID and a name.
        :param eid: Employee ID
        :param name: Employee name
        """
        self.eid = eid
        self.name = name
    def __str__(self):
        """
       String representation of the Employee object.
       :return: Employee details as a string
       """
        return f"Employee ID = {self.eid}, Employee name = {self.name}"
def findEmp(emp_array, eid):
    """
    Search for an employee by their ID in the employee array.
    :param emp_array: List of Employee objects
    :param eid: Employee ID to search for
    :return: None
    """
    for emp in emp_array:
        if emp.eid == eid:
            print(emp)
            return
    print("There is no employee with the given ID")
def main():
    """
   Main function to read employees, store them in a list, and search for employees.
   :return: None
   """
    employee_array = []
    try:
        with open("employee_info.txt", "r") as file:
            for line in file:
                eid, name = line.strip().split(", ")
                employee_array.append(Employee(int(eid), name))
    except FileNotFoundError:
        print("The file 'employee_info.txt' was not found.")
        return
    # Print all employees
    print("All Employees:")
    for emp in employee_array:
        print(emp)
    print("\nTesting findEmp method:")
    # Test the findEmp method
    findEmp(employee_array, 37)# Example: Employee ID 37
    findEmp(employee_array, 5) # Example: Employee ID 5
if __name__ == "__main__":
    main()
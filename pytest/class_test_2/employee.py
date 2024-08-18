# Write a class called Employee. The __init__() method should 
# take in a first name, a last name, and an annual salary, and store each of these 
# as attributes. Write a method called give_raise() that adds $5,000 to the 
# annual salary by default but also accepts a different raise amount.

class Employee:
    """A simple class representing an employee."""

    def __init__(self, first_name: str, last_name :str, annual_salary :float) -> None:
        """
        Initialize an Employee object.
        
        :param first_name: The first name of the employee.
        :param last_name: The last name of the employee.
        :param annual_salary: The annual salary of the employee.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_amount :float = 5_000) -> None:
        """
        Increase the employee's annual salary by the specified amount.
        
        :param raise_amount: The amount to add to the annual salary (default is $5,000).
        """
        self.annual_salary += raise_amount
        
if __name__ == "__main__":
    em = Employee("Ram", "Bahadur",3000)
    print(em.first_name,em.last_name,em.annual_salary)
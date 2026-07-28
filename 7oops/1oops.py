#oops concept:
from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class Person(ABC):
    def __init__(self, name):
        self._name = name   # encapsulation (protected)

    @abstractmethod
    def get_role(self):
        pass

#inheritance:
# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks   # encapsulation (private)

    # Encapsulation: getter
    def get_marks(self):
        return self.__marks

    def average(self):
        try:
            return sum(self.__marks) / len(self.__marks)
        except ZeroDivisionError:
            return 0

    # Polymorphism (method overriding)
    def get_role(self):
        return "Student"

    def display(self):
        print(f"Name: {self._name}, Role: {self.get_role()}, Average: {self.average():.2f}")

    # Another class to show polymorphism
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def get_role(self):
        return "Teacher"

    def display(self):
        print(f"Name: {self._name}, Role: {self.get_role()}, Subject: {self.subject}")


class Classroom:
    def __init__(self):
        self.people = []  # list

    def add_person(self, person):
        self.people.append(person)

    def show_all(self):
        # Polymorphism: same method call, different behavior
        for person in self.people:
            person.display()

    def unique_names(self):
        # set
        return set(person._name for person in self.people)

    def student_dict(self):
        # dictionary (only students)
        return {
            person._name: person.average()
            for person in self.people
            if isinstance(person, Student)
        }
 # Main execution
if __name__ == "__main__":
    classroom = Classroom()

    try:
        # Create objects
        s1 = Student("Alice", [80, 90, 85])
        s2 = Student("Bob", [70, 75, 72])
        s3 = Student("Charlie", [])  # empty list -> exception handled
        t1 = Teacher("Mr. Smith", "Math")

        # Add to classroom
        classroom.add_person(s1)
        classroom.add_person(s2)
        classroom.add_person(s3)
        classroom.add_person(t1)

        print("\nAll People (Polymorphism Demo):")
        classroom.show_all()

        print("\nUnique Names (Set):")
        print(classroom.unique_names())

        print("\nStudent Dictionary (Name -> Average):")
        print(classroom.student_dict())

        # Exception handling example
        num = int(input("\nEnter a number: "))
        print("100 divided by number =", 100 / num)

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print("Unexpected error:", e)

    finally:
        print("\nProgram finished.")
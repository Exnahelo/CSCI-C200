"""
Project Name: HoweLab9_Demo.py
Purpose: Demonstrate User, Admin, and Student objects for Lab 9 Object Oriented Programming.
Description: Non-interactive Lab 9 demo that creates Admin and Student objects, prints all
required fields, shows setter updates, and calls inherited methods.
File Created Date: 2026-04-15
Author: Daniel Howe
Version: 1.0
"""

"""
Disclosure:
I used outside help from ChatGPT to help construct my blueprint and
check that the program matches the Lab 9 rubric. I used my final project to guide
my design decisions. The final code for this lab was written specifically for this
assignment, and no code was copied from the final project files.
"""

from HoweLab9_Admin import Admin
from HoweLab9_Student import Student


def main():
    print("=" * 50)
    print("Lab 9 OOP Demonstration")
    print("=" * 50)

    print("\n--- Admin Object Demo ---")
    admin1 = Admin("adminUser", "adminPass123", 3)

    print("Admin username:", admin1.getUsername())
    print("Admin password:", admin1.getPassword())
    print("Admin access level:", admin1.getAdminAccessLevel())

    print("\nAdmin setter demonstration:")
    print("Before update:", admin1.getAdminAccessLevel())
    admin1.setAdminAccessLevel(5)
    print("After update:", admin1.getAdminAccessLevel())

    print("Admin action method:", admin1.showAccessLevel())

    print("\n--- Student Object Demo ---")
    student1 = Student("studentUser", "studentPass456", "Daniel", "Howe", "dhowe@iu.edu")

    print("Student username:", student1.getUsername())
    print("Student password:", student1.getPassword())
    print("Student first name:", student1.getFirstName())
    print("Student last name:", student1.getLastName())
    print("Student email:", student1.getEmail())

    print("\nStudent setter demonstration:")
    print("Before update:", student1.getEmail())
    student1.setEmail("daniel.howe@iu.edu")
    print("After update:", student1.getEmail())

    print("Student action method:", student1.getFullName())

    print("\n--- Superclass Method Through Subclass Demo ---")
    print("Student username from User class:", student1.getUsername())
    print("Admin authenticateUser result:", admin1.authenticateUser("adminUser", "adminPass123"))


if __name__ == "__main__":
    main()
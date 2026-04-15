"""
Project Name: HoweLab9_Student.py
Purpose: Define the Student child class for Lab 9 Object Oriented Programming.
Description: Child class that inherits from User and stores first name, last name,
and email with required setters, getters, and an action method.
File Created Date: 2026-04-15
Author: Daniel Howe
Version: 1.0
"""

from HoweLab9_User import User


class Student(User):
    def __init__(self, username, password, firstName, lastName, email):
        super().__init__(username, password)
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"
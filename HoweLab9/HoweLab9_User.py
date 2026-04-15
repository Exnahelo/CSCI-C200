"""
Project Name: HoweLab9_User.py
Purpose: Define the User parent class for Lab 9 Object Oriented Programming.
Description: Parent class for the Lab 9 mini registrar demonstration with username,
password, setters, getters, and authentication behavior.
File Created Date: 2026-04-15
Author: Daniel Howe
Version: 1.0
"""


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def authenticateUser(self, username, password):
        return self.username == username and self.password == password

    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}"
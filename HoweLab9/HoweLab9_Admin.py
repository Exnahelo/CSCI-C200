"""
Project Name: HoweLab9_Admin.py
Purpose: Define the Admin child class for Lab 9 Object Oriented Programming.
Description: Child class that inherits from User and stores an admin access
level with its own setter, getter, and action method.
File Created Date: 2026-04-15
Author: Daniel Howe
Version: 1.0
"""

from HoweLab9_User import User


class Admin(User):
    def __init__(self, username, password, adminAccessLevel):
        super().__init__(username, password)
        self.adminAccessLevel = adminAccessLevel

    def setAdminAccessLevel(self, adminAccessLevel):
        self.adminAccessLevel = adminAccessLevel

    def getAdminAccessLevel(self):
        return self.adminAccessLevel

    def showAccessLevel(self):
        return f"Admin access level: {self.adminAccessLevel}"
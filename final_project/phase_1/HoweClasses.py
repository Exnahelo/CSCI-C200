# HoweClasses.py
# Project: CSCI-C 200 Final Project — Mini Registrar System
# Purpose: OOP class definitions for User (base), Admin, and Student.
#          Admin and Student inherit from User.
# Author: Daniel Howe
# Date: 2026-04-06

import os
import csv


# ─────────────────────────────────────────────
# USER BASE CLASS
# ─────────────────────────────────────────────

class User:
    """
    Base class representing any system user (admin or student).
    Stores credentials privately and provides authentication.
    """

    def __init__(self, username, password):
        self.__username = username   # private: user's login name
        self.__password = password   # private: user's password

    # --- Getters ---
    def get_username(self):
        """Return the user's username."""
        return self.__username

    def get_password(self):
        """Return the user's password."""
        return self.__password

    # --- Setters ---
    def set_username(self, username):
        """Update the user's username."""
        self.__username = username

    def set_password(self, password):
        """Update the user's password."""
        self.__password = password

    def authenticate(self, input_username, input_password):
        """
        Compare provided credentials against stored credentials.
        Returns True if both username and password match (case-sensitive, stripped).
        """
        return (self.__username.strip() == input_username.strip() and
                self.__password.strip() == input_password.strip())

    def __str__(self):
        return f"User: {self.__username}"


# ─────────────────────────────────────────────
# ADMIN SUBCLASS
# ─────────────────────────────────────────────

class Admin(User):
    """
    Subclass of User representing an admin.
    Inherits authentication from User.
    Provides methods to add and view students, courses, and enrollments.
    """

    def __init__(self, username, password):
        super().__init__(username, password)   # call User's __init__

    def __str__(self):
        return f"Admin: {self.get_username()}"

    # ── ADD STUDENT ──────────────────────────
    def add_student(self):
        """
        Prompts for student information in a loop.
        Validates all fields are non-empty and username is unique.
        Re-prompts only the username field if it is a duplicate.
        Saves each new student to students.csv.
        """
        from HoweUtil import (load_students, is_value_unique,
                              save_row_to_csv, STUDENTS_CSV_PATH, STUDENT_HEADERS)

        while True:
            # collect all fields
            first_name = input("  First name: ").strip()
            last_name  = input("  Last name: ").strip()
            username   = input("  Username: ").strip()
            password   = input("  Password: ").strip()
            email      = input("  Email: ").strip()

            # validate no empty fields
            if not all([first_name, last_name, username, password, email]):
                print("  [!] All fields are required. Please try again.\n")
                continue

            # enforce unique username (re-prompt username only if duplicate)
            students = load_students()
            while not is_value_unique(username, students, 2):
                print(f"  [!] Username '{username}' already exists. Choose a different username.")
                username = input("  Username: ").strip()
                if not username:
                    print("  [!] Username cannot be empty.")

            # save to CSV
            save_row_to_csv(
                STUDENTS_CSV_PATH,
                STUDENT_HEADERS,
                [first_name, last_name, username, password, email]
            )
            print(f"  [✓] Student '{username}' added successfully.\n")

            again = input("  Add another student? (yes/no): ").strip().lower()
            if again != "yes":
                break

    # ── ADD COURSE ───────────────────────────
    def add_course(self):
        """
        Prompts for course information in a loop.
        Validates all fields are non-empty and course number is unique.
        Re-prompts only the course number field if it is a duplicate.
        Saves each new course to courses.csv.
        """
        from HoweUtil import (load_courses, is_value_unique,
                              save_row_to_csv, COURSES_CSV_PATH, COURSE_HEADERS)

        while True:
            course_number = input("  Course number: ").strip()
            course_title  = input("  Course title: ").strip()

            # validate no empty fields
            if not all([course_number, course_title]):
                print("  [!] All fields are required. Please try again.\n")
                continue

            # enforce unique course number (re-prompt course number only if duplicate)
            courses = load_courses()
            while not is_value_unique(course_number, courses, 0):
                print(f"  [!] Course number '{course_number}' already exists. Enter a different course number.")
                course_number = input("  Course number: ").strip()
                if not course_number:
                    print("  [!] Course number cannot be empty.")

            # save to CSV
            save_row_to_csv(
                COURSES_CSV_PATH,
                COURSE_HEADERS,
                [course_number, course_title]
            )
            print(f"  [✓] Course '{course_number}' added successfully.\n")

            again = input("  Add another course? (yes/no): ").strip().lower()
            if again != "yes":
                break

    # ── VIEW STUDENTS ────────────────────────
    def view_students(self):
        """
        Loads and displays all student records from students.csv.
        Passwords are excluded from output.
        """
        from HoweUtil import load_students

        students = load_students()
        if not students:
            print("\n  No students on record.\n")
            return

        print("\n" + "─" * 70)
        print(f"  {'First Name':<15} {'Last Name':<15} {'Username':<15} {'Email':<25}")
        print("─" * 70)
        for row in students:
            # row: [first_name, last_name, username, password, email]
            print(f"  {row[0]:<15} {row[1]:<15} {row[2]:<15} {row[4]:<25}")
        print("─" * 70 + "\n")

    # ── VIEW COURSES ─────────────────────────
    def view_courses(self):
        """
        Loads and displays all course records from courses.csv.
        """
        from HoweUtil import load_courses

        courses = load_courses()
        if not courses:
            print("\n  No courses on record.\n")
            return

        print("\n" + "─" * 55)
        print(f"  {'Course Number':<20} {'Course Title':<35}")
        print("─" * 55)
        for row in courses:
            print(f"  {row[0]:<20} {row[1]:<35}")
        print("─" * 55 + "\n")

    # ── VIEW ENROLLMENTS ─────────────────────
    def view_enrollments(self):
        """
        Loads and displays all enrollment records.
        Joins with courses.csv to show course title alongside course number.
        """
        from HoweUtil import load_enrollments, load_courses

        enrollments = load_enrollments()
        courses     = load_courses()

        if not enrollments:
            print("\n  No enrollments on record.\n")
            return

        print("\n" + "─" * 75)
        print(f"  {'Username':<20} {'Course Number':<20} {'Course Title':<35}")
        print("─" * 75)
        for row in enrollments:
            username      = row[0]
            course_number = row[1]
            course_title  = "Unknown Title"   # default if course not found
            for course in courses:
                if course[0] == course_number:
                    course_title = course[1]
                    break
            print(f"  {username:<20} {course_number:<20} {course_title:<35}")
        print("─" * 75 + "\n")


# ─────────────────────────────────────────────
# STUDENT SUBCLASS
# ─────────────────────────────────────────────

class Student(User):
    """
    Subclass of User representing a student.
    Inherits authentication from User.
    Provides methods to enroll in courses and view enrolled courses.
    """

    def __init__(self, username, password):
        super().__init__(username, password)   # call User's __init__

    def __str__(self):
        return f"Student: {self.get_username()}"

    # ── IS ENROLLED ──────────────────────────
    def is_enrolled(self, course_number):
        """
        Checks if this student is already enrolled in the specified course.
        Returns True if enrolled, False otherwise.
        """
        from HoweUtil import load_enrollments

        enrollments = load_enrollments()
        for row in enrollments:
            # row: [username, course_number]
            if row[0] == self.get_username() and row[1] == course_number:
                return True
        return False

    # ── ENROLL ───────────────────────────────
    def enroll(self, course_number):
        """
        Enrolls this student in the specified course.
        Checks for duplicate enrollment before saving.
        Returns True if enrollment succeeded, False if already enrolled.
        """
        from HoweUtil import (save_row_to_csv,
                              ENROLLMENTS_CSV_PATH, ENROLLMENT_HEADERS)

        if self.is_enrolled(course_number):
            return False   # already enrolled

        save_row_to_csv(
            ENROLLMENTS_CSV_PATH,
            ENROLLMENT_HEADERS,
            [self.get_username(), course_number]
        )
        return True

    # ── VIEW MY COURSES ──────────────────────
    def view_my_courses(self):
        """
        Displays all courses this student is enrolled in.
        Filters enrollment CSV by this student's username,
        joins with courses CSV to retrieve course titles,
        deduplicates results, and prints formatted output.
        """
        from HoweUtil import load_enrollments, load_courses

        enrollments = load_enrollments()
        courses     = load_courses()

        # filter and join
        student_courses = []
        for row in enrollments:
            if row[0] == self.get_username():
                course_number = row[1]
                course_title  = "Unknown Title"
                for course in courses:
                    if course[0] == course_number:
                        course_title = course[1]
                        break
                entry = [course_number, course_title]
                if entry not in student_courses:   # deduplicate
                    student_courses.append(entry)

        # display
        if not student_courses:
            print(f"\n  Hello {self.get_username()}! You are not enrolled in any courses.\n")
            return

        print(f"\n  Hello {self.get_username()}! Below are courses you are enrolled in:\n")
        for entry in student_courses:
            print(f"  Course Number: {entry[0]}, Title: {entry[1]}")
        print()

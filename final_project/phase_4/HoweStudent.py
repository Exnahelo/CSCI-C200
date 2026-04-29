# HoweStudent.py
# Project: CSCI-C 200 Final Project — Mini Registrar System
# Purpose: Student module executable. Handles student login and provides
#          a menu-driven interface for enrolling in courses and viewing
#          enrolled courses.
# Author: Daniel Howe
# Date: 2026-04-06

import sys
import os

# ensure imports resolve from the same directory as this file
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from HoweClasses import Student
from HoweUtil import login_control, load_courses, STUDENTS_CSV_PATH, MAX_LOGIN_ATTEMPTS


# ─────────────────────────────────────────────
# PROGRAM HEADER
# ─────────────────────────────────────────────

def print_header():
    """Display the student module header."""
    print("\n" + "=" * 50)
    print("   Mini Registrar System — Student Module")
    print("=" * 50 + "\n")


# ─────────────────────────────────────────────
# STUDENT MENU
# ─────────────────────────────────────────────

def show_menu():
    """Display the student menu options."""
    print("─" * 40)
    print("  Student Menu")
    print("─" * 40)
    print("  1. Enroll in a course")
    print("  2. View my courses")
    print("  3. Exit")
    print("─" * 40)


# ─────────────────────────────────────────────
# ENROLL IN COURSE
# ─────────────────────────────────────────────

def enroll_in_course(student_obj):
    """
    Displays available courses and allows the student to enroll in one.
    Validates that the entered course number exists in courses.csv.
    Calls student_obj.enroll() which handles duplicate enrollment checking.
    Student can type 'back' to return to the menu without enrolling.
    """
    courses = load_courses()

    if not courses:
        print("\n  No courses are available for enrollment at this time.\n")
        return

    # display numbered course list
    print("\n  Available courses:\n")
    for i, row in enumerate(courses, start=1):
        print(f"  {i}. {row[0]} — {row[1]}")
    print()

    # prompt for course number
    while True:
        course_input = input("  Enter a course number to enroll (or 'back' to return): ").strip()

        if course_input.lower() == "back":
            return   # return to student menu

        # validate course number exists in courses list
        valid_numbers = [row[0] for row in courses]
        if course_input not in valid_numbers:
            print(f"  [!] '{course_input}' is not a valid course number. Please try again.\n")
            continue

        # attempt enrollment
        result = student_obj.enroll(course_input)
        if result:
            print(f"  [✓] Successfully enrolled in {course_input}.\n")
        else:
            print(f"  [!] You are already enrolled in {course_input}.\n")
        return   # return to student menu after one enrollment attempt


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print_header()

    # ── LOGIN ────────────────────────────────
    print("  Please log in to continue.\n")
    success, student_obj = login_control(STUDENTS_CSV_PATH, MAX_LOGIN_ATTEMPTS, Student)

    if not success:
        print("  Access denied. Exiting.\n")
        sys.exit()

    print(f"\n  Welcome, {student_obj.get_username()}!\n")

    # ── MENU LOOP ────────────────────────────
    while True:
        show_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            enroll_in_course(student_obj)

        elif choice == "2":
            student_obj.view_my_courses()

        elif choice == "3":
            print("\n  Goodbye!\n")
            sys.exit()

        else:
            print("  [!] Invalid choice. Please enter 1, 2, or 3.\n")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()

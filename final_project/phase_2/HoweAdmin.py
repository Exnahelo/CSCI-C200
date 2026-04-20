# HoweAdmin.py
# Project: CSCI-C 200 Final Project — Mini Registrar System
# Purpose: Admin module executable. Handles admin login and provides
#          a menu-driven interface for managing students, courses,
#          and viewing enrollment data.
# Author: Daniel Howe
# Date: 2026-04-06

import sys
import os

# ensure imports resolve from the same directory as this file
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from HoweClasses import Admin
from HoweUtil import login_control, ADMIN_CSV_PATH, MAX_LOGIN_ATTEMPTS


# ─────────────────────────────────────────────
# PROGRAM HEADER
# ─────────────────────────────────────────────

def print_header():
    """Display the admin module header."""
    print("\n" + "=" * 50)
    print("   Mini Registrar System — Admin Module")
    print("=" * 50 + "\n")


# ─────────────────────────────────────────────
# ADMIN MENU
# ─────────────────────────────────────────────

def show_menu():
    """Display the admin menu options."""
    print("─" * 40)
    print("  Admin Menu")
    print("─" * 40)
    print("  1. Add a new student")
    print("  2. Add a new course")
    print("  3. View all students")
    print("  4. View all courses")
    print("  5. View all enrollments")
    print("  6. Exit")
    print("─" * 40)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print_header()

    # ── LOGIN ────────────────────────────────
    print("  Please log in to continue.\n")
    success, admin_obj = login_control(ADMIN_CSV_PATH, MAX_LOGIN_ATTEMPTS, Admin)

    if not success:
        print("  Access denied. Exiting.\n")
        sys.exit()

    print(f"\n  Welcome, {admin_obj.get_username()}!\n")

    # ── MENU LOOP ────────────────────────────
    while True:
        show_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            print("\n  --- Add a New Student ---")
            admin_obj.add_student()

        elif choice == "2":
            print("\n  --- Add a New Course ---")
            admin_obj.add_course()

        elif choice == "3":
            print("\n  --- All Students ---")
            admin_obj.view_students()

        elif choice == "4":
            print("\n  --- All Courses ---")
            admin_obj.view_courses()

        elif choice == "5":
            print("\n  --- All Enrollments ---")
            admin_obj.view_enrollments()

        elif choice == "6":
            print("\n  Goodbye!\n")
            sys.exit()

        else:
            print("  [!] Invalid choice. Please enter a number from 1 to 6.\n")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()

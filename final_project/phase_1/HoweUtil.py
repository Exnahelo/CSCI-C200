# HoweUtil.py
# Project: CSCI-C 200 Final Project — Mini Registrar System
# Purpose: Shared utility functions and constants used by both
#          HoweAdmin.py and HoweStudent.py.
# Author: Daniel Howe
# Date: 2026-04-06

import csv
import os

# ─────────────────────────────────────────────
# CONSTANTS — single source of truth
# ─────────────────────────────────────────────

ADMIN_CSV_PATH       = "admins.csv"
STUDENTS_CSV_PATH    = "students.csv"
COURSES_CSV_PATH     = "courses.csv"
ENROLLMENTS_CSV_PATH = "enrollments.csv"

MAX_LOGIN_ATTEMPTS = 5

STUDENT_HEADERS    = ["first_name", "last_name", "username", "password", "email"]
COURSE_HEADERS     = ["course_number", "course_title"]
ENROLLMENT_HEADERS = ["username", "course_number"]


# ─────────────────────────────────────────────
# READ CSV
# ─────────────────────────────────────────────

def read_csv(filepath):
    """
    Opens a CSV file and returns all data rows as a list of lists.
    The header row is skipped.
    Input:  filepath (str) — path to the CSV file
    Output: list of lists (each inner list is one data row)
    """
    rows = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)   # skip header row
        for row in reader:
            rows.append(row)
    return rows


# ─────────────────────────────────────────────
# LOGIN CONTROL
# ─────────────────────────────────────────────

def login_control(filepath, max_attempts=5, user_class=None):
    """
    Manages the login loop for either admin or student modules.
    Loads credentials from filepath, prompts for username and password,
    creates user_class instances for comparison, and enforces a lockout
    after max_attempts failed attempts.

    Column indices:
      - admins.csv:   username=0, password=1
      - students.csv: username=2, password=3

    Input:  filepath (str), max_attempts (int), user_class (Admin or Student)
    Output: (True, user_obj) on success | (False, None) on lockout
    """
    # determine column indices based on which file is being used
    if filepath == STUDENTS_CSV_PATH:
        username_idx = 2
        password_idx = 3
    else:
        username_idx = 0
        password_idx = 1

    # load credential data
    credential_data = read_csv(filepath)

    attempts = 0
    while attempts < max_attempts:
        input_username = input("  Username: ").strip()
        input_password = input("  Password: ").strip()

        # check against every stored credential row
        for row in credential_data:
            stored = user_class(row[username_idx], row[password_idx])
            if stored.authenticate(input_username, input_password):
                return (True, stored)   # login successful

        # failed attempt
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"  [!] Invalid credentials. {remaining} attempt(s) remaining.\n")
        else:
            print("  [!] Too many failed attempts. Account locked.\n")

    return (False, None)


# ─────────────────────────────────────────────
# LOAD FUNCTIONS
# ─────────────────────────────────────────────

def load_students():
    """
    Returns all student rows from students.csv, or [] if the file doesn't exist.
    Output: list of lists
    """
    if not os.path.exists(STUDENTS_CSV_PATH):
        return []
    return read_csv(STUDENTS_CSV_PATH)


def load_courses():
    """
    Returns all course rows from courses.csv, or [] if the file doesn't exist.
    Output: list of lists
    """
    if not os.path.exists(COURSES_CSV_PATH):
        return []
    return read_csv(COURSES_CSV_PATH)


def load_enrollments():
    """
    Returns all enrollment rows from enrollments.csv, or [] if the file doesn't exist.
    Output: list of lists
    """
    if not os.path.exists(ENROLLMENTS_CSV_PATH):
        return []
    return read_csv(ENROLLMENTS_CSV_PATH)


# ─────────────────────────────────────────────
# UNIQUENESS CHECK
# ─────────────────────────────────────────────

def is_value_unique(value, data, column_index):
    """
    Checks whether a value already exists in a specific column of the data.
    Comparison is case-insensitive and strips whitespace.

    Input:  value (str), data (list of lists), column_index (int)
    Output: True if value is NOT found (unique), False if it already exists
    """
    for row in data:
        if row[column_index].strip().lower() == value.strip().lower():
            return False   # duplicate found
    return True


# ─────────────────────────────────────────────
# SAVE ROW TO CSV
# ─────────────────────────────────────────────

def save_row_to_csv(filepath, headers, new_row):
    """
    Appends a new row to a CSV file.
    If the file does not exist, creates it and writes the header row first.
    If the file already exists, appends the new row only (no header).

    Input:  filepath (str), headers (list of str), new_row (list of str)
    Output: None (side effect: creates or modifies a CSV file on disk)
    """
    if not os.path.exists(filepath):
        # first run — create file and write header + first row
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(new_row)
    else:
        # file exists — append row only
        with open(filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(new_row)

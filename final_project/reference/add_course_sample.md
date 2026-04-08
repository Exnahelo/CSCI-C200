# Reference: Add a New Course — Instructor Sample Code

> **Source:** Class-provided pseudocode/sample from instructor.
> This is a reference for understanding the expected pattern. Your implementation will follow this logic using your own variable names, OOP structure, and utility functions.

---

## Overview

This sample demonstrates the pattern for adding a new course, including:

- Checking if the course CSV file exists (first run vs. subsequent runs)
- Enforcing course number uniqueness via a helper function
- Reading instructor usernames from a separate CSV and displaying them as a selection list

---

## Sample Pseudocode

```python
choice = input("Select 'c' to add a new course")

if choice == 'c':

    course = []
    fw = open("course.csv", "w")
    # write the column header
    # ...

    # check if the course number (cn) is unique
    # file read first
    if file doesn't exist:  # which means it is the first course
        cn = input("Please enter a course number")
        ct = input("Please enter a course title")

        # find a list of instructor usernames and display to the user
        # 1. read from ins.csv, stored in a 2-D array insArray
        frd = open('ins.csv', 'r')
        # column[2] stores all the usernames
        # loop through insArray and form a string that looks like a dropdown list
        frd.readLine()
        namesDropdown = ""
        for i in insArray:
            oneName = i[2]
            namesDropdown = namesDropdown + oneName + "\n"
        print("Please select a username in this list and enter a username")
        print(namesDropdown)

        ins = input("Please enter an instructor username")

        # ready to write one line which is a string with values, separated by commas

    else:
        while True:
            # get course number
            cn = input("Please enter a course number")

            if isCourseUnique(cn) == True:
                break
            else:
                print("Course already added. Please enter a new course number.")

        # get course title
        # display instructor dropdown, same as above
        # get instructor username
        # write one line to the csv
```

---

## Uniqueness Check Function

```python
def isCourseUnique(cn):
    # open course.csv to read
    cf = open("course.csv", "r")

    # read off the column header
    # read all data into a 2D array ca
    # column[0] stores the course number
    for i in ca:
        if cn == i[0]:
            return False

    return True
```

---

## Notes for Implementation

- In your implementation, `isCourseUnique()` maps to `is_value_unique()` in `HoweUtil.py` (or `Admin.add_course()` in the OOP version)
- The instructor username dropdown is an **extension** — the base project only requires course number and course title; instructor assignment is an enhancement
- Use `os.path.exists()` to check if the CSV file exists before attempting to read it
- The `save_row_to_csv()` utility function handles both first-run (write headers) and append scenarios

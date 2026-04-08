# Reference: Online Help Session Sample Codes — Instructor Provided

> **Source:** Class-provided sample code from online help session (`onlineHelpSessionSampleCodes.txt`).
> This is a reference for understanding the expected patterns. Your implementation will follow this logic using your own variable names, OOP structure, and utility functions.

---

## Part 1 — Ensuring Unique Student Usernames (When Adding a Student)

### Usage Pattern in Executable

```python
firstName = input("Please enter student first name:")
# ... collect other fields ...
userName = input("Please enter username:")

if checkUniqueStudentUsername(userName) == True:
    # take all the values collected (firstname, lastname, username, pwd, ...)
    # either create an array and write the array to student.csv
    # or append a long string separated by commas to the file
else:
    # prompt again or show error
```

---

### `checkUniqueStudentUsername(un)` — Utility Function

```python
import os

def checkUniqueStudentUsername(un):
    # read the student.csv data into an array
    if os.path.exists("student.csv") == False:
        return True
    else:
        # read the data rows into a 2D array called dataValueArray (not the column header)
        # see lines 31 to 43 in sample file fileRead.py
        # ...

        # loop through this 2D array and check if un matches any value in the username column
        # in the finalProject.docx, username is column index 2 (0-indexed)
        for i in range(len(dataValueArray)):
            newRow = dataValueArray[i]
            if un == newRow[2]:
                return False

        return True
```

---

## Part 2 — Ensuring Unique Enrollment (No Duplicate Course Enrollment)

### `checkUniqueEnrollment(cn, un)` — Utility Function

```python
import os

def checkUniqueEnrollment(cn, un):
    # read the enrollment.csv data into an array
    if os.path.exists("enrollment.csv") == False:
        return True
    else:
        # read the data rows into a 2D array called dataValueArray
        # ...

        # check if the username AND course number combination already exists
        for i in range(len(dataValueArray)):
            newRow = dataValueArray[i]
            if cn == newRow[0] and un == newRow[1]:
                return False

        return True
```

### Usage Pattern in Student Module

```python
userName = input("Please enter username to login")

# print out a list of courses (course number and title) by looping through course.csv

courseNumber = input("Please enter your choice of course by entering a course number")

if checkUniqueEnrollment(userName, courseNumber) == True:
    # append userName and courseNumber to file
    # if file doesn't exist, write header line then append the value line
    # otherwise, only append the value line
```

---

## Part 3 — Generic Uniqueness Check (Alternative Pattern)

The instructor also suggested a single reusable function that can check uniqueness for any column in any file:

```python
def checkUniqueness(value, columnIndex, fileName):
    # check if 'value' already exists in 'columnIndex' of 'fileName'
    # returns True if unique (value not found), False if duplicate
```

This maps directly to `is_value_unique(value, data, column_index)` in `HoweUtil.py`.

---

## Notes for Implementation

| Instructor Function | Your Implementation |
| --- | --- |
| `checkUniqueStudentUsername(un)` | `is_value_unique(username, students_data, 2)` or `Admin.add_student()` uniqueness check |
| `checkUniqueEnrollment(cn, un)` | `is_enrolled(username, course_number)` in `HoweUtil.py` or `Student.is_enrolled()` |
| `checkUniqueness(value, columnIndex, fileName)` | `is_value_unique(value, data, column_index)` in `HoweUtil.py` |

- Always use `os.path.exists()` before attempting to read a CSV file
- The column index for username in `students.csv` is `2` (0-indexed: first_name=0, last_name=1, username=2)
- The enrollment CSV stores `username` at index `0` and `course_number` at index `1` in your design

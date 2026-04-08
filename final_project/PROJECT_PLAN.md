# CSCI-C 200 Final Project — Master Build Plan

> **Single source of truth.** This document contains the full project plan, rubric-mapped checklists, build order, and submission strategy.
> **Extra Credit:** Both Option 1 (Algorithm Design Document) and Option 2 (OOP) are being completed as core requirements.

---

## File Map

```map
Project Root/
├── admins.csv              ← manual (only manual CSV)
├── HoweAdmin.py            ← admin executable
├── HoweStudent.py          ← student executable
├── HoweUtil.py             ← shared utility functions + constants
├── HoweClasses.py          ← User, Admin, Student classes
├── HoweAlgorithmDesign.docx← Extra Credit Option 1
│
├── students.csv            ← generated (do NOT submit)
├── courses.csv             ← generated (do NOT submit)
└── enrollments.csv         ← generated (do NOT submit)
```

---

## Blueprint Refinements (Locked In)

1. **`login_control()` gets `user_class` param from day one.**
   Phase 1 passes `Admin`, Phase 3 passes `Student`. No retrofitting.

2. **Smarter re-prompting on duplicates.**
   - `add_student()`: if username is taken, re-prompt only username — not all 5 fields.
   - `add_course()`: if course number is taken, re-prompt only course number.

3. **Enrollment CSV column order: `username,course_number`** (index 0,1).
   Instructor sample is flipped — ours is internally consistent, just stay aware.

4. **All constants in `HoweUtil.py`.**
   Both executables import paths/headers from one source of truth.

5. **Algorithm design doc is a living document** — drafted alongside code, not scrambled at Phase 4.

---

## CSV Schemas

### admins.csv (manual)

```csv
username,password
```

- At least 3 rows, realistic values

### students.csv (generated)

```csv
first_name,last_name,username,password,email
```

- username at index 2, must be unique

### courses.csv (generated)

```csv
course_number,course_title
```

- course_number at index 0, must be unique

### enrollments.csv (generated)

```csv
username,course_number
```

- username at index 0, course_number at index 1
- Combo of username + course_number must be unique

---

## OOP Class Hierarchy

```Hierarchy
User (base)
├── __init__(username, password)     → private __username, __password
├── get_username() / set_username()
├── get_password() / set_password()
├── authenticate(input_user, input_pass) → bool
└── __str__() → "User: {username}"

Admin(User)
├── __init__(username, password)     → super().__init__()
├── __str__() → "Admin: {username}"
├── add_student()                    [Phase 2]
├── add_course()                     [Phase 2]
├── view_students()                  [Phase 3]
├── view_courses()                   [Phase 3]
└── view_enrollments()               [Phase 3]

Student(User)
├── __init__(username, password)     → super().__init__()
├── __str__() → "Student: {username}"
├── is_enrolled(course_number)       [Phase 3]
├── enroll(course_number)            [Phase 3]
└── view_my_courses()                [Phase 4]
```

---

## Utility Functions (HoweUtil.py)

### Constants

```python
ADMIN_CSV_PATH = "admins.csv"
STUDENTS_CSV_PATH = "students.csv"
COURSES_CSV_PATH = "courses.csv"
ENROLLMENTS_CSV_PATH = "enrollments.csv"
MAX_LOGIN_ATTEMPTS = 5
STUDENT_HEADERS = ["first_name", "last_name", "username", "password", "email"]
COURSE_HEADERS = ["course_number", "course_title"]
ENROLLMENT_HEADERS = ["username", "course_number"]
```

### Function Contracts

**`read_csv(filepath)`**

- Input: filepath (str)
- Process: open file, read rows, skip header
- Output: list of lists (each inner list = one data row)

**`login_control(filepath, max_attempts=5, user_class=None)`**

- Input: filepath, max_attempts, user_class (Admin or Student)
- Process: load credentials, loop up to max_attempts, create user_class instances for comparison
- Output: (True, user_obj) on success, (False, None) on lockout
- Note: For student login, filepath is students.csv; username is at index 2, password at index 3

**`load_students()`**

- Returns read_csv(STUDENTS_CSV_PATH) or [] if file doesn't exist

**`load_courses()`**

- Returns read_csv(COURSES_CSV_PATH) or [] if file doesn't exist

**`load_enrollments()`**

- Returns read_csv(ENROLLMENTS_CSV_PATH) or [] if file doesn't exist

**`is_value_unique(value, data, column_index)`**

- Iterates data, compares stripped/lowercased value against column
- Returns True if unique, False if duplicate

**`save_row_to_csv(filepath, headers, new_row)`**

- If file doesn't exist: write headers + row
- If file exists: append row only

---

## Admin Menu (HoweAdmin.py)

```python
1. Add a new student       → admin_obj.add_student()
2. Add a new course        → admin_obj.add_course()
3. View all students       → admin_obj.view_students()
4. View all courses        → admin_obj.view_courses()
5. View all enrollments    → admin_obj.view_enrollments()
6. Exit
```

---

## Student Menu (HoweStudent.py)

```python
1. Enroll in a course      → enroll_in_course(student_obj)
2. View my courses         → student_obj.view_my_courses()
3. Exit
```

### enroll_in_course(student_obj) — lives in HoweStudent.py

1. Load courses from courses.csv
2. If no courses: print message, return
3. Display numbered list of courses
4. Prompt for course number (or 'back')
5. Validate course number exists
6. Call student_obj.enroll(course_number)
7. Print success or "already enrolled"

---

## Login Control Algorithm (both modules)

```Text
load credentials from CSV using read_csv()
attempts = 0

while attempts < max_attempts:
    prompt username
    prompt password

    for each row in credentials:
        create user_class(row[username_idx], row[password_idx])
        if stored.authenticate(input_user, input_pass):
            return (True, stored)

    attempts += 1
    remaining = max_attempts - attempts
    if remaining > 0: print "X attempt(s) remaining"
    else: print "Account locked."

return (False, None)
```

**Column indices for login:**

- admins.csv: username=0, password=1
- students.csv: username=2, password=3

---

## Edge Cases

| Scenario | Handling |
| ---------- | ---------- |
| Empty field during add | Print error, re-prompt entire entry |
| Duplicate username (add student) | Print error, re-prompt username only |
| Duplicate course number (add course) | Print error, re-prompt course number only |
| CSV doesn't exist on first run | load_* returns [], save_row_to_csv creates with headers |
| 5 failed logins | Print lockout, exit |
| Correct creds on attempt 5 | Login succeeds (check before incrementing) |
| Student enrolls in same course twice | is_enrolled() catches it, print "already enrolled" |
| View with no data | Print friendly "no records" message |
| Course in enrollment but not in courses.csv | Display "Unknown Title" |
| Extra whitespace | .strip() on all inputs |
| Case sensitivity | Usernames/passwords are case-sensitive (exact match) |
| Uniqueness checks | Case-insensitive (.strip().lower()) |

---

## Phase Checklists (Rubric-Mapped)

### Phase 1 — Submission 1 (Blue) · Due: April 8, Wednesday

#### Setup & Admin Login Control

- [ ] Manually create `admins.csv` with **at least 3 admins** (realistic usernames & passwords) *(2 pts)*
- [ ] Implement admin login that reads from the admin CSV file
- [ ] Limit failed login attempts to **5 tries** before locking out *(3 pts)*
- [ ] Create `HoweUtil.py` with reusable functions *(5 pts)*
- [ ] Create `HoweAdmin.py` executable for the admin module

#### Extra Credit — OOP (Option 2): Class Foundation

- [ ] Define `User` base class — `__init__()`, `__str__()`, `authenticate()`, getters/setters
- [ ] Define `Admin(User)` subclass — inherits from `User`; add admin-specific method stubs
- [ ] Store class definitions in `HoweClasses.py`
- [ ] Use `Admin` object in `HoweAdmin.py` for login (create Admin instance, call `authenticate()`)

**Submit:** `admins.csv`, `HoweAdmin.py`, `HoweUtil.py`, `HoweClasses.py`

---

### Phase 2 — Submission 2 (Purple) · Due: April 22, Wednesday

#### Add a New Student

- [ ] Collect student info: first name, last name, unique username, password, email *(2 pts)*
- [ ] Ensure each **student username is unique** across all students *(5 pts)*
- [ ] Allow admin to **keep adding students** until they choose to stop *(5 pts)*
- [ ] Save student information to `students.csv` (program-generated) *(3 pts)*

#### Add a New Course

- [ ] Collect course info: unique course number and course title *(2 pts)*
- [ ] Ensure each **course number is unique** *(5 pts)*
- [ ] Allow admin to **keep adding courses** until they choose to stop *(2 pts)*
- [ ] Save course information to `courses.csv` (program-generated) *(3 pts)*

#### Extra Credit — OOP (Option 2): Admin Methods

- [ ] Implement `Admin.add_student()` — collects input, checks uniqueness, saves to CSV
- [ ] Implement `Admin.add_course()` — collects input, checks uniqueness, saves to CSV
- [ ] Define `Student(User)` subclass skeleton in `HoweClasses.py` (stubs only)
- [ ] Admin menu in `HoweAdmin.py` creates an `Admin` instance and calls its methods

**Submit:** `admins.csv`, `HoweAdmin.py`, `HoweUtil.py`, `HoweClasses.py`

---

### Phase 3 — Submission 3 (Green) · Due: April 29, Wednesday

#### Admin Module — View Data & Navigation

- [ ] View all students — retrieve from `students.csv` *(2 pts)*
- [ ] View all students — nicely formatted output *(3 pts)*
- [ ] View all courses — retrieve from `courses.csv` *(2 pts)*
- [ ] View all courses — nicely formatted output *(3 pts)*
- [ ] View all enrollments — retrieve from `enrollments.csv` *(2 pts)*
- [ ] View all enrollments — nicely formatted output (with course title) *(3 pts)*
- [ ] Admin can **navigate easily** among all features (menu-driven) *(5 pts)*
- [ ] Admin can **exit the program** easily *(5 pts)*

#### Extra Credit — OOP (Option 2): Admin View Methods

- [ ] Implement `Admin.view_students()` method
- [ ] Implement `Admin.view_courses()` method
- [ ] Implement `Admin.view_enrollments()` method

#### Student Module — Login & Enrollment

- [ ] Student login — authenticate against `students.csv` *(2 pts)*
- [ ] Student login — 5-attempt lockout *(3 pts)*
- [ ] Display course list and allow student to select a course to enroll *(5 pts)*
- [ ] Prevent a student from **enrolling in the same course twice** *(5 pts)*
- [ ] Save enrollment info to `enrollments.csv` *(3 pts)*

#### Extra Credit — OOP (Option 2): Student Methods

- [ ] Implement `Student.enroll(course_number)` — checks uniqueness, saves to enrollment CSV
- [ ] Implement `Student.is_enrolled(course_number)` — checks enrollment CSV for duplicate
- [ ] `HoweStudent.py` creates a `Student` instance after login and calls its methods

**Submit:** `admins.csv`, `HoweAdmin.py`, `HoweStudent.py`, `HoweUtil.py`, `HoweClasses.py`

---

### Phase 4 — Submission 4 (Red) · Due: May 6, Wednesday

#### Student Module — View Enrollments & Navigation

- [ ] Retrieve enrolled courses for the **logged-in student only** from `enrollments.csv` *(5 pts)*
- [ ] Student can **only see their own** enrolled courses *(5 pts)*
- [ ] Output is well-structured, contains **course number and course title**, no duplicates *(5 pts)*
  - Example:

    ```Text
    Hello dhowe2025! Below are courses you are enrolled in:
    Course Number: CSCI-C200, Title: Introduction to Computers
    Course Number: CSCI-C211, Title: Introduction to Computer Science
    ```

- [ ] Student can **navigate easily** among all features (menu-driven) *(2 pts)*
- [ ] Student can **exit the program** easily *(3 pts)*

#### Extra Credit — OOP (Option 2) *(20 pts total)*

- [ ] Implement `Student.view_my_courses()` — filters by username, joins with courses CSV, deduplicates, prints formatted output
- [ ] All 3 classes (`User`, `Admin`, `Student`) complete with fields, `__init__`, `__str__`, getters/setters, all methods
- [ ] Inheritance correct: `Admin(User)` and `Student(User)` call `super().__init__()`
- [ ] Both executables use object instances and invoke class methods throughout

#### Extra Credit — Algorithm Design Document (Option 1) *(20 pts total)*

- [ ] `HoweAlgorithmDesign.docx` — WORD document with **Problem Description** section *(5 pts)*
- [ ] New page per file with title *(3 pts)*
  - Page 1: Problem Description
  - Page 2: Algorithm Design for `HoweAdmin.py`
  - Page 3: Algorithm Design for `HoweStudent.py`
  - Page 4: Algorithm Design for `HoweUtil.py`
  - Page 5: Algorithm Design for `HoweClasses.py`
- [ ] Each page shows the **overall structure** of the file *(7 pts)*
- [ ] Each page shows the **action plan** for every function and executable section *(5 pts)*

#### Final Submission Requirements

- [ ] Submit `admins.csv` with all submissions
- [ ] Submit at least one executable file with all submissions
- [ ] Submit at least one utility file with all submissions
- [ ] Submit `HoweClasses.py` with Submission 4
- [ ] Submit `HoweAlgorithmDesign.docx` with Submission 4
- [ ] Note in submission comments: **"Submitting both Extra Credit Option 1 and Option 2"**
- [ ] If AI or external resources were used, submit a WORD document explaining what was used and which parts of the program were affected

---

## Build Order

### Step 1 — HoweClasses.py

- [ ] User base class (complete)
- [ ] Admin(User) subclass (all methods)
- [ ] Student(User) subclass (all methods)
- [ ] Test: instantiate, authenticate, __str__

### Step 2 — HoweUtil.py

- [ ] Constants (all paths + headers)
- [ ] read_csv()
- [ ] login_control() with user_class param
- [ ] load_students() / load_courses() / load_enrollments()
- [ ] is_value_unique()
- [ ] save_row_to_csv()
- [ ] Test each function independently

### Step 3 — HoweAdmin.py

- [ ] Create admins.csv (3+ entries)
- [ ] Login flow with Admin class
- [ ] Full 6-option menu loop
- [ ] Test: login, lockout, add student, add course, all views

### Step 4 — HoweStudent.py

- [ ] Login flow with Student class
- [ ] Full 3-option menu loop
- [ ] enroll_in_course() function
- [ ] Test: login, enroll, duplicate rejection, view my courses

### Step 5 — End-to-End Testing

- [ ] Admin: login → add 3 students → add 3 courses → view all three
- [ ] Student: login → enroll in 2 courses → view my courses
- [ ] Duplicate enrollment rejected
- [ ] 5 failed logins → lockout
- [ ] First run (no CSVs) → files created cleanly
- [ ] Data persists across runs

### Step 6 — HoweAlgorithmDesign.docx

- [ ] Page 1: Problem description
- [ ] Page 2: HoweAdmin.py structure + action plan
- [ ] Page 3: HoweStudent.py structure + action plan
- [ ] Page 4: HoweUtil.py structure + action plan per function
- [ ] Page 5: HoweClasses.py structure + action plan per class/method

---

## Notes

- All CSV files **except `admins.csv`** are generated by the program — do not create them manually.
- Each submission builds on the previous one — submit **all work done so far** each time.
- If a previous part is redone after a later submission, notify the TA for regrading (max **90% credit** on the regraded portion).
- There are **no late submissions** for any part.
- Reference materials (instructor samples) are in `final_project/reference/` — use them to understand expected patterns, not to copy directly.
- Extra credit is submitted with **Submission 4 only**.

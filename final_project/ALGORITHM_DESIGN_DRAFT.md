# HoweAlgorithmDesign — Draft

> This is the working draft. Final version will be exported as HoweAlgorithmDesign.docx for submission with Phase 4.

---

## Page 1 — Problem Description

This program implements a mini version of a university registrar system. Data is stored in CSV files. The system has two modules:

**Admin Module (`HoweAdmin.py`):**
An admin logs in using credentials stored in `admins.csv` (the only manually created CSV). After authentication (with a 5-attempt lockout), the admin can add new students (saved to `students.csv`), add new courses (saved to `courses.csv`), and view all students, courses, and enrollments in formatted output. The admin navigates via a 6-option menu and can exit cleanly.

**Student Module (`HoweStudent.py`):**
A student logs in using credentials from `students.csv` (created by admins). After authentication (same 5-attempt lockout), the student can enroll in available courses (saved to `enrollments.csv`) and view their own enrolled courses with course titles. The student navigates via a 3-option menu and can exit cleanly.

**Shared Components:**

- `HoweUtil.py` — Utility functions shared by both modules: CSV reading, login control, data loading, uniqueness checking, and CSV writing.
- `HoweClasses.py` — Object-oriented class definitions using inheritance. `User` is the base class storing credentials and authentication. `Admin(User)` adds data management methods. `Student(User)` adds enrollment methods.

**Data Files:**

- `admins.csv` — Admin credentials (manual, username + password)
- `students.csv` — Student records (generated, first_name + last_name + username + password + email)
- `courses.csv` — Course records (generated, course_number + course_title)
- `enrollments.csv` — Enrollment records (generated, username + course_number)

---

## Page 2 — Algorithm Design for the Admin Module (HoweAdmin.py)

### Overall Structure

- Imports: `HoweClasses` (Admin), `HoweUtil` (login_control, constants)
- Constants: `ADMIN_CSV_PATH`, `MAX_LOGIN_ATTEMPTS` (imported from HoweUtil)
- Main flow: login → menu loop → exit

### Action Plan

**Login Section:**

1. Display program header ("Mini Registrar — Admin Module")
2. Call `login_control(ADMIN_CSV_PATH, MAX_LOGIN_ATTEMPTS, Admin)`
3. Receive tuple: `(success, admin_obj)`
4. If success is False: print "Access denied. Exiting." → exit program
5. If success is True: print welcome message with admin_obj.get_username()

**Menu Loop:**

1. Display menu options 1–6
2. Prompt for choice
3. Route:
   - "1" → `admin_obj.add_student()`
   - "2" → `admin_obj.add_course()`
   - "3" → `admin_obj.view_students()`
   - "4" → `admin_obj.view_courses()`
   - "5" → `admin_obj.view_enrollments()`
   - "6" → print "Goodbye." → exit
   - else → print "Invalid choice."
4. After each action, loop back to display menu

**Exit:**

- Option 6 prints goodbye message and ends program cleanly

---

## Page 3 — Algorithm Design for the Student Module (HoweStudent.py)

### Overall Structure_

- Imports: `HoweClasses` (Student), `HoweUtil` (login_control, load_courses, constants)
- Constants: `STUDENTS_CSV_PATH`, `MAX_LOGIN_ATTEMPTS` (imported from HoweUtil)
- Main flow: login → menu loop → exit
- Helper function: `enroll_in_course(student_obj)`

### Action Plan_

**Login Section:**

1. Display program header ("Mini Registrar — Student Module")
2. Call `login_control(STUDENTS_CSV_PATH, MAX_LOGIN_ATTEMPTS, Student)`
3. Receive tuple: `(success, student_obj)`
4. If success is False: print "Access denied. Exiting." → exit program
5. If success is True: print welcome message with student_obj.get_username()

**Menu Loop:**

1. Display menu options 1–3
2. Prompt for choice
3. Route:
   - "1" → `enroll_in_course(student_obj)`
   - "2" → `student_obj.view_my_courses()`
   - "3" → print "Goodbye." → exit
   - else → print "Invalid choice."
4. After each action, loop back to display menu

**enroll_in_course(student_obj):**

1. Load courses using `load_courses()`
2. If no courses: print "No courses available." → return
3. Display numbered list: "1. CSCI-C200 — Introduction to Computers" etc.
4. Prompt for course number (or 'back' to return)
5. If 'back': return to menu
6. Validate entered course number exists in courses list
7. If invalid: print error, re-prompt
8. Call `student_obj.enroll(course_number)`
9. If returns True: print "Successfully enrolled in [course_number]."
10. If returns False: print "You are already enrolled in this course."

**Exit:**

- Option 3 prints goodbye message and ends program cleanly

---

## Page 4 — Algorithm Design for Utility Functions (HoweUtil.py)

### Overall_ Structure

- Imports: `csv`, `os`, `HoweClasses` (Admin, Student)
- Constants: all CSV file paths and header lists
- Functions: 7 utility functions serving both modules

### Action_ Plan

**`read_csv(filepath)`**

- Input: filepath (string)
- Open file at filepath using csv.reader
- Read all rows into a list
- Skip the first row (header)
- Return remaining rows as list of lists
- Output: list of lists

**`login_control(filepath, max_attempts=5, user_class=None)`**

- Input: filepath (str), max_attempts (int), user_class (Admin or Student class)
- Load credential data using read_csv(filepath)
- Determine column indices based on filepath:
  - admins.csv: username_idx=0, password_idx=1
  - students.csv: username_idx=2, password_idx=3
- Set attempts = 0
- While attempts < max_attempts:
  - Prompt for username (strip whitespace)
  - Prompt for password (strip whitespace)
  - For each row in credential data:
    - Create instance: stored = user_class(row[username_idx], row[password_idx])
    - If stored.authenticate(input_username, input_password): return (True, stored)
  - Increment attempts
  - remaining = max_attempts - attempts
  - If remaining > 0: print "Invalid credentials. X attempt(s) remaining."
  - Else: print "Too many failed attempts. Account locked."
- Return (False, None)
- Output: tuple of (bool, user_object or None)

**`load_students()`**

- Input: none
- If os.path.exists(STUDENTS_CSV_PATH) is False: return []
- Else: return read_csv(STUDENTS_CSV_PATH)
- Output: list of lists or empty list

**`load_courses()`**

- Input: none
- Same pattern as load_students() using COURSES_CSV_PATH
- Output: list of lists or empty list

**`load_enrollments()`**

- Input: none
- Same pattern as load_students() using ENROLLMENTS_CSV_PATH
- Output: list of lists or empty list

**`is_value_unique(value, data, column_index)`**

- Input: value (str), data (list of lists), column_index (int)
- For each row in data:
  - If row[column_index].strip().lower() == value.strip().lower(): return False
- Return True
- Output: bool (True if unique, False if duplicate)

**`save_row_to_csv(filepath, headers, new_row)`**

- Input: filepath (str), headers (list of str), new_row (list of str)
- If os.path.exists(filepath) is False:
  - Open file in write mode
  - Write headers as first row using csv.writer
  - Write new_row
- Else:
  - Open file in append mode
  - Write new_row only
- Output: none (side effect: creates or modifies file)

---

## Page 5 — Algorithm Design for OOP Classes (HoweClasses.py)

### Overall_Structure_

- Three classes with inheritance: User (base), Admin(User), Student(User)
- Admin and Student both call super().__init__(username, password)
- User handles credentials and authentication
- Admin handles data entry and viewing
- Student handles enrollment and course viewing

### Action_Plan_

***User (base class)***

`__init__(self, username, password)`:

- Store username as private field self.__username
- Store password as private field self.__password

`get_username(self)` / `get_password(self)`:

- Return the private field value

`set_username(self, username)` / `set_password(self, password)`:

- Set the private field to the new value

`authenticate(self, input_username, input_password)`:

- Compare self.__username.strip() with input_username.strip()
- Compare self.__password.strip() with input_password.strip()
- Return True if both match, False otherwise

`__str__(self)`:

- Return "User: {self.__username}"

---

***Admin(User) subclass***

`__init__(self, username, password)`:

- Call super().__init__(username, password)

`__str__(self)`:

- Return "Admin: {self.get_username()}"

`add_student(self)`:

1. Enter outer loop (keeps adding until admin says no)
2. Prompt for first_name, last_name, username, password, email (all stripped)
3. If any field is empty: print error, continue (restart loop)
4. Load existing students using load_students()
5. Enter inner loop for username uniqueness:
   - If is_value_unique(username, students, 2) is False:
     - Print "Username already exists."
     - Re-prompt for username only
   - Else: break inner loop
6. Save row using save_row_to_csv(STUDENTS_CSV_PATH, STUDENT_HEADERS, [fields])
7. Print "Student added successfully."
8. Prompt "Add another student? (yes/no)"
9. If not "yes": break outer loop

`add_course(self)`:

1. Enter outer loop
2. Prompt for course_number, course_title (stripped)
3. If any field empty: print error, continue
4. Load existing courses using load_courses()
5. Inner loop for course number uniqueness:
   - If is_value_unique(course_number, courses, 0) is False:
     - Print "Course number already exists."
     - Re-prompt for course number only
   - Else: break inner loop
6. Save using save_row_to_csv(COURSES_CSV_PATH, COURSE_HEADERS, [fields])
7. Print "Course added successfully."
8. Prompt "Add another course? (yes/no)"
9. If not "yes": break

`view_students(self)`:

1. Load students using load_students()
2. If empty: print "No students on record." → return
3. Print header: First Name, Last Name, Username, Email (no password)
4. Print separator line
5. For each row: print row[0], row[1], row[2], row[4] (skip index 3 = password)

`view_courses(self)`:

1. Load courses using load_courses()
2. If empty: print "No courses on record." → return
3. Print header: Course Number, Course Title
4. Print separator line
5. For each row: print row[0], row[1]

`view_enrollments(self)`:

1. Load enrollments using load_enrollments()
2. Load courses using load_courses()
3. If enrollments empty: print "No enrollments on record." → return
4. Print header: Username, Course Number, Course Title
5. Print separator line
6. For each enrollment row:
   - username = row[0], course_number = row[1]
   - Look up course_title by matching course_number in courses data
   - If no match found: course_title = "Unknown Title"
   - Print username, course_number, course_title

---

***Student(User) subclass***

`__init__(self, username, password)`:

- Call super().__init__(username, password)

`__str__(self)`:

- Return "Student: {self.get_username()}"

`is_enrolled(self, course_number)`:

1. Load enrollments using load_enrollments()
2. For each row in enrollments:
   - If row[0] == self.get_username() AND row[1] == course_number: return True
3. Return False

`enroll(self, course_number)`:

1. Call self.is_enrolled(course_number)
2. If already enrolled: return False
3. Save using save_row_to_csv(ENROLLMENTS_CSV_PATH, ENROLLMENT_HEADERS, [self.get_username(), course_number])
4. Return True

`view_my_courses(self)`:

1. Load enrollments using load_enrollments()
2. Load courses using load_courses()
3. Initialize empty list: student_courses = []
4. For each enrollment row:
   - If row[0] == self.get_username():
     - course_number = row[1]
     - Look up course_title from courses (default "Unknown Title")
     - entry = [course_number, course_title]
     - If entry not already in student_courses: append it (deduplication)
5. If student_courses is empty:
   - Print "Hello {username}! You are not enrolled in any courses."
   - Return
6. Print "Hello {username}! Below are courses you are enrolled in:"
7. For each entry: print "Course Number: {entry[0]}, Title: {entry[1]}"

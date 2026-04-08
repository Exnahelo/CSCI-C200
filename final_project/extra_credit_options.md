# CSCI-C 200 Final Project — Extra Credit Options

> **Both options will be completed.** This project is built with OOP from Phase 1 and includes a full Algorithm Design document submitted with Phase 4.

---

## Option 1 — Algorithm Design Document *(20 pts)*

Create an Algorithm Design file for the final project as a WORD document demonstrating the high-level design for both modules.

### Rubric

| Requirement | Points |
| --- | --- |
| Algorithm design file is a WORD document and includes a **Problem Description** section | 5 |
| Start the design for each program file on a **new page** with a title (e.g., "Algorithm Design for the Admin Module") | 3 |
| Each design shows the **overall structure** of the file | 7 |
| Algorithm design clearly shows the **action plan** for each executable file and each function | 5 |
| **Option 1 Total** | **20** |

### Scope

- Cover all program files: `HoweAdmin.py`, `HoweStudent.py`, `HoweUtil.py`, and the OOP class file
- Each file gets its own page with a clear title
- Problem Description section describes the full registrar system
- Action plan for each function must match the implemented code

### Submission

- Submit as a WORD document alongside program files in **Submission 4 (Phase 4)**

---

## Option 2 — Object-Oriented Programming *(20 pts)*

Use OOP methods to complete the project. Create at least three classes (`User`, `Student`, `Admin`) and use class methods throughout both modules. Inheritance must be implemented.

### Rubric_

| Requirement | Points |
| --- | --- |
| At least 3 classes created; each class definition is complete and correct (fields, must-have methods, setters/getters, special methods) | 9 |
| Inheritance implemented correctly — `Student` and `Admin` inherit from `User`; super class and sub class responsibilities are correct | 6 |
| OOP used correctly in executables — object instances are created and appropriate methods are invoked | 5 |
| **Option 2 Total** | **20** |

### Class Design Overview

#### `User` (base class)

- **Fields:** `username`, `password`
- **Methods:** `__init__()`, `__str__()`, `authenticate(input_username, input_password)`, getters/setters

#### `Admin(User)` (subclass)

- **Inherits:** `username`, `password`, `authenticate()`
- **Additional Methods:** `add_student()`, `add_course()`, `view_students()`, `view_courses()`, `view_enrollments()`

#### `Student(User)` (subclass)

- **Inherits:** `username`, `password`, `authenticate()`
- **Additional Methods:** `enroll(course_number)`, `is_enrolled(course_number)`, `view_my_courses()`

### Submission_

- Submit the class file alongside program files in **Submission 4 (Phase 4)**
- Note in submission comments that both Option 1 and Option 2 are being submitted for extra credit

---

## Notes

- Both options are worth 20 pts each (40 pts total extra credit)
- Both are submitted together with Submission 4
- Building with OOP from Phase 1 avoids retrofitting — the class structure evolves naturally across all four phases
- The Algorithm Design document will document the final implemented design

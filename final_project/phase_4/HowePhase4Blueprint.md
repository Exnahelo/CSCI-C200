# HowePhase4Blueprint.md — CSCI-C 200 Final Project: Phase 4

***Submission 4 (Red) · Due: May 6, Wednesday · 25 Points + OOP Completion & Algorithm Design Document (Extra Credit)***

---

## 1. Overview

Phase 4 completes the student module and delivers both extra credit options. The student can now view all courses they are personally enrolled in, with output that is well-structured, contains both course number and course title, and contains no duplicate information. Full student menu navigation and a clean exit are finalized.

For Extra Credit Option 2, `Student.view_my_courses()` is implemented, completing the full OOP class hierarchy. For Extra Credit Option 1, `HoweAlgorithmDesign.docx` is written as a WORD document covering all program files. The working draft is maintained in `ALGORITHM_DESIGN_DRAFT.md`.

---

## 2. Phase Objectives (Rubric Mapping)

| Requirement | Points |
| --- | --- |
| Student: view enrolled courses — retrieve from enrollment CSV | 5 |
| Student: view enrolled courses — only show the logged-in student's courses | 5 |
| Student: view enrolled courses — well-structured output with course number and title, no duplicates | 5 |
| Student: easy navigation among features (menu-driven) | 2 |
| Student: easy exit | 3 |
| **Phase 4 Total** | **25** |

### Extra Credit — OOP Option 2 (completed this phase) *(20 pts)*

| Requirement | Phase 4 Contribution |
| --- | --- |
| `Student.view_my_courses()` implemented | In `HoweClasses.py` |
| All 3 classes complete with fields, `__init__`, `__str__`, getters/setters, all methods | Final state of `HoweClasses.py` |
| Inheritance correct: `Admin(User)` and `Student(User)` call `super().__init__()` | Verified in `HoweClasses.py` |
| OOP used correctly in both executables | `HoweAdmin.py` and `HoweStudent.py` |

### Extra Credit — Algorithm Design Document Option 1 (completed this phase) *(20 pts)*

| Requirement | Deliverable |
| --- | --- |
| WORD document with Problem Description section | `HoweAlgorithmDesign.docx` |
| New page per file with title | Pages 1–5 in `HoweAlgorithmDesign.docx` |
| Overall structure of each file shown | Per-file sections |
| Action plan for each executable and function | Per-function descriptions |

---

## 3. File Structure

### Files Modified This Phase

| File | Change |
| --- | --- |
| `HoweStudent.py` | Replace Phase 3 placeholder for "View my courses" with `student_obj.view_my_courses()`; finalize navigation and exit |
| `HoweClasses.py` | Implement `Student.view_my_courses()` |

### New Files Created This Phase

| File | Type | Responsibility |
| --- | --- | --- |
| `HoweAlgorithmDesign.docx` | Extra Credit (Option 1) | Algorithm Design document covering all program files |

### Files Submitted This Phase

- `admins.csv` (unchanged)
- `HoweAdmin.py` (complete from Phase 3)
- `HoweStudent.py` (updated — fully complete)
- `HoweUtil.py` (unchanged)
- `HoweClasses.py` (updated — fully complete)
- `HoweAlgorithmDesign.docx` (new — Extra Credit Option 1)

> **Do not submit** `students.csv`, `courses.csv`, or `enrollments.csv`.
> **Note in submission comments:** "Submitting both Extra Credit Option 1 and Option 2."

---

## 4. Output Design

### Student Enrolled Courses Output

**Required format (from rubric):**

```text
Hello dhowe2025! Below are courses you are enrolled in:

Course Number: CSCI-C200, Title: Introduction to Computers
Course Number: CSCI-C211, Title: Introduction to Computer Science
```

**Rules:**

- Only courses belonging to the logged-in student are shown
- Each course appears exactly once (no duplicates)
- Both course number and course title are displayed
- Course title is looked up from `courses.csv` using the course number from `enrollments.csv`
- If the student has no enrollments, print a friendly "no courses" message

---

## 5. OOP Class Design — Phase 4 Completion

### 5.1 `Student.view_my_courses()` — Implemented

```python
def view_my_courses(self):
    from HoweUtil import load_enrollments, load_courses
    enrollments = load_enrollments()
    courses = load_courses()

    # filter and join
    student_courses = []
    for row in enrollments:
        if row[0] == self.get_username():
            course_number = row[1]
            course_title = "Unknown Title"
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
```

---

### 5.2 Complete Class Hierarchy Summary

```hierarchy
User (base class)
├── __init__(username, password)         → private __username, __password
├── get_username() / set_username()
├── get_password() / set_password()
├── authenticate(input_username, input_password) → bool (case-sensitive, stripped)
└── __str__() → "User: {username}"

Admin(User)
├── __init__(username, password)         → super().__init__()
├── __str__() → "Admin: {username}"
├── add_student()                        [Phase 2]
├── add_course()                         [Phase 2]
├── view_students()                      [Phase 3]
├── view_courses()                       [Phase 3]
└── view_enrollments()                   [Phase 3]

Student(User)
├── __init__(username, password)         → super().__init__()
├── __str__() → "Student: {username}"
├── is_enrolled(course_number) → bool    [Phase 3]
├── enroll(course_number) → bool         [Phase 3]
└── view_my_courses()                    [Phase 4]
```

---

## 6. Algorithm Design

### 6.1 Finalized Student Menu Algorithm

```algarithm
After successful student login (student_obj is authenticated Student instance):

Repeat:
    Display student menu:
        1. Enroll in a course
        2. View my courses
        3. Exit

    Prompt for choice

    If choice = "1": enroll_in_course(student_obj)
    Else if choice = "2": student_obj.view_my_courses()
    Else if choice = "3": print "Goodbye." → sys.exit()
    Else: print "Invalid choice."

Until user exits
```

---

### 6.2 `Student.view_my_courses()` Algorithm

```algorithm
Load enrollments from enrollments.csv using load_enrollments()
Load courses from courses.csv using load_courses()

Initialize empty list: student_courses = []

For each enrollment row:
    If row[0] == self.get_username():
        course_number = row[1]
        course_title = "Unknown Title"
        For each course row:
            If course[0] == course_number:
                course_title = course[1]
                Break
        entry = [course_number, course_title]
        If entry not in student_courses:
            Append entry to student_courses   (deduplication)

If student_courses is empty:
    Print "Hello {username}! You are not enrolled in any courses."
    Return

Print "Hello {username}! Below are courses you are enrolled in:"
For each entry in student_courses:
    Print "Course Number: {entry[0]}, Title: {entry[1]}"
```

---

## 7. Variable Design

| Variable | Type | Purpose |
| --- | --- | --- |
| `student_courses` | list of lists | Each entry is `[course_number, course_title]` for the logged-in student |
| `course_title` | string | Title looked up from `courses.csv` for a given course number |
| `entry` | list | A single `[course_number, course_title]` pair used for deduplication check |

---

## 8. Edge Cases & Validation

| Scenario | Handling |
| --- | --- |
| Student has no enrollments | Print "Hello [username]! You are not enrolled in any courses." |
| A course number in `enrollments.csv` doesn't match any row in `courses.csv` | Display "Unknown Title" rather than crashing |
| `enrollments.csv` doesn't exist | `load_enrollments()` returns `[]`; student sees "not enrolled" message |
| `courses.csv` doesn't exist | `load_courses()` returns `[]`; all titles display as "Unknown Title" |
| Duplicate rows in `enrollments.csv` for same student/course | Deduplication in `view_my_courses()` ensures each course appears only once |
| Student selects invalid menu option | Print "Invalid choice." and re-display menu |
| Student exits from menu | Print "Goodbye." and end program cleanly |

---

## 9. Extra Credit Option 1 — Algorithm Design Document Structure

`HoweAlgorithmDesign.docx` must be a WORD document. Working draft is in `ALGORITHM_DESIGN_DRAFT.md`.

**Page 1 — Problem Description** *(5 pts)*

- Purpose: mini registrar system with admin and student modules
- Data storage: CSV files for admins, students, courses, enrollments
- Admin module: login, add students, add courses, view all data
- Student module: login, enroll in courses, view enrolled courses
- OOP design: User base class, Admin and Student subclasses with inheritance
- Files: `HoweAdmin.py`, `HoweStudent.py`, `HoweUtil.py`, `HoweClasses.py`

**Page 2 — Algorithm Design for `HoweAdmin.py`** *(3 pts structure + 5 pts action plan)*

- Imports, constants, main flow: login → menu loop → exit
- Action plan: login section, 6-option menu routing, exit

**Page 3 — Algorithm Design for `HoweStudent.py`** *(3 pts structure + 5 pts action plan)*

- Imports, constants, main flow: login → menu loop → exit
- Action plan: login section, 3-option menu routing, `enroll_in_course()` helper, exit

**Page 4 — Algorithm Design for `HoweUtil.py`** *(3 pts structure + 5 pts action plan)*

- Imports, constants, 7 functions
- Action plan per function: input → processing → output

**Page 5 — Algorithm Design for `HoweClasses.py`** *(3 pts structure + 5 pts action plan)*

- Three classes with inheritance
- Action plan per class and method

---

## 10. Development Sequence

1. Implement `Student.view_my_courses()` in `HoweClasses.py`
2. Update `HoweStudent.py` — replace Phase 3 placeholder with `student_obj.view_my_courses()`
3. Finalize student menu loop — confirm navigation returns to menu after every action
4. End-to-end test: login as student → enroll in 2 courses → view enrolled courses → verify output format
5. Edge case test: student with no enrollments → verify friendly message
6. Edge case test: verify no duplicate courses appear in output
7. Write `HoweAlgorithmDesign.docx` — follow the 5-page structure above

---

## 11. Submission Checklist

- [ ] `admins.csv` — unchanged
- [ ] `HoweAdmin.py` — complete from Phase 3
- [ ] `HoweStudent.py` — fully complete: login, enroll, view my courses, navigation, exit
- [ ] `HoweUtil.py` — all utility functions complete
- [ ] `HoweClasses.py` — all 3 classes complete with all methods
- [ ] `HoweAlgorithmDesign.docx` — 5-page algorithm design document
- [ ] Student can view only their own enrolled courses
- [ ] Output includes course number and course title for each enrollment
- [ ] Output contains no duplicate course entries
- [ ] Output greeting includes the student's username
- [ ] Student menu navigates cleanly between all options
- [ ] Student can exit the program from the menu
- [ ] All 3 classes (`User`, `Admin`, `Student`) are complete and correct
- [ ] Inheritance implemented correctly (`super().__init__()` called in both subclasses)
- [ ] Both executables create object instances and invoke class methods
- [ ] Algorithm Design document has Problem Description, one page per file, structure and action plan for each function
- [ ] Submission comment notes: "Submitting both Extra Credit Option 1 and Option 2"
- [ ] If AI or external resources were used, submit a WORD document explaining what was used and which parts of the program were affected

---

## 12. Full Project File Summary

| File | Created In | Role |
| --- | --- | --- |
| `admins.csv` | Phase 1 (manual) | Admin credentials — only manually created CSV |
| `HoweAdmin.py` | Phase 1 | Admin module executable |
| `HoweUtil.py` | Phase 1 | Shared utility functions and constants for both modules |
| `HoweClasses.py` | Phase 1 | `User`, `Admin`, `Student` class definitions |
| `HoweStudent.py` | Phase 3 | Student module executable |
| `HoweAlgorithmDesign.docx` | Phase 4 | Extra Credit Option 1 — Algorithm Design document |
| `students.csv` | Phase 2 (generated) | Student records — do not submit |
| `courses.csv` | Phase 2 (generated) | Course records — do not submit |
| `enrollments.csv` | Phase 3 (generated) | Enrollment records — do not submit |

---

## 13. Conceptual Summary

Phase 4 closes the loop on the student experience and delivers the full extra credit package. `Student.view_my_courses()` is the final method in the class hierarchy — it performs a two-step operation: filtering the enrollment CSV by the logged-in username, then joining with the courses CSV to retrieve human-readable titles. The deduplication step ensures clean output regardless of the CSV state. The Algorithm Design document captures the complete architecture of the system, serving as both a submission artifact and a portfolio reference. Together, the OOP design and the algorithm document demonstrate a level of engineering rigor well beyond the base requirements.

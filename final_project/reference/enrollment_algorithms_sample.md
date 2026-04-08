# Reference: Enrollment Algorithms — Instructor Sample

> **Source:** Class-provided pseudocode from instructor (`algorithmsForEnrollment.txt`).
> This is a reference for understanding the expected logic. Your implementation will follow these patterns using your own variable names, OOP structure, and utility functions.

---

## Part 1 — Student Enrolls in a Course

### Algorithm Steps

```python
1. Read course.csv file and store data in a 2-D array (enData)

2. Loop through enData and display each course to the user:

    print("Here are courses you can enroll in:")
    N1, T1
    N2, T2
    N3, T3

3. Ask user to enter the course number to enroll:

    selectedCourses = []

    while True:
        cn = input("Please enter a course number to enroll")

        # loop through enData and check if cn is one of the allowed values
        for i in range(len(enData)):
            newRow = enData[i]
            if cn == newRow[0]:
                # check if cn and username combination is already in enroll.csv
                # if not, append the cn
                selectedCourses.append(cn)
                break

        continue = input("Do you wish to enroll in another course? Enter yes or no")
        if continue == "no":
            break

4. Write the selectedCourses array to enroll.csv, along with the student username:
    # loop through the array and do file append
```

---

## Part 2 — Student Views Their Enrolled Courses

### Algorithm Steps_

```python
1. Read data from enroll.csv and store in enData array:

    # the array looks like this:
    N1, U1
    N2, U2
    N3, U1

2. Read data from course.csv and store in crData array:

    # the array looks like this:
    N1, T1
    N2, T2
    N3, T3

3. Select courses the student is enrolled in:

    # assume username is the variable storing the student username from login
    username = "U1"

    enrolledCourses = []
    for i in range(len(enData)):
        newRow = enData[i]
        if username == newRow[1]:
            enrolledCourses.append(newRow[0])

    # when loop finishes, enrolledCourses looks like: [N1, N3]

4. Output course information using enrolledCourses and crData:

    for i in range(len(enrolledCourses)):
        cn = enrolledCourses[i]
        # loop through crData and output the matching title
        for j in range(len(crData)):
            newRow = crData[j]
            if cn == newRow[0]:
                print("Course Number: " + cn + ", Course Title: " + newRow[1])
                break
```

---

## Notes for Implementation

- **Part 1** maps to `Student.enroll(course_number)` in the OOP version, or `enroll_student()` in `HoweUtil.py`
- **Part 2** maps to `Student.view_my_courses()` in the OOP version, or `get_student_courses(username)` + `display_student_courses(username)` in `HoweUtil.py`
- The enrollment CSV column order in the instructor sample is `course_number, username` — note your implementation uses `username, course_number` (check your column index references accordingly)
- The duplicate enrollment check (`checkUniqueEnrollment`) is shown in `help_session_sample_codes.md`
- The inner loop for matching course titles is the join operation between `enrollments.csv` and `courses.csv`

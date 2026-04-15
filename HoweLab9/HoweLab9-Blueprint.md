# Lab9 Blueprint

This blueprint stays within the scope of **Lab 9 – Object Oriented Programming** and is aligned to the assignment rubric.

## Objective

Build a small OOP demonstration for the mini registrar project with:

- one parent class: `User`
- two child classes: `Admin` and `Student`
- one executable file that demonstrates the required object-oriented behavior

## Scope rule

Stay inside the assignment.

Do **not** redesign the registrar system.
Do **not** add extra architecture.
Do **not** add compatibility layers unless they are necessary to complete the required demo.
Do **not** expand the project beyond the rubric.

## Required file structure

To match the rubric requirement to have a class file for each class definition, use this structure:

- `User.py`
- `Admin.py`
- `Student.py`
- `Lab9Demo.py`

If you want to reuse ideas from existing project files, that is fine, but the Lab 9 deliverable should still clearly present one file per class plus one executable demo file.

## 1. Parent class: `User`

In `User.py`, create a parent class named `User`.

### Required fields
- `username`
- `password`

### Required method groups
Include these three groups of methods:

1. Must-have methods  
   - constructor such as `__init__`
   - string or display helper if you want one

2. Setters and getters  
   Include setters and getters for:
   - `username`
   - `password`

3. Action method  
   Include at least one action method such as:
   - `authenticateUser()`

## 2. Child class: `Admin`

In `Admin.py`, create a child class named `Admin` that inherits from `User`.

### Required Admin field
Add at least one Admin-specific field, such as:
- `adminAccessLevel`

### Required Admin methods
- constructor that uses inheritance correctly
- setter/getter for the Admin-specific field
- at least one Admin action method

The action method can be simple. It only needs to show that `Admin` has behavior of its own.

## 3. Child class: `Student`

In `Student.py`, create a child class named `Student` that inherits from `User`.

### Required Student fields
Add these Student-specific fields:
- `firstName`
- `lastName`
- `email`

### Required Student methods
- constructor that uses inheritance correctly
- setters/getters for:
  - `firstName`
  - `lastName`
  - `email`
- at least one Student action method

The action method can be simple. It only needs to show that `Student` has behavior of its own.

## 4. Executable file requirement

Create one executable file for the lab demonstration:

- `Lab9Demo.py`

This file must:

1. Create at least one `Admin` object
2. Print all field values for the `Admin` object
3. Call a setter method on the `Admin` object
4. Print the updated Admin field value after the setter call
5. Create at least one `Student` object
6. Print all field values for the `Student` object
7. Call a setter method on the `Student` object
8. Print the updated Student field value after the setter call
9. Invoke a superclass method through a subclass object

## 5. What `Lab9Demo.py` must show

### Admin demo
- create one `Admin` object
- print:
  - `username`
  - `password`
  - `adminAccessLevel`
- call one Admin setter
- print the updated Admin field value

### Student demo
- create one `Student` object
- print:
  - `username`
  - `password`
  - `firstName`
  - `lastName`
  - `email`
- call one Student setter
- print the updated Student field value

### Superclass-method demo
Call a `User` method through a subclass object.

Examples:
- call `getUsername()` using a `Student` object
- call `getUsername()` using an `Admin` object
- call `authenticateUser()` using either subclass object

## 6. Disclosure comment block

In `Lab9Demo.py`, include a block comment below the file header.

That comment must state whether outside help was used.

If outside help was used, say:
- what resource helped
- what part of the program it influenced

Use a truthful statement.

## 7. Keep it simple

Use straightforward beginner-friendly Python.

Do not add:
- menus
- extra CSV workflows
- advanced abstractions
- unnecessary helper layers
- major changes to the existing registrar project

Only add what is needed to meet the lab rubric.

## 8. Suggested implementation order

1. Create `User.py` with required fields and method groups
2. Create `Admin.py` so `Admin` inherits from `User`
3. Create `Student.py` so `Student` inherits from `User`
4. Add all required setters/getters
5. Add one action method to each child class
6. Create `Lab9Demo.py`
7. Run the program and verify every rubric item appears in output
8. Add the required disclosure comment block

## 9. Final checklist

### `User`
- [ ] `User` class exists
- [ ] `username` field exists
- [ ] `password` field exists
- [ ] must-have methods exist
- [ ] getters/setters exist
- [ ] one action method exists

### `Admin`
- [ ] `Admin` inherits from `User`
- [ ] `Admin` has at least one field of its own
- [ ] `Admin` setter/getter exists for its own field
- [ ] `Admin` has at least one action method

### `Student`
- [ ] `Student` inherits from `User`
- [ ] `Student` has `firstName`
- [ ] `Student` has `lastName`
- [ ] `Student` has `email`
- [ ] `Student` setters/getters exist
- [ ] `Student` has at least one action method

### Executable file
- [ ] one `Admin` object is created
- [ ] all Admin field values are printed
- [ ] one Admin setter is called
- [ ] updated Admin field value is printed
- [ ] one `Student` object is created
- [ ] all Student field values are printed
- [ ] one Student setter is called
- [ ] updated Student field value is printed
- [ ] one superclass method is invoked through a subclass object

### Submission requirement
- [ ] disclosure comment block is included in the executable file

## 10. Rubric alignment notes

This blueprint is designed to satisfy the rubric by making these points explicit:

- `User` is the superclass with `username` and `password`
- `User` has three method groups
- `Admin` inherits from `User`
- `Admin` has at least one field of its own
- `Admin` has setters/getters and one action method
- `Student` inherits from `User`
- `Student` has `firstName`, `lastName`, and `email`
- `Student` has setters/getters and one action method
- each class has its own class file
- one executable file demonstrates object creation, field printing, setter use, and superclass-method invocation
- the executable file includes the required disclosure statement

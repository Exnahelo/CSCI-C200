# CSCI-C200 — Lab 9: Object Oriented Programming

**Due:** April 15, Wednesday, 11:59pm  
**Accept Until:** April 22, Wednesday, 11:59pm, with late penalties

## Purpose

Software applications provide a virtual world simulating the world we live in. In the real world, objects exist everywhere, from the physical objects we can see with our eyes, such as tables, phones, houses, students, and so on, to concepts such as course evaluations or transactions.

In general, if we can describe something with many different attributes, we call it an **object**. For instance, we can describe a student through attributes such as first name, last name, email, student ID, weight, height, and so on. Thus, the student is an object.

Lots of software applications have been developed using these objects, and one example is the Canvas we use on campus. On Canvas, many object concepts are used, including student, course, assignment, and instructor, and these objects are designed to simulate how they interact with each other in the real world.

You will practice Object-Oriented Programming through this lab and learn to develop software applications using the OOP method.

## Learning Outcomes

Upon successful completion of this lab, you will be able to:

- Understand the relationship between a class and an object
- Understand the relationship between a parent class and a child class
- Create a class with required elements
- Create object instances based on a class definition
- Create subclasses with required elements
- Create object instances from subclasses
- Separate class files and executable files

## Description

Use the mini registrar’s system you are developing for the final course project to create classes and objects, and write executable code to demonstrate how objects work.

## Tasks

- Create a super (parent) class called `User`.
  - Define `username` and `password` fields.
  - Define three groups of methods:
    - Group 1: must-have methods
    - Group 2: setters and getters
    - Group 3: action methods such as `authenticateUser()`

- Create subclasses to simulate `Admin` and `Student`.
  - They should inherit from the `User` class.
  - Define necessary fields for each object.
  - A `Student` object must have at least three fields:
    - first name
    - last name
    - email
  - An `Admin` object can have an `adminAccessLevel` field whose values can be integers.

- Define necessary methods in each subclass, with at least one action method in Group 3.

- Have a separate class file for each class definition.

- Create an executable file with statements to:
  - create an object instance for each subclass
  - print out all field values for each object
  - call a setter method in each object to set a field value
  - invoke a method in the super class through a subclass object  
    Example: print out the username of a student by calling the `getUsername()` method in the super class `User`

## Rubric

### Super Class

- Super class is created, with at least `username` and `password` fields. (5)
- Super class has three groups of methods defined. (5)
- Super class has all the setters and getters. (5)

### Admin Class

- Admin class is created and inherits from the super class. (5)
- Admin class has at least one field of its own. (5)
- Admin class has all the necessary setters and getters. (5)
- Admin class has at least one action method. (5)

### Student Class

- Student class is created and inherits from the super class. (5)
- Student class has necessary fields of its own. (5)
- Student class has all the necessary setters and getters. (5)
- Student class has at least one action method. (5)

### Executable File Demonstration

- At least one object instance is created for the `Admin` class. (5)
- All field values for the admin object are printed on the console. (5)
- A setter method is called on the admin object. (5)
- At least one object instance is created for the `Student` class. (5)
- All field values for the student object are printed on the console. (5)
- A setter method is called on the student object. (5)
- A method in the super class is invoked through a subclass object. (5)

### Resource Disclosure

- Explain whether you received help from any other resources.
- If you got help from any other resources, such as:
  - a classmate
  - a website
  - a generative AI tool

  explain:
  - where you got help, ideas, or code samples
  - what part of your program is affected
  - what code was borrowed, if any

- Use a block of comments below your file header in the executable file to explain. (10)

**Important:** If you do not explain this, and your program contains code similar to another resource, you will receive a **0** on this assignment.

## Submission

Submit all your files on Canvas.

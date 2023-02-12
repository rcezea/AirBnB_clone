# AirBnB Clone - The Console
---
## Description

This project is the first step towards building a full web application of the AirBnB clone. In this first step we are building a console, a custom command interpreter that will be used in subsequent AirBnB projects to manage objects of our classes.

This console will allow us to do the following:

* Create a `new object`
* Retrieve an object from a `file, a database etc…`
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Usage

* The console can be run in both interactive and non-interactive mode.
* It prints a prompt **(hbnb)** and waits for the user for input.

### Interactive Mode

```cmd
$ ./console.py
(hbnb) help


Documented commands (type help <topic>):

========================================

EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```
### Non-Interactive Mode

```cmd

$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):

========================================

EOF  help  quit

(hbnb)

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

Documented commands (type help <topic>):

========================================

EOF  help  quit

(hbnb)

$

```
## Commands

Command | Description

--- | ---

`quit` | Exits the program
`EOF` | Exits the program
`create <class>` | Creates an instance of a class
`show <class> <id>` | Prints the string representation of an instance of a class based on class name and id
`destroy <class> <id>` | Deletes instance of a class based on class name and id
`all` | Prints all string representations of all instances
`all <class>` | Prints all string representations of all instances based on class name
`update <class> <id> <attribute name> "<attribute value>"` | Updates an attribute of an instance based on class name and id
`<class>.all()` | Retrieves all instances of a class
`<class>.count()` | Retrieves the number of instances of a class
`<class>.show(<id>)` | Retrieves an instance based on its id
`<class>.destroy(<id>)` | Destroys an instance based on its id

---

# PART 2 OF AIRBNB CLONE - WEBSTATIC 

Web static, what?

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static page
Learn to Code HTML & CSS (until “Creating Lists” included)
Inline Styles in HTML
Specifics on CSS Specificity
CSS SpeciFishity
Introduction to HTML
CSS
MDN
center boxes
Learning Objectives

General
What is HTML
How to create an HTML page
What is a markup language
What is the DOM
What is an element / tag
What is an attribute
How does the browser load a webpage
What is CSS
How to add style to an element
What is a class
What is a selector
How to compute CSS Specificity Value
What are Box properties in CSS


Requirements

General
Allowed editors: vi, vim, emacs
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be W3C compliant and validate with W3C-Validator
All your CSS files should be in styles folder
All your images should be in images folder
You are not allowed to use !important and id (#... in the CSS file)
You are not allowed to use tags img, embed and iframe
You are not allowed to use Javascript
Current screenshots have been done on Chrome 56 or more.
No cross browsers
You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

## Authors
* **Lerato Masha** - Github: [Leratho](https://github.com/leratho) 
* **Richard E** - Github: [rcezea](https://github.com/rcezea) 

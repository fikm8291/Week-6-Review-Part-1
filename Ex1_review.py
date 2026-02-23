# -------------------------------------------
# Exercise 1: Revision & String Methods
# -------------------------------------------
#
# GOAL:
# 1. Review core concepts: variables, input, if/else, loops, and operators.
# 2. Master String Methods: .lower(), .upper(), and .strip().
# 3. Practise the Core Git Workflow: Stage -> Commit -> Push.
#
# CONCEPT:
# String methods are built-in functions that let you modify or check text easily.
# - .lower() converts text to lowercase (e.g. "Apple" becomes "apple").
# - .upper() converts text to uppercase (e.g. "apple" becomes "APPLE").
# - .strip() removes "whitespace" (extra spaces) from the start and end of a string.
#
# -------------------------------------------


# -------------------------------------------
# Task 1: User Input & Variables Review
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: User Input & Variables Review\n"
    + "-------------------------------------------")

# DEMO: How to use a string method
# -------------------------------------------
# To use a method, you put a dot '.' after the variable name, 
# then the method name followed by brackets ().
#
# example_word = "  PYTHON  "
# clean_word = example_word.strip()  # Removes spaces -> "PYTHON"
# lower_word = clean_word.lower()    # Makes lowercase -> "python"
# -------------------------------------------

# TODO:
# 1. Ask the user for their name and age.
# 2. Use the .strip() method on their name to remove any accidental extra spaces.
# 3. Convert their age to an integer using int().
# 4. Print a friendly message using an f-string.
#
# EXPECTED OUTPUT:
# Enter your name:    Alice   
# Enter your age: 20
# Hello, Alice! You are 20 years old.

# Write your code below:


# -------------------------------------------
# Task 2: Decision Making (if / else)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Decision Making (if / else)\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their favourite colour.
# 2. Use the .lower() method to "normalise" their answer so capital letters don't break your logic.
# 3. Use if/elif/else to:
#    - Print "Nice choice!" if the colour is "blue".
#    - Print "That’s a bright choice!" if the colour is "yellow".
#    - Otherwise, print "That’s an interesting colour!"

# Write your code below:


# -------------------------------------------
# Task 3: Multiplication Table (For Loops)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: Multiplication Table\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a number between 1 and 10.
# 2. Use a for loop and the range() function to print the multiplication table 
#    for that number (from 1 up to 10).
#
# EXPECTED OUTPUT:
# Enter a number: 3
# 3 x 1 = 3
# ...
# 3 x 10 = 30

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Core Tasks. Let's save.
# 1. Save this file (Ctrl+S or Cmd+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex1_revision.py
#    git commit -m "Completed core revision tasks"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Username Generator
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: Username Generator\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their first name and their favourite number.
# 2. Convert the name to lowercase.
# 3. Combine them into a single string to create a username.
# 4. Print: "Your username could be: [username]"

# Write your code below:


# Extension 2: Counting with Conditions
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Counting with Conditions\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a number (int).
# 2. Use a for loop to iterate from 1 up to that number.
# 3. Inside the loop, use the modulus operator (%) to check if the current 
#    number is Even or Odd, and print the result for each number.
#
# Hint: if number % 2 == 0:

# Write your code below:


# Extension 3: Secure Password Checker (While Loops)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: Secure Password Checker\n"
    + "-------------------------------------------")

# TODO:
# 1. Set a variable 'correct_password' to "python123".
# 2. Create a variable 'attempts' starting at 3.
# 3. Use a while loop to let the user try to log in.
# 4. The loop should continue while attempts are greater than 0.
# 5. Inside the loop:
#    - Ask for the password and use .strip().lower() on the input.
#    - If it matches, print "Access granted" and use 'break' to stop the loop.
#    - If it's wrong, subtract 1 from attempts and print how many tries are left.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Extensions. Let's save.
# 1. Save this file.
# 2. Run:
#    git add Ex1_revision.py
#    git commit -m "Completed revision extensions"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: Student Score Checker
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: Student Score Checker\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a student’s name and three separate test scores.
# 2. Calculate the average of the three scores.
# 3. Use logic to determine a grade feedback:
#    - 70 or more: "Excellent!"
#    - 50 to 69: "Good effort!"
#    - Below 50: "Needs improvement."
# 4. Print a summary. Use .title() on the student's name so it looks professional.
#
# EXPECTED OUTPUT:
# Student: Emma
# Average Score: 71.7
# Feedback: Excellent!

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex1_revision.py
#    git commit -m "Completed student score checker"
#    git push origin main
# -------------------------------------------

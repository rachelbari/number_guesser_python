# Python Number Guesser Game
In this project, you will build a number guessing game to play in the command line. The python program randomly generates a random number, and the user guesses what the number is. If the user's guess is correct, the program will tell them they're correct and quit out. Otherwise, the program will tell them if their guess is too high or low. 

# Lesson Skills:
* Integers and strings
* Integer operations
* Variables
* Random function
* Input/output
* Loops

# Integers/strings
* In programming languages, we can think about data in terms of different categories. For example, we consider words and sentences ("hi friend!") to be different from integers (100), or even decimal numbers (1.2345)
* Two common data types are **integers** and **strings**
  - **Integers** are whole numbers. They can be positive or negative, but cannot be followed by a decimal point. Examples of integers include 1, 2, 5, 1000, -586003, 7575757575
  - **Strings** are sequences of characters. When using strings, we always put quotes around the word/sentence. Examples of strings include, "code", "hello world", "i love my dog"
 - [More on python data types](https://realpython.com/python-data-types/)

# Python Comparison Operators

# Variables
* Variables are used to store data values, so we can use them later.

* Declaring an integer variable
``` 
my_lucky_number = 15
```

* Declaring a string variable
```
  my_name = "Rachel"
 ```
* Note: in some programming languages, when you define a variable, you must also declare what data type it will store. Python is dynamically typed, which means we don't have to declare what type each variable is.
* [More on python variables](https://realpython.com/python-variables/)

# Random function
* A function is a block of code that runs when it is called. You can also pass data, known as parameters, into a function.
* You can write your own functions, use python built-in functions, or even use functions that other people have written!
* The random function is a special function that generates a random number. For example
```
import random
print random.randint(1, 5) # returns a random number between 1 and 5
```

# Input/output
* Since this game is run through the command line, we can store user input and print back to the command line


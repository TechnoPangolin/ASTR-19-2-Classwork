'''
Title: CJ1_p3.py
Author: April Ewers
Date: 2025-04-02
Assignment: Code Journal #1 Prompt #3
Task: Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, 
call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
'''

#define the functiuon per the given formula
def f(x):
    return x ** 3 + 8

#define main function
def main(args=None):
    #print the result of f(9)
    print(f(9))

    #check if f(9) is greater than 27
    if f(9) > 27:
        #print the string if it is
        print("YAY!")

if __name__ == "__main__":
    main()

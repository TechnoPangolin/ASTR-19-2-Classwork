'''
Title: CJ1_p2.py
Author: April Ewers
Date: 2025-04-02
Assignment: Code Journal #1 Prompt #2
Task: Write a Python program that prints the sum of two floating point numbers, 
    the difference between two integers, and the product of a floating point number and an integer. 
    In each case, have the program print out the data type of the resulting answer.
'''

def main():
    #create two floats
    flt1, flt2 = 0.123, 1.23
    #get their sum
    sum = flt1 + flt2
    #output their sum
    print(sum)
    #output the data type of the result
    print(type(sum))

    #create two ints
    int1, int2 = 5, 9
    #get the difference between them
    diff = abs(int1 - int2)
    #output their diff
    print(diff)
    #output the data type of the result
    print(type(diff))

    #get the product of a float and an int 
    prod = flt2 * int2
    #output product of float and int w/ previous vars
    print(prod)
    #output the data type of the result
    print(type(prod))

if __name__ == "__main__":
    main()
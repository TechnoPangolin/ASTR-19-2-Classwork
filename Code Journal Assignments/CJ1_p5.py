'''
Title: CJ1_p5.py
Author: April Ewers
Date: 2025-04-02
Assignment: Code Journal #1 Prompt #5
Task: Write a Python program that writes out a table of the function sin(x) vs. x, 
        where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.
'''

import math

def main():
    #print a formatted table header
    print("{:^8}{:^8}".format("x", "sin(x)"))

    #loop through a thousand values between [0, 2). I was unclear if 2 was meant to be included, but this way makes a clean thousand by
    #stepping in increments of .002
    for i in range(1000):
        #calculate the sine value
        sin = math.sin(i/500)
        #output the values centered in 8 character wide columns with enough decimal places to appreciate
        print("{:^8.3f}{:^8.5f}".format(i/500, sin))



if __name__ == "__main__":
    main()
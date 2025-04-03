'''
Title: CJ1_p4.py
Author: April Ewers
Date: 2025-04-02
Assignment: Code Journal #1 Prompt #4
Task: Write a Python program that declares a class describing your favorite animal. Have the data members of the class represent the following physical parameters of the animal: 
        length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). 
        Write an initialization function that sets the values of the data members when an instance of the class is created. 
        Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
'''

def main():
    #create a snake
    s1 = Snake()
    #tell me about the snake you just made up
    s1.describe()

class Snake:

    #Initialize with values accurately reflecting a snake
    def __init__(self):
        self.lengthArms = 0.0
        self.lengthLegs = 0.0
        self.numEyes = 2
        self.hasTail = True
        self.isFurry = False

    #Function to describe a snake via print statements using the class values.
    def describe(self):
        #use string formatting to insert values
        print("A snake's arms are {} centimeters long.".format(self.lengthArms))
        print("A snake's legs are {} centimeters long.".format(self.lengthLegs))
        print("A snake has {} eyes.".format(self.numEyes))
        #use ternaries to change the text used based on boolean values
        print("A snake {} a tail.".format("has" if self.hasTail else "does not have"))
        print("A snake {} furry.".format("is" if self.isFurry else "isn't"))
    

if __name__ == "__main__":
    main()
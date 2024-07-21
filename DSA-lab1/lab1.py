# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Yuvraj Singh
# Student Number: 155580210
#

# Function 1: wins_rock_scissors_paper
def wins_rock_scissors_paper(Player1, Player2):
    
    if Player1.upper() == "ROCK" and Player2.upper() == "SCISSORS":
        return True
    elif Player1.upper() == "PAPER" and Player2.upper() == "ROCK":
        return True
    elif Player1.upper() == "SCISSORS" and Player2.upper() == "PAPER":
        return True
    else:
        return False

# Function 2: factorial calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function 3: fibonacci series
def fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function 4: sum_to_goal
def sum_to_goal(Number, GoalNumber):
    for i in range(len(Number)):
        for j in range(i+1, len(Number)):
            if Number[i] + Number[j] == GoalNumber:
                return Number[i] * Number[j]
    return 0

# Python class: UpCounter
class UpCounter:
    def __init__(self, step_size=1):
        self.count_value = 0
        self.step_size = step_size

    def count(self):
        return self.count_value

    def update(self):
        self.count_value += self.step_size

# Python class: DownCounter 
class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.step_size
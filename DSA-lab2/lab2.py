# copy over your code from lab 1 to this file

def fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def sum_to_goal(Number, GoalNumber):
    for i in range(len(Number)):
        for j in range(i+1, len(Number)):
            if Number[i] + Number[j] == GoalNumber:
                return Number[i] * Number[j]
    return 0

    

    
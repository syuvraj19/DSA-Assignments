#
# Author: Yuvraj Singh
# Student Number: 155580210
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(num):
    base_case = 1          
    if(num > 1) :
        base_case= num * factorial(num-1)
    
    return base_case

print(factorial(5))

def linear_search(list, key):
    def l_search_recursive(lst, num):
        if lst[0] == num:
            return 0
        return 1 + l_search_recursive(lst[1:], num)
    try: return l_search_recursive(list, key)
    except IndexError: return -1
    
print(linear_search([10,5,4,7,1,0],5))


def binary_search(list, key):
    def b_search_recursive(first, num):
        if first[0] == num:
            return 0
        return 1 + b_search_recursive(first[1:], num)
    try: return b_search_recursive(list, key)
    except IndexError: return -1
    
print(binary_search([0,1,2,3,4,5],4))
# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)

ANALYSIS
		
def function1(value, number):
    if (number == 0):         # 1 operation
        return 1              # 1 operation
    elif (number == 1):       # 1 operation
        return value          # 1 operation
    else:
        return value * function1(value, number-1)  # 2 operations (multiplication and recursive call) 
                                                  # + T(number-1) operations from the recursive call

T(number) represents the number of ops needed to our function
So I can actually rewrite our count summary as follows:
    T(number)=4+2+T(number-1)
             =6+T(number-1)
             =T(1)=2 and T(0)=2
There are a total of (number-1) 6's.We know this because we need to reach T(1) to get the 2.
T(number)=6(number−1)+2=6n−4
Thus, T(number) is O(number)
```


## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

ANALYZE
	
def recursive_function2(mystring, a, b):
    if (a >= b):  # 2 operations (comparison and return)
        return True  # 1 operation
    else:
        if (mystring[a] != mystring[b]):  # 2 operations (two comparisons)
            return False  # 1 operation
        else:
            return recursive_function2(mystring, a + 1, b - 1)  # 2 operations (addition and subtraction) + T(len(mystring) - 1)

def function2(mystring):
    return recursive_function2(mystring, 0, len(mystring) - 1)  # 2 operations (subtraction and function call)


Let len(mystring) = number # the length of given string
Therefore, T(len(mystring)) = T(number) and T(number) represents the number of ops needed to our function
So, I can actually rewrite our count summary as follows:
    T(number)=6+2+2+T(number-1)
             =10+T(number-1)
            
There are a total of (number-1) 10's. We know this because we need to reach T(number-1) to get the 3.
T(number)=10(number−1)+3= 10 number − 7
Thus, T(number) is O(number)

```

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

def function3(value, number):
	if (number == 0):  #1
		return 1       #1
	elif (number == 1): #1
		return value     #1
	else:
		half = number /2   #2
		result = function3(value, half)  #1+T(number-1)
		if (number % 2 == 0):     #2
			return result * result   #1
		else:
			return value * result * result #2

    T(number)=4+2+2+2+1+1+T(number-1)
             =12+T(number-1)
             =T(1)=2 and T(0)=2
             
There are a total of (number-1) 12's.
T(number)=12(number−1)+2=12n−10
Thus, T(number) is O(number)

```

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?

--> Because I was doing it for the first time, writing recursive functions was quite difficult for me. It was difficult, but it was also incredibly interesting. I also did some research on the internet to find relevant knowledge on this issue, and I used my notes to solve these tasks.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 

--> I used the same method to identify a component that symbolises the numerous calculations needed for a specific data size. The most useful distinction I can make is that a significant portion of the math required for our function during the recursion will be T(n-1). T(n), in the absence of recursion, would be the substantial number of operations necessary to carry out a linear or binary operation.
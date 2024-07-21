# Lab 2

### function 1:

Analyze the following function with respect to number

```python

def function1(number):
	total=0;

	for i in range(0,number):
		x = (i+1)
		total+=(x*x)

	return total

Step 2: Count your operations

def function1(number):
	total=0;                 //1

	for i in range(0,number):   //n+1
		x = (i+1)               //n+2
		total+=(x*x)            //3(n)

	return total               //1

Step 3: You can simplify the expression 
Expand the expression: (3n) * (n + 1) * ( n + 2)

Step 4: So, the simplified expression is: 5n + 4
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6

Step 2: Count your operations

def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6   //6(1) //6 operators are used to calculate the value of the given number and all operators are called only one time. 

Step 3: You can simplify the expression ((n)*(n+1)*(2*n + 1))/6 as follows:
Expand the expression: (n) * (n + 1) * (2 * n + 1)

Step 4: So, the simplified expression is: (2n^3 + 3n^2 + n) / 6

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

Step 2: Count your operations

def function3(list):
	for i in range (0,len(list)-1):      //3+n-1
		for j in range(0,len(list)-1-i): //(n-1)(4+n-1) 
			if(list[j]>list[j+1]):       //2*(1+n)
				tmp=list[j]              //1*(1+n)
                list[j]=list[j+1]        //2*(1+n)
				list[j+1]=tmp            //2*(1+n)

Step 3: Expand the expression: 3 + n - 1 + (n - 1) * (4 + n - 1) * (2 + 1 + 2 + 2) 

Step 4: So, the simplified expression is: 3n^2 - 4n + 6

```
### function 4:

Analyze the following function with respect to number

```python

def function4(number):
	total=1
	for i in range(1 to number):
		total=total*(i+1)
	return total

Step 2: Count your operations

def function4(number):
	total=1                      //1
	for i in range(1, number):   //1+(n-1)
		total*=(i+1)        //3(n-1)
	return total                //1

Step 3: Now, let's sum up all the operations: 1 + (1 + (n - 1)) + 3 * (n - 1) + 1

Step 4: So, the simplified expression is: 4 * n - 2

```


## In class portion

### Group members
List the members of your group member below:

	* Yuvraj Singh
	* Dai Anh Bui
	* Yeonsu Park
	* Avreet Kaur
	* Ravneet Kaur
	* Truong An Huynh

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

|--------------|--------------------------|--------------------------|
| Team member  | Timing for fibonacci(39) | Timing for sum_to_number | 
|--------------|--------------------------|--------------------------|
| Yuvraj Singh    | 2.787695768998674     | 0.6345022569967114       |
| Anh Bui         | 3.1233632679977745    | 0.6248804529896006       |
| Yeonsu Park     | 3.8891809229999694    | 0.8880597179999654       |
| Avreet Kaur     | 2.95                  | 0.77                     |
| Ravneet Kaur    | 1.08                  | 0.25                     |
| Truong An Huynh | 2.87                  | 0.61                     |
|--------------|--------------------------|--------------------------|

### Summary 

|--------------|-----------|--------------------|-------------------|
|    function  |  fastest  |       slowest      |     difference    |
|--------------|-----------|--------------------|-------------------|
|sum_to_number | 1.08      | 3.8891809229999694 | 2.809180922999969 |
|fibonacci     | 0.25      | 0.8880597179999654 | 0.638059717999965 |
|--------------|-----------|--------------------|-------------------|

### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

Answers Discussed in the reflection -

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?

A1- After looking at both scripts, I came to the conclusion that the way a piece of code is approached as well as its syntax have a significant impact on how long it takes to run.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  

A2-  Yes, there was a difference in the amount of space used since, as was indicated in the discussion section, the code for the Fibonacci function with the recursion used more space than the other code. Therefore, different algorithms undoubtedly utilise varying amounts of time and space.

3. What sort of conclusions can you draw based on your observations?

A3- I conclude that: Difference in syntax as well as in approach to write a piece of code uses different amount of time as well as in memory. Moreover, the performance of the device also matters as one of my friend was also trying to solve the code in the similar way as i did but his code was running faster than me for fibonacci and was slowest for sum to number.
 




# Lab 5 Reflection and Observations

* Yuvraj Singh
* Avreet Kaur
* Ravneeet Kaur

## Heap Insertion

### Picture of heap created with 10 values
![1](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/99aab1f6-8485-4d87-846f-4f79b4a6437d)

### Pictures of adding 11th value to heap

![2](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/d211562c-cd09-465e-9ac5-c5dea323eade)

## Heap Removal

### Picture after 1 value was removed from heap

![3](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/04436b7a-302f-4209-87f3-a1e8cc30a314)



### Picture after 2 value was removed from heap

![33](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/190f7801-7cc7-491c-bebf-cd2fb03002df)


### Picture after 3 value was removed from heap

![4](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/39ef9ed3-0cdf-4993-bdba-c9e8370751c3)

### Values removed (in order removed):

3, 11, 17

## Array representation of heap

![5](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/6344d1b3-4d99-45c0-a296-416132793d82)

### Picture of heap

![6](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/fb60b62c-1a0f-4eb0-827c-904f545934e5)
### Array representation of heap

![7](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/c14c377d-06af-4470-a2b3-9e4833cda50a)

## Creating a heap from array


### Photograph of your array and heap

![8](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/a3eb6dc9-6187-47fc-a76b-b2b354052490)

![9](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/32cb5527-bec2-43fe-8828-e13850df5226)

* What number is the first non-leaf node starting from bottom?
Answer- 74
* What index is that node at?
Answer- Index 2

### Photograph of heap created by Heapify


## HeapSort

Initial questions (do first):
## How many values are in your array?
Answer - 11

## what is index of last value in array?
Answer - 10

## After doing 1 removal operation

![20](https://github.com/seneca-dsa456-f23/labs-yuvraj-singh5/assets/144463738/d9d69380-34f6-40eb-af66-02ba3cc59a0d)

## Question 1: what was the first value removed? How does this number compare with others in heap (biggest? smallest?)
* Answer- 91 was the first value removed. 91 was the biggest among all.
  
## Question 2: Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* There are 10 values in the heap. The index of the bottom right-most value in the heap is 9.

## After doing 2 removal operations:

## Perform another remove from the heap and adjust the array to match
## What was the second value removed and how does it compare with others still in heap?
Answer - 74

## Look at your heap portion of the array after you did this removal.. how many values are in what is the index of the bottom right most value in heap?
Answer- here are 9 values in the index and the index the bottom right most value in heap is 8. 

## Are there any open spots in the array that is not part of the heap and not holding anything useful?
Answer- No the parent nodes have either two child or no childs hence, it is evenly filled.


## After doing 3 removal operations:

* Perform another remove from the heap and adjust the array to match
## What was the second value removed and how does it compare with others still in heap?
Answer- 64. I was the top most value in the heap.

## Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
Answer- There are 8 values in the index and the index the bottom right most value in heap is 7.

## Are there any open spots in the array that is not part of the heap and not holding anything useful?
The parent node 21 has only one child i.e, 3 and hence it is incomplete.

## Reflection

(This last part is to be completed individually.)

## Write a short paragraph about what you learned from this lab. Discuss what you learned about heaps and heap sort.
  
Answer- Heap Sort is a sort that is based on creating and eradicating binary heaps. A Priority Queue is implemented using the binary heap. In a queue, the first value added is typically the first value removed. With a priority queue, the value that exits the queue next is determined by its priority.

Basic operations on the binary Heap include:

* insert - add an item to the binary heap
* delete - removes the item with the highest priority in the binary heap.

## What was the most surprising thing you learned about heaps?

Answer- The most interesting thing I discovered in this heap lab was that a priority queue is an abstract data type. As with queues and stacks, the underlying storage and access are independent of the operation of the priority queue. A priority queue and a queue are similar in that both are used to order data. However, you sort things according to their priority value rather than the date they were added. The item with the highest priority is at the front of the priority queue (and will be deleted if an item needs to be dequeued). This is the kind of line you could see in a hospital's emergency room. The severity of the disease, as contrasted to who arrived first, is what really matters.

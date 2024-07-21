#    Main Author(s): Yuvraj Singh
#    Main Reviewer(s): Ravneet Kaur & Avreet Kaur

class Stack:

	def __init__(self , cap = 10):
		self.data = [None] * cap
		self.top = -1
		self.capacity_value = cap		

	
	def capacity(self):
		return self.capacity_value

	def push(self, data):
		if self.top == self.capacity_value - 1:  # Stack is full, need to resize    
			new_data = [None] * (2 * self.capacity_value)
			for i in range(self.capacity_value):
				new_data[i] = self.data[i]
			
			self.data = new_data
			self.capacity_value *= 2

		self.top += 1
		self.data[self.top] = data

	def pop(self):
		if self.top == -1:
			raise IndexError('pop() used on empty stack')
		value = self.data[self.top]

		self.top -= 1

		return value

	def get_top(self):
		if self.top == -1:
			return None
		return self.data[self.top]

	def is_empty(self):
		return self.top == -1

	def __len__(self):
		return self.top + 1


class Queue:


	def __init__(self, cap = 10):
		self.data = [None] * cap
		self.front = 0  # Represents the index of the front element
		self.size = 0	# Number of elements currently in the queue
		self.capacity_value = cap

	def capacity(self):
		return self.capacity_value

	def enqueue(self, data):
		if self.size == self.capacity_value:  # Queue is full, need to resize
			new_data = [None] * (2 * self.capacity_value)
            
			for i in range(self.capacity_value):
            	
				new_data[i] = self.data[(self.front + i) % self.capacity_value]
            
			self.data = new_data
			self.front = 0      
			self.capacity_value *= 2

		self.data[(self.front + self.size) % self.capacity_value] = data
		self.size += 1

	def dequeue(self):
		if self.size == 0:  # Queue is empty
            
			raise IndexError('dequeue() used on empty queue')
		
		
		value = self.data[self.front]
		self.front = (self.front + 1) % self.capacity_value
		self.size -= 1
		return value

	def get_front(self):
		if self.size == 0:
			return None
		return self.data[self.front]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size



class Deque:

	def __init__(self, cap = 10):
		self.data = [None] * cap
		self.front = 0  # Represents the index of the front element
		self.size = 0   # Number of elements currently in the deque
		self.capacity_value = cap


	def capacity(self):
		return self.capacity_value
	
	
	def resize(self, new_cap):
		new_data = [None] * new_cap
		for i in range(self.size):
			new_data[i] = self.data[(self.front + i) % self.capacity_value]
		self.data = new_data
		self.front = 0
		self.capacity_value = new_cap

	def push_front(self, data):
		if self.size < self.capacity_value: # Deque is not full, no need to resize
			self.front = (self.front - 1) % self.capacity_value
			self.data[self.front] = data
			self.size += 1
		else: # Deque is full, need to resize
			self.resize(2 * self.capacity_value)
			self.push_front(data)


	def push_back(self, data):
		if self.size == self.capacity_value:  # Deque is full, need to resize
			self.resize(2 * self.capacity_value)
		self.data[(self.front + self.size) % self.capacity_value] = data
		self.size += 1

	def pop_front(self):
		if self.size == 0:  # Deque is empty
			raise IndexError('pop_front() used on empty deque')
		value = self.data[self.front]
		self.front = (self.front + 1) % self.capacity_value
		self.size -= 1
		return value

	def pop_back(self):
		if self.size == 0:  # Deque is empty
			raise IndexError('pop_back() used on empty deque')
		back_index = (self.front + self.size - 1) % self.capacity_value
		value = self.data[back_index]
		self.size -= 1
		return value

	def get_front(self):
		if self.size == 0:
			return None
		return self.data[self.front]


	def get_back(self):
		if self.size == 0:
			return None
		return self.data[(self.front + self.size - 1) % self.capacity_value]


	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size

	def __getitem__(self, k):
		if k < 0 or k >= self.size:
			raise IndexError('Index out of range')
		return self.data[(self.front + k) % self.capacity_value]

#    Main Author(s): Yuvraj Singh
#    Main Reviewer(s): 

class Stack:

	class Node:
		def __init__(self, data):
			self.data = data;
			self.next = None;
	

	def __init__(self, cap = 10):
		self.cap = cap
		self.top = None
		self.size = 0


	def capacity(self):
		return self.cap

	def push(self, data):
		if self.size == self.cap:
			self.cap *= 2
		if self.size < self.cap:
			new_node = self.Node(data)
			new_node.next = self.top 
			self.top = new_node 
			self.size += 1 


	def pop(self):
		if not self.is_empty():
			data = self.top.data
			self.top = self.top.next
			self.size -= 1
			return data
		else:
			raise IndexError("pop() used on empty stack")

	def get_top(self):
		if not self.is_empty():
			return self.top.data

	def is_empty(self):
		return self.size == 0;

	def __len__(self):
		return self.size


class Queue:
	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def __init__(self, cap = 10):
		self.cap = cap
		self.size = 0
		self.first = None
		self.last = None

	def capacity(self):
		return self.cap

	def enqueue(self, data):
		new_node = self.Node(data)
		if self.size == self.cap:
			self.cap *= 2
		if self.first is None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node	
		self.size += 1

	def dequeue(self):
		if not self.is_empty():
			value = self.first.value
			self.first = self.first.next
			self.size -= 1
			return value
		else:
			raise IndexError("dequeue() used on empty queue")



	def get_front(self):
		if not self.is_empty():
			return self.first.value
		else:
			return None

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size



class Deque:

	class Node:
		def __init__(self, value):
			if isinstance(value, int):
				self.value = value
			else:
				self.value = None
			self.next = None
			self.prev = None


	def __init__(self, cap = 10):
		self.front = 0
		self.back = -1
		self.cap = cap
		self.size = 0
		self.data = [None] * self.cap

	def capacity(self):
		return self.cap

	def resize(self):
		new_cap = self.cap * 2
		new_data = [None] * new_cap
		for i in range(self.size):
			new_data[i] = self.data[(self.front + i) % self.cap]
		self.data = new_data
		self.cap = new_cap
		self.front = 0
		self.back = self.size - 1

	def push_front(self, data):
		if self.size == self.cap:
			self.resize()
		self.front = (self.front - 1) % self.cap
		self.data[self.front] = data
		self.size += 1
	def push_back(self, data):
		if self.size == self.cap:
			self.resize()
		self.back = (self.back + 1) % self.cap
		self.data[self.back] = data
		self.size += 1

	def pop_front(self):
		if self.is_empty():
			raise IndexError('pop_front() used on empty deque')
		data = self.data[self.front]
		self.front = (self.front + 1) % self.cap
		self.size -= 1
		return data

	def pop_back(self):
		if self.is_empty():
			raise IndexError('pop_back() used on empty deque')
		data = self.data[self.back]
		self.back = (self.back - 1) % self.cap
		self.size -= 1
		return data

	def get_front(self):
		if self.is_empty():
			return None
		return self.data[self.front]

	def get_back(self):
		if self.is_empty():
			return None
		return self.data[self.back]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size

	def __getitem__(self, k):
		if k < 0 or k >= self.size:
			raise IndexError('Index out of range')
		return self.data[(self.front + k) % self.cap]

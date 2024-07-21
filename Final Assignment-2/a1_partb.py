#    Main Author(s): Ravneet Kaur
#    Main Reviewer(s): Yuvraj Singh and Avreet Kaur

class DoublyLinked:
	#Node class 
	class Node:
		#initiation the node with data,next,prev.
		def _init_(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev 
		# to get data
		def get_data(self):
			return self.data
		# to get next node
		def get_next(self):
			return self.next
		#to get the prev node
		def get_previous(self):
			return self.prev
	#initiation for the doubly linked list with front and back.
	def _init_(self, data = None):
			self.front = None
			self.back = None
	#to get the front node
	def get_front(self):
		if self.front is not None:
			return self.front
		else:
			return None
	#to get the back node
	def get_back(self):
		if self.back is not None:
			return self.back
		else:
			return None
	#to add data to the front of the list 
	def push_front(self, data):
			new = self.Node(data, next = self.front)
			if self.front == None:
				self.front = new
				self.back = new
			else:
				self.front.prev = new
				self.front = new
	#to add data to the back of the list 
	def push_back(self,data):
			new = self.Node(data,None,prev = self.back)
			if self.back == None:
				self.front = self.back = new
			else:
				self.back.next = new
				self.back = new
	#to remove the first data node from the list.
	def pop_front(self):
			if self.front == None:
				raise IndexError('pop_front() used on empty list')
			data = self.front.data
			self.front = self.front.next
			if self.front:
				self.front.prev = None
			else:
				self.back = None
			return data
	#remove the last data node from the list.
	def pop_back(self):
			if self.back == None:
				raise IndexError('pop_back() used on empty list')
			data = self.back.data
			self.back = self.back.prev
			if self.back:
				self.back.next = None
			else:
				self.front = None
			return data
	#to check if the list is empty or not
	def is_empty(self):
			return self.front == None
	#to add data into the list positioned after node
	def insert_after(self, data, node):
			if node == None:
				self.push_front(data)
			else:
				new = self.Node(data, node.get_next(),prev = node)
				if node.get_next() is not None:
					node.get_next().prev = new
				else:
					self.back = new
				node.next = new
	# function returns a reference to the node where data is found, None if data is not found
	def search(self, data):
			curr = self.front
			while curr is not None:
				if curr.data == data:
					return curr
				curr = curr.get_next()
			return None
	#to receive the number of pieces of data stored in the list
	def _len_(self):
			count = 0
			curr = self.front
			while curr is not None:
				count +=1
				curr = curr.get_next()
			return count

	#to return True if the values in the linked list form a palindrome, False otherwise. 
	def is_palindrome(self):
		def is_palindrome_recursive(front,back):
			if front == None:
				return True
			if back == None: 
				return True
			if front.data == back.data:
				return is_palindrome_recursive(front.get_next(),back.get_previous())
			return False
		return is_palindrome_recursive(self.front,self.back)
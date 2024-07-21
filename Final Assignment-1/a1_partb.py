#    Main Author(s): Ravneet Kaur
#    Main Reviewer(s): 

class DoublyLinked:
	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data 
			self.next = next
			self.prev = prev

		def get_data(self):	#this function returns data stored in node
			return self.data

		def get_next(self):	#this function returns reference to next node in DoublyLinked
			return self.next

		def get_previous(self):	#this function returns reference to previous node in DoublyLinked
			if self.prev is not None:
				return self.prev
			else:
				return None

	def __init__(self, data = None):
			self.first_node = self.Node(None)
			self.last_node = self.Node(None)
			self.first_node.next = self.last_node
			self.last_node.prev = self.first_node
			self.length = 0

	def get_front(self):	#This function returns a reference to the first data node in the list. If list is empty, function returns None.
			if self.first_node.next != self.last_node:
				return self.first_node.next
			else:
				return None


	def get_back(self):	#This function returns a reference to the last data node in the list. If list is empty, function returns None.
			if self.last_node.prev != self.first_node:
				return self.last_node.prev
			else:
				return None

	def push_front(self, data):	#This function adds data to the front of the list (before the first data node). This function returns nothing.
			new_node = self.Node(data, self.first_node.next, self.first_node)
			self.first_node.next.prev = new_node
			self.first_node.next = new_node
			self.length += 1

	def push_back(self,data):	#This function adds data to the back of the list (after the last data node). This function returns nothing.
			new_node = self.Node(data, self.last_node, self.last_node.prev)
			self.last_node.prev.next = new_node
			self.last_node.prev = new_node
			self.length += 1

	def pop_front(self):	#This function removes the first data node from the list. Function returns value stored in that node.
			if self.first_node.next == self.last_node:
				raise IndexError('pop_front() used on empty list')
			data = self.first_node.next.get_data()
			self.first_node.next = self.first_node.next.next
			self.first_node.next.prev = self.first_node
			self.length -= 1
			return data

	def pop_back(self):	#This function removes the last data node from the list. Function returns value stored in that node.
			if self.last_node.prev == self.first_node:
				raise IndexError('pop_back() used on empty list')
			data = self.last_node.prev.get_data()
			self.last_node.prev = self.last_node.prev.prev
			self.last_node.prev.next = self.last_node
			self.length -= 1
			return data

	def is_empty(self):	#This function returns True if the list is empty, False otherwise.
			return self.first_node.next == self.last_node

	def insert_after(self, data, node):	#This function is passed a piece of data and a reference to a node within the list. Function will add data into the list positioned after node. If node == None, function inserts data at the front of the list. function returns nothing.
			if node is None:
				self.push_front(data)
			else:
				new_node = self.Node(data, node.next, node)
				node.next.prev = new_node
				node.next = new_node
				self.length += 1

	def search(self, data):	#This function returns a reference to the node where data is found, None if data is not found
			current = self.first_node.next
			while current!= self.last_node:
				if current.get_data() == data:
					return current
				current = current.get_next()
			return None

	def __len__(self):
			return self.length

	def is_palindrome(self):	#This function returns True if the values in the linked list form a palindrome, False otherwise. 
			def is_palindrome_recursive(first, last):
				if first == last:
					return True
				if first.get_data() != last.get_data():
					return False
				if first.get_next() == last.get_data():
					return True
				return is_palindrome_recursive(first.get_next(), last.get_previous())

			if self.first_node is None:
				return True
			return is_palindrome_recursive(self.first_node, self.last_node)







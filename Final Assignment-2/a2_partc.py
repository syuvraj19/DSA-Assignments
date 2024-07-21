#    Main Author(s): Ravneet Kaur
#    Main Reviewer(s): Dilli Sharma


class MinHeap:
    def __init__(self, arr=None):    # initializes MinHeap instance
        if arr is None:
            arr = []
        self.heap = arr
        self.build_heap()

    def insert(self, element):    # adds an element to the heap
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):    # returns the smallest value in the heap with changing the data structure
        if not self.is_empty():
            return self.heap[0]
        else:
            return None

    def extract_min(self):    # removes the smallest value from the heap and returns the given value
        if not self.is_empty():
            min_value = self.heap[0]
            min_element = self.heap.pop()
            if len(self.heap) > 0:
                self.heap[0] = min_element
                self._heapify_down(0)
            return min_value
        else:
            return None

    def is_empty(self):    # returns true if the heap is empty, otherwise false
        return len(self.heap) == 0

    def __len__(self):    # returns the length of heap
        return len(self.heap)

    def build_heap(self):    # builds the heap from the given list of values
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):    # moves the element up the heap as needed
        while index > 0:
            parent_index = (index - 1) // 2    # swaps the element with its parent if the element is smaller
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):    # moves the element down the heap as needed
        n = len(self.heap)
        while index < n // 2:    # loops until the current node is a leaf node
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_child_index = left_child_index

            if right_child_index < n and self.heap[right_child_index] < self.heap[left_child_index]:    # finds the index of the existing smaller child
                min_child_index = right_child_index

            if self.heap[index] > self.heap[min_child_index]:    # swaps the smaller child if the current node is larger
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

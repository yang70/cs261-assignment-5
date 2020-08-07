# Course: CS261 - Data Structures
# Assignment: 5, Part 2 - Min Heap
# Student: Matthew Yang
# Description: Implementation of the Min Heap as described in the instructions


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object
        """
        # Find index at the end of the current array
        current_index = self.heap.length()

        # Insert new node at the last index
        self.heap.append(node)

        # Find the parent index
        parent_index = (current_index - 1) // 2

        # Start comparing with parent and swapping places until the parent
        # is less than or equal to the inserted node, or reaching the beginning
        # of the array
        while (parent_index >= 0) and (self.heap.get_at_index(parent_index) > node):
            self.heap.swap(parent_index, current_index)

            current_index = parent_index
            parent_index  = (current_index - 1) // 2

        return

    def get_min(self) -> object:
        """
        Returns the object with minimum key without removing. Raises
        a MinHeapException if empty
        """
        # Raise if empty
        if self.is_empty():
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes and returns the object with minimum key. Raises a
        MinHeapException if empty
        """
        # Raise if empty
        if self.is_empty():
            raise MinHeapException

        # Save the minimun key node
        min_node = self.heap.get_at_index(0)

        # Remove the last element of the array
        last_node = self.heap.pop()

        # If array is not empty we need to set last node at root and
        # percolate it down into place
        if not self.is_empty():
            self.heap.set_at_index(0, last_node)

            # Set tracking variables
            current_index     = 0
            left_child_index  = 1
            right_child_index = 2
            last_index        = self.heap.length() - 1
            percolating       = True

            # Loop while last node still requires percolation
            while percolating:
                # If both child indexes are out of the array bounds, stop percolating
                if left_child_index > last_index and right_child_index > last_index:
                    percolating = False
                # If left child index is out of bounds check right child index
                elif left_child_index > last_index:
                    # If last node is still greater then child, swap places
                    # and set current index as the destination. Otherwise
                    # stop percolating
                    if last_node > self.heap.get_at_index(right_child_index):
                        self.heap.swap(current_index, right_child_index)
                        current_index = right_child_index
                    else:
                        percolating = False
                # If right child index is out of bounds check left child index
                elif right_child_index > last_index:
                    # If last node is still greater then child, swap places
                    # and set current index as the destination. Otherwise
                    # stop percolating
                    if last_node > self.heap.get_at_index(left_child_index):
                        self.heap.swap(current_index, left_child_index)
                        current_index = left_child_index
                    else:
                        percolating = False
                # If both child indexes are still in bounds
                else:
                    # Get the child nodes
                    left_child_node  = self.heap.get_at_index(left_child_index)
                    right_child_node = self.heap.get_at_index(right_child_index)

                    # Compare the smaller of the two child nodes with last node
                    # and if last node is greater, swap with the child and set
                    # current index as the destination index. Otherwise stop
                    # percolating
                    if left_child_node < right_child_node:
                        if last_node > left_child_node:
                            self.heap.swap(current_index, left_child_index)
                            current_index = left_child_index
                        else:
                            percolating = False
                    else:
                        if last_node > right_child_node:
                            self.heap.swap(current_index, right_child_index)
                            current_index = right_child_index
                        else:
                            percolating = False

                # Set the new child indices for the next loop iteration
                left_child_index  = (current_index * 2) + 1
                right_child_index = (current_index * 2) + 2

        # Return the min node from way up top
        return min_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives and sets a DynamicArray as the underlying heap and
        sorts it into a proper heap
        """
        # Set a new DynamicArray as heap data attribute and
        # get the length of the given da
        self.heap = DynamicArray()
        length    = da.length()

        # Return if empty as no work to do
        if length == 0:
            return

        # Copy the items from the given array to heap
        index = 0

        while index < length:
            self.heap.append(da.get_at_index(index))
            index += 1

        # Find first non leaf node index, or parent of the last
        # item in the array
        sorting_index = (length - 2) // 2

        while sorting_index >= 0:
            current_node = self.heap.get_at_index(sorting_index)

            # Set tracking variables
            current_index     = sorting_index
            left_child_index  = (current_index * 2) + 1
            right_child_index = (current_index * 2) + 2
            last_index        = length - 1
            percolating       = True

            # Loop while current node still requires percolation
            while percolating:
                # If both child indexes are out of the array bounds, stop percolating
                if left_child_index > last_index and right_child_index > last_index:
                    percolating = False
                # If left child index is out of bounds check right child index
                elif left_child_index > last_index:
                    # If current node is still greater then child, swap places
                    # and set current index as the destination. Otherwise
                    # stop percolating
                    if current_node > self.heap.get_at_index(right_child_index):
                        self.heap.swap(current_index, right_child_index)
                        current_index = right_child_index
                    else:
                        percolating = False
                # If right child index is out of bounds check left child index
                elif right_child_index > last_index:
                    # If current node is still greater then child, swap places
                    # and set current index as the destination. Otherwise
                    # stop percolating
                    if current_node > self.heap.get_at_index(left_child_index):
                        self.heap.swap(current_index, left_child_index)
                        current_index = left_child_index
                    else:
                        percolating = False
                # If both child indexes are still in bounds
                else:
                    # Get the child nodes
                    left_child_node  = self.heap.get_at_index(left_child_index)
                    right_child_node = self.heap.get_at_index(right_child_index)

                    # Compare the smaller of the two child nodes with current node
                    # and if current node is greater, swap with the child and set
                    # current index as the destination index. Otherwise stop
                    # percolating
                    if left_child_node < right_child_node:
                        if current_node > left_child_node:
                            self.heap.swap(current_index, left_child_index)
                            current_index = left_child_index
                        else:
                            percolating = False
                    else:
                        if current_node > right_child_node:
                            self.heap.swap(current_index, right_child_index)
                            current_index = right_child_index
                        else:
                            percolating = False

                # Set the new child indices for the next loop iteration
                left_child_index  = (current_index * 2) + 1
                right_child_index = (current_index * 2) + 2

            sorting_index -= 1

        return


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)


    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())


    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())


    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)

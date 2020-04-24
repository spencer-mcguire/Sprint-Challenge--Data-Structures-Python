from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # create a queue
        # new item gets added to the tail while there is empty space. 
        # set the current (start of the ring) to the head and keep it there
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if the ring is full
        # remove the head and add to the tail
        # need to check if the start of the ring is at the head
        # if it is, set the start of the ring to the tail
        if self.storage.length == self.current:
            head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # grab the start of the ring 
        # add that node to the list so that is the first thing
        #check where the start is in the ring. if there is a next set that as the next node, if not set the next node is the head
        # loop until there are no more nodes left to display 
        start = self.current
        list_buffer_contents.append(start.value)
        if start.next is not None:
            next_node = start.next
        else:
            next_node = self.storage.head

        while next_node != start:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

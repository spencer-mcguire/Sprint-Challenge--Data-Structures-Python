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

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

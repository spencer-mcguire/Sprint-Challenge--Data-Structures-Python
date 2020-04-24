class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # literally need to just change the list to the other direction.
        # head next is now none and the tails next is not none 
        # can use 3 pointer that we figured out in class. 
        # can use included methods on the node itself 
        # if the nodes next == None
        # set the node to self.head and return to break recursion
        # else: recursively pass in the next node method to keep trying to find the next node
        # set a var to the method to get the next node
        # set next node on that var while passing in the current node
        # set the nodes next to None if it makes it all the way there
        if node is None:
            return
        if node.get_next() == None:
            self.head = node
            return
        self.reverse_list(node.next_node, None)
        temp_node = node.get_next()
        temp_node.set_next(node)
        node.set_next(None)

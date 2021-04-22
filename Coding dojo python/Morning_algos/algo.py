class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class SLL(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        # returns a boolean on whether or not there are nodes in the list
        if self.head == None:
            return True
        else:
            return False

    def front(self):
        # returns the value of the first node or None
        if self.is_empty():
            return None
        else:
            return self.head.val

    def add_front(self, value):
        # add a new node to the beginning of the list
        new_node = Node(value)
        new_node.next
        runner = self.head
        while runner != None:
            return runner


    def remove_front(self):
        # removes and returns the first node of the list
        pass

    def print_values(self):
        # print the values of the list 
        pass

my_list = SLL()
my_list.add_front(5)
my_list.add_front(4)
my_list.add_front(3)
my_list.print_values()
# should print 3 -> 4 -> 5 ->
removed_val = my_list.remove_front()
print(removed_val)
# should print 3
my_list.print_values()
# should print 4 -> 5 ->

def append(self, after_val, new_val):
    new_node = Node(new_val)
    runner = self.head
    if runner.val == after_val:
        new_node.next = runner.next
        runner.next == new_node
        return
    runner = runner.next
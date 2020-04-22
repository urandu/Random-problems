"""
How do you find the middle element of a singly linked list in one pass?
For example: Given a linked list, the middle element in this linked list is 8.
15 -> 9 -> 8 -> 5 -> 6 -> NULL

1.number of elements will always be odd



"""

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Linkedlist:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.start_node is None:
            self.start_node = new_node
            return
        node = self.start_node
        while node.next is not None:
            node = node.next
        node.next = new_node

def get_mid_number(number):
    import math
    return math.ceil(number/2)

def create_linked_list(list):
    linked_list = Linkedlist()
    linked_list.start_node = Node(list[0])
    [linked_list.insert_at_end(list[x]) for x in range(1,len(list)) ]

    return linked_list

def navigate_list(node, count = 0):
    count += 1
    current_node_position = count

    if node.next is not None:
        total, found = navigate_list(node.next, count)

        if found:
            return total, found
        else:
            if(current_node_position == get_mid_number(total)):
                return node.value, True
            return total, found

    return count, False


def get_middle_node(linked_list):
    mid_node, _ = navigate_list(linked_list.start_node)
    return mid_node

list = [15,9,8,5,6]

linked_list = create_linked_list(list)

mid_node = get_middle_node(linked_list)

print(mid_node)




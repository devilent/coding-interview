class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def print_node(self):
        temp = self
        while temp:
            print(temp.val)
            temp = temp.next

def solution(node):
    fast = node
    slow = node
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
        print(stack)

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop
        if top != slow.val:
            return False
        slow = slow.next
    return True

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node
    
    def __str__(self):
        return str(self.data)
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def solution(node, num, offset) -> (int, Node):
    if not node.next:
        return (num - offset + 1, None)
    answer = solution(node.next, num + 1, offset)
    if num == answer[0]:
        return (num, node)
    else:
        return answer

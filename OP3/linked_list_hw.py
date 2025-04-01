
#SIMPLE

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)
print(stringify(Node(1, Node(2, Node(3)))))




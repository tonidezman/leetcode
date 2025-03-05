class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node("dummy head")
        self.tail = Node("dummy tail")
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if not curr or index != 0 or curr == self.tail:
            return -1
        return curr.val


    def addAtHead(self, val: int) -> None:
        new_head, prev_node, next_node = Node(val), self.head, self.head.next
        prev_node.next = new_head
        new_head.next = next_node
        next_node.prev = new_head
        new_head.prev = prev_node


    def addAtTail(self, val: int) -> None:
        new_tail, prev_node, next_node = Node(val), self.tail.prev, self.tail
        prev_node.next = new_tail
        new_tail.next = next_node
        next_node.prev = new_tail
        new_tail.prev = prev_node


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if not curr or index != 0 and curr == self.tail:
            return
        
        new_node, prev_node = Node(val), curr.prev
        prev_node.next = new_node
        new_node.next = curr
        curr.prev = new_node
        new_node.prev = prev_node
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if not curr or index != 0 or curr == self.tail:
            return
        
        prev_node, next_node = curr.prev, curr.next
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
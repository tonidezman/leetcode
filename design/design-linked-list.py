class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            prev_head = self.head
            self.head = Node(val)
            prev_head.prev = self.head
            self.head.next = prev_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            prev_tail = self.tail
            self.tail = Node(val)
            self.tail.prev = prev_tail
            prev_tail.next = self.tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= self.length:
            return
        curr = self.head
        for i in range(index):
            curr = curr.next
        prev = curr.prev
        new_node = Node(val)
        prev.next = new_node
        new_node.prev = prev
        new_node.next = curr
        curr.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        if curr == self.head:
            self.head = None
            self.tail = None
        elif curr == self.tail:
            prev = curr.prev
            prev.next = None
            self.tail = prev
        prev = curr.prev
        prev.next = curr.next
        curr.next.prev = prev

        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
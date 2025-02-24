class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        # dummy = Node("dummy")
        self.head = None
        self.tail = None
        
    def get(self, index: int) -> int:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            if curr is None:
                return -1
            index -= 1
        return curr.val
            
    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
            return

        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr is None:
            self.addAtTail(val)
            return

        new_node = Node(val)
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node
        return

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr is None:
            return
        prev = curr.prev
        if prev is None:
            self.head = curr.next
            self.head.prev = None
            return
        prev.next = curr.next
        if curr.next:
            curr.next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
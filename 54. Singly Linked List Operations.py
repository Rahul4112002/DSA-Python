class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()
            
    def insert_at(self, val, position):
        if position == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current
    
    def delete(self,val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                while temp.next is not None:
                    if temp.val == val:
                        found = True
                        break
                
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traversal()
        
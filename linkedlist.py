class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def insert(self,head,data):
        if not head:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head
    
    def display(self,head):
        while head:
            print "->"+str(head.data),
            head = head.next
            
    def delete(self,head,data):
        if head.data == data:
            temp = head
            head = temp.next
            del temp
            return head
        prev = head
        current = head.next
        while current:
            if current.data == data:
                prev.next=current.next
                del current
                return head
            else:
                prev = current
                current = current.next
        return head
    
    def size(self,head):
        count = 0
        while head:
            count+=1
            head=head.next
        return count
        
'''
SAMPLE INPUT

set1 = linkedlist()
head = None
head = set1.insert(head,2)
head = set1.insert(head,3)
head = set1.insert(head,4)
head = set1.insert(head,5)
set1.display(head)
set1.size(head)

'''

# Head Node[1,next] => [2,next] => [3,next] => tail Node [4, None]

class Node:
    def __init__(self , value = 0 , nextNode = None):
        self.val = value
        self.next = nextNode    



head = Node(100) 
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500) 

result = []

current = head
length=0

while current != None:
    print(current.val , end=" ") 
    length+=1
    current = current.next
print(length)
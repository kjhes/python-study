# 단일 연결 리스트 : 노드가 data 와 link 로 구성
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
node1 = Node(10)
print("저장 값:",node1.data)
print("다음 노드:",node1.next)

class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None

head = Node2(10)
head.next=Node2(20)
head.next.next=Node2(30)

cur = head

while cur is not None:
    print(cur.data)
    cur = cur.next


class s_list:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node=Node3(data)

        if self.head is None:
            self.head = new_node
            return
        curr=self.head

        while curr.next is not None:
            curr = curr.next
        curr.next=new_node
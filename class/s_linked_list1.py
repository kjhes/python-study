# s_linked_list1.py
# 단일 연결 리스트 :노드가 data와 link 로 구성

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1 = Node(10)
print("저장 값:",node1.data)
print("다음 노드:", node1.next)

# 노드 세개 연결하여 출력
class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None

head = Node2(10)
head.next = Node2(20)
head.next.next= Node2(30)

cur = head # 첫위치를 현재위치로 정함

while cur is not None: # None이 아닐때까지 반복
    print(cur.data) # 노드의 값 출력
    cur=cur.next # 다음노드로 현재위치를 변경

# --------------------------------
class Node3:
    def __init__(self,data):
        self.data=data
        self.next=None

class S_list:
    def __init__(self):
        self.head=None #head는 첫위치를 기억하는 변수

    def append(self, data):
        new_node =Node3(data) # 새 노드 등장 다른 클래스의 객체를 생성한 것임 다른 class 안에서

        if self.head is None: # 노드가 전혀 없으면
            self.head= new_node # 새로운 노드부터 시작
            return
        
        curr=self.head #첫 위치를 현재위치로도 정함

        while curr.next is not None: #끝까지 이동(None 일때까지)
            curr = curr.next #뒤로 하나씩 이동

        curr.next=new_node #마지막 노드 뒤에 새 노드 연결
    
    def print_list(self):
        curr=self.head 
        if curr is None:
           print("연결리스트가 비어있습니다")
           return
        while curr is not None:
            count = 0
            current = self.head
            while current is not None:
                count +=1
                current = current.next
            print(curr.data, end="->")
            curr=curr.next
        print("None")
        print("length : ",count)

    def inset_first(self,data):
        new_node=Node3(data) # 새로운 노드를 생성,아직 값은 안줌

        new_node.next = self.head # head 위치를 새 노드의 한칸 뒤에 넣음 즉 head 앞에 new_node 를 넣음 
        self.head = new_node # head 위치를 new_node 로 바꿔서 결과적으로 head 앞에 new_node 하나가 추가된 리스트가 돼었음
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count
    def delete(self,target): # 노드 삭제를 하는 함수
        if self.head is None: # 첫 노드부터 None 이 나오면 삭제할 node list 자체가 없다는 뜻
            print("list is empty")
            return 
        if self.head.data == target:
            self.head = self.head.next
        current = self.head # 첫 위치 정보를 담은 current 변수를 하나만듬 - 순회용 참조 변수
        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                print("target 삭제 완료")
                return 
            current = current.next
        print("값을 찾지 못함")


    def delete2(self,target):
        if self.head is None or self.head == target:
            return 
        current = self.head.next
        while current is not None:
            if current == target :
                current = current.next
                return 
            else :
                current = current.next # head 자체는 원본으로 보관 해야함 그럼 원본이 target 인 경우에 예외로 하나 만들어야 겠네 

    
s = S_list()
s.append(100)
s.append(200)
s.append(300)
s.inset_first(50)
s.print_list()
print("length : ",s.length() , "list : ",s.print_list())



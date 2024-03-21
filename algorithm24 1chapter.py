'''
def gcd(a,b):
    while(b !=0):
        r = a%b
        a = b
        b =r
    return a

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

num =gcd(num1, num2)
print("두 숫자의 최대공약수는", num, "입니다.")
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        list_content = []
        while current:
            list_content.append(current.data)
            current = current.next
        print("리스트의 내용:", list_content)

def main():
    linked_list = SinglyLinkedList()
    node_count = int(input("노드의 개수: "))

    for i in range(1, node_count + 1):
        data = int(input(f"노드 #{i} 데이터: "))
        linked_list.add(data)

    linked_list.display()

if __name__ == "__main__":
    main()

class node:
    def __init__(self, data, ref):
        self.data = data
        self.ref = ref

class LL:
    def __init__(self):
        self.head=None
    def insertAtBegin(self, data):
        a = node(data, self.head)
        self.head = a
        
    def printLL(self):
        if self.head is None:
            print("LL empty")
        itr = self.head
        while itr:
            print(itr.data,end=" ")
            itr = itr.ref
        print()
    def insertAtEnd(self,data):
        a = node(data,None)
        itr = self.head
        while itr.ref:
            itr = itr.ref
        itr.ref = a
    def lengthOfLL(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.ref
        return count

    def lengthOfLl(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.ref
        return count 
    def isCycle():                       #Floyd's algorithm
        fast = self.head
        slow = self.head
        while fast and slow and fast.ref:
            fast = fast.ref.ref
            slow = slow.ref
            if fast == slow:
                print("Repeats")
                break
'''    
    def combineSort(head1, head2):
        temp = node(0, None)
        while True:
            if head1.ref is not None:
'''                

obj = LL()

obj.insertAtBegin(2234)
obj.insertAtBegin(1112)
obj.insertAtBegin(343)
obj.insertAtBegin(221)
obj.insertAtBegin(23)
obj.insertAtBegin(1)

obj.printLL()

ls2 = LL()

ls2.insertAtBegin(5)
ls2.insertAtBegin(4)
ls2.insertAtBegin(3)
ls2.insertAtBegin(2)
ls2.insertAtBegin(0)

ls2.printLL()

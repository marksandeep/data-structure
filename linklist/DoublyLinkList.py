class Node(object):
    def __init__(self):
        self.prev = None
        self.data = None
        self.next = None


class DoublyLinkList(object):
    def __init__(self):
        self.start = None
    
    def CreateDoublyList(self, data):
        node = Node()
        node.data = data
        if self.start == None:
            node.next = None
            node.data = data
            self.start = node
            node.prev = self.start
            return
        head = self.start
        while head.next != None:
            head = head.next
        head.next = node
        node.prev = head
    
    def DisplayDoublyLinkList(self):
        head = self.start
        while head.next != None:
            print (head.data)
            head = head.next
    
    def AddNodeAtSpecificPosiion(self, data, n):
        head = self.start
        counter = 1
        while counter != n:
            head = head.next
            counter = counter + 1
        node = Node()
        node.data = data
        temp = head.next
        node.next = head.next
        head.next = node
        node.prev = temp
    
    def DeleteNodeFromASpecific(self, n):
        head = self.start
        count = 1
        while count != n:
            head = head.next
            count = count + 1
        head.next = head.next.next
        head.next.next.prev = head







if __name__ == "__main__":
    a = DoublyLinkList()
    a.CreateDoublyList(2)
    a.CreateDoublyList(4)
    a.CreateDoublyList(12)
    a.CreateDoublyList(4)
    print ('==============')
    a.DisplayDoublyLinkList()
    print ("***************")
    a.AddNodeAtSpecificPosiion(23, 2)
    a.DisplayDoublyLinkList()
    print("&&&&&&&&&&&&&&&&&&&&&&&")
    import pdb;pdb.set_trace()
    a.DeleteNodeFromASpecific(2)
    a.DisplayDoublyLinkList()




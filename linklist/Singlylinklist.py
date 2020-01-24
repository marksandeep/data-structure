class Node(object):
    def __init__(self):
        self.next = None
        self.data = None


class SinglyLinkList(object):
    def __init__(self):
        self.start = None
    
    def CreateNode(self, data):
        node = Node()
        node.data = data
        if self.start == None:
            self.start = node
            node.next = None
            return
        p = self.start
        while p.next != None:
            p = p.next
        p.next = node
    
    def DisplayList(self):
        p = self.start
        while p.next != None:
            print (p.data)
            p = p.next
    
    def InsertNodeAtGivenPlace(self, data, n):
        p = self.start
        counter = 1
        while counter != n:
            p = p.next
            counter = counter + 1
        node = Node()
        node.data = data
        temp = p.next
        p.next = node
        node.next = temp

    def DeleteNodeAtGivenPlace(self, n):
        p = self.start
        counter = 1
        while counter != n:
            p = p.next
            counter = counter + 1
        p.next = p.next.next
        
        



if __name__ == "__main__":
    a = SinglyLinkList()
    # import pdb; pdb.set_trace()
    a.CreateNode(2)
    a.CreateNode(3)
    a.CreateNode(4)
    a.CreateNode(5)
    a.DisplayList()
    print("++++++++++++++++++++++++++++")
    a.InsertNodeAtGivenPlace(19, 2)
    a.DisplayList()
    print ('------------------------')
    a.DeleteNodeAtGivenPlace(2)
    a.DisplayList()
        



        



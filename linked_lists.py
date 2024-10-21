class Node:
    def __init__(self,curr=None,next = None):
        self.curr = curr
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_head = Node(data,self.head)
        self.head = new_head

    def del_begin(self):
        if self.head:
            self.head = self.head.next

    def print(self):
        itr  = self.head
        llstr = ""
        while itr:
            llstr = llstr + str(itr.curr) + "--->"
            itr = itr.next
        print(llstr)
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        print(count)
        return count
    
    def insert_at(self,index,data):
        itr = self.head
        count = 0
        if index < 0 or index > self.get_length():
            raise Exception("index is not valid")
        if index == 0:
            self.insert_begin(data)
            return
        while itr:
            if count == index-1:
                new = Node(data,itr.next)
                itr.next = new
                
                return
            itr = itr.next
            count +=1

#############################################

    def insert_end(self,data):
        if not self.head:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(data)

    def del_at(self,index):
        if index< 0 or index>=self.get_length():
            raise Exception("index out of range")
        if index == 0:
            self.del_begin()
        count = 0
        itr = self.head
        while itr:
            if index-1 == count:
                itr.next = itr.next.next
                return
            count +=1
            itr = itr.next

    def del_end(self):
        last_index = self.get_length()-1
        itr = self.head
        count = 0
        while itr:
            if last_index-1 == count:
                itr.next = None
                return
            count +=1
            itr = itr.next
                

            



example = LinkedList()
example.insert_begin(5)
example.print()

example.insert_begin(6)
example.print()

example.del_begin()
example.print()

example.insert_begin(10)
example.print()

example.get_length()
example.print()


example.insert_at(1,9)
example.print()


example.insert_end(45)
example.print()


example.del_at(0)
example.print()

example.del_end()
example.print()


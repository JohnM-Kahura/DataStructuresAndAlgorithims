class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        
        self.head=node

    def insert_at_end(self,data):
        # handles the case where linked list is empty
        
        if self.head == None:
            self.head=Node(data,None)
            return
        # iterator variable 
        itr=self.head
        # run while itr.next is not None
        while itr.next:
            itr=itr.next
        # if it finds itr.next as None this means we have reached the end of the linked list 
        # add data here
        itr.next=Node(data,None)        

    def print(self):
        if self.head == None:
            print('Linked list is empty')   
            return
        itr=self.head
        llstr='' #linked list string
        while itr:
            llstr += str(itr.data) +'----->'
            itr=itr.next
        print(llstr) 

    def get_len(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    def insert_values(self,list_data):
       
        for data in list_data:
            self.insert_at_end(data)
    def del_and_insert(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_begining(data)

    def remove_at(self,index):
        if index<0 or index>self.get_len():
            raise Exception('Invalid index')
        if index==0:
            self.head=self.head.next 
        count=0    
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>self.get_len():
            raise Exception('Invalid index')  

        if index==0:
            self.insert_at_begining(data)

        itr=self.head
        count=0
        while itr:
            if index==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1       
            











    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head==None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return   
        

    def remove_by_value(self, data):
        # Remove first node that contains data
        pass

# make the following calls
ll = LinkedList()
# ll.insert_values(["banana","mango","grapes","orange"])
# ll.print()
# ll.insert_after_value("mango","apple") # insert apple after mango
# ll.print()
# ll.remove_by_value("orange") # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()
ll.insert_at_begining(78)
ll.insert_at_begining(38)
ll.insert_at_end(28)
ll.insert_at_end(48)
ll.insert_values(['john','alec','nora'])
ll.print()
# ll.remove_at(1)
ll.print()
ll.remove_at(6)
ll.insert_at(3,9)
ll.print()
print(ll.get_len())
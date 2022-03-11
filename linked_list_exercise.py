class Node:
    def __init___(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init___(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head == None:
            print('Linked list is empty')   
            return
        itr=self.head
        llstr='' #linked list string
        while itr:
            llstr += str(itr) +'----->'
            itr=itr.next
        print(llstr)    






def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    pass

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
ll.print()
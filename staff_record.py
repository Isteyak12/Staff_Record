class Node:
    def __init__(self, data, rate):
        self.data = data
        self.rate = rate
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_back(self, val, rate):
        self.size += 1
        # runtime is O(1) best case
        # runtime is O(n) avg/worst case
        new_node = Node(val, rate)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # current = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = new_node

    def insert_front(self):
        self.size += 1
        # runtime is O(1) best/avg/worst case
        # runtime is O(n)
        new_node = Node(val, rate)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # current = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_back(self):
        # runtime is O(n)=1 best as 1 elem removed
        # runtime is O(n)=n until last elem is removed
        self.size -= 1
        if (self.size == 1):
            self.head = None
            self.tail = None
        if (self.size == 2):
            self.tail = self.head
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None

    def remove_front(self):
        # runtime is O(1) in all cases
        # as direct assingnment of
        # elements happen
        self.size -= 1
        if (self.size == 1):
            self.head = None
            self.tail = None
        if (self.size == 2):
            self.head = self.tail
        if (self.size > 2):
            self.head = self.head.next

    # def count_dup():

    # def sort_names(LL linklist):
    #     temp=linklist
    #     curr=linklist.next
    #     while temp is not None:

    #         while(j>0):
    #             if()
    #             j-=1

    # def names(self):
    def print_p(self):
        print("Hella")
        current = self.head
        while current is not None:
            print(current.data, " : ", current.rate)
            current = current.next


l1 = LL()
l1.insert_back("man", 0)
l1.print_p()

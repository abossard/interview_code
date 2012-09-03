class LinkedList(object):
    
    class Node(object):
        
        list = None
        data = None
        next = None
        
        def __init__(self, list, data, next):
            self.list = list
            self.data = data
            self.next = next
            
        def __unicode__(self):
            if self.next:
                return "%s -> %s"%(self.data, self.next.__unicode__())
            else:
                return self.data
    
    head = None
    tail = None
    
    def __init__(self):
        pass
        
    def purge(self):
        self.head = None
        self.tail = None
        
        
    @property
    def is_empty(self):
        return self.head == None
        
    @property
    def first(self):
        if self.head:
            return self.head
        else:
            raise ContainerEmpty

    @property
    def last(self):
        if self.last:
            return self.last
        else:
            raise ContainerEmpty
                        
    def prepend(self, data):
        new_node = LinkedList.Node(self, data, self.head)
        if not self.head:
            self.tail = new_node
        self.head = new_node

    def append(self, data):
        new_node = LinkedList.Node(self, data, None)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
    def __unicode__(self):
        return self.head.__unicode__()


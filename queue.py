class Queue(object):
    
    a = list()
    b = list()
    
    def enqueue(self, data):
        tmp = self.b.pop() if self.b else None
        while tmp:
            self.a.append(tmp)
            tmp = self.b.pop() if self.b else None
        self.a.append(data)
        tmp = self.a.pop() if self.a else None
        while tmp:
            self.b.append(tmp)
            tmp = self.a.pop() if self.a else None
    
    def dequeue(self):
        return self.b.pop() if self.b else None
    
    def size(self):
        return len(self.b)
        
    def __unicode__(self):
        return self.b
        
q = Queue()
q.enqueue('first')
q.enqueue('second1')
q.enqueue('second2')
q.enqueue('second3')
q.enqueue('last')
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
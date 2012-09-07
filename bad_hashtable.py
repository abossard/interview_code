# Well, hello

class Hashtable(object):
    data = None
    size = 0
    capacity = 0
    next_index = 0
    
    class Entry(object):
        key = None
        value = None
        def __init__(self, key, value):
            self.key = key
            self.value = value
    
    def __init__(self, initial_size=10):
        self.capacity = initial_size
        self.data = [None] * self.capacity
        
    def put(self, key, value):
        self.data[self.next_index] = self.Entry(key, value)
    
    def get(self, key):
        for data in self.data:
            if data.key == key:
                return data.value
        return None
        
    def __str__(self):
        output = 'Hashtable:\n'
        for data in self.data:
            output += "%s: %s\n"%(data.key, data.value) if data else "[empty]\n"
        return output
        
hashtable = Hashtable()
hashtable.put('key','value')
print hashtable.get('key')
print hashtable
class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def get(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        

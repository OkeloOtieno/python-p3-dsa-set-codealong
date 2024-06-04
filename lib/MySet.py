class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
        
    def has(self, key):
        return key in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            return True
        return False
    
    def size(self):
        return len(self.dictionary)
    

    def clear(self):
        self.dictionary = {}
        return self


# hash maps stors key followed by

# key -> hash function-> generates an address-> which stores the value

# hash function takes key as an input (string index)

# we can use ascii numbers to implement an hash function


def get_hash(key):
    h=0
    for char in key:
        h += ord(char)
    return h%100

#print(get_hash("march 28"))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] #value in each of these elements is none
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    #def add(self, key, value):
    # add can be replaced by __setitem
    def __setitem__(self, key, value):
        h = self.get_hash(key) # first retrieve hash
        self.arr[h] = value

    #def get(self, key):
    # get can be replaced by getitem
    def __getitem__(self, key):
        # get function only called for a key
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key) # first step is always get the hash index
        self.arr[h] = None    
t = HashTable()
t.get_hash('march 6')
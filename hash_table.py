class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        index = self.hash(key)

        if index not in self.collection:
            self.collection[index] = {}

        # store key-value inside nested dictionary
        self.collection[index][key] = value

    def remove(self, key):
        index = self.hash(key)

        if index in self.collection:
            if key in self.collection[index]:
                del self.collection[index][key]

                # if bucket becomes empty, optionally clean it
                if not self.collection[index]:
                    del self.collection[index]

    def lookup(self, key):
        index = self.hash(key)

        if index in self.collection:
            return self.collection[index].get(key)

        return None

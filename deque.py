# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
# Make it possible to represent the content of the custom class calling print.


#Example:
#```python
#>>> d = HistoryDict()
#>>> d.set_value("bar", 43)
#>>> d.history

#["bar"]

#>>>print(d)

#'{"bar": 43}'
#```

#/After your own implementation of the class have a look at `collections.deque` https://docs.python.org/3/library/collections.html#collections.deque/

class Deque():
    def __init__(self, max_sz):
        self.arr = [None for _ in range(max_sz)]
        self.head = self.tail = 0
        self.max_sz = max_sz
        self.size = 0

    def push_front(self, el):
        if self.size >= self.max_sz:
            self.pop_back()
        self.arr[self.head] = el
        self.head = (self.head-1) % self.max_sz
        self.size += 1
        print(self.head, self.tail)

    def push_back(self, el):
        if self.size >= self.max_sz:
            self.pop_front()
        self.arr[self.tail] = el
        self.tail = (self.tail+1) % self.max_sz
        self.size += 1
        print(self.head, self.tail)
    
    def pop_front(self):
        if self.size == 0:
            return None
        x = self.arr[self.head] 
        self.arr[self.head] = None
        self.head = (self.head + 1) % self.max_sz
        self.size -= 1
        return x
    
    def pop_back(self):
        if self.size == 0:
            return None
        self.tail = (self.tail - 1) % self.max_sz
        x = self.arr[self.tail] 
        self.arr[self.tail] = None
        self.size -= 1
        return x

    def get_items(self):
        res = []
        end = self.tail-1
        cnt = self.size
        while cnt > 0:
            res.append(self.arr[end])
            end = (end - 1) % self.max_sz
            cnt -= 1
        return res


MAX_STORE_SZ = 10

class HistoryDict():
    def __init__(self):
        self.hist_data = Deque(MAX_STORE_SZ)
        self.data = {}

    def set_value(self, key, val):
        self.data[key] = val
        self.hist_data.push_back(key)

    def history(self):
        return [el for el in self.hist_data.get_items()] 


#https://pythonworld.ru/moduli/modul-collections.html
from collections import deque

class HistoryDict2():
    def __init__(self):
        self.hist_data = deque(maxlen=MAX_STORE_SZ)
        self.data = {}

    def set_value(self, key, val):
        self.data[key] = val
        self.hist_data.append(key)

    def history(self):
        return list(self.hist_data)


if __name__=='__main__':
    d = HistoryDict()
    print(d.history())
    d.set_value("to", 10)
    d.set_value("into", 11)
    d.set_value("foo", 12)
    d.set_value("boo", 13)
    d.set_value("blue", 14)
    d.set_value("rooster", 15)
    d.set_value("roster", 16)
    d.set_value("booster", 17)
    d.set_value("brewster", 18)
    d.set_value("schuster", 19)
    d.set_value("wooster", 20)
    d.set_value("klooster", 21)
    d.set_value("morale booster", 22)
    print(d.history())




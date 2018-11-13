#!/usr/bin/env python3
#Counter: convering my old CS140 constructor
#learning projects to python to learn about
#object-oriented stuff in python rather than java
#one thing I noticed is the lack of access modifiers
#but they were largely an annoyance in java
#and lead to antipatterns like getters and setters
class Counter:
    def __init__(self,counter): #__init__ = constructor
                         #self = this
                         #(comparing java to python)
        self.counter = counter
    def increment(self):
        self.counter += 1
    def decrement(self):
        self.counter -= 1
    def getValue(self):
        return self.counter
    def setValue(self, newValue):
        self.counter = newValue

counter_1 = Counter(5)
counter_1.increment()
print(counter_1.getValue())


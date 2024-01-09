# sequence_iter.py
#How iter, next and iteration works


#define a list of numbers
Y = [1,2,3,4]

# The class is the iterator, which implements the __iter__
# and __next__ method
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

#calling the iterator, which returns self
    def __iter__(self):
        return self

#iterates over the next item in the list
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
#Parse a variable or iteraable object "obj"                                             
obj= SequenceIterator(Y**2)
print(obj._sequence)
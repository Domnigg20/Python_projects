# sequence_iter.py
#How iter, next and iteration works

Y = [1,2,3,4]
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
obj= SequenceIterator(Y**2)
print(obj._sequence)
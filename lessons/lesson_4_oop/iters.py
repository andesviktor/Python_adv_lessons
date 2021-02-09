# lis = [1,2,3,4]
# iter_lis = iter(lis)
# print(next(iter_lis))
# Note: Итерация
class MyIter:
    def __init__(self,stop):
        self.stop = stop
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < self.stop:
            return self.count
        else:
            raise StopIteration

#m_iter = MyIter(3)
for i in MyIter(3):
    print(i)
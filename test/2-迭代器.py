
class Demo():
    def __init__(self,container):
        self.count=-1
        self.container=container
        self.len_ = len(container)
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        if self.count>=self.len_:
            raise StopIteration
        else:
            return self.container[self.count]*2
import copy

t=[1,2,3]
a=Demo(t)
print(a.container)
print('#'*30)
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
print(a,b,c,d,sep='\n')
print('#'*30)
a.container[1]=666
print(a.container)
print('a:{} {}\nb:{} {}\nc:{} {}\nd:{} {}'.format(a,a.container,b,b.container,c,c.container,d,d.container))


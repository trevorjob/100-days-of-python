def add(a,b):
        return a + b

def sub(a,b):
        return a - b

def mul(a,b):
        return a * b

def div(a,b):
        if a == 0:
                raise ValueError('a must be greater than zero')
        return a / b


class Employee:
        
        raise_amt = 1.05
        
        def __init__(self, first, last, pay) -> None:
                self.first = first
                self.last = last
                self.pay = pay
                
        @property
        def email(self):
                return f'{self.first}.{self.last}@email.com'
        
        @property
        def fullname(self):
                return f'{self.first} {self.last}'
        
        def apply_raise(self):
                self.pay = int(self.pay* self.raise_amt)
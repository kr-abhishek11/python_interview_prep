class MyClass:
    def __init__(self,value):
        self._value = value

    @property
    def get_value(self):
        return self._value
    
    @property
    def set_value(self):
        return self._value
    
    @set_value.setter
    def set_value(self,new_value):
        self._value = new_value + 1
    
obj1 = MyClass(10)
print(obj1.get_value)
obj1.set_value = 10
print(obj1.set_value)
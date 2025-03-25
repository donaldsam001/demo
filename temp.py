class person():
    def __init__(self, name, age):
        self._name = name
        self.age = age
    def _display(self):
        return self._name, self.age

p=person('John', 30)
print(p._display())
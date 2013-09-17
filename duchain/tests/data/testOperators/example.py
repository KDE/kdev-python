class Add(): pass
class Sub(): pass
class Mul(): pass
class Floordiv(): pass
class Mod(): pass
class Divmod(): pass
class Pow(): pass
class Lshift(): pass
class Rshift(): pass
class And(): pass
class Xor(): pass
class Or(): pass

class Example():
    def __add__(self, other):
        return Add()
    def __sub__(self, other):
        return Sub()
    def __mul__(self, other):
        return Mul()
    def __floordiv__(self, other):
        return Floordiv()
    def __mod__(self, other):
        return Mod()
    def __divmod__(self, other):
        return Divmod()
    def __pow__(self, other, modulo):
        return Pow()
    def __lshift__(self, other):
        return Lshift()
    def __rshift__(self, other):
        return Rshift()
    def __and__(self, other):
        return And()
    def __xor__(self, other):
        return Xor()
    def __or__(self, other):
        return Or()

print(1)


class A:
    def __init__(self, field):
        self.field = field


class B(A):
    def my_method(self):
        print("my_method in B")

class C(A):
    def my_method(self):
        print("my_method in C")


b = B(1)
print(b.field)
b.my_method()
b = C(2)
b.my_method()

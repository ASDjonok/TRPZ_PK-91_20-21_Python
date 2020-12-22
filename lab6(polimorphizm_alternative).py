print(1)


class A:
    def __init__(self, field):
        self.field = field


class B:
    def my_method(self):
        print("my_method in B")

class C:
    def my_method(self):
        print("my_method in C")


b = B()
# print(b.field)
b.my_method()
b = C()
b.my_method()

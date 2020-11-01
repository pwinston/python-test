class A:
    def __init__(self):
        super().__init__()
        print("A")


class B:
    def __init__(self):
        super().__init__()
        print("B")


class D(A, B):
    def __init__(self):
        super().__init__()
        print("D")


d = D()

print(D.__mro__)

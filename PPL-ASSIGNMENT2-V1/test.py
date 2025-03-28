# class A:
#     def __init__(self):
#         print('A')

# class C:
#     def __init__(self):
#         print('C')

#     def stalk(self):
#         print('stalk')

# class B:
#     def __init__(self):
#         print('B')
    
#     def stalk(self):
#         print('stalkB')

# class D(A, B):
#     def __init__(self):
#         print('D')
#         super().__init__()

# class E(C, A):
#     def __init__(self):
#         print('E')
#         super().__init__()

# class F(D, E, B):
#     def __init__(self):
#         print('F')
#         super().__init__()
# print(F.__mro__)




# class X:
#     def show(self):
#         print("X")

# class Y:
#     def show(self):
#         print("Y")

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class C(A, B):
#     pass

# print(C.__mro__)  # Kiểm tra MRO


class X:
    def show(self):
        print("X")

class Y(X):
    def show(self):
        print("Y")

class Z(X):
    def show(self):
        print("Z")

class A(Y, Z):
    def show(self):
        print("A")

class B(Y, Z):
    def show(self):
        print("B")

class C(A, B):
    def show(self):
        print("C")

print(C.__mro__)

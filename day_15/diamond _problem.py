class A:
    def a_method(self):
        print("from a method")

class B(A):

    def a_method(self):
        print("Overridden by B Class")

    def b_method(self):
        print("from b")

class C(A):

    def a_method(self):
        print("Overridden by C Class")

    def c_method(self):
        print("From c")

class D(B, C):
    def d_method(self):
        print("From B and C")

d_obj = D()
d_obj.a_method()

class A:
 def __init__(self):
    self.calc_i(368)
 
 def calc_i(self, i):
    self.i = 39 * i
class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
 
    def calc_i(self, i):
        self.i = 34 * i

b = B()

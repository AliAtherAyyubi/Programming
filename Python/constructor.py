

class A:
    def __init__(self):
        self.prod(2)
        # print("construct of A")

    # def prod(self,n):
    #     self.n=5*n
        
class B(A):
    def __init__(self):
        super().__init__()
        print("construct of B",self.n)


    def prod(self,n):
        self.n=3*n



b=B()
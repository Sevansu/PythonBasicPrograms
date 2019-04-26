class a:
    def f1(self):
        print("Method 1")

class b(a):
    def f1(self):
        print("Method 2")
        super().f1()
obj=b()
obj.f1()

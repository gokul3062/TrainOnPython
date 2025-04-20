
class parent:
    def __init__(self , name):
        self.name = name
    
    def check(self):
        return "It is Working"

class child(parent):
    def __init__(self , name):
        super().__init__(name)
    
    @property
    def access(self):
        return self.name
    

temp = child('Go-Cool')
print(temp.access , temp.check())
        
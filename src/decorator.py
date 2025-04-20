

#property decorato r

class decorator:
    def __init__(self):
        self.val = 3.14
    
    @property
    def pi(self):
        return 3.14 * 2

print(decorator().pi)


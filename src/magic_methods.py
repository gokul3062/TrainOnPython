class solution1:
    def __init__(self , num):
        self.val = num
    
    def __mul__(self , next):
        return self.val * next.val

class solution3:
    def __init__(self):
        self.arr = [0 , 2 , 3 , 4 , 5 , 6 , 7]

    def __len__(self):
        return len(self.arr)

    def __getitem__(self , i):
        return self.arr[i]
    
    def __setitem__(self , i , n):
        self.arr[i] = n
    
    def append(self , n):
        self.arr.append(n)

temp = solution3()
temp[0] = 1
temp.append(1000)
for n in temp:
    print('val' , n)
print('len' , len(temp))

print('MUL' , solution1(23) * solution1(332))

#Magic Methods
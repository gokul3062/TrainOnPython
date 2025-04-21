
import time

#With Yield
def fn():
    i = 0
    while i < 10000000:
        yield i
        i += 1
    
#Without Yield
def fn1():
    i = 0
    arr = []
    while i < 10000000:
        arr.append(i)
        i += 1
    
    return arr

start = time.time()
listN = []
for n in fn():
    listN.append(n ** 2)

end = time.time()
print(f"Time Taken with Yield {end - start:.2f}")

start = time.time()
listN = []
for n in fn1():
    listN.append(n ** 2)

end = time.time()

print(f"Time Taken without Yield {end - start:.2f}")


#Using Next in generator
generator = fn()
for _ in range(5):
    val = next(generator)
    print(val)
    

#Can be used in Memory Effecient Tasks
# def read_lines(filename):
#     with open(filename) as f:
#         for line in f:
#             yield line.strip()

# for line in read_lines("big_file.txt"):
#     process(line)  # Processes line-by-line, memory safe!

#import random to genenerate random numbers
import random

#generate random 20 numbers and store it in a file 
arr20 = []
for i in range(0,20):
    n = random.randint(1,6000)
    arr20.append(n)
print(arr20)
with open('arr20.txt','w') as f:
    f.write(str(arr20))
print("The above is array of 20 elements")
print("  ")
print(type(arr20))
#lines = arr20.read().split(',')


#generate random 100 numbers and store it in a file 
arr100 = []
for i in range(0,100):
    n = random.randint(1,6000)
    arr100.append(n)
print(arr100)
with open('arr100.txt','w') as f:
    f.write(str(arr100))
print("The above is array of 100 elements")
print(" ")


#generate random 1000 numbers and store it in a file 
arr1000 = []
for i in range(0,1000):
    n = random.randint(1,6000)
    arr1000.append(n)
print(arr1000)
with open('arr1000.txt','w') as f:
    f.write(str(arr1000))
print("The above is array of 1000 elements")
print(" ")


#generate random 4000 numbers and store it in a file 
arr4000 = []
for i in range(0,4000):
    n = random.randint(1,6000)
    arr4000.append(n)
print(arr4000)
with open('arr4000.txt','w') as f:
    f.write(str(arr4000))
print("The above is array of 4000 elements")
print(" ")

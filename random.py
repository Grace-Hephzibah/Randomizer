import time

a = time.gmtime()[5]
b = time.gmtime()[4]

print("What is the biggest value that you want in this random function ? ")
x = int(input())

print((a**b)%x)

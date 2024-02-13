#Factorial of numbers
def factorial(a):
    i = 1
    while a>1:
        i = a * i
        a = a - 1
        r = a * i
    print("The Factorial value of the given number is",r)

print("####Factorial of numbers####")
n = int(input("The Number to find its Factorial Value: "))
factorial(n)
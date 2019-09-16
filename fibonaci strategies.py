#recursiv
"""""
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))

"""""

#if else
"""""
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))
"""

#cu for
"""""
def fibo(n):
    f1, f =1, 1
    for i in range(2 ,n):
        f1, f = f, f1+f
    return f


n = int(input())
print(fibo(n))
"""
#cu while
"""""
def fibo(n):
    f1, f = 1, 1
    while f < n:
        f1, f= f, f1+f
    return f


n = int(input())
print(fibo(n))
"""

"""""
x = 2.5
if type(x) == int:
    print("e unu intreg")
elif type(x) == float:
    print("e unu real")
else:
    print("nu e numar")
"""

"""""
import turtle
drept= turtle.Pen()
drept.forward(100)
drept.left(90)
drept.forward(50)
drept.left(90)
drept.forward(100)
drept.left(90)
drept.forward(50)
x=input()
"""
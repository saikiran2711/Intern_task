2.Write a Python function to find the next number in the series  2, 3, 10, 15, 26, 35, 50, 63, ?

Code:

def find_next(n):
    for i in range(1,n+1):
        val = i%2==0 and (i**2) - 1 or (i**2) + 1
        print(val)


find_next(9)


3.3. Write a Python Code that takes input as the values of x, y, a, b to solve the following equation:
[ {x + (1/y) }**a * {x – (1/y)}**b] / [ {y + (1/x) }**a * {y – (1/x)}**b]

Code :
x,y,a,b = list(map(int, input("enter x y a b with space in between : ").split(' ')))
exp = ( (x+(1/y))**a * (x-(1/y))**b ) / ( (y+(1/x))**a * (y-(1/x))**b )
print(exp)
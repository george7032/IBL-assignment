arithmetic = input("Enter an arithmetic expression: ")

#one hace to enter a value followed by space,
#then the arguement followed by space then the last value.
x, y, z = arithmetic.split()

x1=float(x)

z1=float(z)

#conditions

if y == ("+"):
    answer=x1 + z1

if y == ("-"):
    answer=x1-z1

if y==("*"):
    answer=x1*z1

if y== ("/"):
    answer=x1/z1

print(answer)
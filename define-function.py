#This line of code defines a function calles "squared"
#Squared function takes the square of the input provided
def squared(x):
    y=x*x
    return y

z=input("Enter a number:")
print("Square of",z,"is:", squared(int(z)))

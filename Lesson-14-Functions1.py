
def summa(x, y):
    return x+y

def factorial(x):
    "Calculate Factorial of number X"
    vidpovid = 1
    for i in range(1, x+1):
        vidpovid = vidpovid * i
    return vidpovid


print(factorial(1))
print(factorial(5))

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

#-----------------------------

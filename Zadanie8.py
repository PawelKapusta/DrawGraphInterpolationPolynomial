import numpy as np
from sympy import simplify, Symbol
import matplotlib.pyplot as plt

def function(x):
    return 1/(1+5*pow(x,2))

def lagrangeFucntion(x, k, x_values):
    n=len(x_values)
    l=1.
    for j in range(n):
        if k==j :
            continue
        l=l*((x-x_values[j])/(x_values[k]-x_values[j]))
    return l

def interpellationLagrange(x, x_values, y_values):
    n=len(x_values)
    wielomiann = np.array([lagrangeFucntion(x, i, x_values) for i in range(n)])
    p=np.dot(y_values, wielomiann)
    return p

pointsArray=[]
print("My calculated points")
for i in range(0, 65):
   pointsArray.append(-1 + (i / 32.0))
   print("x{} = {}".format((i + 1), "%0.7f" % pointsArray[i]))
temp=np.array(pointsArray)

pointsValue=[]
for i in range(0, 65):
    pointsValue.append(function(pointsArray[i]))

print("Our values of polynomial: ")
for a in pointsValue:
    print(a)
temp2=np.array(pointsValue)


print ("My polynomial: >>>>")
X= Symbol('x')
y = interpellationLagrange(X, temp, temp2)#Calculate Lagrange interpolation
print(y)

x=np.linspace(-1.,1.,65*100)# set x from -1 to 1


plt.title = ('graph')
plt.scatter(temp, temp2)
plt.axhline()
plt.axvline()
plt.grid(True)
plt.plot(x, interpellationLagrange(x, temp, temp2), 'r')
plt.show()

plt.savefig('graph')
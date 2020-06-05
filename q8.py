import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

def f(x,y):
  return np.vstack((y[1],4*y[0]-x))
def bc(ya,yb):
  return np.array([ya[0]-0,yb[0]-2])
  
x=np.linspace(0,1)

y=np.zeros([2,len(x)])
y[0]=np.linspace(0,2,len(x))

def ygiven(x):
  return x+np.e**2/(np.e**4-1)*(np.exp(2*x)-np.exp(-2*x))

result=solve_bvp(f,bc,x,y)
resultf=result.sol(x)[0]

plt.plot(x,resultf,label='numerucal solution.')
plt.plot(x,ygiven(x),label='analytic solution.')

plt.legend()
plt.xlabel('x')
plt.ylabel('y') 
plt.show()

import numpy as np
import matplotlib.pyplot as plt 

x=np.linspace(0,0.5,100)
h=x[1]-x[0] 

y=np.zeros([len(x),2])
y[0]=[1/3,1/3]

def f(x,y):
  dy1=32*y[0]+66*y[1]+2/3*x+2/3 
  dy2=-66*y[0]-133*y[1]-1/3*x-1/3
  return np.array([dy1,dy2])

for j in range(len(x)-1):
  k1=h*f(x[j],y[j])
  k2=h*f(x[j]+h/2,y[j]+k1/2)
  k3=h*f(x[j]+h/2,y[j]+k2/2)
  k4=h*f(x[j]+h,y[j]+k3) 
  y[j+1]=x[j]+(k1+2*k2+2*k3+k4)/6

plt.plot(x,y[:,0])
plt.plot(x,y[:,1])

plt.xlabel('t.')


plt.show() 
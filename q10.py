import numpy as np
import matplotlib.pyplot as plt 

n=512  
dx=1
xmin=-(n-1)*dx/2 

x=np.zeros(n)
k=np.zeros(n) 
fx=np.zeros(n)
fk=np.zeros(n)

for i in range(n):
  x[i]=xmin+i*dx 
  if -1<x[i]<1:
    fx[i]=1
  else:
    fx[i]=0


dft=np.fft.fft(fx)/np.sqrt(n) 
k=2*np.pi*np.fft.fftfreq(n,dx)

#sorting dft and k in ascending orders of k.
l=np.argsort(k)
k=k[l]
dft=dft[l]

fk=dx*np.sqrt(n/(2.0*np.pi))*np.exp(-1j*k*xmin)*dft
plt.subplot(222)    
plt.plot(k,np.real(fk),label='numerical ft of f(x)')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.legend()
plt.show
 
plt.subplot(121)
plt.plot(x,fx)
plt.xlabel('x')
plt.ylabel('fx')

plt.show
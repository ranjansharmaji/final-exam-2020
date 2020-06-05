import numpy as np
import matplotlib.pyplot as plt

data=np.random.rand(1024)

plt.figure(figsize=[7,20])

plt.subplot(411)
plt.hist(data,density=True)
plt.xlabel('uniform disribution')
plt.ylabel('density')

n=len(data)
dft1=np.fft.fft(data)/np.sqrt(n)

k1=2*np.pi*np.fft.fftfreq(n)
l=np.argsort(k1)

k=k1[l]
dft=dft1[l]
powerspectrum=abs(dft)**2

plt.subplot(412)
plt.plot(k,powerspectrum)
plt.xlabel('k')
plt.ylabel('powerspectrum')

print('minimum and maximum k',min(k),max(k))       

#binned power spectrum.
bin=np.linspace(min(k),max(k),6)
binavrage=[]
for i in range(5):
  bin_p_spec=powerspectrum[(k-bin[i])*(bin[i+1]-k)>0]        
  binavrage.append(np.mean(bin_p_spec))

plt.subplot(413)
plt.bar(bin[0:5],binavrage,width=1,label='binned power-spectrum.')      
plt.xlabel('k')
plt.ylabel('power-spectrum')
plt.legend()

plt.show()        

#Due to randomness we get avrage power spectrum coresponding to k=0 as there are random frequency so we expect power spectrum along k=0.
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter
import fft_test5

fs=500
Ts=1/fs
t=np.linspace(0,1,fs)
y=np.sin(2*np.pi*100*t)+3*np.sin(2*np.pi*30*t)+2*np.sin(2*np.pi*50*t)
plt.subplot(221)
plt.plot(t,y)

yf=np.fft.fft(y)
xf=np.fft.fftfreq(len(yf),Ts)
plt.subplot(222)
plt.plot(xf,np.abs(yf))

plt.subplot(223)
b,a=fft_test5.butter_bandpass(40,100,fs,5)
yt=fft_test5.butter_bandpass_filter(y,40,100,fs,5)
plt.plot(t, yt)


plt.subplot(224)
yf2=np.fft.fft(yt)
xf2=np.fft.fftfreq(len(yf2),Ts)
plt.plot(xf2,np.abs(yf2))
plt.show()
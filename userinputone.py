from typing import Union
from wave import Wave_write, Wave_read
import jstereo as js
from jstereo import filtmono
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
#wav file reading
import wave
from scipy.io import wavfile
from scipy.io.wavfile import read

y = wave.open('Cleanmono.wav', 'r')

wavefilename = input("Which wav file do you want to use?")

sr, data = wavfile.read(wavefilename)

#create filters
bfc = int(input("Enter fc for LPF"))
lpf = signal.firwin(101, cutoff=bfc, fs=sr, pass_zero = True)

fc1 = int(input ("Enter fc1 for BPF"))
fc2 = int(input ( "Enter fc2 for BPF"))

bpf = signal.firwin(101, [fc1, fc2], fs =sr, pass_zero = False)

fch = input("Enter filter type (LPF or BPF)")

if fch == 'LPF':
    fch1=lpf
    fch2=lpf
else:
    fch1 = bpf
    fch2 = bpf

#check if mono or stereo
if data.ndim>1:
    print('Track is in stereo')
    left = data[:, 0]
    right = data[:, 1]
    data = js.filtcomb(left, right, fch1, fch2)
else:
    print('Track is mono')
    if fch =='LPF':
        print('LPF applied')
        data = filtmono(data, lpf)
    else:
        print('HPF applied')
        data = filtmono(data,bpf)


#testdef
#data = js.filtcomb(left, right, b, b)

#data = np.convolve(tf,x)
#data1 = np.convolve(b,right)
#data2 = np.convolve(tf,left)

#data = np.vstack((data2,data1)).T

#The writing is the same (I will check in audacity, so I need to filter it correctly
#then see if it is writing correctly
wavfile.write('test1.wav', sr, data.astype(np.int16))

print('done')
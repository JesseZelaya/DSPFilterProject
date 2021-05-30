from scipy.io import wavfile
import numpy as np
def filtcomb(left, right, filter1, filter2):
    data1 = np.convolve(filter1, right)
    data2 = np.convolve(filter2, left)

    data0 = np.vstack((data2, data1)).T

    return data0

def filtmono(mfile, filter):
    data1 = np.convolve(filter, mfile)
    return data1

#sr, data = wavfile.read('Clean.wav')

#left = data[:, 0]
#right = data[:, 1]
#return

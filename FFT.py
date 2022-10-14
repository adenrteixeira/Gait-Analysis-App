import numpy as np

def FFT(x,N):
    """
    Function to calculate the Fast Fourier Transform using
    numpy.fft library and create opportunity to have variy
    the size of the coeficients that exists. 
    Here its called N
    """
    if N < len(x):
        x = x[:N]
    elif N > len(x):
        x = (x + [0] * N)[:N] # adds zeros to the size of N

    X = np.fft.fft(x,N)
    
    return X

def IFFT(X,N):
    """
    Function to calculate the Fast Fourier Transform using
    numpy.fft library and create opportunity to have variy
    the size of the coeficients that exists. 
    Here its called N
    """
    X = X.ravel().tolist() # convert to list

    if N < len(X):
        X = X[:N]
    elif N > len(X):
        X = (X + [0] * N)[:N] # adds zeros to the size of N

    x = np.fft.ifft(X,N)
    
    return x


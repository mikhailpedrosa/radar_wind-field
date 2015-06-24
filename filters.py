__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Methods Filtering - Moving Average, Gaussian, Median'
__version__ = '0.1'
__date__ = '13/04/2015'

import numpy as np
from scipy import ndimage
from memory_profiler import profile

#@profile()
def moving_average(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """
    #window = np.ones(window_size)/float(window_size)
    #np.convolve(values, window, 'same')
    matrix = np.zeros((len(values),))

    for index in range(len(values)):
         matrix[index] = np.nansum(values[index:(index+window_size)])

    return matrix/float(window_size)


#@profile() - Implementar
def gauss(values, sigma):
    """

    :param values:
    :param sigma:
    :return:
    """
    matrix = np.zeros((len(values),))
    #Mean_V = np.zeros([len(x_bins), len(y_bins)])
    print matrix.shape
    exit()
    for i, x_bin in enumerate(x_bins[:-1]):
        bin_x = (x > x_bins[i]) & (x <= x_bins[i+1])
        if (sum(x > 0 for x in bin_xy) > 0) :
            matrix[i,:]=np.nanmean(V[bin_x][bin_xy])



    filter_gauss = ndimage.gaussian_filter(values, sigma=sigma)
    #r = range(-int(values/2),int(values/2)+1)
    #filter_gauss = [1 / (sigma * math.sqrt(2*math.pi)) * math.exp(-float(x)**2/(2*sigma**2)) for x in r]
    return filter_gauss

#@profile()
def median(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """
    matrix = np.zeros((len(values),))

    for index in range(len(values)):
        matrix[index] = np.nanmedian(values[index:(index+window_size)])

    return matrix
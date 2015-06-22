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
def gauss(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """
    window = ndimage.gaussian_filter(values, sigma=window_size)

    return np.convolve(values, window, 'same')

#@profile() - Implementar
def median(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """
    window = np.ones(int(window_size))/float(window_size)

    return np.convolve(values, window, 'same')
__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Methods Filtering - Moving Average, Gaussian, Median'
__version__ = '0.1'
__date__ = '13/04/2015'

import numpy as np
from scipy import ndimage
from memory_profiler import profile


#@profile()
def vap_moving_average(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """

    matrix = np.zeros((10, 360, 253))

    for elevation in np.arange(10):
            for rang in np.arange(253):
                for azimuth in np.arange(360):
                    matrix[elevation, azimuth, rang] = np.nansum(values[elevation, azimuth:(azimuth + window_size), rang])
    return matrix / float(window_size)


#@profile()
def vap_median(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """

    matrix = np.zeros((10, 360, 253))

    for elevation in np.arange(10):
            for rang in np.arange(253):
                for azimuth in np.arange(360):
                    matrix[elevation, azimuth, rang] = np.nanmedian(values[elevation, azimuth:(azimuth + window_size), rang])
    return matrix / float(window_size)


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

    for index in np.arange(len(values)):
         matrix[index] = np.nansum(values[index:(index + window_size)])

    return matrix / float(window_size)


#@profile()
def median(values, window_size):
    """

    :param values:
    :param window_size:
    :return:
    """
    matrix = np.zeros((len(values),))

    for index in np.arange(len(values)):
        matrix[index] = np.nanmedian(values[index:(index + window_size)])

    return matrix


#@profile() - Implementar
def gauss(values, sigma):
    """

    :param values:
    :param sigma:
    :return:
    """
    matrix = np.zeros((len(values),))

    for index in np.arange(len(values)):
        print values
        print values[index:(index + sigma)]
        print np.isnan([values[index:(index + sigma)]])
        if np.isnan([values[index:(index + sigma)]]):
            vetor = values[index:(index + sigma)]
            matrix = ndimage.gaussian_filter(vetor, sigma=sigma)
    return matrix
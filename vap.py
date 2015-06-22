__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'

import math
import numpy as np
from memory_profiler import profile

ELEVATION_LIST = {
    'X': ["0.5", "1.5", "2.5", "3.5", "4.5", "5.5", "6.5", "7.5", "8.5", "9.5", "10.5", "11.5", "12.5"],
    'S': ["-0.5", "0.0", "0.5", "1.0", "2.0", "3.0", "4.0", "5.5", "7.0", "8.5"],
}


#@profile()
def vap(radar):
    """
    Implementacao da tecnica de Processamento VAP (Velocity-Azimuth Processing)
    Implementation of the technical processing of VAP (Velocity-Azimuth Processing)
    :param radar: Radar object - Objeto Radar
    :return:
    """
    #The horizontal wind components u and v
    u = np.zeros((10,360,253))
    v = np.zeros((10,360,253))

    u_1 = np.zeros((10,360,253))
    u_2 = np.zeros((10,360,253))
    v_1 = np.zeros((10,360,253))
    v_2 = np.zeros((10,360,253))

    velocity_radial = radar.fields['velocity']['data'].reshape(10,360,253)
    azimuth =  radar.azimuth['data']
    #ca = velocity_ca(velocity_radial)
    #cb = velocity_cb(velocity_radial)
    nsweeps = radar.nsweeps
    nrays = radar.nrays / 10
    ngates = radar.ngates

    #print nsweeps, nrays, ngates

    for elevation in range(nsweeps-1):
        for theta in range(nrays-1):
            for rang in range(ngates-1):
                u_1[elevation, theta, rang] = np.multiply(velocity_radial[elevation, theta+1, rang], math.cos(azimuth[theta] - 1))
                u_2[elevation, theta, rang] = np.multiply(velocity_radial[elevation, theta-1, rang], math.cos(azimuth[theta] + 1))
                u[elevation, theta, rang] = (u_1[elevation, theta, rang] - u_2[elevation, theta, rang]) / float(math.sin(2))

                #print elevation, theta, rang, "\n", u_1[elevation, theta, rang], "\n", u_2[elevation, theta, rang], "\n", u[elevation, theta, rang]

                v_1[elevation, theta, rang] = np.multiply(velocity_radial[elevation, theta-1, rang], math.sin(azimuth[theta] + 1))
                v_2[elevation, theta, rang] = np.multiply(velocity_radial[elevation, theta+1, rang], math.sin(azimuth[theta] - 1))

                v[elevation, theta, rang] = (v_1[elevation,theta,rang] - v_2[elevation,theta,rang]) / float(math.sin(2))
                #print elevation, theta, rang
    return u, v

# def velocity_ca(velocity_radial):
#     """
#     :param velocity_radial:
#     :return:
#     """
#
#     for degree in range(1, 361):
#         ca = velocity_radial[:,degree-1,:]
#         #print velocity_ca
#         #raw_input()
#     return ca


# def velocity_cb(velocity_radial):
#
#     for degree in range(1, 361):
#         if degree != 360:
#             cb = velocity_radial[:,degree+1,:]
#         else:
#             cb = velocity_radial[:,degree,:]
#         #raw_input()
#     return cb
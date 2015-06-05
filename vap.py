__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import math
import numpy as np

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

    velocity_radial = radar.fields['velocity']['data'].reshape(10,360,253)
    azimuth = radar.azimuth['data']

    ca = velocity_ca(radar)
    cb = velocity_cb(radar)

    print azimuth[0]

    for elevation in range(10):
        for theta in range(360):
            for rang in range(253):
                u_1 = velocity_radial[elevation, theta, rang] * math.cos(azimuth[theta] - 1)
                u_2 = velocity_radial[elevation, theta, rang] * math.cos(azimuth[theta] + 1)

                u[theta] = (u_1 - u_2) / (math.sin(2))

                v_1 = velocity_radial[elevation, theta, rang] * math.sin(radar.azimuth['data'][theta] + 1)
                v_2 = velocity_radial[elevation, theta, rang] * math.sin(radar.azimuth['data'][theta] - 1)

                v[theta] = (v_1 - v_2) / (math.sin(2))

    return

def velocity_ca(radar):

    velocity_radial = radar.fields['velocity']['data'].reshape(10,360,253)

    for degree in range(360):
        velocity_ca = velocity_radial

    return


def velocity_cb(radar):
    return


#@profile()
def dic_azimuth_elevation(radar):
    velocity_matrix = radar.fields['velocity']['data']
    elevation_list = ELEVATION_LIST
    range_list = radar.range['data']
    azimuth_list = radar.azimuth['data']


    print elevation_list
    #print matrix_velocity.shape, list_azimuth.shape, list_range.shape, list_elevation.shape

    dera = {elevation_list: {range_list: {azimuth_list: velocity_matrix}}}

    #dic = (dera, radar.fields['velocity']['data'])

    #print dera
    #print a

    #print radar.info()

    return
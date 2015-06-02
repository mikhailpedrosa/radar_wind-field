__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'

import os
import pyart
import math
import numpy as np
import matplotlib.pyplot as plt

ELEVATION_LIST = {
    'X': ["0.5", "1.5", "2.5", "3.5", "4.5", "5.5", "6.5", "7.5", "8.5", "9.5", "10.5", "11.5", "12.5"],
    'S': ["-0.5", "0.0", "0.5", "1.0", "2.0", "3.0", "4.0", "5.5", "7.0", "8.5"],
}

def plot_image(radar):
    """
    Funcao para Plotar Imagem do Radar
    Plot function for Radar Image
    :param localdir: Directory of PyFuncemeClimateTools - Diretorio do PyFuncemeClimateTools
    :param radar: Radar Object - Objeto Radar
    :return:
    """

    #create the plot using RadarMapDisplay
    display = pyart.graph.RadarMapDisplay(radar)
    display.plot_ppi_map('velocity', 0, vmin=-10., vmax=10.,
                         min_lat=-9.6, max_lat=-0.9,
                         max_lon=325.5, min_lon=316.,
                         lat_lines=radar.latitude['data'],
                         lon_lines=radar.longitude['data'])
    display.plot_range_rings([100., 200., 300., 400.])
    display.plot_point(radar.longitude['data'][0], radar.latitude['data'][0])
    #plt.show()
    #plt.close()
    plt.savefig('Radar_Quixeramobim_Band_S - Product VAP.png', format='png')


def plot_graph(radar):

    y = radar.azimuth['data'].reshape(10,360)
    v = radar.fields['velocity']['data'].reshape(10,360,253)
    x = v[2,:,100]

    plt.plot(y[2,:], x, lw=1)
    plt.ylim(-25,25)
    plt.show()
    #plt.savefig('Radar_Quixeramobim_Band_S - Velocity X Azimuth.png', format='png')


def read_radar():
    """
    Leitura do arquivo bruto (Sigmet) do Radar
    Reading the raw file (Sigmet) Radar
    :return: Radar object with all its features - Objeto Radar com todas as suas Caracteristicas
    """
    filename = 'XXX140331061059.RAW1JMJ'
    local_dir = os.path.dirname(__file__)
    radar = pyart.io.read_sigmet(filename)

    return radar


def vap(radar):
    """
    Implementacao da tecnica de Processamento VAP (Velocity-Azimuth Processing)
    Implementation of the technical processing of VAP (Velocity-Azimuth Processing)
    :param radar: Radar object - Objeto Radar
    :return:
    """
    #The horizontal wind components u and v
    u = np.zeros(3600)
    v = np.zeros(3600)
    for i in range(len(radar.azimuth['data'])):

        #radar.azimuth['data'][i+1] - radar.azimuth['data'][i] = 1
        u_1 = 1 * math.cos(radar.azimuth['data'][i] - 1)
        u_2 = 1 * math.cos(radar.azimuth['data'][i] + 1)
        u[i] = (u_1 - u_2) / (math.sin(2))

        v_1 = 1 * math.sin(radar.azimuth['data'][i] + 1)
        v_2 = 1 * math.sin(radar.azimuth['data'][i] - 1)
        v[i] = (v_1 - v_2) / (math.sin(2))

    return

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


if __name__ == '__main__':
    radar = read_radar()
    #print radar.info()
    a =  radar.fields['velocity']['data'].reshape(10,360,253)
    #print a[0,:,0]
    #exit()
    #plot_image(radar)
    plot_graph(radar)

    #dic_azimuth_elevation(radar)
    #vap(radar)

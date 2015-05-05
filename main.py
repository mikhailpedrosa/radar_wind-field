__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'

import os
import pyart
import math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

__file__ = "/usr/local/lib/python2.7/dist-packages/PyFuncemeClimateTools/"

def plotImage(radar, localdir):
    """
    Funcao para Plotar Imagem do Radar
    :param radar: Objeto Radar
    :return:
    """

    # map = Basemap(projection='cyl',
    #               llcrnrlat=-9.6,
    #               urcrnrlat=-0.9,
    #               llcrnrlon=316.,
    #               urcrnrlon=325.5,
    #               resolution='l')
    # map.drawcountries(linewidth=0.4)
    # map.drawcoastlines(linewidth=0.4)
    # map.drawstates(linewidth=0.4)
    #
    # map.readshapefile(localdir + '/shp/ceara', 'world', drawbounds=True, linewidth=.5, color='k')

    #create the plot using RadarMapDisplay (recommended method)
    display = pyart.graph.RadarMapDisplay(radar)
    display.plot_ppi_map('velocity', 0, vmin=-10., vmax=10.,
                         min_lat=-9.6, max_lat=-0.9,
                         max_lon=325.5, min_lon=316.,
                         lat_lines=radar.latitude['data'],
                         lon_lines=radar.longitude['data'])
    display.plot_range_rings([100., 200., 300., 400.])
    display.plot_point(radar.longitude['data'][0], radar.latitude['data'][0])
    plt.show()
    #plt.savefig('Radar_Quixeramobim_Band_S - Product VAP.png', format='png')

def read_radar():
    """
    Leitura do arquivo bruto (Sigmet) do Radar
    :return: Objeto Radar com todas as suas Caracteristicas
    """
    filename = 'XXX140331061059.RAW1JMJ'
    local_dir = os.path.dirname(__file__)
    radar = pyart.io.read_sigmet(filename)

    return radar


def vap(radar):
    """
    Implementacao da tecnica de Processamento VAP (Velocity-Azimuth Processing)
    :param radar:
    :return:
    """

    #The horizontal wind components u and v
    u, v = []
    for teta in range(len(radar.azimuth['data'])):
        u_1 = 1 * math.cos(radar.azimuth['data'][teta] - (radar.azimuth['data'][teta] - radar.azimuth['data'][teta+1]))
        u_2 = 1 * math.cos(radar.azimuth['data'][teta] + (radar.azimuth['data'][teta] - radar.azimuth['data'][teta+1]))
        u_3 = math.sin((2 * (radar.azimuth['data'][teta] - radar.azimuth['data'][teta+1])))
        u[teta] = (u_1 - u_2) / u_3

        v_1 = 1 * math.sin(radar.azimuth['data'][teta] + (radar.azimuth['data'][teta] - radar.azimuth['data'][teta+1]))
        v_2 = 1 * math.sin(radar.azimuth['data'][teta] - (radar.azimuth['data'][teta] - radar.azimuth['data'][teta+1]))
        v_3 = math.sin((2 * (radar.azimuth['data'][teta] - radar.azimuth['data'][teta+1])))
        v[teta] = (v_1 - v_2) / v_3


    return


if __name__ == '__main__':
    radar = read_radar()
    #vap(radar)
    plotImage(radar, __file__)

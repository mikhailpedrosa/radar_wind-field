__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import matplotlib.pyplot as plt
import pyart
from mpl_toolkits.basemap import Basemap

__file__ = "/usr/local/lib/python2.7/dist-packages/PyFuncemeClimateTools/"

def plotImage(radar):
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
                           min_lon=-316., max_lon=325.5,
                           min_lat=-0.9, max_lat=9.6,
                           lat_0=radar.latitude['data'][0],
                           lon_0=radar.longitude['data'][0])

    # display.plot_ppi_map('velocity', 0, vmin=-5., vmax=5.,
    #                      lat_0=radar.latitude['data'][0],
    #                      lon_0=radar.longitude['data'][0])

    display.plot_point(radar.longitude['data'][0], radar.latitude['data'][0])
    plt.show()


def read_radar():
    """
    Leitura do arquivo bruto (Sigmet) do Radar
    :return: Objeto Radar com todas as suas Caracteristicas
    """
    filename = 'XXX140331061059.RAW1JMJ'
    radar = pyart.io.read_sigmet(filename)

    return radar


def vap(radar):
    """
    Implementacao da tecnica de Processametno VAP (Velocity-Azimuth Processing)
    :param radar:
    :return:
    """

    return


if __name__ == '__main__':
    radar = read_radar()
    vap(radar)
    plotImage(radar)

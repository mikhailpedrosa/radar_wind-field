__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import pyart
import matplotlib.pyplot as plt
from memory_profiler import profile

#@profile()
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

#@profile()
def plot_graph(radar):

    azimuth = radar.azimuth['data'].reshape(10,360)
    velocity = radar.fields['velocity']['data'].reshape(10,360,253)

    y = velocity[2,:,1]
    x = azimuth[2,:]

    figure = plt.figure()
    ax = figure.add_subplot(111)
    plt.plot(x, y, lw=1, label='Raw Vr')

    ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_color('none')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    plt.grid()
    plt.ylim(-20,20)
    plt.xlim(0,360)
    plt.title("Radar Quixeramobim - Velocity x Azimuth", fontstyle='italic')
    plt.ylabel('Velocity (m/s)')
    ax.set_xlabel('Azimuth (degree)')
    ax.xaxis.set_label_coords(0.5,-0.05)
    plt.legend(fontsize='10')
    #plt.show()
    #plt.close()
    plt.savefig('Radar_Quixeramobim_Band_S - Velocity X Azimuth.png', format='png')
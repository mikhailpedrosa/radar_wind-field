__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Methods for Plot Images, Vector and Graphs'
__version__ = '0.1'
__date__ = '13/04/2015'

import pyart
import matplotlib.pyplot as plt
from filters import *
from memory_profiler import profile


#@profile()
def plot_image_no_map(radar):
    """
    Funcao para Plotar Imagem do Radar
    Plot function for Radar Image
    :param localdir: Directory of PyFuncemeClimateTools - Diretorio do PyFuncemeClimateTools
    :param radar: Radar Object - Objeto Radar
    :return:
    """

    #create the plot using RadarDisplay
    display = pyart.graph.RadarDisplay(radar)
    display.plot('velocity', 0, vmin=-35., vmax=35.)

    # axislabels = '#000066', '#14217A', '#20398A', '#2D519B', '#3B6BAC', '#4A85BE', '#59A0D0', '#66B7E0', '#75D2F2', '#FFFFFF',
    #             '#FFEA00', '#FFCC00', '#FFB600', '#FF9900', '#FF7E00', '#FF6600', '#FF4900', '#FF3300', '#FF0000'

    #display.plot_colorbar(field= ['#000066', '#20398A', '#3B6BAC', '#59A0D0', '#66B7E0', '#75D2F2', '#FFFFFF', '#FFEA00', '#FFCC00', '#FFB600', '#FF7E00', '#FF4900', '#FF0000'])

    display.plot_range_rings([100., 200., 300., 400.])
    #display.plot_cross_hair(radar.latitude['data'], radar.longitude['data'] )
    #display.plot_point(radar.longitude['data'][0], radar.latitude['data'][0])
    #plt.show()
    plt.savefig('Radar_Qxb_Band_S - Image Velocity Wind (No Map).png', format='png')
    plt.close()


#@profile()
def plot_graph_points_no_filters(radar, r):

    azimuth = radar.azimuth['data'].reshape(10,360)
    velocity = radar.fields['velocity']['data'].reshape(10,360,253)

    y = velocity[2,:,r]
    x = azimuth[2, :]

    figure = plt.figure()
    ax = figure.add_subplot(111)

    plt.scatter (x, y, label='Raw Vr' )

    ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_color('none')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    plt.grid()
    plt.ylim(-35.,35.)
    plt.xlim(0,360)
    plt.title("Radar Quixeramobim - Velocity x Azimuth - ({:.2f} km Range)".format((r*1490)/1000.), fontstyle='italic')
    plt.ylabel('Velocity (m/s)')
    ax.set_xlabel('Azimuth (degree)')
    ax.xaxis.set_label_coords(0.5,-0.05)
    plt.legend(fontsize='10')
    #plt.show()
    plt.savefig("Radar_Qxb_Band_S - Velocity x Azimuth - ({:.2f} km Range) - Points (No Filter).png".format((r*1490)/1000.), format='png')
    plt.close()

#@profile()
def plot_graph_lines_no_filters(radar, r):

    azimuth = radar.azimuth['data'].reshape(10,360)
    velocity = radar.fields['velocity']['data'].reshape(10,360,253)

    y = velocity[2,:,r]
    x = azimuth[2, :]

    figure = plt.figure()
    ax = figure.add_subplot(111)

    plt.plot(x, y, lw='1', label='Raw Vr')

    ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_color('none')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    plt.grid()
    plt.ylim(-35.,35.)
    plt.xlim(0,360)
    plt.title("Radar Quixeramobim - Velocity x Azimuth ({:.2f} km Range)".format((r*1490)/1000.), fontstyle='italic')
    plt.ylabel('Velocity (m/s)')
    ax.set_xlabel('Azimuth (degree)')
    ax.xaxis.set_label_coords(0.5,-0.05)
    plt.legend(fontsize='10')
    #plt.show()
    plt.savefig('Radar_Qxb_Band_S - Velocity x Azimuth ({:.2f} km Range) - Line (No Filter).png'.format((r*1490)/1000.), format='png')
    plt.close()


#@profile()
def plot_vector_no_filters(radar, r, u, v):
    azimuth =  radar.azimuth['data'].reshape(10,360)
    rang = radar.range['data']
    velocity_radial = radar.fields['velocity']['data'].reshape(10,360,253)

    theta, ran = np.meshgrid(azimuth[3,:], rang[r])

    figure = plt.figure()
    plt.subplot(111, polar=True)
    plt.quiver(theta, ran, u[3,:,r], v[3,:,r], velocity_radial[3,:,r])
    #plt.barbs(theta, ran, u[3,:,r], v[3,:,r], velocity_radial[3,:,r])
    plt.tight_layout()
    plt.show()
    plt.close()


#@profile()
def plot_image_map(radar):
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
    plt.show()
    plt.savefig("Radar_Qxb_Band_S - Image Velocity Wind.png", format='png')
    plt.close()


#@profile()
def plot_graph_points_filters(radar, r):

    azimuth = radar.azimuth['data'].reshape(10,360)
    velocity = radar.fields['velocity']['data'].reshape(10,360,253)

    y = velocity[2,:,r]
    x = azimuth[2, :]

    y = moving_average(y,2)

    figure = plt.figure()
    ax = figure.add_subplot(111)
    plt.scatter (x, y, label='Raw Vr' )

    ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_color('none')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    plt.grid()
    plt.ylim(-35.,35.)
    plt.xlim(0,360)
    plt.title("Radar Quixeramobim - Velocity x Azimuth ({:.2f} km Range)".format((r*1490)/1000.), fontstyle='italic')
    plt.ylabel('Velocity (m/s)')
    ax.set_xlabel('Azimuth (degree)')
    ax.xaxis.set_label_coords(0.5,-0.05)
    plt.legend(fontsize='10')
    #plt.show()
    plt.savefig("Radar_Qxb_Band_S - Velocity x Azimuth - ({:.2f} km Range) - Points.png".format((r*1490)/1000.), format='png')
    plt.close()

#@profile()
def plot_graph_lines_filters(radar, r):

    azimuth = radar.azimuth['data'].reshape(10,360)
    velocity = radar.fields['velocity']['data'].reshape(10,360,253)

    y = velocity[2,:,r]
    x = azimuth[2, :]

    #y = moving_average(y,3)
    y = gauss(y,3)
    #y = median(y,3)

    figure = plt.figure()
    ax = figure.add_subplot(111)
    plt.plot(x, y, lw='1', label='Raw Vr')

    ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_color('none')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    plt.grid()
    plt.ylim(-35.,35.)
    plt.xlim(0,360)
    plt.title("Radar Quixeramobim - Velocity x Azimuth ({:.2f} km Range)".format((r*1490)/1000.), fontstyle='italic')
    plt.ylabel('Velocity (m/s)')
    ax.set_xlabel('Azimuth (degree)')
    ax.xaxis.set_label_coords(0.5,-0.05)
    plt.legend(fontsize='10')
    #plt.show()
    plt.savefig("Radar_Qxb_Band_S - Velocity x Azimuth - ({:.2f} km Range) - Line.png".format((r*1490)/1000.), format='png')
    plt.close()

#@profile()
def plot_vector_filters(radar, r, u, v):
    azimuth =  radar.azimuth['data'].reshape(10,360)
    rang = radar.range['data']
    velocity_radial = radar.fields['velocity']['data'].reshape(10,360,253)

    theta, ran = np.meshgrid(azimuth[3,:], rang[r])

    y = moving_average(velocity_radial, 3)

    figure = plt.figure()
    figure.add_subplot(111, polar=True)
    #x = (1 * math.cos(theta)) - (1 * math.sin(theta))
    #y = (1 * math.sin(theta))  + (1 * math.cos(theta))
    #q = ax.quiver(theta, r, x, y)

    plt.quiver(theta, ran, u[3,:,r], v[3,:,r], velocity_radial[3,:,r])
    #plt.barbs(theta, r, u[3,:,135], v[3,:,135], velocity_radial[3,:,135])
    #plt.show()
    #plt.close()
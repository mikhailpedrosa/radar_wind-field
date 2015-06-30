__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import datetime
from read import read_radar
from graphical import *
from vap import vap

if __name__ == '__main__':

    print "----Velocity-Azimuth Processing Technique----"

    #Range (1-253)
    r = 1

    radar = read_radar()
    start = datetime.datetime.now()
    #u, v = vap(radar)
    #np.save('vectoru', u)
    #np.save('vectorv', v)
    u1 = np.load('vectoru.npy')
    v1 = np.load('vectorv.npy')
    dif = datetime.datetime.now() - start
    print '%i s' % dif.seconds
    #plot_image_no_map(radar)
    #plot_image_map(radar)
    #plot_graph_lines_no_filters(radar, r)
    #plot_graph_points_no_filters(radar, r)
    #plot_graph_lines_filters(radar, r)
    #plot_graph_points_filters(radar, r)
    plot_graph(radar, r)
    #plot_vector_quiver(radar, r, u1, v1)
    #plot_vector_barbs(radar, r, u, v)
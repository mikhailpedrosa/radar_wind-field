__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com> e Arthur Costa <arthur.opa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import datetime
import os
from graphical import *
from vap import *

#@profile()
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

if __name__ == '__main__':
    start = datetime.datetime.now()
    radar = read_radar()
    a =  radar.fields['velocity']['data'].reshape(10,360,253)
    #print a[0,:,0]
    #exit()
    #vap(radar)
    #dic_azimuth_elevation(radar)
    #plot_image(radar)
    plot_graph_points(radar)
    plot_graph_lines(radar)
    dif = datetime.datetime.now() - start
    print '%i s' % dif.seconds



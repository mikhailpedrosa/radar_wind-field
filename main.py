__author__ = 'mikhail pedrosa'

__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import matplotlib.pyplot as plt
import pyart

def main():
    filename = 'XXX140331061059.RAW1JMJ'

    # create the plot using RadarDisplay (recommended method)
    radar = pyart.io.read(filename)
    display = pyart.graph.RadarDisplay(radar)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    display.plot('reflectivity', 0, vmin=-32, vmax=64.)
    display.plot_range_rings([100, 200, 300, 400])
    display.plot_cross_hair(5.)
    plt.show()

if __name__ == '__main__':
    main()
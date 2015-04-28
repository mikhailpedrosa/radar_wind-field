__author__ = 'mikhail pedrosa'

__author__ = 'Mikhail Pedrosa <mikhailj.pedrosa@gmail.com>'
__description__ = 'Single-Doppler Radar Wind-Field Retrieval Experiment On a Qualified Velocity-Azimuth Processing Technique'
__version__ = '0.1'
__date__ = '13/04/2015'


import matplotlib.pyplot as plt
import pyart

def plotImage(radar):
    display = pyart.graph.RadarMapDisplay(radar)
    # display.plot_ppi_map('spectrum_width', 0, vmin=-5., vmax=5.,
    #                        min_lon=-316., max_lon=324,
    #                        min_lat=-0.9, max_lat=9.,
    #                        lat_0=radar.latitude['data'][0],
    #                        lon_0=radar.longitude['data'][0])
    display.plot_ppi_map('spectrum_width', 0, vmin=-5., vmax=5.,
                         lat_0=radar.latitude['data'][0],
                         lon_0=radar.longitude['data'][0])
    #display.plot_range_ring(200., line_style='k--')
    #display.plot_line_xy(radar.longitude['data'][0], radar.latitude['data'][0], line_style='k-')
    display.plot_point(radar.longitude['data'][0], radar.latitude['data'][0])
    plt.show()

def main():
    filename = 'XXX140331061059.RAW1JMJ'
    radar = pyart.io.read(filename)
     # create the plot using RadarMapDisplay (recommended method)
    plotImage(radar)

if __name__ == '__main__':
    main()
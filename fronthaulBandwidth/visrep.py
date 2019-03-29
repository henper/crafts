'''
Created on Mar 29, 2019

@author: eponhik
'''
from model.highband import Highband
import matplotlib.pyplot as mat

if __name__ == '__main__':
        
    iqFormats = range(4, 32)
    
    grossBandwidths = list()
    netBandwidths = list()
    
    for iqFormat in iqFormats:
        hb = Highband(iqFormat=iqFormat)
        grossBandwidths.append(hb.calcGrossBandwidth())
        netBandwidths.append(hb.calcNetFronthaulBw())
    
    mat.scatter(iqFormats, grossBandwidths, label='Unaware')
    mat.plot(iqFormats, netBandwidths, label='Aware')
    
    mat.title('Net bandwidth usage, TDD Awareness')
    mat.xlabel('IQ Format [bits]')
    mat.ylabel('Bandwidth [bits/s]')
    
    mat.plot()
    mat.legend()
    mat.show()
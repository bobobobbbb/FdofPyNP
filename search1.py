#!~/Desktop/Reporsitories/ENV3/bin python3
#FDofPyNP

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address[0].coordinates)    
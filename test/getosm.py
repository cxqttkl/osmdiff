#!/usr/bin/env python

from osmdiff import OSMChange, AugmentedDiff
from osmdiff.osm import Node, Way, Relation
import  time


def sleeptime(hour, min, sec):
    return hour*3600 + min*60 + sec;
_interval = sleeptime(0,1,0)


debug = True

# r = OSMChange(debug=debug)
# r.get_state()
# r.retrieve()
#
# print(r)
# 2、中国的经纬度范围大约为：纬度3.86~53.55，经度73.66~135.05

while 1==1:

    a = AugmentedDiff(
        minlon=119,
        minlat=22,
        maxlon=124,
        maxlat=26,
        debug=debug)
    a.get_state()
    a.retrieve()
    print(a)
    time.sleep(_interval)


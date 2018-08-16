#!/bin/env python
# encoding=utf8

import os
import ez.lib.ezShapefile as shapefile
import create_tiles


def create_shapefile_latlon(fd, extent, level):
    fn = os.path.join(fd, '%d_%f_%f_%f_%f'%(level,extent[0],extent[1],extent[2],extent[3]))
    wr = shapefile.writer(fn, shapefile.Polygon)
    wr.addField("id")
    wr.addField("url", length=80)
    for tile in create_tiles.create_google_tiles_lonlat(extent, level):
        lon_min, lon_max, lat_min, lat_max = tile[-1]
        wr.shapePolygon([((lon_min,lat_min),(lon_min,lat_max),(lon_max,lat_max),(lon_max,lat_min),(lon_min,lat_min))])
        col, row = tile[0], tile[1]
        url = "http://mt2.google.cn/vt/lyrs=m&hl=zh-CN&gl=cn&x=%d&y=%d&z=%d"%(col, row, level)
        wr.record(('%d_%d'%(col, row), url))
    wr.close()


if __name__ == '__main__':
    fd = r'D:\tmp\tmp'

    extent = -180, 180, -85.05112877980656, 85.05112877980656
    for level in range(8):
        create_shapefile_latlon(fd, extent, level)

    extent = 116.375, 116.5, 39.91667, 40
    for level in range(11, 18):
        create_shapefile_latlon(fd, extent, level)

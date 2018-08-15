#!/bin/env python
# encoding=utf8

from pyproj import Proj

proj_webmercator = Proj(init='epsg:3857')


class Tile:

    def __init__(self, row, col, level):
        pass

    def bbox(self):
        pass

    def center(self):
        pass



def lonlat_to_xy(lon, lat):
    global proj_webmercator
    return proj_webmercator(lon, lat)


def xy_to_lonlat(x, y):
    global proj_webmercator
    return proj_webmercator(x, y, inverse=True)


def create_google_tiles_web(extent, level):
    #todo: international latlon and xy sequence
    #left_bottom = pj(min_lon, min_lat, inverse=True)
    print(extent, level)


def create_google_tiles_latlon(extent, level):
    #todo: international latlon and xy sequence
    print(extent, level)
    min_lat, max_lat, min_lon, max_lon = extent
    pj = Proj(init='epsg:3857')
    #latlons = [(min_lat,min_lon), (max_lat,min_lon), (max_lat,max_lon), (min_lat,max_lon)]
    lonlats = [(min_lon,min_lat), (min_lon,max_lat), (max_lon,max_lat), (max_lon,min_lat)]
    xys = [lonlat_to_xy(lon,lat) for lon,lat in lonlats]
    print(xys)
    xs = [x for x,y in xys]
    ys = [y for x,y in xys]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    create_google_tiles_web((min_x, max_x, min_y, max_y), level)

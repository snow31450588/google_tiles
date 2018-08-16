#!/bin/env python
# encoding=utf8

from pyproj import Proj

proj_webmercator = Proj(init='epsg:3857')


def lonlat_to_xy(lon, lat):
    global proj_webmercator
    return proj_webmercator(lon, lat)


def xy_to_lonlat(x, y):
    global proj_webmercator
    return proj_webmercator(x, y, inverse=True)


FULL_WIDTH = 20037508.3427892*2

def web_to_index(web, level):
    #web = FULL_WIDTH/2 - web
    level_span = FULL_WIDTH/(2**level)
    index = int(web/level_span)
    index = min(index, 2**level-1)
    return index


def cell_to_extent(row, col, level):
    level_span = FULL_WIDTH/(2**level)
    x_min = col*level_span
    x_max = (col+1)*level_span
    y_min = row*level_span
    y_max = (row+1)*level_span
    return x_min, x_max, y_min, y_max


def cell_to_extent_web(row, col, level):
    level_span = FULL_WIDTH/(2**level)
    x_min = col*level_span
    x_max = (col+1)*level_span
    y_min = row*level_span
    y_max = (row+1)*level_span
    return x_min - FULL_WIDTH/2, x_max - FULL_WIDTH/2, y_min - FULL_WIDTH/2, y_max - FULL_WIDTH/2


def cell_to_extent_lonlat(row, col, level):
    x_min, x_max, y_min, y_max = cell_to_extent(row, col, level)
    lon_min, lat_min = xy_to_lonlat(x_min - FULL_WIDTH/2, FULL_WIDTH/2 - y_min)
    lon_max, lat_max = xy_to_lonlat(x_max - FULL_WIDTH/2, FULL_WIDTH/2 - y_max)
    return lon_min, lon_max, lat_max, lat_min


def create_google_tiles_web(extent, level):
    x_min, x_max, y_min, y_max = extent
    col_min = web_to_index(x_min + FULL_WIDTH/2, level)
    col_max = web_to_index(x_max + FULL_WIDTH/2, level)
    row_min = web_to_index(FULL_WIDTH/2-y_max, level)
    row_max = web_to_index(FULL_WIDTH/2-y_min, level)
    return [(col, row, cell_to_extent_lonlat(row,col,level)) for row in range(row_min,row_max+1) for col in range(col_min,col_max+1)]


def create_google_tiles_lonlat(extent, level):
    lon_min, lon_max, lat_min, lat_max = extent
    x_min, y_min = lonlat_to_xy(lon_min, lat_min)
    x_max, y_max = lonlat_to_xy(lon_max, lat_max)
    return create_google_tiles_web((x_min, x_max, y_min, y_max), level)

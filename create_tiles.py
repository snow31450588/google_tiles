#!/bin/env python
# encoding=utf8

from pyproj import Proj

HALF_WIDTH = 20037508.3427892
FULL_WIDTH = HALF_WIDTH * 2
proj_webmercator = Proj(init='epsg:3857')

def lnglat_to_web(lng, lat):
    x, y = proj_webmercator(lng, lat)
    x += HALF_WIDTH
    y = HALF_WIDTH - y
    return x, y

def web_to_lnglat(x, y):
    x -= HALF_WIDTH
    y = HALF_WIDTH - y
    return proj_webmercator(x, y, inverse=True)

def _web_to_index(level, web):
    level_span = FULL_WIDTH/(2**level)
    index = int(web/level_span)
    index = min(index, 2**level-1)
    index = max(index, 0)
    return index

def cell_to_extent_web(level, col, row):
    level_span = FULL_WIDTH/(2**level)
    x_min = col*level_span
    x_max = (col+1)*level_span
    y_min = row*level_span
    y_max = (row+1)*level_span
    return x_min, x_max, y_min, y_max

def cell_to_extent_lnglat(level, col, row):
    x_min, x_max, y_min, y_max = cell_to_extent_web(level, col, row)
    lng_min, lat_min = web_to_lnglat(x_min, y_max)
    lng_max, lat_max = web_to_lnglat(x_max, y_min)
    return lng_min, lng_max, lat_min, lat_max

def create_google_tiles_web(level, extent):
    x_min, x_max, y_min, y_max = extent
    col_min = _web_to_index(level, x_min)
    col_max = _web_to_index(level, x_max)
    row_min = _web_to_index(level, y_min)
    row_max = _web_to_index(level, y_max)
    return [(col, row, cell_to_extent_lnglat(level,col,row)) for row in range(row_min,row_max+1) for col in range(col_min,col_max+1)]

def create_google_tiles_lnglat(level, extent):
    lng_min, lng_max, lat_min, lat_max = extent
    x_min, y_min = lnglat_to_web(lng_min, lat_max)
    x_max, y_max = lnglat_to_web(lng_max, lat_min)
    return create_google_tiles_web(level, (x_min, x_max, y_min, y_max))


def web_to_cell(x, y, level):
    col = _web_to_index(level, x)
    row = _web_to_index(level, y)
    return col, row

def lnglat_to_cell(lng, lat, level):
    x, y = lnglat_to_web(lng, lat)
    return web_to_cell(x, y, level)

def web_to_vertex(x, y, level, col, row):
    x_min, x_max, y_min, y_max = cell_to_extent_web(row, col, level)
    x *= 4096/(x_max-x_min)
    y *= 4096/(y_max-y_min)
    return int(x), int(y)

def lnglat_to_vertex(lng, lat, level, col, row):
    x, y = lnglat_to_web(lng, lat)
    return web_to_vertex(x, y, level, col, row)

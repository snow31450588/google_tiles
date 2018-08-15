#!/bin/env python
# encoding=utf8

import unittest
import create_tiles


class create_tiles_Test(unittest.TestCase):

    def setUp(self):
        self.lat_min = -85.05112877980656
        self.lon_min = -180
        self.lat_max = 85.05112877980656
        self.lon_max = 180
        self.x_min = -20037508.3427892
        self.y_min = -20037508.3427892
        self.x_max = 20037508.3427892
        self.y_max = 20037508.3427892


    def test_latlon_to_xy_leftbottom(self):
        x_min, y_min = create_tiles.lonlat_to_xy(self.lon_min, self.lat_min)
        self.assertAlmostEqual(x_min, self.x_min, msg="x value is not correct")
        self.assertAlmostEqual(y_min, self.y_min, msg="y value is not correct")


    def test_latlon_to_xy_lefttop(self):
        x_min, y_max = create_tiles.lonlat_to_xy(self.lon_min, self.lat_max)
        self.assertAlmostEqual(x_min, self.x_min, msg="x value is not correct")
        self.assertAlmostEqual(y_max, self.y_max, msg="y value is not correct")


    def test_latlon_to_xy_rightbottom(self):
        x_max, y_min = create_tiles.lonlat_to_xy(self.lon_max, self.lat_min)
        self.assertAlmostEqual(x_max, self.x_max, msg="x value is not correct")
        self.assertAlmostEqual(y_min, self.y_min, msg="y value is not correct")


    def test_latlon_to_xy_righttop(self):
        x_max, y_max = create_tiles.lonlat_to_xy(self.lon_max, self.lat_max)
        self.assertAlmostEqual(x_max, self.x_max, msg="x value is not correct")
        self.assertAlmostEqual(y_max, self.y_max, msg="y value is not correct")


    def test_latlon_to_xy_center(self):
        x, y = create_tiles.lonlat_to_xy(0, 0)
        self.assertAlmostEqual(x, 0, msg="x value is not correct")
        self.assertAlmostEqual(y, 0, msg="y value is not correct")


    def test_xy_to_latlon_leftbottom(self):
        lon_min, lat_min = create_tiles.xy_to_lonlat(self.x_min, self.y_min)
        self.assertAlmostEqual(lon_min, self.lon_min, msg="lon value is not correct")
        self.assertAlmostEqual(lat_min, self.lat_min, msg="lat value is not correct")


    def test_xy_to_latlon_lefttop(self):
        lon_min, lat_max = create_tiles.xy_to_lonlat(self.x_min, self.y_max)
        self.assertAlmostEqual(lon_min, self.lon_min, msg="lon value is not correct")
        self.assertAlmostEqual(lat_max, self.lat_max, msg="lat value is not correct")


    def test_xy_to_latlon_rightbottom(self):
        lon_max, lat_min = create_tiles.xy_to_lonlat(self.x_max, self.y_min)
        self.assertAlmostEqual(lon_max, self.lon_max, msg="lon value is not correct")
        self.assertAlmostEqual(lat_min, self.lat_min, msg="lat value is not correct")


    def test_xy_to_latlon_righttop(self):
        lon_max, lat_max = create_tiles.xy_to_lonlat(self.x_max, self.y_max)
        self.assertAlmostEqual(lon_max, self.lon_max, msg="lon value is not correct")
        self.assertAlmostEqual(lat_max, self.lat_max, msg="lat value is not correct")


    def test_xy_to_latlon_center(self):
        lon, lat = create_tiles.xy_to_lonlat(0, 0)
        self.assertAlmostEqual(lon, 0, msg="lon value is not correct")
        self.assertAlmostEqual(lat, 0, msg="lat value is not correct")


    def test_create_google_tiles_web(self):
        self.assertTrue(False, "Not implemented!")


    def test_create_google_tiles_latlon(self):
        #extent = self.lat_min, self.lat_max, self.lon_min, self.lon_max
        #create_tiles.create_google_tiles_latlon(extent, 17)
        self.assertTrue(False, "Not implemented!")


if __name__ == '__main__':
    unittest.main(verbosity=2)

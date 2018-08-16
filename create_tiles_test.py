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


    def test_web_to_index(self):
        index = create_tiles.web_to_index(0, 0)
        self.assertEqual(0, index)
        index = create_tiles.web_to_index(-20037508.3427892, 0)
        self.assertEqual(0, index)
        index = create_tiles.web_to_index(20037508.3427892, 0)
        self.assertEqual(0, index)


    def test_cell_to_extent_web(self):
        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(0, 0, 1)
        self.assertAlmostEqual(-20037508.3427892, x_min)
        self.assertAlmostEqual(0, x_max)
        self.assertAlmostEqual(-20037508.3427892, y_min)
        self.assertAlmostEqual(0, y_max)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(0, 1, 1)
        self.assertAlmostEqual(0, x_min)
        self.assertAlmostEqual(20037508.3427892, x_max)
        self.assertAlmostEqual(-20037508.3427892, y_min)
        self.assertAlmostEqual(0, y_max)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(1, 0, 1)
        self.assertAlmostEqual(-20037508.3427892, x_min)
        self.assertAlmostEqual(0, x_max)
        self.assertAlmostEqual(0, y_min)
        self.assertAlmostEqual(20037508.3427892, y_max)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(1, 1, 1)
        self.assertAlmostEqual(0, x_min)
        self.assertAlmostEqual(20037508.3427892, x_max)
        self.assertAlmostEqual(0, y_min)
        self.assertAlmostEqual(20037508.3427892, y_max)


    def test_cell_to_extent_lonlat(self):
        lon_min, lon_max, lat_min, lat_max = create_tiles.cell_to_extent_lonlat(0, 0, 1)
        self.assertAlmostEqual(-180, lon_min)
        self.assertAlmostEqual(0, lon_max)
        self.assertAlmostEqual(0, lat_min)
        self.assertAlmostEqual(85.05112877980656, lat_max)

        lon_min, lon_max, lat_min, lat_max = create_tiles.cell_to_extent_lonlat(0, 1, 1)
        self.assertAlmostEqual(0, lon_min)
        self.assertAlmostEqual(180, lon_max)
        self.assertAlmostEqual(0, lat_min)
        self.assertAlmostEqual(85.05112877980656, lat_max)

        lon_min, lon_max, lat_min, lat_max = create_tiles.cell_to_extent_lonlat(1, 0, 1)
        self.assertAlmostEqual(-180, lon_min)
        self.assertAlmostEqual(0, lon_max)
        self.assertAlmostEqual(-85.05112877980656, lat_min)
        self.assertAlmostEqual(0, lat_max)

        lon_min, lon_max, lat_min, lat_max = create_tiles.cell_to_extent_lonlat(1, 1, 1)
        self.assertAlmostEqual(0, lon_min)
        self.assertAlmostEqual(180, lon_max)
        self.assertAlmostEqual(-85.05112877980656, lat_min)
        self.assertAlmostEqual(0, lat_max)


    def test_create_google_tiles_web_level0(self):
        self.assertTrue(False, "Not implemented!")


    def test_create_google_tiles_latlon_level0(self):
        extent = self.lon_min, self.lon_max, self.lat_min, self.lat_max
        tiles = create_tiles.create_google_tiles_lonlat(extent, 0)
        self.assertEqual(1, len(tiles), "level 0 has %d tiles"%len(tiles))


    def test_create_google_tiles_latlon_level1(self):
        extent = self.lon_min, self.lon_max, self.lat_min, self.lat_max
        tiles = create_tiles.create_google_tiles_lonlat(extent, 1)
        self.assertEqual(4, len(tiles), "level 1 has %d tiles"%len(tiles))


    def test_create_google_tiles_latlon_level17(self):
        extent = self.lon_min, self.lon_max, self.lat_min, self.lat_max
        #tiles = create_tiles.create_google_tiles_lonlat(extent, 17)
        #self.assertEqual(1, len(tiles), "level 17 has %d tiles"%len(tiles))
        self.assertTrue(False, "Not implemented!")




if __name__ == '__main__':
    unittest.main(verbosity=2)

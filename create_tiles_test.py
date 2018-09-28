#!/bin/env python
# encoding=utf8

import unittest
import create_tiles

LAT_MAX = 85.05112877980656
WIDTH = 20037508.3427892

class create_tiles_Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_latlon_to_xy_leftbottom(self):
        x, y = create_tiles.lnglat_to_web(-180, -LAT_MAX)
        self.assertAlmostEqual(x, 0, msg="x value is not correct")
        self.assertAlmostEqual(y, WIDTH*2, msg="y value is not correct")

    def test_latlon_to_xy_lefttop(self):
        x, y = create_tiles.lnglat_to_web(-180, LAT_MAX)
        self.assertAlmostEqual(x, 0, msg="x value is not correct")
        self.assertAlmostEqual(y, 0, msg="y value is not correct")

    def test_latlon_to_xy_rightbottom(self):
        x, y = create_tiles.lnglat_to_web(180, -LAT_MAX)
        self.assertAlmostEqual(x, WIDTH*2, msg="x value is not correct")
        self.assertAlmostEqual(y, WIDTH*2, msg="y value is not correct")

    def test_latlon_to_xy_righttop(self):
        x, y = create_tiles.lnglat_to_web(180, LAT_MAX)
        self.assertAlmostEqual(x, WIDTH*2, msg="x value is not correct")
        self.assertAlmostEqual(y, 0, msg="y value is not correct")

    def test_latlon_to_xy_center(self):
        x, y = create_tiles.lnglat_to_web(0, 0)
        self.assertAlmostEqual(x, WIDTH, msg="x value is not correct")
        self.assertAlmostEqual(y, WIDTH, msg="y value is not correct")

    def test_xy_to_latlon_leftbottom(self):
        lng, lat = create_tiles.web_to_lnglat(0, WIDTH*2)
        self.assertAlmostEqual(lng, -180, msg="lon value is not correct")
        self.assertAlmostEqual(lat, -LAT_MAX, msg="lat value is not correct")

    def test_xy_to_latlon_lefttop(self):
        lng, lat = create_tiles.web_to_lnglat(0, 0)
        self.assertAlmostEqual(lng, -180, msg="lon value is not correct")
        self.assertAlmostEqual(lat, LAT_MAX, msg="lat value is not correct")

    def test_xy_to_latlon_rightbottom(self):
        lng, lat = create_tiles.web_to_lnglat(WIDTH*2, WIDTH*2)
        self.assertAlmostEqual(lng, 180, msg="lon value is not correct")
        self.assertAlmostEqual(lat, -LAT_MAX, msg="lat value is not correct")

    def test_xy_to_latlon_righttop(self):
        lng, lat = create_tiles.web_to_lnglat(WIDTH*2, 0)
        self.assertAlmostEqual(lng, 180, msg="lon value is not correct")
        self.assertAlmostEqual(lat, LAT_MAX, msg="lat value is not correct")

    def test_xy_to_latlon_center(self):
        lng, lat = create_tiles.web_to_lnglat(WIDTH, WIDTH)
        self.assertAlmostEqual(lng, 0, msg="lon value is not correct")
        self.assertAlmostEqual(lat, 0, msg="lat value is not correct")

    def test_web_to_index_min(self):
        index = create_tiles._web_to_index(0, 0)
        self.assertEqual(index, 0)
        index = create_tiles._web_to_index(1, 0)
        self.assertEqual(index, 0)
        index = create_tiles._web_to_index(2, 0)
        self.assertEqual(index, 0)

    def test_web_to_index_center(self):
        index = create_tiles._web_to_index(0, WIDTH)
        self.assertEqual(index, 0)
        index = create_tiles._web_to_index(1, WIDTH)
        self.assertEqual(index, 1)
        index = create_tiles._web_to_index(2, WIDTH)
        self.assertEqual(index, 2)

    def test_web_to_index_max(self):
        index = create_tiles._web_to_index(0, WIDTH*2)
        self.assertEqual(index, 0)
        index = create_tiles._web_to_index(1, WIDTH*2)
        self.assertEqual(index, 1)
        index = create_tiles._web_to_index(2, WIDTH*2)
        self.assertEqual(index, 3)

    def test_cell_to_extent_web(self):
        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(0, 0, 0)
        self.assertAlmostEqual(x_min, 0)
        self.assertAlmostEqual(x_max, WIDTH*2)
        self.assertAlmostEqual(y_min, 0)
        self.assertAlmostEqual(y_max, WIDTH*2)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(1, 0, 0)
        self.assertAlmostEqual(x_min, 0)
        self.assertAlmostEqual(x_max, WIDTH)
        self.assertAlmostEqual(y_min, 0)
        self.assertAlmostEqual(y_max, WIDTH)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(1, 1, 0)
        self.assertAlmostEqual(x_min, WIDTH)
        self.assertAlmostEqual(x_max, WIDTH*2)
        self.assertAlmostEqual(y_min, 0)
        self.assertAlmostEqual(y_max, WIDTH)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(1, 0, 1)
        self.assertAlmostEqual(x_min, 0)
        self.assertAlmostEqual(x_max, WIDTH)
        self.assertAlmostEqual(y_min, WIDTH)
        self.assertAlmostEqual(y_max, WIDTH*2)

        x_min, x_max, y_min, y_max = create_tiles.cell_to_extent_web(1, 1, 1)
        self.assertAlmostEqual(x_min, WIDTH)
        self.assertAlmostEqual(x_max, WIDTH*2)
        self.assertAlmostEqual(y_min, WIDTH)
        self.assertAlmostEqual(y_max, WIDTH*2)

    def test_cell_to_extent_lnglat(self):
        lng_min, lng_max, lat_min, lat_max = create_tiles.cell_to_extent_lnglat(0, 0, 0)
        self.assertAlmostEqual(lng_min, -180)
        self.assertAlmostEqual(lng_max, 180)
        self.assertAlmostEqual(lat_min, -LAT_MAX)
        self.assertAlmostEqual(lat_max, LAT_MAX)

        lng_min, lng_max, lat_min, lat_max = create_tiles.cell_to_extent_lnglat(1, 0, 0)
        self.assertAlmostEqual(lng_min, -180)
        self.assertAlmostEqual(lng_max, 0)
        self.assertAlmostEqual(lat_min, 0)
        self.assertAlmostEqual(lat_max, LAT_MAX)

        lng_min, lng_max, lat_min, lat_max = create_tiles.cell_to_extent_lnglat(1, 1, 0)
        self.assertAlmostEqual(lng_min, 0)
        self.assertAlmostEqual(lng_max, 180)
        self.assertAlmostEqual(lat_min, 0)
        self.assertAlmostEqual(lat_max, LAT_MAX)

        lng_min, lng_max, lat_min, lat_max = create_tiles.cell_to_extent_lnglat(1, 0, 1)
        self.assertAlmostEqual(lng_min, -180)
        self.assertAlmostEqual(lng_max, 0)
        self.assertAlmostEqual(lat_min, -LAT_MAX)
        self.assertAlmostEqual(lat_max, 0)

        lng_min, lng_max, lat_min, lat_max = create_tiles.cell_to_extent_lnglat(1, 1, 1)
        self.assertAlmostEqual(lng_min, 0)
        self.assertAlmostEqual(lng_max, 180)
        self.assertAlmostEqual(lat_min, -LAT_MAX)
        self.assertAlmostEqual(lat_max, 0)

    def test_create_google_tiles_web_level0(self):
        extent = (0, WIDTH*2, 0, WIDTH*2)
        tiles = create_tiles.create_google_tiles_web(0, extent)
        self.assertEqual(1, len(tiles), "level 0 has %d tiles"%len(tiles))

    def test_create_google_tiles_web_level1(self):
        extent = (0, WIDTH*2, 0, WIDTH*2)
        tiles = create_tiles.create_google_tiles_web(1, extent)
        self.assertEqual(4, len(tiles), "level 0 has %d tiles"%len(tiles))

    def test_create_google_tiles_latlon_level0(self):
        extent = (-180, 180, -LAT_MAX, LAT_MAX)
        tiles = create_tiles.create_google_tiles_lnglat(0, extent)
        self.assertEqual(1, len(tiles), "level 0 has %d tiles"%len(tiles))

    def test_create_google_tiles_latlon_level1(self):
        extent = (-180, 180, -LAT_MAX, LAT_MAX)
        tiles = create_tiles.create_google_tiles_lnglat(1, extent)
        self.assertEqual(4, len(tiles), "level 1 has %d tiles"%len(tiles))

    def test_create_google_tiles_latlon_level17(self):
        #extent = self.lon_min, self.lon_max, self.lat_min, self.lat_max
        #tiles = create_tiles.create_google_tiles_lnglat(17, extent)
        #self.assertEqual(1, len(tiles), "level 17 has %d tiles"%len(tiles))
        self.assertTrue(False, "Not implemented!")

    def test_web_to_cell(self):
        col, row = create_tiles.web_to_cell(WIDTH, WIDTH, 0)
        self.assertEqual(col, 0)
        self.assertEqual(row, 0)

        col, row = create_tiles.web_to_cell(WIDTH, WIDTH, 1)
        self.assertEqual(col, 1)
        self.assertEqual(row, 1)

        col, row = create_tiles.web_to_cell(WIDTH, WIDTH, 2)
        self.assertEqual(col, 2)
        self.assertEqual(row, 2)

    def test_lnglat_to_cell(self):
        col, row = create_tiles.lnglat_to_cell(0, 0, 0)
        self.assertEqual(col, 0)
        self.assertEqual(row, 0)

        col, row = create_tiles.lnglat_to_cell(0, 0, 1)
        self.assertEqual(col, 1)
        self.assertEqual(row, 1)

        col, row = create_tiles.lnglat_to_cell(0, 0, 2)
        self.assertEqual(col, 2)
        self.assertEqual(row, 2)

    def test_web_to_vertex(self):
        x, y = create_tiles.web_to_vertex(0, 0, 0, 0, 0)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        x, y = create_tiles.web_to_vertex(WIDTH, WIDTH, 0, 0, 0)
        self.assertEqual(x, 2048)
        self.assertEqual(y, 2048)

        x, y = create_tiles.web_to_vertex(WIDTH*2, WIDTH*2, 0, 0, 0)
        self.assertEqual(x, 4096)
        self.assertEqual(y, 4096)

    def test_lnglat_to_vertex_level0(self):
        x, y = create_tiles.lnglat_to_vertex(-180, LAT_MAX, 0, 0, 0)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        x, y = create_tiles.lnglat_to_vertex(0, 0, 0, 0, 0)
        self.assertEqual(x, 2048)
        self.assertEqual(y, 2048)

        x, y = create_tiles.lnglat_to_vertex(180, -LAT_MAX, 0, 0, 0)
        self.assertEqual(x, 4096)
        self.assertEqual(y, 4096)

    def test_lnglat_to_vertex_level1(self):
        x, y = create_tiles.lnglat_to_vertex(-180, LAT_MAX, 1, 0, 0)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        x, y = create_tiles.lnglat_to_vertex(0, 0, 1, 0, 0)
        self.assertEqual(x, 4096)
        self.assertEqual(y, 4096)

        x, y = create_tiles.lnglat_to_vertex(0, 0, 1, 1, 1)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        x, y = create_tiles.lnglat_to_vertex(180, -LAT_MAX, 1, 1, 1)
        self.assertEqual(x, 4096)
        self.assertEqual(y, 4096)


if __name__ == '__main__':
    unittest.main(verbosity=2)

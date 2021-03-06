#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lizepy
import unittest

class TestLizePy(unittest.TestCase):

    def setUp(self):
        pass

    def test_ip(self):
        ip = lizepy.get_ip()
        self.assertNotEqual(ip, '')
        self.assertNotEqual(ip, None)

    def test_geoip(self):
        ip = lizepy.get_geoip()
        self.assertTrue(isinstance(ip, lizepy.GeoIP))

    def test_geoip_google(self):
        geoip = lizepy.get_geoip('8.8.8.8')

        self.assertEqual(geoip.ip, geoip['ip'])
        self.assertEqual(geoip.country_code, geoip['country_code'])
        self.assertEqual(geoip.country_code3, geoip['country_code3'])
        self.assertEqual(geoip.country, geoip['country'])
        self.assertEqual(geoip.region_code, geoip['region_code'])
        self.assertEqual(geoip.region, geoip['region'])
        self.assertEqual(geoip.city, geoip['city'])
        self.assertEqual(geoip.postal_code, geoip['postal_code'])
        self.assertEqual(geoip.continent_code, geoip['continent_code'])
        self.assertEqual(geoip.latitude, geoip['latitude'])
        self.assertEqual(geoip.longitude, geoip['longitude'])
        self.assertEqual(geoip.dma_code, geoip['dma_code'])
        self.assertEqual(geoip.area_code, geoip['area_code'])
        self.assertEqual(geoip.asn, geoip['asn'])
        self.assertEqual(geoip.isp, geoip['isp'])
        self.assertEqual(geoip.timezone, geoip['timezone'])

        self.assertEqual(geoip['country'] , 'United States')
        self.assertEqual(geoip['dma_code'] , '0')
        self.assertEqual(geoip['area_code'] , '0')
        self.assertEqual(geoip['ip'] , '8.8.8.8')
        self.assertEqual(geoip['asn'] , 'AS15169')
        self.assertEqual(geoip['continent_code'] , 'NA')
        self.assertEqual(geoip['isp'] , 'Google Inc.')
        self.assertEqual(geoip['longitude'] , -97)
        self.assertEqual(geoip['latitude'] , 38)
        self.assertEqual(geoip['country_code'] , 'US')
        self.assertEqual(geoip['country_code3'] , 'USA')

    def test_geoip_none(self):
        self.assertRaises(AssertionError, lizepy.get_geoip, 1)

if __name__ == '__main__':
    unittest.main()

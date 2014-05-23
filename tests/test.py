import unittest

import lizepy

class TestLizePy(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_valid_ip_empty(self):
        self.assertFalse(lizepy.is_valid_ip(''))

    def test_is_valid_ip_none(self):
        self.assertFalse(lizepy.is_valid_ip(None))

    def test_is_valid_ip_v4_0_0_0_0(self):
        self.assertTrue(lizepy.is_valid_ip('0.0.0.0'))

    def test_is_valid_ip_v4_255_255_255_255(self):
        self.assertTrue(lizepy.is_valid_ip('255.255.255.255'))

    def test_is_valid_ip_v4_127_0_0_1(self):
        self.assertTrue(lizepy.is_valid_ip('127.0.0.1'))

    def test_is_valid_ip_v4_127_0_0_400(self):
        self.assertFalse(lizepy.is_valid_ip('127.0.0.400'))

    def test_is_valid_ip_v4_255_0_256_255(self):
        self.assertFalse(lizepy.is_valid_ip('255.0.256.255'))

    def test_is_valid_ip_v6_2001(self):
        self.assertTrue(lizepy.is_valid_ip('2001:0db8:85a3:08d3:1319:8a2e:0370:7344'))

    def test_is_valid_ip_v6_1(self):
        self.assertTrue(lizepy.is_valid_ip('::1'))

    def test_is_valid_ip_v6_2607(self):
        self.assertTrue(lizepy.is_valid_ip('2607:f0d0:1002:51::4'))

    def test_ip(self):
        ip = lizepy.get_ip()
        self.assertIsInstance(ip, unicode)

    def test_ip_with_invalid_url(self):
        # Force an error.
        lizepy.TELIZE_BASE_URL_IP = 'http://www.example.com/ip'
        ip = lizepy.get_ip()
        self.assertIsNone(ip)

    def test_geoip(self):
        ip = lizepy.get_geoip()
        self.assertIsInstance(ip, lizepy.GeoIP)

    def test_geoip_with_invalid_url(self):
        # Force an error.
        lizepy.TELIZE_BASE_URL_GEOIP = 'http://www.example.com/ip'
        ip = lizepy.get_geoip()
        self.assertIsNone(ip)

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
        self.assertRaises(lizepy.get_geoip(None))

if __name__ == '__main__':
    unittest.main()

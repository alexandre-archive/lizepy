import iptools
import json
import re
import urllib2

from cStringIO import StringIO

TELIZE_BASE_URL = 'http://www.telize.com'
TELIZE_BASE_URL_IP = TELIZE_BASE_URL + '/jsonip'
TELIZE_BASE_URL_GEOIP = TELIZE_BASE_URL + '/geoip/'

class InvalidIPException(Exception):

    def __init__(self, ip):
        self.msg = '%s is not a valid IP address.' % ip

    def __str__(self):
         return repr(self.msg)

class GeoIP:

    def __init__(self):
        self.ip = None # (Visitor IP address, or IP address specified as parameter)
        self.country_code = None # (Two-letter ISO 3166-1 alpha-2 country code)
        self.country_code3 = None # (Three-letter ISO 3166-1 alpha-3 country code)
        self.country = None # (Name of the country)
        self.region_code = None # (Two-letter ISO-3166-2 state / region code)
        self.region = None # (Name of the region)
        self.city = None # (Name of the city)
        self.postal_code = None # (Postal code / Zip code)
        self.continent_code = None # (Two-letter continent code)
        self.latitude = None # (Latitude)
        self.longitude = None # (Longitude)
        self.dma_code = None # (DMA Code)
        self.area_code = None # (Area Code)
        self.asn = None # (Autonomous System Number)
        self.isp = None # (Internet service provider)
        self.timezone = None # (Time Zone)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__.get(key)

def __json(value):
    try:
        return json.loads(value)
    except ValueError:
        return None

def __get(url):

    req = urllib2.Request(url, headers={ 'Accept': 'application/json' })

    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        response = e

    if response.headers.get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        body = f.read()
    else:
        body = response.read()

    return {'code' : response.code, 'body' : __json(body)}

def is_valid_ip(ip):
    if not ip: return False
    return iptools.ipv4.validate_ip(ip) or iptools.ipv6.validate_ip(ip)

def get_ip():
    '''
        Returns the visitor IP address (IPv4 or IPv6).
        :return The visitor IP address.
        :rtype str, unicode or None
    '''
    response = __get(TELIZE_BASE_URL_IP)

    if response['code'] == 200:
        return response['body'].get('ip')
    else:
        return None

def get_geoip(ip=None):
    '''
        Return the visitor GeoIP data or the data for the given IP.
        :return GeoIP data for the visitor IP or the giver IP.
        :rtype GeoIP or None
    '''
    url = TELIZE_BASE_URL_GEOIP

    if ip:
        assert(type(ip) == str)

        if not is_valid_ip(ip):
            raise InvalidIPException(ip)

        url = url + ip

    response = __get(url)

    if response['code'] == 200:

        b = response['body']
        g = GeoIP()

        g.ip = b.get('ip')
        g.country_code = b.get('country_code')
        g.country_code3 = b.get('country_code3')
        g.country = b.get('country')
        g.region_code = b.get('region_code')
        g.region = b.get('region')
        g.city = b.get('city')
        g.postal_code = b.get('postal_code')
        g.continent_code = b.get('continent_code')
        g.latitude = b.get('latitude')
        g.longitude = b.get('longitude')
        g.dma_code = b.get('dma_code')
        g.area_code = b.get('area_code')
        g.asn = b.get('asn')
        g.isp = b.get('isp')
        g.timezone = b.get('timezone')

        return g
    else:
        return None
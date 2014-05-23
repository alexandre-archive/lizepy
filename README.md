# pylize

Python lib for Telize JSON IP and GeoIP REST API

### usage

```python
import pylize
```

### Methods from pylize:

```python
ip = pylize.get_ip()
print(ip)
geoip = pylize.get_geoip('8.8.8.8')
```


### Properties from GeoIP class

```python
geoip.ip or geoip['ip']
geoip.country_code or geoip['country_code']
geoip.country_code3 or geoip['country_code3']
geoip.country or geoip['country']
geoip.region_code or geoip['region_code']
geoip.region or geoip['region']
geoip.city or geoip['city']
geoip.postal_code or geoip['postal_code']
geoip.continent_code or geoip['continent_code']
geoip.latitude or geoip['latitude']
geoip.longitude or geoip['longitude']
geoip.dma_code or geoip['dma_code']
geoip.area_code or geoip['area_code']
geoip.asn or geoip['asn']
geoip.isp or geoip['isp']
geoip.timezone or geoip['timezone']
```


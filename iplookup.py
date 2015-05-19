import geoip2.database

reader = geoip2.database.Reader("GeoLite2-City.mmdb")

class userLookup:
	city = country = region = location = ""
	def __init__(self, ip):
		self.ip = reader.city(ip)
		self.city = self.ip.city.name
		self.country = self.ip.country.name
		self.region = self.ip.subdivisions.most_specific.name
		self.location = "%s, %s, %s" % (self.city, self.region, self.country)


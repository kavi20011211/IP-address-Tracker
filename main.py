import time

from ip2geotools.databases.noncommercial import DbIpCity

from geopy import Nominatim


def ipa ():from ip2geotools.databases.noncommercial import DbIpCity
ip = input("Enter your ip :")

response = DbIpCity.get(ip, api_key="free")

print("\n")

print("Your region is : {0}".format(response.region))

print("\n")

print("************************")

print("Your country is :{0}".format(response.country))
print("\n")

print("************************")                                       

print("Your city is :{0}".format(response.city))
print("\n")

print("************************")

print("Your longitude is :{0}".format(response.longitude))
print("\n")

print("************************")

print("Your latitude is :{0}".format(response.latitude))
print("\n")
print("************************")
print("\n\n\n")

coord=(format(response.longitude),format(response.latitude))

print(coord)
print("\n\n")

from geopy import Nominatim                                       

geolocator=Nominatim(user_agent='test/1')
location=geolocator.reverse(f'{coord[1]},{coord[0]}')
print(location.address)


print("\n\n\n")


print("Please close the application and and try again to search a new IP address")

time.sleep(60)


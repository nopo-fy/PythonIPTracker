import ipapi

print('What IP would you like to track')
ip = str(raw_input('~ '))

country = ipapi.location(ip, None, 'country')
region = ipapi.location(ip, None, 'region')
city = ipapi.location(ip, None, 'city')
longitude = ipapi.location(ip, None, 'longitude')
latitude = ipapi.location(ip, None, 'latitude')
timezone = ipapi.location(ip, None, 'timezone')
postal = ipapi.location(ip, None, 'postal')

print('IP :' + ip)
print('Country : ' + country)
print('Region : ' + region)
print('City : ' + city)
print('Postal : ' + postal)
print('Lon : ' + longitude)
print('Lat : ' + latitude)
print('Time : ' + timezone)
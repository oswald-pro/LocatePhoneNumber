import phonenumbers
import folium
from PhoneNumbers import number
from phonenumbers import geocoder

# Get your API key from https://opencagedata.com/
Api_key = '<YOUR API KEY>'

oswaldNumber = phonenumbers.parse(number)

# Get Country Location of the number
yourLacation = geocoder.description_for_number(oswaldNumber, 'fr')
print(yourLacation)

# Get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "fr"))

# Get latitude and longitude
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Api_key)

query = str(yourLacation)
results = geocoder.geocode(query)

#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=13)
folium.Marker([lat, lng], popup=yourLacation).add_to(myMap)

# Save Map in HTML file
myMap.save("myLocation.html")

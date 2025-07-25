import phonenumbers
import opencage
import folium
from num import number
from phonenumbers import geocoder, carrier

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Location: ", location)

service_pro = phonenumbers.parse(number)
print("Service Provider: ",carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '04c157d1d57549958d4c73dbe1caf830'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Lattitude: ",lat,"Longitude: ", lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")

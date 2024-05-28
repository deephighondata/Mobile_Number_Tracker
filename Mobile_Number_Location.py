import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
import folium
number = input("ENTER MOBILE NUMBER (WITH COUNTRY CODE) : ")
Key = "453b6c62ebeb4ac5b0af5bcaf6b36f7d"
check_mobile_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_mobile_number,'en')
print("THE COUNTRY/STATE WHERE THIS NUMBER IS REGISTERED : ",number_location)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
carrier_name=carrier.name_for_number(service_provider,'en')
print("THE NAME OF THE SERVICE PROVIDER IS : ",carrier_name)
from opencage.geocoder import OpenCageGeocode
geocode = OpenCageGeocode(Key)
query = str(number_location)
location = geocode.geocode(number_location)
lat = location[0]['geometry']['lat']
lng = location[0]['geometry']['lng']
print('LATITUDE OF THE THE LOCATION OF THE NUMBER IS : ',lat)
print('LONGITUDE OF THE THE LOCATION OF THE NUMBER IS : ',lng)
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker(location=[lat, lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
gb_number = phonenumbers.parse(number)
timezone_mobile = timezone.time_zones_for_number(gb_number)
print("THE TIMEZONE WHERE THE NUMBER IS REGISTERED : ",timezone_mobile)

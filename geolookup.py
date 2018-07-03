from geopy.geocoders import Nominatim
import webbrowser
geolocator = Nominatim()
address = input("Give me an address :")
location = geolocator.geocode(address)
latitude = str(location.latitude)
longitude = str(location.longitude)
url = "https://www.google.co.uk/maps/@"+latitude+","+longitude+","+"18z"
webbrowser.open_new_tab(url)
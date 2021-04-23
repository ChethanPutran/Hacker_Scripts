import phonenumbers
from mynumber import number
from phonenumbers import geocoder
from phonenumbers import carrier


#Getting country details
country = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(country,"en"))

#Getting service provider details
serviceProvider = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(serviceProvidire,"en"))

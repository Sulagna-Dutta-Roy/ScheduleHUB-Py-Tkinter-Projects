import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

ch_number=phonenumbers.parse("","CH")
print(geocoder.description_for_number(ch_number,"de"))
ro_number=phonenumbers.parse("","en")
print(carrier.name_for_number(ro_number,"en"))

import iot_mal
import time
import requests
from firebase import firebase


firebase = firebase.FirebaseApplication('https://bluetoothlegattandgraphclean.firebaseio.com/', None) #https://draft-11d6c.firebaseio.com https://bluetoothlegattandgraphclean.firebaseio.com/

def get_location():
  location_position = location_handler.get_position_info()
  print("Location: {}".format(location_position))
  return location_position

def location_is_valid(location_dict):
  return location_dict["loc_status"]


# Main
location_handler = iot_mal.location()
location_handler.set_config(True)
location_handler.set_mode(4)

location_config = location_handler.get_config()
print("Config: {}".format(location_config))

while True:
  location_map = get_location()
  isValid = location_is_valid(location_map)
  result = firebase.post('User1/Location', location_map) #originally location_map
  print result
  print("location_map: {}".format(location_map))
  print("isValid: {}".format(isValid))

  time.sleep(0.5)
  
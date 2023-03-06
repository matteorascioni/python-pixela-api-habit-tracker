# Before to run this program this program run this commands:
# python3 -m venv venv
# pip3 install requests
import requests
from datetime import datetime

TOKEN = "" #Put a token between 8 and 128 characters here
USERNAME = "" #Put your username here
ID = "" #Put a graphId here
headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create a user
pixela_endpoint = "https://pixe.la/v1/users" 
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Create a Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Create a pixel
today = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cicle today? "), 
}
# response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)


# Update a pixel
pixel_update_date = datetime(year=2023,month=3,day=5)
formatted_pixel_update_date = pixel_update_date.strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formatted_pixel_update_date}"
pixel_update_data = {
    "quantity": "", #Put your kilometers updates here 
}
# response = requests.put(url=pixel_update_endpoint,json=pixel_update_data, headers=headers)
# print(response.text)


# Delete a pixel
pixel_delete_date = datetime(year=2023,month=3,day=5)
formatted_pixel_delete_date = pixel_delete_date.strftime("%Y%m%d")
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formatted_pixel_delete_date}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
import requests
from datetime import date

TOKEN = "fr5a4$WAs#%35ds56ujq"
USERNAME = "dagm101"
GRAPH_ID = "graph10545"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "100 Days of code",
    "unit": "days",
    "type": "int",
    "color": "kuro",
}
headers= {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = date.today().strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": f"{today}",
    "quantity": "1"

}
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.today().strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "10"
}
requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
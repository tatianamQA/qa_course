import requests
from urllib.parse import quote

BASE_URL = "http://127.0.0.1:8080"

with open("mars_photo1.jpg", "rb") as image_file:
    response = requests.post(f"{BASE_URL}/upload", files={"image": image_file})

print(response.status_code)
print(response.json())

image_url = response.json()["image_url"]
filename = image_url.split("/")[-1]
encoded_filename = quote(filename)

get_response = requests.get(
    f"{BASE_URL}/image/{encoded_filename}",
    headers={"Content-Type": "text"}
)

print(get_response.status_code)
print(get_response.json())

delete_response = requests.delete(f"{BASE_URL}/delete/{encoded_filename}")

print(delete_response.status_code)
print(delete_response.json())
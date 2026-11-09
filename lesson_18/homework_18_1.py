import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()
data = search_response.json()
print(data)

nasa_id_first = data["collection"]["items"][0]["data"][0]["nasa_id"]
print(nasa_id_first)
nasa_id_sec = data["collection"]["items"][1]["data"][0]["nasa_id"]
print(nasa_id_sec)

asset_url_first = asset_url_template.format(nasa_id=nasa_id_first)
print(asset_url_first)
asset_response_first = requests.get(asset_url_first)
asset_response_first.raise_for_status()
asset_data_first = asset_response_first.json()
print(asset_data_first)

first_jpg = None
for item in asset_data_first["collection"]["items"]:
    if item["href"].endswith(".jpg"):
        first_jpg = item["href"]
        break

print(first_jpg)
image_response_first = requests.get(first_jpg)
image_response_first.raise_for_status()
with open("mars_photo1.jpg", "wb") as file:
    file.write(image_response_first.content)

asset_url_sec = asset_url_template.format(nasa_id=nasa_id_sec)
print(asset_url_sec)
asset_response_sec = requests.get(asset_url_sec)
asset_response_sec.raise_for_status()
asset_data_sec = asset_response_sec.json()
print(asset_data_sec)

sec_jpg = None
for item in asset_data_sec["collection"]["items"]:
    if item["href"].endswith(".jpg"):
        sec_jpg = item["href"]
        break

print(sec_jpg)
image_response_sec = requests.get(sec_jpg)
image_response_sec.raise_for_status()
with open("mars_photo2.jpg", "wb") as file:
    file.write(image_response_sec.content)

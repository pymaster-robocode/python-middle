import asyncio
import requests
import os

ACCESS_KEY = "accesskey"
SAVE_DIR = "images_async"
os.makedirs(SAVE_DIR, exist_ok=True)

search_url = "https://api.unsplash.com/search/photos"
params = {"query": "cute cats", "per_page": 5, "client_id": ACCESS_KEY}
response = requests.get(search_url, params=params)
data = response.json()

def download_image_sync(url, filename):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"Downloaded {filename}")

async def main():
    tasks = []
    for i, photo in enumerate(data.get("results"), 1):
        img_url = photo["urls"]["regular"]
        filename = f"{SAVE_DIR}/img_{i}.jpg"
        t = asyncio.to_thread(download_image_sync, img_url, filename)
        tasks.append(t)
    await asyncio.gather(*tasks)

asyncio.run(main())

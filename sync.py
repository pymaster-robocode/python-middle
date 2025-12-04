import requests
import os


ACCESS_KEY = "YOUR_UNSPLASH_ACCESS_KEY"
SAVE_DIR = "images_sync"
os.makedirs(SAVE_DIR, exist_ok=True)


def download_image(url, filename):
   img = requests.get(url)
   with open(filename, "wb") as f:
       f.write(img.content)


def sync_download(keyword, count=5):
   url = "https://api.unsplash.com/search/photos"
   params = {"query": keyword, "per_page": count, "client_id": ACCESS_KEY}
   data = requests.get(url, params=params).json()


   for i, photo in enumerate(data["results"], 1):
       img_url = photo["urls"]["regular"]
       filename = f"{SAVE_DIR}/{keyword}_{i}.jpg"
       download_image(img_url, filename)
       print(f"Downloaded {filename}")


sync_download("cute cat", 5)

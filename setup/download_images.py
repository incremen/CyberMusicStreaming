import os
import requests

def download_images():
   img_dir = "album_pics"
   
   os.makedirs(img_dir, exist_ok=True)
   for i in range(1, 51):
       response = requests.get(f"https://via.assets.so/album.png?id={i}&q=95&w=360&h=360&fit=fill")
       with open(f"{img_dir}/img_{i}.png", "wb") as f:
           f.write(response.content)
           
           
download_images()

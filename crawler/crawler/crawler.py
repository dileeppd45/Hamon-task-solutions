import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_image_urls(base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')
        image_list = []
        for img in img_tags:
            if img['src'].startswith("https://media.gettyimages.com/id/") and "photo/" in img['src']:
                split_url = img['src'].split("/")
                img_id = split_url[4]
                img_name = split_url[6]
                nam = img_name.split("?")[0].split(".")
                file_name = f"{nam[0]}-{img_id}.{nam[1]}"
                image_list.append({"src": img['src'], "file_name": file_name})

        return image_list

    return None

def download_and_save_images(image_list, folder_path, limit=60):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for i, img_info in enumerate(image_list[:limit], start=1):
        img_url = img_info["src"]
        file_name = img_info["file_name"]
        file_path = os.path.join(folder_path, file_name)

        response = requests.get(img_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded ({i}/{limit}): {file_name}")
        else:
            print(f"Failed to download: {file_name}")

def main():
    base_url = "https://www.gettyimages.in/photos/aamir-khan-actor"
    image_list = get_image_urls(base_url)

    if image_list:
        folder_path = "../images"
        download_and_save_images(image_list, folder_path, limit=60)
    else:
        print("Failed to fetch image URLs.")


if __name__ == "__main__":
    main()
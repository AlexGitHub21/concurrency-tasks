import os
import requests
import threading

#Задание 12. Реализуйте программу, использующую многопоточность, для загрузки изображений из интернета параллельно.
# Каждый поток загружает свое изображение и сохраняет его на диск.

def download_image(url, filename):
    os.makedirs("images", exist_ok=True)
    try:
        img_data = requests.get(url).content
        with open(os.path.join("images", filename), "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Ошибка загрузки: {e}")


thread_image_1 = threading.Thread(target=download_image, args=("https://cdn.pixabay.com/photo/2025/10/26/13/00/ai-generated-9917901_1280.png", "bird.png"), name="download_image_1")
thread_image_2 = threading.Thread(target=download_image, args=("https://cdn.pixabay.com/photo/2024/03/30/15/51/cat-8664948_1280.jpg", "cat.jpg"), name="download_image_2")

thread_image_1.start()
thread_image_2.start()

thread_image_1.join()
thread_image_2.join()
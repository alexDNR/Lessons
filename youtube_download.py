from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input('Введи URL для скачивания файла: ')

yt = YouTube(url, on_progress_callback = on_progress) # сюда передаём урл для скачивания и две функции остлеживания скачивания

print(f"Название видео -- {yt.title}")
print(f"Количество просмотров -- {yt.views}")

video = yt.streams.get_highest_resolution()
video.download('D:/Lessons')
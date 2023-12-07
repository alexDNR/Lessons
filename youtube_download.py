from pytube import YouTube

# функция подсчёта количества загруженных байт
def progress_download(stream, chunk, bytes_remaining):
    downloaded = max_file_size - bytes_remaining
    percent = downloaded/max_file_size * 100
    print(f"Загружено -- {percent:.2f}%")

# функция окончания скачивания
def complite (stream, path):
    print(f'Выполнено -- {path}')

url = input('Введи URL для скачивания файла: ')

yt = YouTube(url, progress_download, complite) # сюда передаём урл для скачивания и две функции остлеживания скачивания

print(f"Название видео -- {yt.title}")
print(f"Количество просмотров -- {yt.views}")
print(f"Длительность видео -- {yt.length/60:.2f} минут")

video = yt.streams.get_highest_resolution()
max_file_size = video.filesize
print(f'Объём файла = {max_file_size} байт')
video.download('D:/Lessons')
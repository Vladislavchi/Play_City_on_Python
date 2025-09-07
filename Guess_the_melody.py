import os
from random import choice
import pygame

def play_music(path_of_the_music):

    # Укажите путь к флешке
    flash_drive_path = path_of_the_music

    # Получить список всех файлов в указанной директории
    files = os.listdir(flash_drive_path)

    # Отфильтровать только файлы с расширением .mp3
    mp3_files = [file for file in files if file.endswith(".mp3")]

    random_mus = choice(mp3_files)

    # Инициализация Pygame
    pygame.init()

    # Укажите путь к файлу MP3
    file_path = f"{path_of_the_music}\{random_mus}"

    # Создание объекта для воспроизведения музыки
    pygame.mixer.music.load(file_path)

    # Воспроизведение музыки
    pygame.mixer.music.play()
    return random_mus[:-4]

start = input("Привет, это игра угадай мелодию, напиши старт чтобы начать: ").lower()
path_files = input("Напиши путь к папке с музыкой, например C:\path_to_music : ")

true = 0
false = 0

while start == "старт" or start == "дальше":
    count = 0

    play_music(path_files)
    mus = play_music(path_files)
    print(mus)

    while input("Пиши название трека: ").lower() != mus.lower():
        if input("Неправильное название, попробуй еще раз, если не знаешь пиши НЕ ЗНАЮ: ").lower() == "не знаю":
            false += 1
            count += 1
            break

    if count == 0:
        pygame.mixer.music.stop()
        start = input("Супер! Ты отгадал трек, пиши ДАЛЬШЕ и слушай следующий: ").lower()
        true += 1
    elif count > 0:
        pygame.mixer.music.stop()
        start = input("Ничего страшного, надеюсь угадаешь следующий, пиши ДАЛЬШЕ и слушай дальше: ").lower()
    if start != "дальше":
        break

pygame.quit()

print(f"Вот столько ты отгадал {true}, и вот столько не угадал {false}, отличная игра!")

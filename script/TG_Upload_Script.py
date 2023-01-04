import os
import json
import shutil
from lib import TelegraphLib
from lib import TelegramLib
from lib import Directory_lib
from lib import Image_lib
from script import Date_Time_Script
from script import Resize_script
import random
from script import tags_html
from progress.bar import IncrementalBar

def open_settings_file(name_settings_file: str) -> dict:
    """
    Функция для открытия файлов формата JSON и считывания данных из него.
    Если файл не обнаружен, то ловит исключение FileNotFoundError.
    :param name_settings_file: путь до файла JSON
    :return: Dict - Словарь с данными из файла
    """
    try:
        with open(os.path.abspath(name_settings_file), "r", encoding="utf-8") as profile_settings:
            profile_json_dict = json.load(profile_settings)
        return profile_json_dict
    except FileNotFoundError:
        print("Не обнаружен файл {}".format(name_settings_file))


# Menu
def menu_profile(profile_json_dict: dict) -> dict:
    while True:
        os.system("cls")
        print("------------------------------------------\n"
              "|    Telegram Script v_3.0.1 by RaFox    |\n"
              "------------------------------------------"
              )
        print("Выбираем профиль:")
        for number_profile, setting_profile in profile_json_dict.items():
            print("\nИмя профиля: {}\nНомер профиля: {}".format(setting_profile["Name Profile"], number_profile))
        print("______________________________________________________")
        answer_user_profile = input("\nВведите номер профиля: ")
        if profile_json_dict.get(answer_user_profile):
            setting_profile_user = profile_json_dict.get(answer_user_profile)
            break
        print("Не найден профиль с таким номером")
    return setting_profile_user


#  Script
# TODO: Тут нужно добавить функцию, которая проверяет наличие в директории нужных разделов, при отсутствие, создает их.
# dir_path_script = os.path.abspath(os.path.join("..", os.path.dirname(os.path.abspath(__file__))))
dir_path_script = os.path.abspath(os.path.join(".."))
print("!!!!!")
print(dir_path_script)
# TODO: Исправить работу с путями в скрипте при запуске с другой рабочей директории.
profile_file = open_settings_file(os.path.join(dir_path_script, "etc", "Profile_file.json"))
setting_account = menu_profile(profile_file)
settings_dict = open_settings_file(os.path.join(dir_path_script, "account_set", setting_account["Name_Settings"]))

Telegraph = TelegraphLib.TelegraphLib(name_channel=settings_dict["name_channel"],
                                      url_channel=settings_dict["url_channel"],
                                      api_telegraph=settings_dict["API_Telegraph"])

Telegram = TelegramLib.TelegramLib(name_user_admin=settings_dict["name_user_admin"],
                                   channel=settings_dict["channel"],
                                   api_hash=settings_dict["api_hash"],
                                   api_id=settings_dict["api_id"])

tags_file = settings_dict["tags_file"]  # Получаем данные по тегам.
tags_dict = open_settings_file(os.path.join(dir_path_script, "etc", tags_file))

# Считываем данные из директории с файлами.
directory = Directory_lib.Directory()
directory_dict = directory.search_directory(os.path.join(dir_path_script, "TG", "Upload"), False)

#  Собираем список с объектами datetime
date_time_post_list = Date_Time_Script.DateTime.tg_date_time()

# Обрабатываем изображения и проверяем размер изображений.
Resize_script.ImageResize(directory_dict, 5000).resizeTG()
Image_lib.Images.merge_image(directory_dict)
os.system("cls")
#  Запускаем основной скрипт загрузки и создания постов.
folder_list = list()
for folder, image_list in directory_dict.items():
    if not image_list:
        continue
    folder_list.append(folder)

random.shuffle(folder_list)  # Перемешиваем список с директориями

for folder in folder_list:
    image_folder_dict = directory.search_directory(folder, False)
    for folder_dir, image_list in image_folder_dict.items():
        if not image_list:
            continue
        name_folder = os.path.basename(folder_dir)
        html_image = ""
        bar = IncrementalBar('Check_Resize_Image - {}'.format(name_folder), max=len(image_list))
        for image in image_list:
            if image.endswith(".gif"):
                continue
            if image == "Post.jpg":
                image_merge = os.path.join(folder_dir, image)
            html_image += Telegraph.download_img(os.path.join(folder_dir, image))
            bar.next()
        url_page_tg = Telegraph.create_page_telegraph(name_folder, html_image)
        count_image = len(image_list)
        name_start, name_end = name_folder.split(" - ")
        name_tags, tags_code = tags_dict[name_start]["Name"], tags_dict[name_start]["Tags"]  # Получаем имя и теги
        html_text = tags_html.TagsHTML.tg_html(name_folder=name_folder,
                                               url_page=url_page_tg,
                                               number_photo=count_image,
                                               tags_name=name_tags,
                                               tags_id=tags_code)
        date_time_post = date_time_post_list.pop(0)
        if not image_merge:
            print("Отсутствует изображение для поста!")
            raise Exception
        Telegram.app.run(Telegram.creat_post_telegram(image=image_merge, text_post=html_text, date=date_time_post))
        bar.finish()
        print("Создан пост {} на дату {}".format(name_folder, date_time_post))
        shutil.rmtree(folder)

import os
from progress.bar import ShadyBar


class Directory:

    @classmethod
    def search_directory(cls, user_path: str, size_dir_flag=True) -> int or dict:
        """
        Составляет словарь директорий и файлов в них.

        :param size_dir_flag: True - Возвращает из функции размер всех файлов в директории.
        :param user_path: путь до обрабатываемых директорий
        :return: root_file_dict словарь key - путь до директории, value - список файлов в директории.
        """
        root_file_dict = {}
        size_dir = 0
        bar = ShadyBar(f'Scanning - {user_path}', suffix='%(percent)d%%')
        for root, dirs, files in os.walk(user_path):  # собираем данные по файлам и директориям
            for file in files:  # Пробегаемся по списку с файлами и сохраняем размеры изображений
                filename_path = os.path.join(root, file)
                size_dir += os.path.getsize(filename_path) / 1024 / 1024
            root_file_dict.update({root: files})  # Собираем в словарь
            bar.next()
        bar.finish()
        os.system("cls")
        if size_dir_flag:
            return size_dir
        else:
            return root_file_dict

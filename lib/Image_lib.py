import pathlib

from PIL import Image
import os


class Images:

    def __init__(self, path_file: str) -> None:
        self.__path_file = path_file
        self.__images_file = Image.open(path_file)
        self.__width, self.__height = self.__images_file.size
        self.__size_images = os.path.getsize(path_file)

    def set_width_height_size(self) -> None:
        """
        Обновляем атрибуты класса из объекта изображения.
        :return: None
        """
        self.__width, self.__height = self.__images_file.size
        self.__size_images = os.path.getsize(self.__path_file)

    def get_info_file(self):
        return self.__images_file, self.__width, self.__height, self.__size_images

    def check_size_width(self, max_size: int) -> bool:
        """
        Проверка максимального размера изображения по ширине.

       :param max_size: int - максимальный размер изображения, передается в пикселях.
       :return: bool - True если размер изображения больше, чем максимальное значение, False если меньше.
        """
        if self.__width > max_size:
            return True
        else:
            return False

    def check_size_hight(self, max_size: int) -> bool:
        """
        Проверка максимального размера изображения по высоте.

        :param max_size: int - максимальный размер изображения, передается в пикселях.
        :return: bool - True если размер изображения больше, чем максимальное значение, False если меньше.
        """
        if self.__height > max_size:
            return True
        else:
            return False

    def check_size_weight(self, max_weight: int) -> bool:
        """
        Проверка размера файла с изображением.

        :param max_weight: int - максимальный размер(вес) файла.
        :return: - True если размер изображения больше, чем максимальное значение, False если меньше.
        """
        if self.__size_images > max_weight:
            return True
        else:
            return False

    def resize_image_width(self, size_width: int) -> None:
        """
        Уменьшает размер изображения по ширине, с расчетом новой высоты.

        :param size_width: int - Принимает новый размер ширины для изображения.
        """
        self.__images_file.thumbnail(size=(size_width, self.__height))  # Меняем размер изображения
        self.__images_file.save(self.__path_file)  # Сохранение изображения
        self.set_width_height_size()

    def resize_image_hight(self, size_hight: int) -> None:
        """
        Уменьшает размер изображения по высоте, с расчетом новой ширины.

        :param size_hight: int - Принимает новый размер высоты для изображения.
        """
        self.__images_file.thumbnail(size=(self.__width, size_hight))  # Меняем размер изображения
        self.__images_file.save(self.__path_file)  # Сохранение изображения
        self.set_width_height_size()

    def rename_extension(self, new_extension: str) -> None:
        """Смена расширения файла.
        file_path: str - Путь до файла.
        new_extension: str - Новое расширение формата (jpg, bmp, png).
        """
        folder_path, name = os.path.split(self.__path_file)
        name_file = pathlib.PurePath(self.__path_file).stem  # получаем путь до файла без расширения файла.
        new_name = "{name}.{extension}".format(name=name_file, extension=new_extension)
        new_name_path = os.path.join(folder_path, new_name)
        os.rename(self.__path_file, new_name_path)
        self.__path_file = new_name

    def extension_check_true(self, extension: str) -> bool:
        """Проверка расширения у файла, если заданное расширение присутствует, возвращает True"""
        if self.__path_file.endswith(".{}".format(extension)):
            return True

    def extension_check_false(self, extension: str) -> bool:
        """Проверка расширения у файла, если заданное расширение отсутствует, возвращает True"""
        if not self.__path_file.endswith(".{}".format(extension)):
            return True

    # def reduction_weight(self, path_user, ratio_resize):
    #     """
    #     Метод уменьшение веса изображения, за счет уменьшения сжатия по ширине и высоте.
    #
    #     :param path_user: Прямой путь до изображения str
    #     :param ratio_resize: Рейтинг уменьшения изображения (0.1 - 0.9) int
    #     :return:
    #     """
    #     image_original = Image.open(path_user)
    #     width, height = image_original.size  # Получение размеров изображения
    #     if width > height:
    #         new_width = int(width * ratio_resize)
    #         new_height = int(new_width * height / width)  # Расчет новой высоты изображения
    #         image_original = image_original.resize((new_width, new_height),
    #                                                Image.Resampling.LANCZOS)  # Изменения размеров изображения
    #         image_original.save(path_user)  # Сохранение изображения
    #     else:
    #         new_height = int(height * ratio_resize)  # Высота
    #         new_width = int(new_height * width / height)  # Расчет новой ширины изображения
    #         image_original = image_original.resize((new_width, new_height),
    #                                                Image.Resampling.LANCZOS)  # Изменения размеров изображения
    #         image_original.save(path_user)  # Сохранение изображения

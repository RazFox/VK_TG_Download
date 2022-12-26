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

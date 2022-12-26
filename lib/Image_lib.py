from PIL import Image
import os


class Images:

    def __init__(self, path_file: str) -> None:
        self.__path_file = path_file
        self.__images_file = Image.open(path_file)
        self.__width, self.__height = self.__images_file.size
        self.__size_images = os.path.getsize(path_file)


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
        self.__images_file.thumbnail(size=(size_width, self.__height)) # Меняем размер изображения
        self.__images_file.save(self.__path_file)  # Сохранение изображения


    def resize_image_hight(self, size_hight: int) -> None:
        """
        Уменьшает размер изображения по высоте, с расчетом новой ширины.

        :param size_hight: int - Принимает новый размер высоты для изображения.
        """
        new_width = int(size_hight * width / height)  # Расчет новой ширины изображения
        image_original = image_original.resize((new_width, size_hight),
                                               Image.Resampling.LANCZOS)  # Изменения размеров изображения
        image_original.save(path_user)  # Сохранение изображения
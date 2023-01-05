import os.path
from lib import Image_lib
from progress.bar import IncrementalBar

class ImageResize:

    def __init__(self, directory_dict, max_size_image, extension):
        self.__directory_dict = directory_dict
        self.__max_size_image = max_size_image
        self.__extension = extension

    def resizeTG(self):

        image_object_list = list()
        for directory, image_list in self.__directory_dict.items():
            if not image_list:
                continue
            len_image_list = len(image_list)
            bar = IncrementalBar('Check_Resize_Image - {}'.format(os.path.basename(directory)), max=len_image_list)
            for image in image_list:
                image_obj = Image_lib.Images(os.path.join(directory, image))
                image_object_list.append(image_obj)
            for image_file in image_object_list:
                if image_file.check_size_width(self.__max_size_image):
                    image_file.resize_image_width(self.__max_size_image)
                if image_file.check_size_hight(self.__max_size_image):
                    image_file.resize_image_hight(self.__max_size_image)
                if image_file.extension_check_false(self.__extension):
                    image_file.rename_extension(self.__extension)
                bar.next()
            bar.finish()

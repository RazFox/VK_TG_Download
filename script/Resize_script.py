from lib import Image_lib

file = "D:\\Python\\Проекты\\VK_TG_Download\\VK\\test_image.jpg"
Image = Image_lib.Images(file)
print(Image)
print("width: {} height: {} size: {}".format(
    Image.get_info_file()[1], Image.get_info_file()[2], Image.get_info_file()[3]
))
if Image.check_size_width(5000):
    Image.resize_image_width(5000)
print("width: {} height: {} size: {}".format(
    Image.get_info_file()[1], Image.get_info_file()[2], Image.get_info_file()[3]
))
if Image.check_size_hight(5000):
    Image.resize_image_hight(5000)
print("width: {} height: {} size: {}".format(
    Image.get_info_file()[1], Image.get_info_file()[2], Image.get_info_file()[3]
))
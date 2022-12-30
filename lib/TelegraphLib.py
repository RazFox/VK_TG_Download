import requests
from telegraph import Telegraph


class TelegraphLib:

    def __init__(self, settings_dict: dict) -> None:
        """
        :param settings_dict: dict - словарь с данными с ключами:
          name_channel: str = Наименование канала
          url_channel: str - ссылка на канал
          API_Telegraph: str - API Telegraph
        """
        self.name_channel = settings_dict["name_channel"]
        self.url_channel = settings_dict["url_channel"]
        self.api_telegraph = settings_dict["API_Telegraph"]

    def create_page_telegraph(self, name_new_page: str, new_url_line: str) -> str:
        """
        Создание новой страницы

        :param name_new_page: str - Название статьи
        :param new_url_line: str - Строка ссылками на изображения
        :return: str - Ссылка на страницу
        """
        telegraph = Telegraph(self.api_telegraph)
        response = telegraph.create_page(
            name_new_page,
            content=None,
            html_content=new_url_line.replace('\n', ''),
            author_name=self.name_channel,
            author_url=self.url_channel,
            return_content=False)
        url_new_page = f'http://telegra.ph/{response["path"]}'
        return url_new_page

    @classmethod
    def download_img(cls, image_path: str) -> str:
        """
        Загрузка изображений на сервис telegraph

        :param image_path: Путь до изображения.
        :return: str ссылки на изображения в html разметке
        """
        with open(image_path, 'rb') as image:
            path = requests.post(
                'https://telegra.ph/upload', files={'file':
                                                        ('file', image,
                                                         'image/jpeg')}).json()[0]['src']

        url_photo = "<img src=https://telegra.ph{}/>".format(str(path))
        return url_photo

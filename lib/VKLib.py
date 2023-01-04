import os
import requests


class VKLib:

    def __init__(self, token: str, v_api: str, group_id: int) -> None:
        self.token = token
        self.v_api = v_api
        self.group_id = group_id
        self.owner_id = int("-{0}".format(group_id))

    def create_album(self, title: str, description: str) -> str:
        """
        Метод создания пустого альбома в группе.
        upload_by_admins_only (0/1) 0 - загрузка фото всем, 1 - только админам группы.
        comments_disabled (0/1) 0 - комментарии включены, 1 - комментарии выключены.
        :param token: Токен
        :param title: Название альбома str
        :param description: Описание альбома str
        :param v_api: Версия API
        :return: id альбома
        """

        album_id = requests.get('https://api.vk.com/method/photos.createAlbum', params={'access_token': self.token,
                                                                                        'title': title,
                                                                                        'group_id': self.group_id,
                                                                                        'description': description,
                                                                                        'upload_by_admins_only': 1,
                                                                                        'comments_disabled': 1,
                                                                                        'v': self.v_api}).json()
        print(album_id)
        return album_id["response"]["id"]

    def server_upload(self, album_id) -> str:
        """
        Метод получения сервера для загрузки фото в ВК
        :param token: Токен
        :param album_id: id альбома
        :param v_api: Версия API
        :return: Сервер для загрузки фото
        """
        server = requests.get('https://api.vk.com/method/photos.getUploadServer',
                              params={'access_token': self.token,
                                      'album_id': album_id,
                                      'group_id': self.group_id,
                                      'v': self.v_api}).json()

        print(server)
        return server["response"]["upload_url"]

    @classmethod
    def upload_photo_album(cls, server: str, list_file: list) -> [str, list, str, str, str]:
        # TODO: Проверить работу метода, вернуть старый вариант
        """
        Метод загрузки фото на сервер ВК.
        :param server: Сервер для загрузки фото
        :param list_file: Список с путями для загрузки фото
        :return: Возвращается данные для сохранения фото:
        server - сервер, photos_list - данные загруженных фотографий, aid - id альбома, gid - id группы, hash - хеш
        """
        new_dict_file = dict()
        if not len(list_file) == 1:
            for elem_num, elem in enumerate(list_file):
                new_dict_file.update({"file{}".format(elem_num + 1): open(elem, "rb")})
        else:
            new_dict_file.update({"file1": open(list_file[0], "rb")})

        upl = requests.post(server, files=new_dict_file).json()

        return upl["server"], upl["photos_list"], upl["aid"], upl["hash"], upl["gid"]

    def photo_save_album(self, server_photo: str, photos_list: list, aid: str, hash_photo: str) -> None:
        """
        Метод сохранения загруженных на сервер фотографий в альбом
        :param server_photo: сервер загрузки
        :param photos_list: данные фото
        :param aid: id альбома
        :param hash_photo: хеш фотографий
        :param v_api: версия API
        :return: json с результатами.
        """
        save = requests.get('https://api.vk.com/method/photos.save',
                            params={'access_token': self.token, 'album_id': aid,
                                    'group_id': self.group_id, 'server': server_photo,
                                    'photos_list': photos_list,
                                    'hash': hash_photo, 'v': self.v_api}).json()

    def wall_post(self, message, attachments, publish_date=None, from_group=0, close_comments=0,
                  copyright=None):
        """
        Метод создания отложенного поста в ВК на стене группы.
        :param message: Сообщение для отправки
        :param publish_date: Дата публикации в unixtime. По молчанию None. Если не указано, то отправка немедленно.
        :param from_group: (0/1) 0 - от имени пользователя, 1 - от имени группы
        :param attachments: Перечисление данных для поста(если их несколько то через запятую:
            Формат <type><owner_id>_<media_id>
            <type> — тип медиа-приложения:
                photo — фотография;
                video — видеозапись;
                audio — аудиозапись;
                doc — документ;
                page — wiki-страница;
                note — заметка;
                poll — опрос;
                album — альбом;
                market — товар;
                market_album — подборка товаров;
                audio_playlist — плейлист с аудио.
            <owner_id> — идентификатор владельца медиа-приложения (если объект находится в сообществе,
                                                                        значение должно быть отрицательным числом).
            <media_id> — идентификатор медиа-приложения.
        :param close_comments: int 1 -  Комментарии к записи отключены, 0 - комментарии к записи включен. По умолчанию 0.
        :param copyright: Источник материала, ссылка. По умолчанию None
        :return: возвращает id поста.
        """
        param = {'access_token': self.token, 'owner_id': self.owner_id, 'from_group': from_group,
                 'message': message,
                 'attachments': attachments,
                 'publish_date': publish_date,
                 'close_comments': close_comments,
                 'copyright': copyright,
                 'v': self.v_api}
        post = requests.get('https://api.vk.com/method/wall.post', params=param).json()
        return post

    def upload_photo_wall(self, folder_image, list_file_upload):
        """
        Метод получает ссылку для загрузки фото на сервер, загружает и сохраняет фото на стену,
        и готовит шаблон для отправки его в метод поста.
        :param folder_image: Путь до директории с изображениями.
        :param list_file_upload: List - список наименований изображений.
        :return: Str - строка через "," c данными по фото, для передачи их в метод поста.
        """
        # Получаем ссылку для загрузки изображений
        url_down = requests.post("https://api.vk.com/method/photos.getWallUploadServer?",
                                 params={"access_token": self.token,
                                         "group_id": self.group_id,
                                         "v": self.v_api}).json()
        upload_url = url_down['response']['upload_url']
        list_info_image = list()

        # Загружаем изображение на url
        for image in list_file_upload:
            image_path = os.path.join(folder_image, image)
            img = {'photo': ('{0}.jpg'.format(image), open(r'{0}'.format(image_path), 'rb'))}
            # Загружаем на сервер фотографию
            photo_info = requests.post(upload_url, files=img).json()
            # Сохраняем данные фотографии на стене
            response = requests.post("https://api.vk.com/method/photos.saveWallPhoto?",
                                     params={"access_token": self.token, "group_id": self.group_id,
                                             "photo": photo_info['photo'],
                                             "hash": photo_info['hash'],
                                             "server": photo_info['server'], "v": self.v_api}).json()
            # Получаем шаблон с данными фотографии для передачи ее в метод создания поста.
            id_user_group = response["response"][0]["owner_id"]
            id = response["response"][0]['id']
            image_wall = "photo" + "{0}".format(id_user_group) + "_" + "{0}".format(id)
            list_info_image.append(image_wall)
        # Объединяем все шаблоны в строку
        image_info_sample = list(map(str, list_info_image))
        wall_image_string = ",".join(image_info_sample)

        return wall_image_string

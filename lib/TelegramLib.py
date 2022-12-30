from pyrogram import Client, enums
import datetime


class TelegramLib:

    def __init__(self, settings_dict: dict) -> None:
        self.api_id = settings_dict["api_id"]
        self.api_hash = settings_dict["api_hash"]
        self.name_user_admin = settings_dict["name_user_admin"]
        self.channel = settings_dict["channel"]
        self.app = self.authorization()

    def authorization(self):
        """
        Авторизация в сервисе Telegram
        :return: object client
        """
        app = Client(name=self.name_user_admin, api_id=self.api_id, api_hash=self.api_hash)
        return app

    def creat_post_telegram(self, image: str, text_post: str, date: datetime) -> None:
        """
        Создание поста в телеграмм
        :param image:
        :param text_post:
        :param date:
        :return:
        """
        self.app.send_photo(self.channel, photo=image, caption=text_post, schedule_date=date,
                            parse_mode=enums.ParseMode.HTML)

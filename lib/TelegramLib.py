from pyrogram import Client, enums


class TelegramLib:

    def __init__(self, name_user_admin: str, channel: str, api_id: str, api_hash) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.name_user_admin = name_user_admin
        self.channel = channel
        self.app = self.authorization()

    def authorization(self):
        """
        Авторизация в сервисе Telegram
        :return: object client
        """
        app = Client(name=self.name_user_admin, api_id=self.api_id, api_hash=self.api_hash)
        return app

    async def creat_post_telegram(self, image: str, text_post: str, date: object) -> None:
        """
        Создание поста в телеграмм
        :param image:
        :param text_post:
        :param date:
        :return:
        """
        async with self.app:
            await self.app.send_photo(self.channel, photo=image, caption=text_post, schedule_date=date,
                                      parse_mode=enums.ParseMode.HTML)

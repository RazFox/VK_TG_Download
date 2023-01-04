import os
import datetime as DT


class DateTime:

    @classmethod
    def tg_date_time(cls):
        """
        Запрашивает у пользователя стартовую и конечную дату и время, и возвращает список с объектами datetime
        :return: list datetime
        """
        date_time_list = list()
        print("Введите стартовую дату и время в формате (День/Месяц/Год Часы:Минуты - 01/11/2022 08:30)")
        start_date_time = input("Стартовая дата и время: ")
        print("Введите дельту в часах")
        time_delta = int(input("Дельта (Целое число): "))
        print("Введите кол-во постов в день.")
        count_post_day = int(input("Кол-во постов (Целое число): "))
        print("Введите кол-во дней для постов (Целое число)")
        count_day = int(input("Вол-во дней: "))
        os.system("cls")
        time_date_obj = DT.datetime.strptime(start_date_time, "%d/%m/%Y %H:%M")
        start_date_obj = DT.datetime.strptime(start_date_time, "%d/%m/%Y %H:%M").date()
        start_date_time = DT.datetime.strptime(start_date_time, "%d/%m/%Y %H:%M").time()

        for day in range(1, count_day + 1):
            for _ in range(count_post_day):
                date_time_list.append(time_date_obj)
                time_date_obj += DT.timedelta(hours=time_delta)
            time_date_obj = DT.datetime.combine(start_date_obj + DT.timedelta(days=day), start_date_time)
        return date_time_list


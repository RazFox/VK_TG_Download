import datetime as DT

class TimeDate:

    @classmethod
    def unixtime_time(cls, *args):
        """
        Принимает *args с датами, преобразовывает их в формат unixtime и возвращает список.
        :param time: str - строка с датой и временем в формате YYYY-MM-DD HH:MM:SS
        :return: List - список дат в формате unixtime
        """
        unix_time = list()
        for data_args in args:
            time_format = DT.datetime.fromisoformat(data_args)
            unix_time.append(int(time_format.timestamp()))
        return unix_time

    @classmethod
    def time_delta_1_day(cls, data_list):
        """
        Меняет даты в списке на +1 день
        :param data_list: List - список дат в unixtime
        :return: List - возвращает новый список с датами в unixtime +1 день
        """
        list_new_date = list()
        for data_unix in data_list:
            data_unix += 86400
            list_new_date.append(data_unix)
        return list_new_date

    @classmethod
    def time_unixtime(cls, date_object):
        """
        Преобразование объекта datetime в формат unixtime
        :param date_object: Объект datetime
        :return: Float - дата и время в формате unixtime
        """
        unixtime_date = date_object.timestamp()
        return unixtime_date

    @classmethod
    def time_object_str(cls, str_date):
        """
        Преобразование строки в формате %Y-%m-%d %H:%M:%S в объект даты.
        :param str_date: Str - дата в формате строки
        :return: Объект date_time
        """
        date_time_object = DT.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
        return date_time_object

    @classmethod
    def date_unixtime_normal(cls, unix_time):
        """
        Принимает дату в формате unixtime и преобразовывает ее в объект datetime в формате '%Y-%m-%d %H:%M:%S'
        :param unix_time: Int = время в формате unixtime
        :return: Объект Datetime
        .strftime('%Y-%m-%d %H:%M:%S')
        """
        date_time_normal = DT.datetime.fromtimestamp(unix_time)
        return date_time_normal

    @classmethod
    def determining_date_week_unixtime(cls, date_object):
        """
        Приринимает объект datetime, и определяет день недели Понедельник - 1... Воскресенье-7.
        :param date_object: Объект в формате datetime
        :return: Int - День недели.
        """
        date_week = DT.datetime.isoweekday(date_object)
        return date_week

    @classmethod
    def time_date_str_join(cls, date_list, time_str):
        """
        Распаковывает дату из списка и объединяет его с временем.
        :param date_list: List - Дата в формате ["day", "mounth", "year"].
        :param time_str: Str - Время в формате "HH:MM:SS"
        :return: Str - Строка с датой и временем в формате "year-mounth-day HH:MM:SS"
        """
        day, mounth, year = date_list
        date_str = "{}-{}-{} {}".format(year, mounth, day, time_str)
        return date_str
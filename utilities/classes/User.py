from utilities.db.db_manager import DBManager
import datetime


class User:
    __email = None
    __first_name = None
    __last_name = None
    __create_date = None
    __about_me = None
    __phone_number = None
    __password = None
    __car_type = None
    __car_color = None

    def __init__(self, email, firstname, lastname, aboutme, phonenum, password, cartype, carcolor):
        self.__email = email
        self.__first_name = firstname
        self.__last_name = lastname
        self.__create_date = datetime.datetime.now().timestamp()
        self.__about_me = aboutme
        self.__phone_number = phonenum
        self.__password = password
        self.__car_type = cartype
        self.__car_color = carcolor

    def register_user(self):
        query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        args = (self.__email, self.__first_name, self.__last_name, self.__create_date, self.__about_me,
                self.__phone_number, self.__password, self.__car_type, self.__car_color)
        isregister = DBManager.commit(query=query, args=args)
        return isregister == 1  # one row was affected

    def update_user(self, first_name, last_name, about_me, phone_number, password, car_type, car_color):
        query = "UPDATE users SET first_name=%s, last_name=%s, about_me=%s, phone_number=%s, password=%s," \
                " car_type=%s, car_color=%s WHERE email=%s;"
        args = (first_name, last_name, about_me, phone_number, password, car_type, car_color, self.__email)
        isupdated = DBManager.commit(query=query, args=args)
        return isupdated == 1  # one row was affected


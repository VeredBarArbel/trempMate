from utilities.db.db_manager import dbManager


class Trip:
    __trip_id = None
    __driver_email = None
    __pickup_date = None
    __pickup_time = None
    __pickup_city = None
    __drop_city = None
    __available_seats = None #current available seats
    __passengers = None #original passenger amount
    __price = None

    def __init__(self, driverEmail, date, time, pickupCity, dropCity, passengers, price):
        self.__driver_email = driverEmail
        self.__pickup_date = date
        self.__pickup_time = time
        self.__pickup_city = pickupCity
        self.__drop_city = dropCity
        self.__available_seats = passengers
        self.__passengers = passengers
        self.__price = price

    def create_trip(self):
        query = "INSERT INTO trips VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        args = (self.__trip_id, self.__driver_email, self.__pickup_date, self.__pickup_time, self.__pickup_city, self.__drop_city,
                self.__available_seats, self.__price, self.__passengers)
        # newDBManager = DBManager()
        isregister = dbManager.commit(query=query, args=args)
        return isregister == 1  # one row was affected

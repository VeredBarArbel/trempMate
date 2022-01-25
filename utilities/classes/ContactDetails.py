from utilities.db.db_manager import dbManager
from datetime import datetime


class Contact:
    __id = None
    __email = None
    __description = None
    __DT = datetime.now()

    def __init__(self, email, description):
        self.__email = email
        self.__description = description

    def create_req(self):
        query = "INSERT INTO contacts VALUES (%s, %s, %s, %s);"
        args = (self.__id, self.__email, self.__description, self.__DT)
        isAddedReq = dbManager.commit(query=query, args=args)
        return isAddedReq == 1  # one row was affected
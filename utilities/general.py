from utilities.db.db_manager import dbManager
from utilities.classes.Trip import Trip
from utilities.classes.User import User

def get_user(email):
    query = 'select * from users where email = %s' % email
    user_result = dbManager.fetch(query)[0] #return a list with the user details
    user = User(user_result[0], user_result[1], user_result[2], user_result[4],
                user_result[5], user_result[6], user_result[7], user_result[8])
    return user #list with all users's details - in order to insert into session

def get_trip(tripID):
    query = 'select * from trips where trip_id = %s' % tripID
    trip_result = dbManager.fetch(query)[0] #return a list with the trip details
    return trip_result

def save_spot(tripId, user):
    #update available seats
    query = 'update trips set available_seats = (available_seats-1) ' \
            'where trip_id = %s and available_seats > 0' % tripId
    isSave = dbManager.commit(query)
    #add to tripuser
    queryuser = 'insert into tripuser (trip, user) values (%s, %s);'
    args = (tripId, user)
    isAdded = dbManager.commit(queryuser, args)
    return (isAdded ==1 and isSave == 1) #update seats amount sucsseeded
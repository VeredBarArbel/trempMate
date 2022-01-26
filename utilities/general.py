from utilities.db.db_manager import dbManager
from utilities.classes.Trip import Trip
from utilities.classes.User import User

def get_user(email):
    # query = 'select * from users where email = %s;' % email
    query = f'select * from users where email = "{email}";'
    user_result = dbManager.fetch(query) #return a list with the user details if exist
    if user_result != False and user_result != []:
        user_result = user_result[0]
        user = User(user_result[0], user_result[1], user_result[2], user_result[4],
                    user_result[5], user_result[6], user_result[7], user_result[8])
    else:
        user = '' #user dosen't exist
    return user #list with all users's details - in order to insert into session

def get_trip(tripID):
    query = 'select * from trips where trip_id = %s' % tripID
    trip_result = dbManager.fetch(query)[0] #return a list with the trip details
    return trip_result

def save_spot(tripId, user, amount):
    #check if there are enough seats
    amount = int(amount)
    checkAmountQuery = 'select available_seats from trips where trip_id = %s' % tripId
    checkAmount = dbManager.fetch(checkAmountQuery)[0][0]
    if checkAmount < amount:
        return "not enough seats"
    #update available seats
    query = 'update trips set available_seats = (available_seats-%s) ' \
            'where trip_id = %s' % (amount, tripId)
    isSave = dbManager.commit(query)
    #add to tripuser
    queryuser = 'insert into tripuser (trip, user, seats_amount) values (%s, %s, %s);'
    args = (tripId, user, amount)
    isAdded = dbManager.commit(queryuser, args)
    return (isAdded ==1 and isSave == 1) #update seats amount sucsseeded


#Ride Hisory
def driver_history(driverEmail):
    query = f'select * from trips where driver = "{driverEmail}"'
    driver_result = dbManager.fetch(query) #return a list with the trip details
    if driver_result != False and driver_result != []:
        return driver_result
    return False

def tremp_history(trempEmail):
    query = f'select * from tripuser as tu join trips as t on tu.trip=t.trip_id' \
            f' where tu.user = "{trempEmail}"'
    tremp_result = dbManager.fetch(query) #return a list with the trip details
    if tremp_result != False and tremp_result != []:
        print(tremp_result)
        return tremp_result
    return False
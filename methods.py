# temporary file to help with route testing, might leave it in

from database import Database as db

def hardware_checkin(one, two):
    cursor = db.hardware_collection.findone()
    for temp in cursor:
        max1 = temp['maxHW1']
        max2 = temp['maxHW2']
        avail1 = temp['availHW1']
        avail2 = temp['availHW2']

    avail1 = avail1 + one
    avail2 = avail2 + two

    db.hardware_collection.update_one({'maxHW1': max1}, {"$set": {'availHW1': avail1}})
    db.hardware_collection.update_one({'maxHW2': max2}, {"$set": {'availHW2': avail2}})
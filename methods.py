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

def hardware_checkout(one, two):
    cursor = db.hardware_collection.findone()
    for temp in cursor:
        max1 = temp['maxHW1']
        max2 = temp['maxHW2']
        avail1 = temp['availHW1']
        avail2 = temp['availHW2']

    if one > avail1:
        if two > avail2:
            return "not enough hw1 and hw2 available"
        return "not enough hw1 available"
    if two > avail2:
        return "not enough hw2 available"

    avail1 = avail1 - one
    avail2 = avail2 - two

    db.hardware_collection.update_one({'maxHW1': max1}, {"$set": {'availHW1': avail1}})
    db.hardware_collection.update_one({'maxHW2': max2}, {"$set": {'availHW2': avail2}})

def project_checkin(proj_id, one, two):
    cursor = db.project_collection.find({'project_id': proj_id})
    for temp in cursor:
        hard1 = temp['hw1']
        hard2 = temp['hw2']

    # use the hardware.py function to update the hardware doc
    hardware_checkin(one, two)

    # checkin means you give to hardware and take from project
    hard1 = hard1 - one
    hard2 = hard2 - two

    db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw1": hard1}})
    db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw2": hard2}})

def project_checkout(proj_id, one, two):
    cursor = db.project_collection.find({'project_id': proj_id})
    for temp in cursor:
        hard1 = temp['hw1']
        hard2 = temp['hw2']

    # use the hardware.py function to update the hardware doc
    hardware_checkout(one, two)

    # checkout means you take from hardware and add to project
    hard1 = hard1 + one
    hard2 = hard2 + two

    db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw1": hard1}})
    db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw2": hard2}})
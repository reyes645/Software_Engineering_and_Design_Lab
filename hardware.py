import driver
from database import Database as db


class Hardware:
    capacity1 = 0
    capacity2 = 0
    availability1 = 0
    availability2 = 0

    def __init__(self, cap1, cap2, av1, av2):
        Hardware.capacity1 = cap1
        Hardware.capacity2 = cap2
        Hardware.availability1 = av1
        Hardware.availability2 = av2

    def check_out_hw(self, one, two):
        # implement pls
        cursor = db.hardware_collection.find({'hw1': Hardware.capacity1})
        for temp in cursor:
            avail1 = temp['availHW1']
        for temp in cursor:
            avail2 = temp['availHW2']

        # check to see if you can actually check out this much from hw1 and hw2
        # maybe have a return statement for failure
        if one > avail1:
            # do something
            pass
        if two > avail2:
            # do something
            pass

        avail1 = avail1 - one
        avail2 = avail2 - two

        db.hardware_collection.update_one({'hw1': Hardware.capacity1}, {"$set": {'availHW1': avail1}})
        db.hardware_collection.update_one({'hw1': Hardware.capacity1}, {"$set": {'availHW2': avail2}})

        # maybe have a statement saying success

    def check_in_hw(self, one, two):
        # implement pls
        cursor = db.hardware_collection.find({'hw1': Hardware.capacity1})
        for temp in cursor:
            avail1 = temp['availHW1']
        for temp in cursor:
            avail2 = temp['availHW2']

        avail1 = avail1 + one
        avail2 = avail2 + two

        db.hardware_collection.update_one({'hw1': Hardware.capacity1}, {"$set": {'availHW1': avail1}})
        db.hardware_collection.update_one({'hw1': Hardware.capacity1}, {"$set": {'availHW2': avail2}})

        # maybe have statement saying success

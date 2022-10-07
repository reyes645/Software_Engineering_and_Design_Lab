import user
# are these imports right HUH
from hardware import Hardware as hardware
from database import Database as db


class Project:
    project_name = ''
    project_id = ''
    hw1 = 0
    hw2 = 0
    collaborators = []

    def __init__(self):
        return

    def add_proj(self, usern, proj_id, proj_name):
        Project.project_name = proj_name
        Project.project_id = proj_id
        Project.collaborators.append(usern)

    def checkout_hw(self, proj_id, hw1, hw2):  # implement
        Project.project_id = proj_id
        cursor = db.project_collection.find({'project_id': proj_id})
        for temp in cursor:
            hard1 = temp['hw1']
        for temp in cursor:
            hard2 = temp['hw2']

        # use the hardware.py function to update the hardware doc
        hardware.check_out_hw(hw1, hw2)

        # checkout means you take from hardware and add to project
        hard1 = hard1 + hw1
        hard2 = hard2 + hw2

        db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw1": hard1}})
        db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw2": hard2}})

        # maybe a return statement for success

    def checkin_hw(self, proj_id, hw1, hw2):  # implement
        Project.project_id = proj_id
        cursor = db.project_collection.find({'project_id': proj_id})
        for temp in cursor:
            hard1 = temp['hw1']
        for temp in cursor:
            hard2 = temp['hw2']

        # use the hardware.py function to update the hardware doc
        hardware.check_in_hw(hw1, hw2)

        # checkin means you give to hardware and take from project
        hard1 = hard1 - hw1
        hard2 = hard2 - hw2

        db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw1": hard1}})
        db.project_collection.update_one({"project_id": proj_id}, {"$set": {"hw2": hard2}})

        # maybe a return statement for success

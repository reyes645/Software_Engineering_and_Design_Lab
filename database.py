<<<<<<< HEAD
from pymongo import MongoClient


class Database:
    client = MongoClient(
        "mongodb+srv://firstUser:elemelem@cluster0.p8gz9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    my_database = client['EE461L_Semester_Project']

    user_collection = my_database['Users']
    project_collection = my_database['Projects']
    hardware_collection = my_database['Hardware']


    def __init__(self):

        # Database.hardware_collection.insert_one({
        # 'capacity1' : 0,
        # 'capacity2' : 0,
        # 'availability1' : 0,
        # 'availability2' : 0,
        #
        # })
        return


#
# class User:
#     username = ''
#     password = ''
#     user_id = ''
#     password_id = ''
#     token = ''
#     project_list = []
#
#     def __init__(self, name, password):
#         exists = user_collection.find_one({"username": name})
#         if exists is not None:
#             print("This user already exists")
#             self.username = name
#             self.password = password
#             return
#         self.username = name
#         self.password = password
#         user_info = {"username": self.username, "password": self.password, "user_id": self.user_id, "password_id": self.password_id, "token": self.token, "project_list": self.project_list}
#         x = user_collection.insert_one(user_info)
#
#     def set_username(self, username):
#         exists = user_collection.find_one({"username": username})
#         if exists is not None:
#             print("This username is already in use")
#             return
#         query = {"username": self.username}
#         new_username = {"$set": {"username": username}}
#         user_collection.update_one(query, new_username)
#         self.username = username
#
#     def get_username(self):
#         x = user_collection.find({}, {"username": 1, "password": 0, "user_id": 0, "password_id": 0, "token": 0, "project_list": 0})
#         for data in x:
#            pass
#         return self.username
#
#     def set_password(self, password):
#         user_collection.update_one({"username": self.username}, {"$set": {"password": password}})
#         self.password = password
#
#     def get_password(self):
#         return self.password
#
#     def set_user_id(self, user_id):
#         user_collection.update_one({"username": self.username}, {"$set": {"user_id": user_id}})
#         self.user_id = user_id
#
#     def get_user_id(self):
#         return self.user_id
#
#     def set_password_id(self, password_id):
#         user_collection.update_one({"username": self.username}, {"$set": {"password_id": password_id}})
#         self.password_id = password_id
#
#     def get_password_id(self):
#         return self.password_id
#
#     def set_token(self, token):
#         user_collection.update_one({"username": self.username}, {"$set": {"token": token}})
#         self.token = token
#
#     def get_token(self):
#         return self.token
#
#     def add_project(self, project):
#         user_collection.update_one({"username": self.username}, {"$set": {"project_list": self.project_list.append(project)}})
#         self.project_list.append(project)
#
#     # returns a list of project IDs
#     # can change this to any other identifier, such as an project name
#     def get_project_list(self):
#         a = []
#         for proj in self.project_list:
#             a.append(proj.get_project_id())
#         return a
#
#
# class Project:
#     project_name = ''
#     project_id = ''
#     hw1 = ''
#     hw2 = ''
#     collaborators = []
#
#     def __init__(self, name, id):
#         exists = project_collection.find_one({"project_id": id})
#         if exists is not None:
#             print("This project already exists")
#             self.project_name = name
#             self.project_id = id
#             return
#         self.project_name = name
#         self.project_id = id
#         project_info = {"project_name": self.project_name, "project_id": self.project_id, "hw1": self.hw1,
#                      "hw2": self.hw2, "collaborators": self.collaborators}
#         x = project_collection.insert_one(project_info)
#
#     def set_project_name(self, name):
#         project_collection.update_one({"project_id": self.project_id}, {"$set": {"project_name": name}})
#         self.project_name = name
#
#     def get_project_name(self):
#         return self.project_name
#
#     def set_project_id(self, id):
#         exists = project_collection.find_one({"project_id": id})
#         if exists is not None:
#             print("This project is already in use")
#             return
#         query = {"project_id": self.project_id}
#         new_id = {"$set": {"project_id": id}}
#         project_collection.update_one(query, new_id)
#         self.project_id = id
#
#     def get_project_id(self):
#         return self.project_id
#
#     # sets the capacity of hw1
#     def set_hw1(self, capacity):
#         project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw1": HardwareSet(capacity)}})
#         self.hw1 = HardwareSet(capacity)
#
#     # gets the availability of hw1
#     def get_hw1(self):
#         return self.hw1.get_availability()
#
#     # uses some amount of available space in hw1
#     def use_hw1(self, qty):
#         project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw1": self.hw1.check_out(qty)}})
#         self.hw1.check_out(qty)
#
#     # return some amount of hardware to gw1
#     def return_hw1(self, qty):
#         self.hw1.check_in(qty)
#
#     # sets the capacity of hw2
#     def set_hw2(self, capacity):
#         project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw2": HardwareSet(capacity)}})
#         self.hw2 = HardwareSet(capacity)
#
#     # gets the availability of hw2
#     def get_hw2(self):
#         return self.hw2.get_availability()
#
#     def use_hw2(self, qty):
#         project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw1": self.hw2.check_out(qty)}})
#         self.hw2.check_out(qty)
#
#     def return_hw2(self, qty):
#         self.hw2.check_in(qty)
#
#     def add_collaborator(self, collaborator):
#         self.collaborators.append(collaborator)
#         project_collection.update_one({"project_id": self.project_id}, {"$set": {"collaborators": self.collaborators}})
#
#     # returns a list of collaborator usernames
#     # can change this to any other identifier, such as an id
#     def get_collaborators(self):
#         a = []
#         for person in self.collaborators:
#             a.append(person.get_username())
#         return a
#
#
# class HardwareSet:
#     set_name = ''
#     capacity = 0
#     available = 0
#
#     def __init__(self, name, c):
#         exists = hardware_collection.find_one({"set_name": name})
#         if exists is not None:
#             print("This hardware set already exists")
#             self.set_name = name
#             self.capacity = c
#             self.available = c
#             return
#         self.set_name = name
#         self.capacity = c
#         self.available = c
#         hardware_info = {"set_name": name, "capacity": c, "available": c}
#         x = hardware_collection.insert_one(hardware_info)
#
#     def get_availability(self):
#         return self.available
#
#     def get_capacity(self):
#         return self.capacity
#
#     def get_checkedout_qty(self):
#         return self.capacity - self.available
#
#     # returns a -1 if the amount you want to check out is more than the amount available
#     # still checks out the available hardware
#     def check_out(self, qty):
#         if qty > self.available:
#             self.available = 0
#             return -1
#         self.available = self.available - qty
#         hardware_collection.update_one({"set_name": self.set_name}, {"$set": {"available": self.self.available}})
#
#     def check_in(self, qty):
#         self.available = self.available + qty
#         hardware_collection.update_one({"set_name": self.set_name}, {"$set": {"available": self.self.available}})
=======
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://firstUser:elemelem@cluster0.p8gz9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

my_database = client['EE461L_Semester_Project']

user_collection = my_database['Users']
project_collection = my_database['Projects']
hardware_collection = my_database['Hardware']


class User:
    username = ''
    password = ''
    user_id = ''
    password_id = ''
    token = ''
    project_list = []

    def __init__(self, name, password):
        exists = user_collection.find_one({"username": name})
        if exists is not None:
            print("This user already exists")
            self.username = name
            self.password = password
            return
        self.username = name
        self.password = password
        user_info = {"username": self.username, "password": self.password, "user_id": self.user_id, "password_id": self.password_id, "token": self.token, "project_list": self.project_list}
        x = user_collection.insert_one(user_info)

    def set_username(self, username):
        exists = user_collection.find_one({"username": username})
        if exists is not None:
            print("This username is already in use")
            return
        query = {"username": self.username}
        new_username = {"$set": {"username": username}}
        user_collection.update_one(query, new_username)
        self.username = username

    def get_username(self):
        x = user_collection.find({}, {"username": 1, "password": 0, "user_id": 0, "password_id": 0, "token": 0, "project_list": 0})
        for data in x:
           pass
        return self.username

    def set_password(self, password):
        user_collection.update_one({"username": self.username}, {"$set": {"password": password}})
        self.password = password

    def get_password(self):
        return self.password

    def set_user_id(self, user_id):
        user_collection.update_one({"username": self.username}, {"$set": {"user_id": user_id}})
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_password_id(self, password_id):
        user_collection.update_one({"username": self.username}, {"$set": {"password_id": password_id}})
        self.password_id = password_id

    def get_password_id(self):
        return self.password_id

    def set_token(self, token):
        user_collection.update_one({"username": self.username}, {"$set": {"token": token}})
        self.token = token

    def get_token(self):
        return self.token

    def add_project(self, project):
        user_collection.update_one({"username": self.username}, {"$set": {"project_list": self.project_list.append(project)}})
        self.project_list.append(project)

    # returns a list of project IDs
    # can change this to any other identifier, such as an project name
    def get_project_list(self):
        a = []
        for proj in self.project_list:
            a.append(proj.get_project_id())
        return a


class Project:
    project_name = ''
    project_id = ''
    hw1 = ''
    hw2 = ''
    collaborators = []

    def __init__(self, name, id):
        exists = project_collection.find_one({"project_id": id})
        if exists is not None:
            print("This project already exists")
            self.project_name = name
            self.project_id = id
            return
        self.project_name = name
        self.project_id = id
        project_info = {"project_name": self.project_name, "project_id": self.project_id, "hw1": self.hw1,
                     "hw2": self.hw2, "collaborators": self.collaborators}
        x = project_collection.insert_one(project_info)

    def set_project_name(self, name):
        project_collection.update_one({"project_id": self.project_id}, {"$set": {"project_name": name}})
        self.project_name = name

    def get_project_name(self):
        return self.project_name

    def set_project_id(self, id):
        exists = project_collection.find_one({"project_id": id})
        if exists is not None:
            print("This project is already in use")
            return
        query = {"project_id": self.project_id}
        new_id = {"$set": {"project_id": id}}
        project_collection.update_one(query, new_id)
        self.project_id = id

    def get_project_id(self):
        return self.project_id

    # sets the capacity of hw1
    def set_hw1(self, capacity):
        project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw1": HardwareSet(capacity)}})
        self.hw1 = HardwareSet(capacity)

    # gets the availability of hw1
    def get_hw1(self):
        return self.hw1.get_availability()

    # uses some amount of available space in hw1
    def use_hw1(self, qty):
        project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw1": self.hw1.check_out(qty)}})
        self.hw1.check_out(qty)

    # return some amount of hardware to gw1
    def return_hw1(self, qty):
        self.hw1.check_in(qty)

    # sets the capacity of hw2
    def set_hw2(self, capacity):
        project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw2": HardwareSet(capacity)}})
        self.hw2 = HardwareSet(capacity)

    # gets the availability of hw2
    def get_hw2(self):
        return self.hw2.get_availability()

    def use_hw2(self, qty):
        project_collection.update_one({"project_id": self.project_id}, {"$set": {"hw1": self.hw2.check_out(qty)}})
        self.hw2.check_out(qty)

    def return_hw2(self, qty):
        self.hw2.check_in(qty)

    def add_collaborator(self, collaborator):
        self.collaborators.append(collaborator)
        project_collection.update_one({"project_id": self.project_id}, {"$set": {"collaborators": self.collaborators}})

    # returns a list of collaborator usernames
    # can change this to any other identifier, such as an id
    def get_collaborators(self):
        a = []
        for person in self.collaborators:
            a.append(person.get_username())
        return a


class HardwareSet:
    set_name = ''
    capacity = 0
    available = 0

    def __init__(self, name, c):
        exists = hardware_collection.find_one({"set_name": name})
        if exists is not None:
            print("This hardware set already exists")
            self.set_name = name
            self.capacity = c
            self.available = c
            return
        self.set_name = name
        self.capacity = c
        self.available = c
        hardware_info = {"set_name": name, "capacity": c, "available": c}
        x = hardware_collection.insert_one(hardware_info)

    def get_availability(self):
        return self.available

    def get_capacity(self):
        return self.capacity

    def get_checkedout_qty(self):
        return self.capacity - self.available

    # returns a -1 if the amount you want to check out is more than the amount available
    # still checks out the available hardware
    def check_out(self, qty):
        if qty > self.available:
            self.available = 0
            return -1
        self.available = self.available - qty
        hardware_collection.update_one({"set_name": self.set_name}, {"$set": {"available": self.self.available}})

    def check_in(self, qty):
        self.available = self.available + qty
        hardware_collection.update_one({"set_name": self.set_name}, {"$set": {"available": self.self.available}})
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391

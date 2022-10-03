class User:
    username = ''
    password = ''
    user_id = ''
    password_id = ''
    token = ''
    project_list = []

    def __init__(self, name, password):
        self.username = name
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_password_id(self, password_id):
        self.password_id = password_id

    def get_password_id(self):
        return self.password_id

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token

    def add_project(self, project):
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

    def __init__(self, name):
        self.project_name = name

    def set_project_name(self, name):
        self.project_name = name

    def get_project_name(self):
        return self.project_name

    def set_project_id(self, id):
        self.project_id = id

    def get_project_id(self):
        return self.project_id

    # sets the capacity of hw1
    def set_hw1(self, capacity):
        self.hw1 = HardwareSet(capacity)

    # gets the availability of hw1
    def get_hw1(self):
        return self.hw1.get_availability()

    # uses some amount of available space in hw1
    def use_hw1(self, qty):
        self.hw1.check_out(qty)

    # return some amount of hardware to gw1
    def return_hw1(self, qty):
        self.hw1.check_in(qty)

    # sets the capacity of hw2
    def set_hw2(self, capacity):
        self.hw2 = HardwareSet(capacity)

    # gets the availability of hw2
    def get_hw2(self):
        return self.hw2.get_availability()

    def use_hw2(self, qty):
        self.hw2.check_out(qty)

    def return_hw2(self, qty):
        self.hw2.check_in(qty)

    def add_collaborator(self, collaborator):
        self.collaborators.append(collaborator)

    # returns a list of collaborator usernames
    # can change this to any other identifier, such as an id
    def get_collaborators(self):
        a = []
        for person in self.collaborators:
            a.append(person.get_username())
        return a


class HardwareSet:
    capacity1 = 0
    available1 = 0

    def __init__(self, c1):
        self.capacity1 = c1
        self.available1 = c1

    def get_availability(self):
        return self.available1

    def get_capacity(self):
        return self.capacity1

    def get_checkedout_qty(self):
        return self.capacity1 - self.available1

    # returns a -1 if the amount you want to check out is more than the amount available
    # still checks out the available hardware
    def check_out(self, qty):
        if qty > self.available1:
            self.available1 = 0
            return -1
        self.available1 = self.available1 - qty

    def check_in(self, qty):
        self.available1 = self.available1 + qty

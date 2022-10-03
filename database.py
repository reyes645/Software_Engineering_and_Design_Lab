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

    def set_user_ID(self, userID):
        self.user_id = userID

    def get_user_ID(self):
        return self.user_id

    def set_password_ID(self, passwordID):
        self.password_id = passwordID

    def get_password_ID(self):
        return self.password_id

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token

    def add_project(self, project):
        self.project_list.append(project)

    def get_projectList(self):
        return self.project_list


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

    def set_hw1(self, capacity):
        self.hw1 = HardwareSet(capacity)

    def get_hw1(self):
        return self.hw1.get_availability()

    def set_hw2(self, capacity):
        self.hw2 = HardwareSet(capacity)

    def get_hw2(self):
        return self.hw2.get_availability()

    def add_collaborator(self, collaborator):
        self.collaborators.append(collaborator)

    def get_collaborators(self):
        return self.collaborators

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

    def check_out(self, qty):
        if qty > self.available1:
            self.available1 = 0
            return -1
        self.available1 = self.available1 - qty

    def check_in(self, qty):
        self.available1 = self.available1 + qty

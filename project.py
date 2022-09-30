import user

class Project:
    project_name = ''
    project_id = ''
    hw1 = 0
    hw2 = 0
    collaborators = []

    def __init__(self):
        return

    def add_proj(self,usern, proj_id, proj_name):
        Project.project_name = proj_name
        Project.project_id = proj_id
        Project.collaborators.append(usern)

    def checkout_hw(self, proj_id, hw1, hw2):
        Project.project_id = proj_id



        return

    def checkin_hw(self, proj_id, hw1, hw2):
        Project.project_id = proj_id

        return


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

<<<<<<< HEAD
    def checkout_hw(self, proj_id, hw1, hw2): #implement
=======
    def checkout_hw(self, proj_id, hw1, hw2):
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        Project.project_id = proj_id



        return

<<<<<<< HEAD
    def checkin_hw(self, proj_id, hw1, hw2): #implement
=======
    def checkin_hw(self, proj_id, hw1, hw2):
>>>>>>> 718e7b04766f0b1112aad1688bedc7369680b391
        Project.project_id = proj_id

        return


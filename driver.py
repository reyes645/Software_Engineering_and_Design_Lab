from user import User
from project import Project
from database import Database
from hardware import Hardware





def take_request(global_request):
    #do forever while loop until new request comes in
    #get request data
    #check if its the same user
    #look for requestType

    requestType = ''

    return requestType




if __name__ == '__main__':

    #initialize database
    db = Database()

    #Take request
    global_request = ''

    #Through hardware database initialize global
    maxHW1 = db.hardware_collection.find_one().maxHW1
    maxHW2 = db.hardware_collection.find_one().maxHW2

    availHW1 = db.hardware_collection.find_one().availHW1
    availHW2 = db.hardware_collection.find_one().availHW2

    # maxHW1 = 1000
    # maxHW2 = 1000
    #                   initialization when database has not been set.
    # availHW1 = 1000
    # availHW2 = 1000
    globalHardware = Hardware(maxHW1, maxHW2, availHW1, availHW2)

    while True:
        requestType = take_request(global_request)

        if requestType == 'signup':
            #get username and password from request
            username = ''
            password = ''

            currentUser = User()
            errcheck = currentUser.signup(username, password, db)

        elif requestType == 'login':
            #get username and password from request
            username = ''
            password = ''


            currentUser = User()
            currentUser.login(username, password, db)


        elif requestType == 'logout':
            #Assumely do nothing since frontend does everything here
            pass


        elif requestType == 'project_page': #to implement
            #get username from request
            #from username go to database and find user object
            #could send entire user
            pass


        elif requestType == 'add_project':
            # find username, project_name in request
            username = ''
            project_name = ''

            currentUser = User()
            currentUser.add_project(username, project_name, db)

        elif requestType == 'join_project':
            # find username, unique project_id in request
            username = ''
            project_id = ''

            currentUser = User()
            currentUser.join_project(username, project_id, db)

        elif requestType == 'edit_proj':
            # find unique username, unique project_id in request
            username = ''
            project_id = ''

            currentUser = User()
            currentUser.edit_proj(username, project_id, db)

        elif requestType == 'check_out_hw': #implement pls
            #find unique project_id, hw1, hw2 in request
            project_id = ''
            hw1 = 0
            hw2 = 0

            curProject = Project()
            #find curProject attributes and put in curProject from database
            # curProject.project_name = db.project_collection.find({'proj_id': project_id}).projname
            cursor = db.project_collection.find({'proj_id': project_id})
            for temp in cursor:
                projName = temp['project_name']
            curProject.project_name = projName
            curProject.project_id = project_id
            # curProject.hw1 = db.project_collection.find({'proj_id': project_id}).hw1
            cursor = db.project_collection.find({'proj_id': project_id})
            for temp in cursor:
                hard1 = temp['hw1']
            curProject.hw1 = hard1
            # curProject.hw2 = db.project_collection.find({'proj_id': project_id}).hw2
            cursor = db.project_collection.find({'proj_id': project_id})
            for temp in cursor:
                hard2 = temp['hw2']
            curProject.hw2 = hard2
            # curProject.collaborators = db.project_collection.find({'proj_id': project_id}).collaborators
            cursor = db.project_collection.find({'proj_id': project_id})
            for temp in cursor:
                collab = temp['collaborators']
            curProject.collaborators = collab

            Project.checkout_hw(project_id, hw1, hw2)

        elif requestType == 'check_in_hw': #implement pls
            # find unique project_id, hw1, hw2 in request
            project_id = ''
            hw1 = 0
            hw2 = 0

            curProject = Project()
            # find curProject attributes and put in curProject from database 
            
            # curProject.project_name = db.project_collection.find({'proj_id': project_id}).project_name
            # curProject.project_id = project_id
            # curProject.hw1 = db.project_collection.find({'proj_id': project_id}).hw1
            # curProject.hw2 = db.project_collection.find({'proj_id': project_id}).hw2
            # curProject.collaborators = db.project_collection.find({'proj_id': project_id}).collaborators
            
            curProject.project_id = project_id
            
            cursor = db.project_collection.find({'proj_id': project_id})
            for temp in cursor:
                projName = temp['proj_name']
                hard1 = temp['hw1']
                hard2 = temp['hw2']
                collab = temp['collaborators']
                
            curProject.project_name = projName
            curProject.hw1 = hard1
            curProject.hw2 = hard2
            curProject.collaborators = collab

            Project.checkin_hw(project_id, hw1, hw2)

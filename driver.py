from user import User
from project import Project
import database
from hardware import Hardware





def take_request(global_request):
    #do forever while loop until new request comes in
    #get request data
    #check if its the same user
    #look for requestType

    requestType = ''

    return requestType




if __name__ == '__main__':

    #Take request
    global_request = ''

    #Through hardware database initialize global hardware
    maxHW1 = 1000
    maxHW2 = 1000

    availHW1 = 1000
    availHW2 = 1000
    globalHardware = Hardware(maxHW1, maxHW2, availHW1, availHW2)

    while True:
        requestType = take_request(global_request)

        if requestType == 'signup':
            #get username and password from request
            username = ''
            password = ''

            currentUser = User()
            errcheck = currentUser.signup(username, password)


        elif requestType == 'login':
            #get username and password from request
            username = ''
            password = ''


            currentUser = User()
            currentUser.login(username, password)


        elif requestType == 'logout':
            #Assumely do nothing since frontend does everything here
            pass


        elif requestType == 'project_page':
            #get username from request
            #from username go to database and find user object
            #could send entire user object or just object_list[]
            pass


        elif requestType == 'add_project':
            # find username, project_name in request
            username = ''
            project_name = ''

            currentUser = User()
            currentUser.add_project(username, project_name)

        elif requestType == 'join_project':
            # find username, unique project_id in request
            username = ''
            project_id = ''

            currentUser = User()
            currentUser.join_project(username, project_id)

        elif requestType == 'edit_proj':
            # find unique username, unique project_id in request
            username = ''
            project_id = ''

            currentUser = User()
            currentUser.edit_proj(username, project_id)

        elif requestType == 'check_out_hw':
            #find unique project_id, hw1, hw2 in request
            project_id = ''
            hw1 = 0
            hw2 = 0

            curProject = Project()
            #find curProject attributes and put in curProject


            Project.checkout_hw(project_id,hw1,hw2)

        elif requestType == 'check_in_hw':
            # find unique project_id, hw1, hw2 in request
            project_id = ''
            hw1 = 0
            hw2 = 0

            curProject = Project()
            # find curProject attributes and put in curProject

            Project.checkin_hw(project_id, hw1, hw2)

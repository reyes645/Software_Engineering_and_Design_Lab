# Website is Live! - [tinyurl.com/bubblesHaaS](https://tinyurl.com/bubblesHaaS)
<img width="1680" alt="Screen Shot 2023-02-03 at 4 25 25 PM" src="https://user-images.githubusercontent.com/22242257/216722695-23fa4196-b9cf-44aa-839d-dd45424977a5.png">

# Hardware-as-a-Service (HaaS) Web Application

A proof of concept (PoC) web application for Hardware-as-a-Service (HaaS), developed as a team project in the Software Engineering and Design Lab course. The application enables users to securely manage projects and request available hardware resources.

## Features

- User account creation and management
- Project management
- Hardware resource request and allocation

## Technologies Used

- React.js (Frontend)
- Python Flask (Backend)
- MongoDB (Data Management)
- Heroku (Deployment)

## How to Run

1. Clone the repository
2. Set up your MongoDB credentials

### Running the React Frontend
1. Open a terminal/command prompt, navigate to the root folder of the React project, and ensure that you have Node.js and npm installed.
2. Install the required dependencies by running npm install
3. Start the React development server by running npm start
4. This will start the React development server, usually at http://localhost:3000.

### Running the Flask Backend (flask_stuff.py)
1. Open another terminal/command prompt, navigate to the folder containing the flask_stuff.py file, and ensure that you have Python installed.
2. Create a virtual environment and install the necessary packages by running:
  - python -m venv venv
  - source venv/bin/activate  # For Linux/macOS
  - venv\Scripts\activate     # For Windows
  - pip install Flask pymongo dnspython
3. Set the Flask environment variables:
  - export FLASK_APP=flask_stuff.py        # For Linux/macOS
  - set FLASK_APP=flask_stuff.py           # For Windows
4. Run the Flask server: flask run
5. This will start the Flask server locally, usually at http://localhost:5000.

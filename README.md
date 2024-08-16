Attendance Marking Web Application
This is a simple web application built using Flask that allows users to mark attendance and view the recorded attendance data. The application uses an in-memory dictionary to store the attendance information.

Features
Mark Attendance: Users can enter their name and the date to mark their attendance.
View Attendance: View the list of all recorded attendance entries.
Project Structure
bash
Copy code
attendance_app/
│
├── templates/
│   ├── index.html        # Template for marking attendance
│   └── attendance.html   # Template for viewing attendance
│
├── app.py                # Main Flask application
└── README.md             # Project documentation
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/attendance_app.git
cd attendance_app
Create a Virtual Environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install Flask
Run the Application:

bash
Copy code
python app.py
Access the Application:

Open your web browser and go to http://127.0.0.1:5000/ to use the application.

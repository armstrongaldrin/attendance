from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Create a dictionary to store attendance data (in-memory)
attendance_data = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    date = request.form.get('date')
    name = request.form.get('name')

    if date not in attendance_data:
        attendance_data[date] = []

        attendance_data[date].append(name)

    return redirect(url_for('home'))

@app.route('/view_attendance')
def view_attendance():
    return render_template('attendance.html', attendance_data=attendance_data)

if __name__ == '__main__':
    app.run(debug=True)

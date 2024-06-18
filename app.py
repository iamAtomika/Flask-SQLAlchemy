#create and endpoint that returns all students with all their data
from utilities import load_data #if importing from csv file
from models import db, Student

#import the `Flask` and `jsonify` classes from the Flask library
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


#Flask application initializing the `app` object.
app = Flask(__name__)



# TEST DATA

# Sample student data
# students = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
#     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
#     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
#     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
#     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
#     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
#     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
#     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
#     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
# ]

# list_test = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'}
# ]

# #OR loading from csv file
# students = load_data('code-platoon-lessons/python-servers/flask_lesson/students.csv')

# @app.route('/', methods=['GET'])
# def home_inst():
#     return jsonify(list_test)




#DATABASE

# Configuration for the PostgreSQL database
# 'postgresql+psycopg://username:password@localhost:5432/database_name'
## CHECK FOR PORT NUMBER using error
## 'postgresql+psycopg://username:password@localhost/students'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://username:password@localhost/students'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app) # Initialize db with Flask app





#API Endpoints 

#route `/students` that responds to GET requests
## http://127.0.0.1:8000/students
@app.route('/students')
def get_students():
    students = Student.query.all()
    student_list = [student.to_dict() for student in students]
    return jsonify(student_list)



# ##students older than 20
# ## http://127.0.0.1:8000/get_old_students
# @app.route('/old_students', methods=['GET'])
# def get_old_students():
#     old_students = []
#     for i in students:
#         if i['age'] > 20:
#             old_students.append(i)
#     return jsonify(old_students)

# ##students younger than 21
# ## http://127.0.0.1:8000/get_young_students
# @app.route('/young_students', methods=['GET'])
# def get_young_students():
#     young_students = []
#     for i in students:
#         if i['age'] < 21:
#             young_students.append(i)
#     return jsonify(young_students)

# ##student younger than 21 and have a letter grade of "A."
# ## http://127.0.0.1:8000/get_advance_students
# @app.route('/advance_students', methods=['GET'])
# def get_advance_students():
#     advance_students = []
#     for i in students:
#         if i['age'] < 21 and i['grade'] == 'A':
#             advance_students.append(i)
#     return jsonify(advance_students)

# ##student keys of 'first_name' and 'last_name' along with their corresponding values.
# ## http://127.0.0.1:8000/get_student_names
# @app.route('/student_names', methods=['GET'])
# def get_student_names():
#     student_names = []
#     for i in students:
#         student_names.append({'first_name': i['first_name'], 'last_name': i['last_name']})
#     return jsonify(student_names)

# ##student keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
# ## http://127.0.0.1:8000/get_student_ages
# @app.route('/student_ages', methods=['GET'])
# def get_student_ages():
#     student_ages = []
#     for i in students:
#         student_ages.append({'first_name': i['first_name'], 'last_name': i['last_name'], 'age': i['age']})
#     return jsonify(student_ages)



#PORT
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, port=8000) #USING PORT 8000


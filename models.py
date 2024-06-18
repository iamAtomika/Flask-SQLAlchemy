from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model): #Model == SQL Table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(1))

    def to_dict(self):
        return {
            'id': self.id, 
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'age': self.age, 
            'grade': self.grade
            }    
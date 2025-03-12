from flask import Flask,request  ,jsonify

Todo = Flask(__name__)
students = [
    {
        'id': 1,
        'name': 'John',
        'age': 22
    },
     {
        'id': 2,
        'name': 'mark',
        'age': 22
    },
     {
        'id': 3,
        'name': 'jane',
        'age': 22
    }
]

@Todo.route('/student_list')
def student_list():
    return jsonify(students)
@Todo.route('/student/get/<int:id>')
def student_id(id):
    print(id)
    for student in students:
        if student['id'] == id:
            return jsonify(student)
    return jsonify('student not found')
    
        
   

if __name__ == '__main__':
    Todo.run(host='127.0.0.1',port=5000,debug=True)

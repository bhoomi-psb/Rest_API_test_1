from flask import Flask, jsonify

todo = Flask(__name__)  # Fixing the Flask app name

# Defining the students list outside of functions
students = [
    {
        'id': 1,
        'student_name': 'std1',
        'age': 21,
        'email': 'std1@gmail.com'
    },
    {
        'id': 2,
        'student_name': 'std2',
        'age': 21,
        'email': 'std2@gmail.com'
    },
    {
        'id': 3,
        'student_name': 'std3',
        'age': 22,
        'email': 'std3@gmail.com'
    }
]

@todo.route('/students-list')
def students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_student(id):
    # Fixing the student search logic
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    todo.run(
        debug=True
    )

from flask import Blueprint, jsonify, request
from users.model.courses_model import Course

blueprint = Blueprint('courses_controller', __name__)
courses = []

# Endpoint to insert users
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    # Get the user data from the request
    course_data = request.get_json()

    # Create a new user
    course = Course(
        id=len(courses) + 1,
        name=course_data["name"],
        description=course_data["description"]
    )

    # Add the new user to the list of users
    courses.append(course)

    # Return the newly inserted user
    return jsonify(course)


# Endpoint to retrieve users based on user_id
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_user(course_id):
    # Find the user with the given user_id
    course = next((course for course in courses if course.id == int(course_id)), None)

    # If the user is not found, return a 404 error
    if course is None:
        return jsonify({"message": "Course not found"}), 404

    # Return the retrieved user
    return jsonify(course)
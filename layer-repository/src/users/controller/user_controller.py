from flask import Blueprint, jsonify, request
from users.model.user_model import User


blueprint = Blueprint('user_controller', __name__)
users = []


# Endpoint to insert users
@blueprint.route("/users", methods=["POST"])
def insert_user():
    # Get the user data from the request
    user_data = request.get_json()

    # Create a new user
    user = User(
        id=len(users) + 1,
        name=user_data["name"],
        email=user_data["email"]
    )

    # Add the new user to the list of users
    users.append(user)

    # Return the newly inserted user
    return jsonify(user)


# Endpoint to retrieve users based on user_id
@blueprint.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    # Find the user with the given user_id
    user = next((user for user in users if user.id == int(user_id)), None)

    # If the user is not found, return a 404 error
    if user is None:
        return jsonify({"message": "User not found"}), 404

    # Return the retrieved user
    return jsonify(user)
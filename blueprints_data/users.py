from flask import Blueprint, jsonify, request


users_dp = Blueprint('user', __name__)


users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]


@users_dp.route('/api/users/', methods=['GET'])
@users_dp.route('/api/users/', methods=['POST'])
@users_dp.route('/api/users/<int:user_id>', methods=['DELETE'])
def users_operations(user_id=None):
    """users_dp get, post, or delete users"""
    if request.method == 'GET':
        return jsonify(users)
    elif request.method == 'POST':
        users.append({"id": len(users), "name": "Meme"})
        return jsonify(users)
    elif request.method == 'DELETE':
        for i in users:
            if i["id"] == user_id and user_id is not None:
                users.remove(i)
                return users, 204
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({'error': 'Method not allowed'}), 405
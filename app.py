from flask import Flask, request, jsonify
from controllers.addition_controller import perform_addition
from models.addition_models import AdditionRequest

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    """
    Endpoint for performing addition on input lists of integers.

    Accepts JSON data with the following format:
    {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }

    Returns JSON response with the following format:
    {
        "batchid": "id0101",
        "response": [3, 7],
        "status": "complete",
        "started_at": "<timestamp>",
        "completed_at": "<timestamp>"
    }
    """
    request_data = request.get_json()
    addition_request = AdditionRequest(**request_data)

    response = perform_addition(addition_request)

    return jsonify(response.dict())


if __name__ == '__main__':
    app.run(debug=True)

# FlaskBatchProcessor

This repository contains a Flask application structured following the Model-View-Controller (MVC) pattern. It includes an endpoint for validating and processing batches of numbers, with request and response validation using Pydantic models.


### Project Structure

The project structure follows the MVC pattern:

  - **controllers/**: Contains controller modules responsible for handling HTTP requests and responses.
    - `addition_controller.py`: Implements the logic for the endpoint `/add`.
  - **models/**: Contains model modules defining Pydantic models for request and response validation.
    - `addition_models.py`: Defines the Pydantic model for request and response validation.
  - **app.py**: Defines the Flask routes and views.
- **tests/**: Contains unit tests for the Flask application.
  - `test_addition_controller.py`: Contains unit tests for the Flask application.

### Dependencies
* Flask

* Pydantic

Install dependencies using:
```
pip install -r requirements.txt
```

### Usage

To run the Flask application, navigate to the project directory and execute run.py:
```
python app.py
```
The application will start running on http://localhost:5000.

### curl request
```
curl -X POST   -H "Content-Type: application/json"   -d '{
        "batchid": "id0101",
        "payload": [[1, 2,7,9], [3,5, 4]]
      }'   http://127.0.0.1:5000/add
```

Expected output:
```
{
  "batchid": "id0101", 
  "completed_at": "2024-06-14T13:56:50.797373", 
  "response": [
    19, 
    12
  ], 
  "started_at": "2024-06-14T13:56:50.622659", 
  "status": "complete"
}
```

To validate and process batches of numbers, send a POST request to /validate with JSON data containing the batch ID and payload of numbers. The response will contain the batch ID, processed results, status, and timestamps.

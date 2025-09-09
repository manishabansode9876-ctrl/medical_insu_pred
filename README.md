# Medical Insurance Prediction API

A Flask-based REST API for predicting medical insurance charges using a trained linear regression model.

## Features

- Predict medical insurance charges based on user input
- Input validation and error handling
- RESTful API endpoints
- Modular and maintainable code structure

## Project Structure

```
medical-insurance-prediction/
├── project_app/
│   ├── __init__.py
│   ├── config.py
│   ├── utils.py
│   ├── linear_reg_model.pkl
│   └── column_data.json
├── templates/
│   └── index.html
├── interface.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd medical-insurance-prediction
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask development server:
```bash
python interface.py
```

2. Access the API:
- Home page: http://localhost:5000/
- Prediction endpoint: http://localhost:5000/predict

## API Endpoints

### POST /predict

Predict medical insurance charges based on input parameters.

**Request Body:**
```json
{
    "age": 30,
    "gender": "male",
    "bmi": 25.5,
    "children": 2,
    "smoker": "no",
    "region": "southeast"
}
```

**Response:**
```json
{
    "status": "success",
    "prediction": 1234.56,
    "message": "Prediction successful"
}
```

## Input Validation

The API validates input parameters according to the following rules:
- Age: Between 18 and 100
- Gender: 'male' or 'female'
- BMI: Between 10 and 50
- Children: Between 0 and 10
- Smoker: 'yes' or 'no'
- Region: Valid region name

## Error Handling

The API returns appropriate error messages for:
- Missing required fields
- Invalid input values
- Model loading errors
- Prediction errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
import os

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    DEBUG = True

    # File paths
    MODEL_FILE_PATH = os.path.join("project_app", 'medical.pkl')
    JSON_FILE_PATH = os.path.join("project_app", 'label_encode.json')

    # Input validation
    MIN_AGE = 18
    MAX_AGE = 100
    MIN_BMI = 10
    MAX_BMI = 50
    MAX_CHILDREN = 5

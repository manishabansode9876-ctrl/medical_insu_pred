import pickle
import json
import numpy as np
import pandas as pd
from project_app.config import Config

class MedicalInsurance:
    """
    A class to handle medical insurance predictions using a trained linear regression model.
    
    Attributes:
        age (int): Age of the insured person
        gender (str): Gender of the insured person ('male' or 'female')
        bmi (float): Body Mass Index of the insured person
        children (int): Number of children/dependents
        smoker (str): Smoking status ('yes' or 'no')
        region (str): Region of residence
    """
    
    def __init__(self, age: int, gender: str, bmi: float, children: int, smoker: str, region: str):
        """
        Initialize the MedicalInsurance class with user input parameters.
        
        Args:
            age (int): Age of the insured person
            gender (str): Gender of the insured person
            bmi (float): Body Mass Index
            children (int): Number of children/dependents
            smoker (str): Smoking status
            region (str): Region of residence
        """
        self.age = age
        self.gender = gender.lower()
        self.bmi = bmi
        self.children = children
        self.smoker = smoker.lower()
        self.region = 'region_' + region.lower()
        self.linear_model = None
        self.column_data = None
        
    def _validate_input(self):
        """Validate the input parameters."""
        if not Config.MIN_AGE <= self.age <= Config.MAX_AGE:  # 18 < age < 100
            raise ValueError(f"Age must be between {Config.MIN_AGE} and {Config.MAX_AGE}")
        
        if self.gender not in ['male', 'female']:
            raise ValueError("Gender must be either 'male' or 'female'")
            
        if not Config.MIN_BMI <= self.bmi <= Config.MAX_BMI:
            raise ValueError(f"BMI must be between {Config.MIN_BMI} and {Config.MAX_BMI}")
            
        if not 0 <= self.children <= Config.MAX_CHILDREN:
            raise ValueError(f"Number of children must be between 0 and {Config.MAX_CHILDREN}")
            
        if self.smoker not in ['yes', 'no']:
            raise ValueError("Smoker must be either 'yes' or 'no'")
            
    def load_model(self):
        """
        Load the trained model and column data from the specified paths.
        
        Raises:
            FileNotFoundError: If model or column data files are not found
            Exception: If there's an error loading the files
        """
        try:
            with open(Config.MODEL_FILE_PATH, 'rb') as f:
                self.linear_model = pickle.load(f)
                
            with open(Config.JSON_FILE_PATH, 'r') as f:
                self.column_data = json.load(f)
                
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Model or data file not found: {str(e)}")
        except Exception as e:
            raise Exception(f"Error loading model or data: {str(e)}")
            
    def get_predict_charges(self):
        """
        Predict medical insurance charges based on the input parameters.
        
        Returns:
            numpy.ndarray: Array containing the predicted charges
            
        Raises:
            ValueError: If input validation fails
            Exception: If there's an error during prediction
        """
        try:
            # Validate input
            self._validate_input()
            
            # Load model and data
            self.load_model()
            
            # Prepare input array
            column_names = self.linear_model.feature_names_in_
            region_index = np.where(column_names == self.region)[0][0]
            
            test_array = np.zeros(self.linear_model.n_features_in_)
            test_array[0] = self.age
            test_array[1] = self.column_data['gender'][self.gender]
            test_array[2] = self.bmi
            test_array[3] = self.children
            test_array[4] = self.column_data['smoker'][self.smoker]
            test_array[region_index] = 1
            
            # Make prediction
            predicted_charges = self.linear_model.predict([test_array])
            
            return predicted_charges
            
        except Exception as e:
            raise Exception(f"Error during prediction: {str(e)}")
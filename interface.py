from flask import Flask, render_template, jsonify, request
from project_app.utils import MedicalInsurance
from project_app.config import Config   # Correct import

app = Flask(__name__)
app.config.from_object(Config)         # Use Config, not config

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_insurance_charges():
    try:
        data = request.form
        required_fields = ['age', 'gender', 'bmi', 'children', 'smoker', 'region']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        age = int(data['age'])
        gender = data['gender'].lower()
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker'].lower()
        region = data['region'].lower()
        
        med_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
        charges = med_ins.get_predict_charges()
        
        # If charges is a list/array
        if isinstance(charges, (list, tuple)):
            charges = float(charges[0])
        else:
            charges = float(charges)
        
        return jsonify({
            "status": "success",
            "prediction": charges,
            "message": "Prediction successful"
        })
        
    except ValueError as e:
        return jsonify({"error": f"Invalid input data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)



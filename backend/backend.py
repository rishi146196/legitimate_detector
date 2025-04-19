from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the fraud prediction model
model = joblib.load("cincyr_up.pkl")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print("Function Called")

    # Create DataFrame with correct feature names
    input_df = pd.DataFrame([{
        "registered": data["registered"],
        "company_age": data["company_age"],
        "valid_address": data["valid_address"],
        "domain_age": data["domain_age"],
        "listed_in_gov_db": data["listed_in_gov_db"],
        "has_audited_reports": data["has_audited_reports"]
    }])
   

    # Predict
    pred = model.predict(input_df)[0]
    
    label_map = {0: "real", 1: "fake"}
    
    response = {"prediction": label_map[int(pred)]}
    

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

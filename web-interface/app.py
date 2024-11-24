import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the model from the .pkl file
with open('gbc_model_and_metrics.pkl', 'rb') as file:
    data = pickle.load(file)

model = data['model']  # Extract the model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        input_data = [
            int(request.form['sex']),
            int(request.form['cp']),
            int(request.form['age']),
            int(request.form['trestbps']),
            int(request.form['chol']),
            int(request.form['fbs']),
            int(request.form['restecg']),
            int(request.form['thalch']),
            int(request.form['exang']),
            float(request.form['oldpeak']),
            int(request.form['slope']),
            int(request.form['ca']),
            int(request.form['thal']),
        ]
        input_data = [input_data]  # Model expects a 2D array

        # Make prediction
        prediction = model.predict(input_data)

        # Map prediction to levels 0, 1, 2, 3, and 4
        level = prediction[0]
        if level == 0:
            output = 'No Cardiovascular Disease (Level 0)'
            suggestion = """1. Maintain a healthy lifestyle with regular exercise and a balanced diet.<br>
                            2. Avoid smoking and excessive alcohol consumption.<br>
                            3. Manage stress through relaxation techniques.<br>
                            4. Keep a regular check on your cholesterol levels.<br>
                            5. Maintain a normal blood pressure."""
        elif level == 1:
            output = 'Mild Cardiovascular Disease (Level 1)'
            suggestion = """1. Schedule regular medical check-ups to monitor your heart health.<br>
                            2. Engage in light to moderate physical activities like brisk walking.<br>
                            3. Limit the intake of saturated fats, salt, and processed foods.<br>
                            4. Consider reducing stress through mindfulness techniques.<br>
                            5. Stay hydrated and maintain a healthy body weight."""
        elif level == 2:
            output = 'Moderate Cardiovascular Disease (Level 2)'
            suggestion = """1. Consult a healthcare provider for a personalized treatment plan.<br>
                            2. Increase physical activity under the guidance of a doctor.<br>
                            3. Monitor and control blood pressure and cholesterol levels.<br>
                            4. Avoid foods high in trans fats and sugars.<br>
                            5. Get regular ECG and blood tests to track heart health."""
        elif level == 3:
            output = 'Severe Cardiovascular Disease (Level 3)'
            suggestion = """1. Seek immediate medical advice and follow a treatment plan recommended by your doctor.<br>
                            2. Consider medication to manage symptoms and prevent complications.<br>
                            3. Limit physical activities and avoid stress-inducing tasks.<br>
                            4. Follow a heart-healthy diet rich in vegetables, fruits, and whole grains.<br>
                            5. Consider cardiac rehabilitation for better heart management."""
        elif level == 4:
            output = 'Critical Cardiovascular Disease (Level 4)'
            suggestion = """1. Consult a doctor immediately for further evaluation and management.<br>
                            2. Avoid strenuous activities and ensure complete rest.<br>
                            3. Follow a strict diet as prescribed by your healthcare provider.<br>
                            4. Prepare for potential medical procedures or surgery as advised.<br>
                            +3
                            5. Monitor your heart condition regularly and follow up frequently with your doctor."""
        else:
            output = 'Unknown condition'
            suggestion = 'Please follow up with your healthcare provider for further assessment.'

    except Exception as e:
        output = f'Error in prediction: {str(e)}'
        suggestion = 'Unable to provide suggestions due to an error in prediction.'

    return render_template('index.html', prediction_text=output, suggestion_text=suggestion, 
                           sex=request.form['sex'], cp=request.form['cp'], age=request.form['age'], 
                           trestbps=request.form['trestbps'], chol=request.form['chol'], 
                           fbs=request.form['fbs'], restecg=request.form['restecg'], 
                           thalch=request.form['thalch'], exang=request.form['exang'], 
                           oldpeak=request.form['oldpeak'], slope=request.form['slope'], 
                           ca=request.form['ca'], thal=request.form['thal'])

if __name__ == "__main__":
    app.run(debug=True)

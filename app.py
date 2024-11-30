from flask import Flask, render_template, request
import pickle
import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('fire_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the fitted label encoders
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html')

# Route for the ML form
@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

# Route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form input data
    structural_type = request.form['structural_type']
    construction_material = request.form['construction_material']
    fire_load_type = request.form['fire_load_type']
    wall_thickness = float(request.form['wall_thickness'])
    height_floors = int(request.form['height_floors'])
    temperature = float(request.form['temperature'])
    wind = float(request.form['wind'])
    humidity = float(request.form['humidity'])
    area_m2 = float(request.form['area_m2'])
    paint = request.form['paint']
    room_number = int(request.form['room_number'])
    room_occupants = int(request.form['room_occupants'])

    # Convert categorical variables to numerical using label encoding
    data = {
        'structural_type': [structural_type],
        'construction_material': [construction_material],
        'fire_load_type': [fire_load_type],
        'wall_thickness': [wall_thickness],
        'height_floors': [height_floors],
        'temperature': [temperature],
        'wind': [wind],
        'humidity': [humidity],
        'area_m2': [area_m2],
        'paint': [paint],
        'room_number': [room_number],
        'room_occupants': [room_occupants]
    }

    # Convert input data into a DataFrame
    input_df = pd.DataFrame(data)

    # Apply label encoding to categorical columns
    input_df['structural_type'] = label_encoders['structural_type'].transform(input_df['structural_type'])
    input_df['construction_material'] = label_encoders['construction_material'].transform(input_df['construction_material'])
    input_df['fire_load_type'] = label_encoders['fire_load_type'].transform(input_df['fire_load_type'])
    input_df['paint'] = label_encoders['paint'].transform(input_df['paint'])

    # Predict using the loaded model
    prediction = model.predict(input_df)

    # Show the prediction (fire_resistance)
    return render_template('predict.html', prediction=round(prediction[0],2))

if __name__ == '__main__':
    app.run(debug=True)

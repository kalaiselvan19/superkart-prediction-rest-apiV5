
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
try:
  #Assuming the model is saved in the 'Backend_files' directory
  model_path = "SuperKart_model.joblib"
  model = joblib.load(model_path)
  print(f"Model loaded successfully from {model_path}")
except Exception as e:
  print(f"Error loading the model: {e}")
  model = None #Set model to None if load fails

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to SuperKart Sales Prediction API</h1>"

@app.route("v1/predict", methods=["POST"])
def predict():
  if model is None:
    return jsonify({"error": "Model not loaded. Please check the server logs."}), 500

  try:
    data = request.get_json(force = True)
    #Ensure the input data  has all required features in the correct order
    #This assumes the input JSON will be a dictionary for a single prediction
    #if you expect multiple predictions, adjust to pd.dataframe(data)
    input_df = pd.DataFrame([data])
    expected_columns  = ["Product_Weight", "Product_Sugar_Content", "Product_Allocated_Area",
                         "Product_MRP", "Store_Size", "Store_Location_City_Type", "Store_Type",
                         "Product_Id_char", "Store_Age_Years", "Product_Type_Category"
                         ]
    input_df = input_df[expected_columns]
    prediction = model.predict(input_df)
    return jsonify({"prediction_sales": float(prediction[0])})
  except Exception as e:
    return jsonify({"error": str(e)}), 400

  @app.route("/v1/predictbatch", methods=["POST"])
  def predictbatch():
    file = request.files["file"]
    if file:
      try:
        batch_df = pd.read_csv(file)
        predited_sales = model.predict(batch_df)
        return jsonify({"predictions": predited_sales.tolist()})
      except Exception as e:
        return jsonify({"error": str(e)}), 400

#To run the app, you would typically use a command like:
if __name__ == "__main__":
  app.run(debug=True)

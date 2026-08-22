
import streamlit as st
import pandas as pd
import requests
import os

#Base URL for Flask Backend
BACKEND_URL = "http://localhost:7860"


#Set the title of the streamlit app
st.title("SuperKart product Sales Prediction")

#section for online prediction
st.subheader("Online Prediction")

#Collect user input for product features
product_weight = st.number_input("Product Weight", min_value=0.0, value=12.0, step=0.1)
product_sugar_content = st.selectbox("Product Sugar Content", ["Low Sugar", "Medium Sugar", "High Sugar"])
product_allocated_area = st.number_input("Product Allocated Area", min_value=0.0, value=0.5, step=0.001, format="%.3f")
product_mrp = st.number_input("Product MRP", min_value=0.0, value=150.0, step=0.1)
store_size = st.selectbox("Store Size", ["Supermaket Type2", "Departmental Store", "Supermarket Type","Food Mart"])
Product_Id_char = st.selectbox("Product Id char", ["FD", "NC", "DR"])
Store_Age_Years = st.number_input("Store Age Years", min_value=0, value=20, step=1)
Product_Type_Category=st.selectbox("Product Type Category",  ["Perishables", "Non Perishables"])


#Convert user input into a Dataframe
input_data = {
    "Product_Weight": product_weight,
    "Product_Sugar_Content": product_sugar_content,
    "Product_Allocated_Area": product_allocated_area,
    "Product_MRP": product_mrp,
    "Store_Size": store_size,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}


#Define the Git Space URL

GIT_FACE_URL = https://github.com/kalaiselvan19


#Make Predictions when the "Predict" button is clicked

if st.button("Predict Product Sales", type="primary"):
  response = requests.post(f"{BACKEND_URL}/predict", json=input_data)
  try:
    if response.status_code == 200:
      prediction = response.json()["prediction_sales"]
      st.success(f"Predicted Sales: {prediction}")
    else:
      st.error(f"Error: {response.status_code}")
  except requests.exceptions.RequestException as e:
    st.error(f"Error: {e}")
  st.text(response.text)


  #For Batch prediction
  st.subheader("Batch Prediction")
  uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type=["csv"])

  if uploaded_file is not None:
    if st.button("Predict Batch", type="primary")
        response = requests.post(f"{BACKEND_URL}/predictbatch", files={"file": uploaded_file})
        if response.status_code == 200:
          predictions = response.json()["predictions"]
          st.success("Batch prediction completed!")
          st.write("Predictions:")
          st.write(predictions)
        else:
          st.error(f"Unable to connect the prediction API: {response.status_code}")

